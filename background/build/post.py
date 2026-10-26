# Finition « caméra » du rendu : halo des néons, vignettage léger, grain fin.
# Usage : python post.py rendu_16bits.png sortie_4k.png sortie_1080p.png
import sys
import cv2
import numpy as np

src, out4k, out1080 = sys.argv[1:4]
raw = cv2.imread(src, cv2.IMREAD_UNCHANGED)[..., :3]
img = raw.astype(np.float32) / (65535.0 if raw.dtype == np.uint16 else 255.0)
h, w = img.shape[:2]

# halo : uniquement les hautes lumières (néons, ON AIR, ampoule)
lum = img @ np.array([0.0722, 0.7152, 0.2126], np.float32)  # BGR
mask = np.clip((lum - 0.78) / 0.22, 0, 1)[..., None]
hi = img * mask
bloom = sum(cv2.GaussianBlur(hi, (0, 0), s * w / 3840) * k for s, k in ((6, 0.35), (18, 0.25), (48, 0.18)))
img = 1 - (1 - img) * (1 - bloom)  # mode écran

# vignettage optique doux
yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) / np.sqrt(2)
img *= (1 - 0.18 * r ** 2.2)[..., None]

# grain de capteur, plus visible dans les ombres
rng = np.random.default_rng(410)
grain = rng.normal(0, 1, (h, w, 1)).astype(np.float32)
grain = cv2.GaussianBlur(grain, (0, 0), 0.6)[..., None]
img += grain * (0.012 * (1 - lum[..., None]) + 0.004)

img = np.clip(img, 0, 1)
cv2.imwrite(out4k, (img * 255 + 0.5).astype(np.uint8), [cv2.IMWRITE_PNG_COMPRESSION, 9])
small = cv2.resize(img, (1920, 1080), interpolation=cv2.INTER_AREA)
cv2.imwrite(out1080, (small * 255 + 0.5).astype(np.uint8), [cv2.IMWRITE_PNG_COMPRESSION, 9])
print("ok", out4k, out1080)
