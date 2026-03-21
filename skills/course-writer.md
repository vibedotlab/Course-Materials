---
name: course-writer
description: Write a chapter of a beginner course. Invoke with the chapter topic and target file name.
---
# Course Chapter Writing Workflow

## Step 1: Load Research
Read /research/[topic].md for verified facts before writing.
If research doesn't exist yet, use the researcher subagent first.

## Step 2: Outline
Draft a chapter outline with 4-6 sections. Consider:
- What does a complete beginner need to know first?
- What's the most confusing part — address it directly
- What's the one thing they must walk away knowing?

## Step 3: Write
Follow the output standards in CLAUDE.md:
- Analogy for every technical concept
- Short paragraphs (3-5 sentences max)
- Quick Summary + Common Mistakes at the end

## Step 4: Quality Check
Before saving the final draft, verify against @docs/quality-checklist.md.
Mark any uncertain facts as [VERIFY: ___] — never guess.

## Step 5: Save
Save to /chapters/chXX-title.md and report what was completed.
