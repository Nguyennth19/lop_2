# KidLearn — 2D Storybook style lock V3

**LOCKED 2026-10-28.** Applies to all new educational illustrations: SH01–SH12 and M01–M12, 24 sheets / 288 catalog entries. Existing approved Robot B / Boy / Girl character art v1.0.1 remains unchanged.

## Style
Vietnamese children's workbook illustration, cheerful saturated harmonious colors, rounded clearly visible dark-colored contours. Use flat fills and 2–4 **distinct hard-edged color patches** per part for volume, small dots and crisp short highlights. Avoid soft airbrush, blurred gradients, glossy 3D/plastic treatment, bloom, glow, realistic texture and fuzzy cast shadows. Clear at 96px. Mathematics requiring exact marks, measurement, currency or clock values must use validated sources or programmatic precision.

## Source sheet mandatory contract
- 12 catalog objects exactly, 4 columns × 3 rows, ordered left-to-right, top-to-bottom.
- Preferred 2048×1536 RGBA PNG: 512×512 per invisible cell. No artificial upscale.
- Reserve **40px minimum transparent margin** inside all four edges of each cell (aim 48–64 px).
- **Genuine transparent alpha**, not checkerboard rendered into pixels; transparent border, no background.
- No text, titles, IDs, watermarks, dividers, borders, decoration or extra objects.
- No overlap or clipping of object silhouette, leaf, stem or accessory.
- Names: `SH01_SOURCE_SHEET_V3.png` … `SH12_SOURCE_SHEET_V3.png`, `M01_SOURCE_SHEET_V3.png` … `M12_SOURCE_SHEET_V3.png`.
- Canonical object ordering from `ASSET_CATALOG_288.csv`; do not infer it from a preview sheet.

## Production and QA
1. Generate 12 exact objects; verify categories and locked style.
2. Validate actual RGBA alpha and inspect full object containment within 40px inset of each 512px cell.
3. Inspect on white, cream, light blue, navy and at 96px; check for fake checkerboard and blurry halos.
4. Only upload passing sheets to relevant Drive `00_SOURCE_SHEETS` and label `CUT_READY`.
5. User cuts and exports one PNG RGBA per asset ID into `01_PNG_MASTER`. Convert to WebP automatically at release.
6. QA states: DRAFT → QA_PENDING / NEEDS_REPAIR → CUT_READY → CUT_DONE → APPROVED. Storage `SYNCED_VERIFIED` is a *separate* check after Drive + GitHub readback.

## Canonical generation prompt
Produce a 2048×1536 transparent RGBA sheet with EXACTLY 12 specified objects, arranged in an invisible 4-column × 3-row grid. Each object centered in a 512px square, at least 40px fully transparent inset from all cell borders. Vietnamese 2D storybook workbook art: cheerful colors, thick rounded dark outlines, flat base colors and distinct sharp-boundary patches/texture dots, **no soft gradients, airbrush, plastic gloss, glow, shadow, photorealism**. No title, text, numbering, grid lines, border, scenic background, extra props or clipped details. Row-major items: [INSERT 12 CANONICAL CATALOG ITEMS]. Verify resulting alpha pixels before marking CUT_READY.

**No automatic style changes to Robot B, Boy or Girl.** Full working copy with acceptance gates is available on Drive in the V3 style-lock document.
