#!/usr/bin/env python3
"""KidLearn release verifier. Safe local read-only checks; no Drive token required."""
from pathlib import Path
from PIL import Image
import csv, hashlib, sys
root=Path(sys.argv[1] if len(sys.argv)>1 else ".").resolve()
path=root/"ASSET_MANIFEST.csv"
if not path.exists(): raise SystemExit("Missing ASSET_MANIFEST.csv")
rows=list(csv.DictReader(path.open(encoding="utf-8-sig",newline="")))
errors=[]
for row in rows:
    asset=row["asset_id"]
    png=root/row["png_path"]
    webp=root/row["webp_path"]
    if not png.exists() or not webp.exists():
        errors.append(f"{asset}: missing PNG or WebP"); continue
    got=hashlib.sha256(png.read_bytes()).hexdigest()
    if got!=row["sha256"]: errors.append(f"{asset}: checksum mismatch")
    im=Image.open(png).convert("RGBA")
    lo,hi=im.getchannel("A").getextrema()
    if not (lo==0 and hi==255): errors.append(f"{asset}: alpha not genuinely mixed")
    if Image.open(webp).mode not in {"RGBA","LA"}: errors.append(f"{asset}: WebP lacks alpha")
print(f"Checked {len(rows)} assets, errors={len(errors)}")
for err in errors: print(" - "+err)
if any(r["review_status"]!="SYNCED_VERIFIED" for r in rows):
    print("Note: this release still requires human QA and two-store readback.")
raise SystemExit(bool(errors))
