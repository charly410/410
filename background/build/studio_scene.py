# Fond studio podcast 410 Gone : scène Blender (Cycles), assets Poly Haven CC0.
# Usage : python studio_scene.py --out rendu.png [--res 1920 1080] [--samples 256] [--fstop 2.8]
import argparse, math, os, random, sys
import bpy, bmesh
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
BRAND = os.path.join(HERE, "brand")

ap = argparse.ArgumentParser()
ap.add_argument("--out", required=True)
ap.add_argument("--res", type=int, nargs=2, default=[1920, 1080])
ap.add_argument("--samples", type=int, default=256)
ap.add_argument("--fstop", type=float, default=4.0)
ap.add_argument("--focus", type=float, default=1.0)
args = ap.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:])

random.seed(410)
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

WALL_Y = 3.2          # mur du fond
ROOM_X = 2.35         # demi-largeur de la pièce
CEIL = 2.7

# ---------------------------------------------------------------- utilitaires

def srgb(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((v + 0.055) / 1.055) ** 2.4 if v > 0.04045 else v / 12.92 for v in c) + (1.0,)


def tex(name):
    for root, _, files in os.walk(ASSETS):
        if name in files:
            return os.path.join(root, name)
    raise FileNotFoundError(name)


def img_node(nt, path, non_color=False, proj="BOX"):
    n = nt.nodes.new("ShaderNodeTexImage")
    n.image = bpy.data.images.load(path, check_existing=True)
    if non_color:
        n.image.colorspace_settings.name = "Non-Color"
    n.projection = proj
    n.projection_blend = 0.25
    return n


def pbr_mat(name, prefix, scale=1.0, tint=None, tint_fac=1.0, rough_mul=1.0, rough_add=0.0,
            normal_strength=1.0, random_offset=False, mono=None):
    """Matériau PBR en projection boîte sur coordonnées objet (taille réelle)."""
    m = bpy.data.materials.new(name)
    nt = m.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    tc = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (scale, scale, scale)
    src = tc.outputs["Object"]
    if random_offset:
        oi = nt.nodes.new("ShaderNodeObjectInfo")
        mul = nt.nodes.new("ShaderNodeVectorMath"); mul.operation = "SCALE"
        mul.inputs["Scale"].default_value = 37.0
        nt.links.new(oi.outputs["Random"], mul.inputs[0])
        add = nt.nodes.new("ShaderNodeVectorMath"); add.operation = "ADD"
        nt.links.new(tc.outputs["Object"], add.inputs[0]); nt.links.new(mul.outputs[0], add.inputs[1])
        src = add.outputs[0]
    nt.links.new(src, mp.inputs["Vector"])
    d = img_node(nt, tex(prefix + "_diff_2k.jpg"))
    nt.links.new(mp.outputs[0], d.inputs[0])
    col = d.outputs["Color"]
    if mono:  # garde la trame de la texture, impose la teinte
        bw = nt.nodes.new("ShaderNodeRGBToBW"); nt.links.new(col, bw.inputs[0])
        mr = nt.nodes.new("ShaderNodeMapRange")
        mr.inputs["To Min"].default_value, mr.inputs["To Max"].default_value = mono
        nt.links.new(bw.outputs[0], mr.inputs[0])
        col = mr.outputs[0]
    if tint:
        mix = nt.nodes.new("ShaderNodeMix"); mix.data_type = "RGBA"; mix.blend_type = "MULTIPLY"
        mix.inputs["Factor"].default_value = tint_fac
        nt.links.new(col, mix.inputs["A"]); mix.inputs["B"].default_value = tint
        col = mix.outputs["Result"]
    nt.links.new(col, bsdf.inputs["Base Color"])
    for ext in (".jpg", ".exr", ".png"):
        try:
            r = img_node(nt, tex(prefix + "_rough_2k" + ext), True); break
        except FileNotFoundError:
            r = None
    if r:
        nt.links.new(mp.outputs[0], r.inputs[0])
        ma = nt.nodes.new("ShaderNodeMath"); ma.operation = "MULTIPLY_ADD"
        ma.inputs[1].default_value = rough_mul; ma.inputs[2].default_value = rough_add
        nt.links.new(r.outputs["Color"], ma.inputs[0]); nt.links.new(ma.outputs[0], bsdf.inputs["Roughness"])
    try:
        n = img_node(nt, tex(prefix + "_nor_gl_2k.exr"), True)
        nm = nt.nodes.new("ShaderNodeNormalMap"); nm.inputs["Strength"].default_value = normal_strength
        nt.links.new(mp.outputs[0], n.inputs[0]); nt.links.new(n.outputs["Color"], nm.inputs["Color"])
        nt.links.new(nm.outputs["Normal"], bsdf.inputs["Normal"])
    except FileNotFoundError:
        pass
    return m


def flat_mat(name, color, rough=0.5, metal=0.0, emit=None, strength=0.0):
    m = bpy.data.materials.new(name)
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = color
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit:
        b.inputs["Emission Color"].default_value = emit
        b.inputs["Emission Strength"].default_value = strength
    return m


def box(name, size, loc, mat, bevel=0.0):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * size[0], v.co.y * size[1], v.co.z * size[2]))
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(name, me); scene.collection.objects.link(o)
    o.location = loc
    o.data.materials.append(mat)
    if bevel:
        mod = o.modifiers.new("bev", "BEVEL"); mod.width = bevel; mod.segments = 3
        mod.limit_method = "NONE"
    for p in me.polygons:
        p.use_smooth = bool(bevel)
    return o


def plane(name, verts, mat):
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], [list(range(len(verts)))])
    o = bpy.data.objects.new(name, me); scene.collection.objects.link(o)
    o.data.materials.append(mat)
    return o


def append(blend_rel, names=None):
    path = os.path.join(ASSETS, blend_rel)
    with bpy.data.libraries.load(path) as (src, dst):
        dst.objects = [n for n in src.objects if (names is None or n in names) and "stash" not in n]
    objs = [o for o in dst.objects if o and o.type == "MESH"]
    return objs


def place(objs, loc, rot_z=0.0, scale=1.0, center=False):
    """Regroupe les objets sous un vide (pour déplacer un asset multi-objets)."""
    e = bpy.data.objects.new("grp", None); scene.collection.objects.link(e)
    if center:  # ramène l'asset à l'origine (pied centré, posé au sol)
        pts = [o.matrix_world @ Vector(c) for o in objs for c in o.bound_box]
        off = Vector(((min(p.x for p in pts) + max(p.x for p in pts)) / 2,
                      (min(p.y for p in pts) + max(p.y for p in pts)) / 2, min(p.z for p in pts)))
        for o in objs:
            if o.parent is None or o.parent not in objs:
                o.location -= off
    for o in objs:
        scene.collection.objects.link(o)
        o.parent = e
        o.matrix_parent_inverse.identity()
    e.location = loc; e.rotation_euler = (0, 0, rot_z); e.scale = (scale,) * 3
    return e


def area_light(name, loc, rot, size, power, color=(1, 1, 1), size_y=None, spread=None):
    l = bpy.data.lights.new(name, "AREA"); l.energy = power; l.color = color[:3]
    if size_y:
        l.shape = "RECTANGLE"; l.size = size; l.size_y = size_y
    else:
        l.size = size
    if spread:
        l.spread = math.radians(spread)
    o = bpy.data.objects.new(name, l); scene.collection.objects.link(o)
    o.location = loc; o.rotation_euler = [math.radians(a) for a in rot]
    return o


def point_light(name, loc, power, color, radius=0.02):
    l = bpy.data.lights.new(name, "POINT"); l.energy = power; l.color = color[:3]; l.shadow_soft_size = radius
    o = bpy.data.objects.new(name, l); scene.collection.objects.link(o); o.location = loc
    return o


def kelvin(k):
    # approximation Tanner Helland, renvoie du RVB linéaire
    t = k / 100
    r = 255 if t <= 66 else 329.698727446 * ((t - 60) ** -0.1332047592)
    g = 99.4708025861 * math.log(t) - 161.1195681661 if t <= 66 else 288.1221695283 * ((t - 60) ** -0.0755148492)
    b = 255 if t >= 66 else (0 if t <= 19 else 138.5177312231 * math.log(t - 10) - 305.0447927307)
    return srgb("#%02x%02x%02x" % tuple(int(max(0, min(255, c))) for c in (r, g, b)))

WARM = kelvin(2700)
NEUTRAL = kelvin(4200)

# ---------------------------------------------------------------- pièce

wall_mat = pbr_mat("mur", "beige_wall_001", scale=0.45, tint=srgb("#2B2A3A"), rough_mul=0.6, rough_add=0.35,
                   normal_strength=0.6)
plane("mur_fond", [(-ROOM_X, WALL_Y, 0), (ROOM_X, WALL_Y, 0), (ROOM_X, WALL_Y, CEIL), (-ROOM_X, WALL_Y, CEIL)], wall_mat)
plane("mur_g", [(-ROOM_X, -1.5, 0), (-ROOM_X, WALL_Y, 0), (-ROOM_X, WALL_Y, CEIL), (-ROOM_X, -1.5, CEIL)], wall_mat)
plane("mur_d", [(ROOM_X, WALL_Y, 0), (ROOM_X, -1.5, 0), (ROOM_X, -1.5, CEIL), (ROOM_X, WALL_Y, CEIL)], wall_mat)
plane("mur_av", [(ROOM_X, -1.5, 0), (-ROOM_X, -1.5, 0), (-ROOM_X, -1.5, CEIL), (ROOM_X, -1.5, CEIL)], wall_mat)
ceil_mat = flat_mat("plafond", srgb("#1C1B24"), rough=0.9)
plane("plafond", [(-ROOM_X, -1.5, CEIL), (-ROOM_X, WALL_Y, CEIL), (ROOM_X, WALL_Y, CEIL), (ROOM_X, -1.5, CEIL)], ceil_mat)
floor_mat = pbr_mat("parquet", "black_walnut_veneer_01", scale=0.7, tint=srgb("#8A7A70"), rough_mul=0.8, rough_add=0.1)
plane("sol", [(-ROOM_X, -1.5, 0), (ROOM_X, -1.5, 0), (ROOM_X, WALL_Y, 0), (-ROOM_X, WALL_Y, 0)], floor_mat)
# plinthe
box("plinthe", (2 * ROOM_X, 0.015, 0.08), (0, WALL_Y - 0.0075, 0.04), flat_mat("plinthe", srgb("#24232F"), 0.6))

# ---------------------------------------------------------------- mur de lattes (gauche)

SL_X0, SL_X1, SL_Z0, SL_Z1 = -2.12, -0.62, 0.0, 2.48
felt = flat_mat("feutre", srgb("#121116"), rough=1.0)
standoff = 0.03
back_y = WALL_Y - standoff - 0.006
box("feutre", (SL_X1 - SL_X0, 0.012, SL_Z1 - SL_Z0), ((SL_X0 + SL_X1) / 2, back_y, (SL_Z0 + SL_Z1) / 2), felt)
walnut = pbr_mat("noyer", "black_walnut_veneer_01", scale=1.6, tint=srgb("#A8968A"), rough_mul=0.7, rough_add=0.15,
                 random_offset=True)
slat_w, slat_gap = 0.027, 0.013
n_slats = int((SL_X1 - SL_X0 + slat_gap) / (slat_w + slat_gap))
x = SL_X0 + slat_w / 2
SLAT_FRONT = back_y - 0.006 - 0.021
for i in range(n_slats):
    box(f"latte_{i}", (slat_w, 0.021, SL_Z1 - SL_Z0), (x, back_y - 0.006 - 0.0105, (SL_Z0 + SL_Z1) / 2), walnut, bevel=0.002)
    x += slat_w + slat_gap
# halo LED indigo derrière le panneau
halo = flat_mat("led_halo", (0, 0, 0, 1), emit=srgb("#6F5CF0"), strength=14.0)
box("led_haut", (SL_X1 - SL_X0 - 0.06, 0.01, 0.01), ((SL_X0 + SL_X1) / 2, WALL_Y - 0.012, SL_Z1 - 0.02), halo)
box("led_droite", (0.01, 0.01, SL_Z1 - 0.1), (SL_X1 - 0.02, WALL_Y - 0.012, SL_Z1 / 2), halo)

# ---------------------------------------------------------------- enseigne néon 410 Gone

bpy.ops.preferences.addon_enable(module="io_curve_svg")
before = set(bpy.data.objects)
bpy.ops.import_curve.svg(filepath=os.path.join(BRAND, "logo-410gone-orange.svg"))
logo = [o for o in bpy.data.objects if o not in before and o.type == "CURVE"]
# cadre utile du logo (unités Blender après import)
mn = Vector((min(o.bound_box[i][0] + o.location.x for o in logo for i in range(8)),
             min(o.bound_box[i][1] + o.location.y for o in logo for i in range(8)), 0))
mx = Vector((max(o.bound_box[i][0] + o.location.x for o in logo for i in range(8)),
             max(o.bound_box[i][1] + o.location.y for o in logo for i in range(8)), 0))
LOGO_W = 0.95
k = LOGO_W / (mx.x - mn.x)
ctr = (mn + mx) / 2
neon_white = flat_mat("neon_blanc", srgb("#FFF6EA"), rough=0.35, emit=srgb("#FFF1DC"), strength=5.0)
neon_orange = flat_mat("neon_orange", srgb("#FFB400"), rough=0.35, emit=srgb("#FFB400"), strength=4.5)
LOGO_POS = Vector((-1.29, SLAT_FRONT - 0.045, 1.72))
for o in logo:
    white = o.data.materials and o.data.materials[0].diffuse_color[2] > 0.5
    o.data.extrude = 0.008 / k
    o.data.bevel_depth = 0.004 / k
    o.data.materials.clear(); o.data.materials.append(neon_white if white else neon_orange)
    # SVG importé dans le plan XY : on le redresse contre le mur
    o.location = (o.location.x - ctr.x, o.location.y - ctr.y, 0)
    e = bpy.data.objects.new("logo_pivot", None); scene.collection.objects.link(e)
    o.parent = e
    e.scale = (k, k, k); e.rotation_euler = (math.radians(90), 0, 0); e.location = LOGO_POS
# lumière que le néon projette sur les lattes : petites sources le long des tracés
bpy.context.view_layer.update()
for o in logo:
    col = o.data.materials[0].node_tree.nodes["Principled BSDF"].inputs["Emission Color"].default_value
    last = None
    for sp in o.data.splines:
        for bp in sp.bezier_points:
            w = o.matrix_world @ bp.co
            if last is None or (w - last).length > 0.035:
                pl = point_light("neon_px", (w.x, SLAT_FRONT - 0.014, w.z), 0.35, tuple(col), radius=0.012)
                pl.visible_camera = False
                last = w
chrome = flat_mat("chrome", srgb("#D8D8DC"), rough=0.2, metal=1.0)
for dx in (-1, 1):
    for dz in (-1, 1):
        s = box("entretoise", (0.014, SLAT_FRONT - LOGO_POS.y, 0.014),
                (LOGO_POS.x + dx * 0.42, (SLAT_FRONT + LOGO_POS.y) / 2, LOGO_POS.z + 0.03 + dz * 0.22),
                chrome, bevel=0.006)

# ---------------------------------------------------------------- panneaux acoustiques indigo (centre)

fabric = pbr_mat("tissu_indigo", "caban", scale=5.0, tint=srgb("#31249F"), rough_mul=0.2, rough_add=0.78,
                 normal_strength=0.7, mono=(0.55, 1.3))
for i, xc in enumerate((-0.33, 0.03, 0.39)):
    box(f"panneau_{i}", (0.33, 0.05, 1.25), (xc, WALL_Y - 0.026, 1.52), fabric, bevel=0.012)

# ---------------------------------------------------------------- buffet bas (centre)

cab = append("modern_wooden_cabinet/modern_wooden_cabinet_2k.blend")
g = place(cab, (-0.02, WALL_Y - 0.25, 0.0))
g.scale = (0.72, 0.68, 0.88)
cp = append("cassette_player/cassette_player_2k.blend")
place(cp, (-0.72, WALL_Y - 0.25, 0.60), rot_z=math.radians(-80), scale=1.0)
vc = append("vintage_video_camera/vintage_video_camera_2k.blend")
place(vc, (-0.50, WALL_Y - 0.22, 0.60), rot_z=math.radians(-110))
vase = append("ceramic_vase_03/ceramic_vase_03_2k.blend")
place(vase, (0.66, WALL_Y - 0.24, 0.60), scale=0.8)
pp2 = append("potted_plant_04/potted_plant_04_2k.blend")
place(pp2, (0.46, WALL_Y - 0.24, 0.60), scale=1.3)

# ---------------------------------------------------------------- étagère (droite)

SH_X = 1.34
sh = append("wooden_display_shelves_01/wooden_display_shelves_01_2k.blend")
place(sh, (SH_X, WALL_Y - 0.19, 0.0))
LEVELS = [0.414, 0.79, 1.165]
books = [o for o in append("decorative_book_set_01/decorative_book_set_01_1k.blend")
         if o.name.startswith(("book_hardcover", "book_softcover", "catalogue"))]
random.shuffle(books)
bi = 0


def book_row(x0, x1, z, y=WALL_Y - 0.21, lean_last=True):
    global bi
    x = x0
    last = None
    while bi < len(books):
        b = books[bi]
        w = b.dimensions.x
        if x + w > x1:
            break
        scene.collection.objects.link(b)
        b.location = (x + w / 2, y, z); b.rotation_euler = (0, 0, 0)
        x += w + random.uniform(0.0, 0.004)
        last = b; bi += 1
    if lean_last and last:
        last.rotation_euler = (0, math.radians(12), 0)
        last.location.x += 0.02


def book_stack(xc, z, n, y=WALL_Y - 0.21):
    global bi
    for j in range(n):
        b = books[bi]; bi += 1
        scene.collection.objects.link(b)
        b.rotation_euler = (0, math.radians(90), math.radians(90 + random.uniform(-6, 6)))
        b.location = (xc, y, z + b.dimensions.x / 2 + sum(books[bi - 1 - t].dimensions.x for t in range(1, j + 1)) * 0)
        z_off = sum(bb.dimensions.x for bb in books[bi - j - 1:bi - 1])
        b.location.z = z + z_off + b.dimensions.x / 2


book_row(SH_X - 0.50, SH_X + 0.05, LEVELS[0])
plant = append("calathea_orbifolia_01/calathea_orbifolia_01_2k.blend")
place(plant, (SH_X + 0.30, WALL_Y - 0.19, LEVELS[0]), scale=0.62)
book_stack(SH_X - 0.33, LEVELS[1], 4)
vc2 = append("ceramic_vase_01/ceramic_vase_01_2k.blend")
place(vc2, (SH_X - 0.05, WALL_Y - 0.2, LEVELS[1]), scale=0.62)
book_row(SH_X + 0.12, SH_X + 0.50, LEVELS[1])
pp = append("potted_plant_04/potted_plant_04_2k.blend")
place(pp, (SH_X - 0.32, WALL_Y - 0.2, LEVELS[2]), scale=0.95)
book_row(SH_X - 0.12, SH_X + 0.48, LEVELS[2])
fr = append("standing_picture_frame_01/standing_picture_frame_01_2k.blend")
place(fr, (SH_X - 0.25, WALL_Y - 0.2, 1.542), rot_z=math.radians(8))
book_stack(SH_X + 0.22, 1.542, 3)
# rubans LED chauds sous les tablettes
strip = flat_mat("led_chaud", (0, 0, 0, 1), emit=WARM, strength=10.0)
for z in LEVELS[1:] + [1.542]:
    box("led_tablette", (0.96, 0.008, 0.004), (SH_X, WALL_Y - 0.33, z - 0.022), strip)

# ---------------------------------------------------------------- enseigne ON AIR

ON_POS = Vector((1.30, WALL_Y - 0.05, 2.14))
frame = flat_mat("boitier", srgb("#101014"), rough=0.4, metal=0.6)
box("onair_boitier", (0.62, 0.07, 0.21), ON_POS, frame, bevel=0.01)
face = flat_mat("onair_face", srgb("#FFB400"), rough=0.3, emit=srgb("#FFB400"), strength=1.3)
box("onair_face", (0.57, 0.004, 0.16), ON_POS + Vector((0, -0.036, 0)), face)
fc = bpy.data.curves.new("onair_txt", "FONT"); fc.body = "ON AIR"
fc.font = bpy.data.fonts.load(os.path.join(BRAND, "Oswald-SemiBold.ttf"))
fc.size = 0.125; fc.align_x = "CENTER"; fc.align_y = "CENTER"; fc.extrude = 0.001; fc.space_character = 1.15
t = bpy.data.objects.new("onair_txt", fc); scene.collection.objects.link(t)
t.data.materials.append(flat_mat("onair_lettres", srgb("#1A1406"), rough=0.6))
t.rotation_euler = (math.radians(90), 0, 0); t.location = ON_POS + Vector((0, -0.04, 0))

# ---------------------------------------------------------------- applique murale

sc = append("industrial_wall_sconce/industrial_wall_sconce_2k.blend")
place(sc, (0.80, WALL_Y, 1.86), rot_z=math.radians(90))
point_light("ampoule_applique", (0.80, WALL_Y - 0.17, 1.80), 18, WARM, radius=0.03)

# ---------------------------------------------------------------- plantes au sol

p1 = append("potted_plant_01/potted_plant_01_1k.blend")
place(p1, (-1.78, WALL_Y - 0.5, 0.0), rot_z=math.radians(30), center=True)

# ---------------------------------------------------------------- éclairage

# douche douce venant du plafond, côté caméra (simule la boîte à lumière du tournage)
area_light("fill", (0.0, 0.3, 2.55), (40, 0, 0), 2.0, 70, NEUTRAL, size_y=1.0)
# lèche-mur chaud au plafond
area_light("wash", (0.0, WALL_Y - 0.6, 2.62), (-25, 0, 0), 3.4, 55, WARM, size_y=0.3, spread=70)

# douche de lumière sur les panneaux indigo : détache la tête et les épaules du fond
sp = bpy.data.lights.new("spot_panneaux", "SPOT"); sp.energy = 90; sp.color = kelvin(3600)[:3]
sp.spot_size = math.radians(55); sp.spot_blend = 0.9; sp.shadow_soft_size = 0.15
spo = bpy.data.objects.new("spot_panneaux", sp); scene.collection.objects.link(spo)
spo.location = (0.03, WALL_Y - 1.0, 2.66)
d = Vector((0.03, WALL_Y, 1.45)) - spo.location
spo.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()

# ---------------------------------------------------------------- caméra & rendu

cam_d = bpy.data.cameras.new("cam"); cam_d.lens = 28; cam_d.sensor_width = 36
cam_d.dof.use_dof = True; cam_d.dof.focus_distance = args.focus; cam_d.dof.aperture_fstop = args.fstop
cam_d.dof.aperture_blades = 7
cam = bpy.data.objects.new("cam", cam_d); scene.collection.objects.link(cam)
cam.location = (0.0, 0.0, 1.22); cam.rotation_euler = (math.radians(90), 0, 0)
scene.camera = cam

world = bpy.data.worlds.new("w"); world.color = (0, 0, 0); scene.world = world

scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = args.samples
scene.cycles.use_denoising = True
scene.cycles.max_bounces = 8
scene.cycles.caustics_reflective = False; scene.cycles.caustics_refractive = False
scene.render.resolution_x, scene.render.resolution_y = args.res
scene.render.resolution_percentage = 100
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "AgX - Medium High Contrast"
scene.view_settings.exposure = 0.25
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_depth = "16"
scene.render.filepath = args.out
if not os.environ.get("NO_RENDER"):
    bpy.ops.render.render(write_still=True)
print("rendu :", args.out)
