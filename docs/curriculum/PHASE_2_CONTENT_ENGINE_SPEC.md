# KidLearn Lớp 2 — Phase 2: Curriculum and worksheet engine

**Created:** 2026-10-28. **Status:** SPEC_READY / SOURCE_CONTENT_PENDING.
**Dependency:** official character set v1.0.1 (art APPROVED; storage SYNCED_VERIFIED). The original v1.0.0 remains immutable.

## Goal
Build verified, engaging Grade 2 Math and Vietnamese lessons. Preserve the approved chibi art style. Keep character images secondary to exercises; only the two subjects appear in the first release.

## Source authority (mandatory)
1. **Level 1:** textbook (SGK) — canonical lesson objectives, facts, examples and exercise scope.
2. **Level 2:** corresponding workbook (SBT) — additional practice, mapped to a textbook lesson.
3. **Level 3:** supplemental/reference books — optional advanced practice, never overriding SGK.
4. **Teacher's guide (SGV):** pedagogical method and lesson boundaries only; NOT a source of questions or answer keys by default.

Organize the curriculum **by lesson title / lesson ID**, not by school week. Preserve exact source names, editions, pages, and exercise IDs.

## Content schema per question
- `question_id` (immutable), `subject` (math/vietnamese), `lesson_id`, `level` (1/2/3).
- `question_type` (single_choice, multi_choice, numeric, arrange, match, fill_blank, reading).
- `stem`, `choices` (if applicable), `answer`, `explanation`, `learning_objective`.
- `source_type` (SGK/SBT/REFERENCE), `source_title`, `edition`, `page`, `exercise_ref`, `source_excerpt_or_image_ref`.
- `verification_status`: DRAFT, SOURCE_MATCHED, ANSWER_CHECKED, PEDAGOGY_REVIEWED, APPROVED.
- `verification_notes`, `reviewer`, `updated_at`; avoid collecting children's personal information.

## Source-grounded extraction rules
- Do not invent source page numbers or claim that generated exercises occur verbatim in the textbook.
- For any generated variation, mark `derived_from_source=true` and keep the anchor exercise.
- Reject unclear scans, missing answer keys and conflicts between editions; queue for human review.
- Check correctness independently for every question and distractor.
- Source citation is required for progression to SOURCE_MATCHED.

## App progression
- Choose subject → lesson (not week) → L1/L2/L3 → question → feedback → progress.
- Default to large touch targets, short text, low visual clutter and encouraging error feedback.
- Keep one question in focus and at most one guide character on an exercise screen.
- Use approved assets from manifest v1.0.1 only.
- Browser preview samples are **layout demonstrations only**, not yet validated SGK content.

## Milestones
1. Confirm subject textbook series, edition and source files.
2. Build canonical lesson map for Math and Vietnamese from SGK, with source citations.
3. Map SBT and reference material to lesson IDs; flag unmatched pages.
4. Create a small verified pilot per subject with answer validation and age-appropriate UX.
5. Child usability test; then scale only after pedagogical and source verification.

## Release gates
- Visual assets: APPROVED and SYNCED_VERIFIED (v1.0.1).
- Curriculum and questions: SOURCE_CONTENT_PENDING, never APPROVED until source and answer reviews.
- No merge to main; no change to v1.0.0; use reviewable branches/PRs.
