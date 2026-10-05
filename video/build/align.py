"""Aligne le texte du script sur les segments de parole détectés (silences ffmpeg).
Pas de modèle ASR disponible : on fait un alignement monotone par programmation
dynamique, coût = écart (log) entre durée réelle d'un segment et durée prédite
par le nombre de syllabes des phrases qu'on lui attribue."""
import json, math, re, subprocess, sys

AUDIO = sys.argv[1]
OUT = sys.argv[2]

# Phrases (unités insécables) — un silence ne peut tomber qu'entre deux phrases.
# id : identifiant de cue utilisé par l'animation.
PHRASES = [
 ("hook_search", "Vous tapez votre nom sur Google…"),
 ("hook_etla", "et là…"),
 ("hook_result", "ce résultat."),
 ("hook_old", "Un vieil article."),
 ("hook_info", "Une info dépassée."),
 ("hook_forget", "Quelque chose que vous préféreriez…"),
 ("hook_oublier", "oublier."),
 ("hook_good", "Bonne nouvelle : on peut le faire disparaître."),
 ("hook_how", "Voyons comment."),
 ("s1_intro", "D'abord, une distinction essentielle."),
 ("s1_deref", "DÉRÉFÉRENCER, c'est retirer un lien des résultats de Google."),
 ("s1_stays", "Le contenu, lui, existe toujours sur le site d'origine —"),
 ("s1_nobody", "simplement, plus personne ne tombe dessus en cherchant."),
 ("s1_suppr", "SUPPRIMER, en revanche, c'est effacer le contenu à la source,"),
 ("s1_source", "directement sur la page web."),
 ("s1_diff", "Et les deux ne s'obtiennent pas de la même façon…"),
 ("s1_people", "ni auprès des mêmes personnes."),
 ("s2_q", "Tout dépend d'une seule question :"),
 ("s2_mine", "est-ce que ce contenu est sur VOTRE site…"),
 ("s2_other", "ou sur celui de quelqu'un d'autre ?"),
 ("s3_intro", "Si c'est votre site, bonne nouvelle : vous avez la main."),
 ("s3_delete", "Vous pouvez supprimer la page."),
 ("s3_404", "Elle renverra alors une erreur quatre cent quatre…"),
 ("s3_410", "ou mieux, une quatre cent dix, qui dit clairement à Google :"),
 ("s3_gone", "« ce contenu a disparu. Définitivement. »"),
 ("s3_keep", "Vous voulez garder la page en ligne, mais hors de Google ?"),
 ("s3_noindex", "Ajoutez simplement une balise no-index."),
 ("s3_speed", "Et pour accélérer les choses,"),
 ("s3_gsc", "passez par l'outil de suppression de la Search Console :"),
 ("s3_mask", "il masque le résultat rapidement, le temps que Google prenne en compte vos modifications."),
 ("s4_intro", "Si le contenu est ailleurs, commencez par le plus simple :"),
 ("s4_mail", "écrivez au responsable du site."),
 ("s4_ask", "Demandez la suppression, l'anonymisation…"),
 ("s4_ask2", "ou, à défaut, l'ajout d'une balise no-index."),
 ("s4b_noreply", "Pas de réponse ?"),
 ("s4b_right", "Vous avez un droit : le droit à l'oubli, renforcé par le èr gé pé dé."),
 ("s4b_allows", "Il vous permet de demander à Google de ne plus associer votre nom à certaines pages."),
 ("s4b_form", "Pour cela, on remplit le formulaire officiel de Google,"),
 ("s4b_id", "avec une pièce d'identité,"),
 ("s4b_urls", "la liste EXACTE des adresses concernées…"),
 ("s4b_just", "et une justification solide."),
 ("s4b_crit", "Google accepte quand l'information est inexacte…"),
 ("s4b_c2", "périmée…"),
 ("s4b_c3", "non pertinente…"),
 ("s4b_c4", "ou excessive."),
 ("s4c_warn", "Attention, piège classique."),
 ("s4c_tool", "L'outil « contenu obsolète » de Google ne sert PAS à déréférencer une page toujours en ligne."),
 ("s4c_only", "Il sert seulement quand le site a déjà modifié ou supprimé la page…"),
 ("s4c_old", "mais que l'ancienne version traîne encore dans les résultats."),
 ("s5_no", "Et si Google dit non ?"),
 ("s5_notover", "Ce n'est pas fini."),
 ("s5_cnil", "Vous pouvez saisir la Cnil."),
 ("s5_force", "Si elle juge votre plainte légitime, elle peut OBLIGER le moteur de recherche à déréférencer le lien."),
 ("s6_recap", "En résumé :"),
 ("s6_mine", "votre site ? Vous agissez directement."),
 ("s6_third", "Un site tiers ? Vous contactez, puis vous activez votre droit à l'oubli."),
 ("s6_refus", "Un refus ?"),
 ("s6_cnil", "Vous saisissez la Cnil."),
 ("s6_cta", "Pour aller plus loin, avec les modèles d'e-mails et la checklist complète… retrouvez notre article en lien, juste en dessous."),
]

def syll(s):
    s = s.lower()
    s = re.sub(r"e\b", "", s)  # e muet final
    return max(1, len(re.findall(r"[aeiouyàâäéèêëîïôöùûü]+", s)))

w = [syll(t) for _, t in PHRASES]

out = subprocess.run(["ffmpeg", "-hide_banner", "-i", AUDIO, "-af",
    "silencedetect=noise=-45dB:d=0.28", "-f", "null", "-"],
    capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
dur = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups()[2]) + \
      60 * int(re.search(r"Duration: (\d+):(\d+)", out).group(2))
# segments de parole
lead = 0.55
segs = []
cur = lead
for s, e in zip(starts, ends):
    if s > cur + 0.05:
        segs.append((cur, s))
    cur = e
segs.append((cur, dur - 0.2))

total_sp = sum(b - a for a, b in segs)
rate = sum(w) / total_sp  # syllabes / seconde
P, S = len(PHRASES), len(segs)
INF = 1e18
# dp[i][j] : meilleures i premières phrases dans j premiers segments
dp = [[INF] * (S + 1) for _ in range(P + 1)]
bk = [[None] * (S + 1) for _ in range(P + 1)]
dp[0][0] = 0
pre = [0]
for x in w: pre.append(pre[-1] + x)
for j in range(1, S + 1):
    d = segs[j - 1][1] - segs[j - 1][0]
    for i in range(1, P + 1):
        for k in range(max(0, i - 8), i):
            if dp[k][j - 1] >= INF: continue
            pred = (pre[i] - pre[k]) / rate
            c = dp[k][j - 1] + math.log(d / pred) ** 2 * (1 + d)
            if c < dp[i][j]:
                dp[i][j] = c; bk[i][j] = k
# reconstruct
i, j = P, S
assign = []
while j > 0:
    k = bk[i][j]
    assign.append((k, i, j - 1)); i, j = k, j - 1
assign.reverse()
cues = {}
for k, i, sj in assign:
    a, b = segs[sj]
    tot = pre[i] - pre[k]
    t = a
    for p in range(k, i):
        cues[PHRASES[p][0]] = round(t, 2)
        t += (b - a) * w[p] / tot
    print(f"{a:7.2f}-{b:7.2f} ({b-a:4.1f}s, pred {tot/rate:4.1f}s) | " + " / ".join(PHRASES[p][1][:40] for p in range(k, i)))
cues["_end"] = round(dur, 2)
json.dump(cues, open(OUT, "w"), indent=1, ensure_ascii=False)
