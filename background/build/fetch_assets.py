# Télécharge les assets Poly Haven (CC0) utilisés par studio_scene.py dans build/assets/.
# Usage : python -I fetch_assets.py
import json, os, urllib.request

ASSETS = {
    "wooden_display_shelves_01": "2k", "decorative_book_set_01": "1k", "potted_plant_01": "1k",
    "potted_plant_04": "2k", "industrial_wall_sconce": "2k", "vintage_video_camera": "2k",
    "cassette_player": "2k", "ceramic_vase_01": "2k", "ceramic_vase_03": "2k",
    "calathea_orbifolia_01": "2k", "modern_wooden_cabinet": "2k", "standing_picture_frame_01": "2k",
    # textures
    "black_walnut_veneer_01": "2k", "beige_wall_001": "2k", "caban": "2k",
}
DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

o = urllib.request.build_opener(); o.addheaders = [("User-Agent", "410gone-studio-bg/1.0")]
urllib.request.install_opener(o)


def get(url, path):
    if os.path.exists(path):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(url, path + ".part"); os.rename(path + ".part", path)


for aid, res in ASSETS.items():
    d = json.load(urllib.request.urlopen(f"https://api.polyhaven.com/files/{aid}"))
    b = d["blend"][res]["blend"]; root = os.path.join(DEST, aid)
    get(b["url"], os.path.join(root, os.path.basename(b["url"])))
    for rel, f in b["include"].items():
        get(f["url"], os.path.join(root, rel))
    print("ok", aid, flush=True)
