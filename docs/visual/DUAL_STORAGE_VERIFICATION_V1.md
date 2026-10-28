# KidLearn Release v1.0.0 — Dual-storage verification and visual QA

**Date:** 2026-10-27 (ICT)  
**Release:** 5 character sheets, 30 isolated PNG RGBA, 30 optimized WebP; original 5 sheets and documentation in Drive; GitHub index with 30 asset IDs.

## Storage verification: SYNCED_VERIFIED

- **Google Drive destination:** [v1.0.0_QA_PENDING](https://drive.google.com/drive/folders/18mNr15yhJVyx7fWPqzDQOokk5iomzpgg)
- [30 PNG](https://drive.google.com/drive/folders/1Vct3DCp4Y28b9-O84fqC1eM_a4enPAr7) / [30 WebP](https://drive.google.com/drive/folders/1wNvA2VWIfl9lghkaAi_MMcstLpj67E3D)
- [5 source sheets](https://drive.google.com/drive/folders/16pMoGDfGUBPkH3_rVxbLKZJC0lhLQJDZ) / [6 documentation files](https://drive.google.com/drive/folders/10SLT-hQ1Isnq56-73BiPKtDZfylRyNYm)
- [Release ZIP in Drive](https://drive.google.com/file/d/1BOTrFixfZrP0peuKpZwNkLmTJkKlWJvi/view); SHA-256 **80917390a3979b32175e9ced4024669ac1be345e655d96fc41707373ebad1a99**. ZIP downloaded back from Drive and checksum matched.
- Every **60/60 individual PNG/WebP** was fetched back from Drive and compared byte-for-byte with the corresponding local release file: **60 matching, 0 mismatches**.
- Local manifest: **30/30 PNG** checksum matched, alpha range included both fully transparent and opaque values.
- GitHub [RELEASE_INDEX_V1.csv](../../assets/RELEASE_INDEX_V1.csv) now records all 30 asset IDs, 30 PNG IDs, 30 WebP IDs, Drive links and local PNG SHA-256; repository metadata readback confirms 30 unique rows.
- Storage status in the GitHub index may be **SYNCED_VERIFIED**. This certifies Drive binary preservation + GitHub metadata index, **not** that binary PNG/WebP files exist in GitHub, nor that artwork is approved.

## Image quality / visual QA: REVIEW_REQUIRED

The original art direction and five character-sheet styles were approved, but the **automatically split individual assets have not all passed visual border QA**.

Priority visual defects suspected from the contact sheet:
1. `KL_BOY_SCHOOL_05_point_book_v1.0.0`: obvious cropped hair/head edge; **NEEDS_REPAIR**.
2. `KL_BOY_SCHOOL_04_write_desk_v1.0.0`: table/desk may be cropped at the outer edge; **MANUAL_CHECK**.
3. `KL_GIRL_HOME_03_write_table_v1.0.0`: table may be cropped at the outer edge; **MANUAL_CHECK**.
4. `KL_GIRL_SCHOOL_04_write_desk_v1.0.0`: desk border may be cropped; **MANUAL_CHECK**.

All other images are **REVIEW_REQUIRED** for final per-pose manual review, because checking a contact sheet is not a full pixel-level review of 30 PNGs.

### Next QA gate

Repair or recreate flagged pose(s) in same locked style, save as a new version (do not silently overwrite v1.0.0), export PNG RGBA and WebP, inspect on cream/white/blue/navy at 96px and 300px, and verify edge transparency. Update both Drive binaries and GitHub manifest with new IDs/hashes. Only after human approval mark **APPROVED** for the artwork, distinct from **SYNCED_VERIFIED** storage.

## Architecture notes
GitHub currently contains the index / policy / prompts / verification instructions. **The image masters live in Drive.** Apps Script deployment, hotlink/CDN strategy, and publication integration are not yet configured. Do not claim an automatic sync job or direct GitHub binary mirror exists.
