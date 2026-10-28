# KidLearn — Character restoration method v1.0.1
Date: 2026-10-28.

## Hard style lock
- Robot: original blue/cyan mascot style B, armor, large eyes, book emblem, dark blue outline, moderate gloss.
- Boys/girls: original approved educational chibi, brown hair, large eyes, pink cheeks, bright palette, soft shading. Keep face, hair, clothing and body design unchanged.
- Do **not** generate a stylistic substitute. Never replace source characters with search images.
- Original 5 source composite sheets in v1.0.0 are the ONLY pixel authority.

## Reproduction workflow / prompt registry
This is a deterministic source-extraction repair, **not** a text-to-image generation prompt. Copy the existing pixel content from the correct connected alpha component in each 3x2 original source sheet; preserve the full extents of hair, arms, desk, feet, accessories and book. Extend outside canvas using transparent alpha only, not invented pixels. Place 20px transparent margin around component. Export PNG RGBA (alpha 0-255) and WebP with transparency (quality 91, method 6). Never crop through visible pixels. Visual review on cream, white, pale blue, navy at 96px and 300px.
All six edited IDs and checksums appear in `assets/RELEASE_INDEX_V1_0_1.csv`.
Review state = REVIEW_REQUIRED; do not infer APPROVED from a checksum.
