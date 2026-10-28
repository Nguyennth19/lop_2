# KidLearn — QA & dual-storage verification v1.0.1
Date: 2026-10-28 (ICT). Release candidate for human visual approval.

## Scope and checks
- Original ZIP v1.0.0 SHA-256: `80917390a3979b32175e9ced4024669ac1be345e655d96fc41707373ebad1a99`. Source images: 5 locked RGBA character sheets.
- Audited 30 PNG and 30 WebP derivatives; identified 6 cutout defects. Re-extracted exactly 6 poses from their corresponding locked source sheets. No new face, hairstyle, costume or visual style generated.
- Other 24 PNG/WebP pairs reused unchanged from v1.0.0 (byte identical).
- All 30 PNGs have true transparent alpha; all 30 WebPs decode with transparency. Contact sheet visual review and source comparisons completed. Preview with homepage, Math and Vietnamese worksheets provided in the ZIP for manual Chrome review.
- 12 repaired image files uploaded to Drive, downloaded back and compared with local SHA-256; uploaded to GitHub as real binary blobs, then SHA-1 Git blob readback matches.
- New 5 source-sheet copies stored on Drive strictly as references. Original v1.0.0 maintained unchanged.
- Release ZIP uploaded to Drive as `KidLearn_Release_v1.0.1.zip`, downloaded back: exact size **19,627,955 bytes**, SHA-256 **185a461e8d1754dbf73bf7110423530f1c78fc79e302a00cdba9fc5534035305**, ZIP archive test successful. [Drive ZIP](https://drive.google.com/file/d/1zBQI1aAWYIr6-bhD49LTdvYWAgNJ_KI2/view). [Drive release folder](https://drive.google.com/drive/folders/1lDde-KUs8sc5UQ3GP0GEuPdLmn2YqT2x).
- GitHub v1.0.1 branch contains 12 changed PNG/WebP binaries and versioned manifest; no merge into `main`.

## Defects and repairs
| Asset canonical ID | Severity | Defect | Resolution |
|---|---|---|---|
| `KL_BOY_HOME_03_write_table` | MEDIUM | Left desk and table top cut | Re-extract from locked RGBA source; preserve original character |
| `KL_BOY_SCHOOL_04_write_desk` | HIGH | Desk right edge and leg cut | Re-extract from locked RGBA source; preserve original character |
| `KL_BOY_SCHOOL_05_point_book` | HIGH | Head and hair clipped | Re-extract from locked RGBA source; preserve original character |
| `KL_GIRL_HOME_03_write_table` | MEDIUM | Desk and hair bow clipped | Re-extract from locked RGBA source; preserve original character |
| `KL_GIRL_SCHOOL_04_write_desk` | MEDIUM | Desk right edge cut | Re-extract from locked RGBA source; preserve original character |
| `KL_GIRL_SCHOOL_05_point_book` | HIGH | Pointing arm and held pencil cut | Re-extract from locked RGBA source; preserve original character |

## Release gate
**STORAGE: SYNCED_VERIFIED** for 12 replaced PNG/WebP, carried assets verified in v1.0.0, and ZIP; GitHub metadata + Drive files verified.
**ART: REVIEW_REQUIRED** for all 30 until human reviews full-size 96px and 300px displays against contrasting backgrounds, approves identity/style and checks Chrome preview.
**APP / pedagogy:** visual demonstration only. Math and Vietnamese items are layout tests, not lessons validated against the textbook. Chrome headless screenshot did not finish in this environment; manual Chrome acceptance is still pending.
**PRODUCTION:** no CDN/Apps Script integration confirmed; do not deploy as approved.

## Browser-render smoke test (headless Chromium)
- Browser: Chromium via Playwright; tested the same HTML markup, CSS and app JS as the ZIP preview. Local `file://` navigation was blocked by sandbox administrator, so images were inlined as base64 **solely for the test run**. The distributed preview remains relative-file based, unchanged.
- Desktop viewport 980 × 790, phone viewport 375 × 812.
- All 7 referenced official WebP images loaded successfully with nonzero natural dimensions.
- Homepage rendered three official characters; Math choice `43` and Vietnamese choice `chăm chỉ` both produced the expected success feedback.
- No browser JavaScript page errors.
- Desktop screenshot: https://drive.google.com/file/d/179W6CtGDvjn0-W1p2NQ2Cpbwy063iDg0/view
- Mobile screenshot: https://drive.google.com/file/d/1W8LRyg39kSlCNxsQbH9FCxM_RPT_zHLQ/view
- **Remaining:** actual user-device Chrome check with extracted ZIP and human visual/attention approval. Do not mark artwork APPROVED.

## Human acceptance — 2026-10-28 (ICT)
The project owner explicitly confirmed hands-on visual use testing of the KidLearn v1.0.1 preview and accepted its appearance and suitability. The child enjoyed the preview. **ART: APPROVED** for the 30 official character assets in this release on the basis of this human acceptance. **STORAGE: SYNCED_VERIFIED** remains unchanged. This approval does not certify pedagogical alignment of sample Math/Vietnamese questions, production deployment, accessibility, or cross-browser/device testing beyond those already recorded. Earlier pending-gate text above is retained as historical pre-approval QA context. No merge into `main` is authorized by this acceptance.
