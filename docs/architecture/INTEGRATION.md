# GitHub + Drive + Google Apps Script (proposed)

**No production connection/deployment configured yet.**

GitHub owns code, visual design locks, manifest, QA and change history.
Drive owns source/reference and approved original image files.
Apps Script may serve approved API/data from Google Sheets/Drive for the KidLearn frontend.
Asset consumption should use stable deployment URLs/cache, not fragile Drive share links as public image CDN.

Flow: Home (Math/Vietnamese) -> lesson by SGK heading -> guide -> LV1 (SGK), LV2 (VBT), LV3 (reference) -> feedback -> progress. SGV pedagogical reference only, not a primary question source.

## Security
Do not commit API keys, Google tokens, service account private keys, clasp credentials or identifiable pupil data/scores. Use least-privilege GAS deployments; owner review before any automated publishing. Never turn user-uploaded assets into public links without review. Avoid automatic release from a style-document change.

## Planned layout
- apps/web/ KidLearn HTML/CSS/JS
- apps/script/ Google Apps Script source
- docs/visual/ locked guides and asset manifest
- assets/approved/ published optimized images (only if rights and size make Git appropriate)
- Drive folders/ source and A4 proof art

Use a review branch/pull request; keep main stable.
