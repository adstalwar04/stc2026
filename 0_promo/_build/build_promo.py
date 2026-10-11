#!/usr/bin/env python3
"""Build workshop_promo.html: one self-contained file with the mascots embedded.

Reads _build/promo_template.html, the mascot PNGs in _build/mascots/, and
_build/stc_india_logo.svg. Writes ../workshop_promo.html.
"""
import base64, io, json, os, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.environ.get("MASCOT_DIR") or os.path.join(HERE, "mascots")
NAMES = ["presenting", "reading", "idea", "explaining", "laptop", "confused", "happy", "thinking"]

def encode(name):
    im = Image.open(os.path.join(ASSETS, f"mascot_{name}.png")).convert("RGBA")
    im.thumbnail((480, 600))
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=82, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()

imgs = {n: encode(n) for n in NAMES}
tpl = open(os.path.join(HERE, "promo_template.html"), encoding="utf-8").read()
logo = "data:image/svg+xml;base64," + base64.b64encode(open(os.path.join(HERE, "stc_india_logo.svg"), "rb").read()).decode()
out = tpl.replace("__IMAGES__", json.dumps(imgs)).replace("__LOGO__", logo)
dest = os.path.join(HERE, "..", "workshop_promo.html")
open(dest, "w", encoding="utf-8").write(out)
print(f"Wrote {os.path.abspath(dest)} ({len(out)//1024} KB)")
