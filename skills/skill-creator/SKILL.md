---
name: skill-creator
description: Create new skills, improve existing skills, and build precise reusable workflows for Claude. Use this skill whenever a user wants to create a skill from scratch, turn a completed workflow into something reusable, edit or improve an existing skill, or make Claude consistently handle a repeated task the same way every time. Trigger on phrases like "turn this into a skill", "save this as a skill", "make a skill for", "help me build a skill", "create a skill that", "I want Claude to always do X" — or whenever automating a repeated task is clearly the right move, even if the user doesn't name it.
---

# Skill Creator

A skill for creating precise, high-quality skills that make Claude reliably handle specific tasks the same way every time.

The quality of any skill comes almost entirely from the quality of the interview before writing it. A vague description produces a vague skill. A precise interview produces a skill that just works.

## The Loop

```
Interview → Draft SKILL.md → Test → Review → Refine → Save
```

Start by figuring out where the user is. If they're saying "I want to make a skill for X", start at Step 1. If they already have a draft, jump to Step 4. If the user wants to skip steps and just go ("vibe with me"), follow their lead.

---

## Step 1: Capture Intent

Understand exactly what the user wants before writing anything.

If there's already a workflow in the conversation — they've been building something with Claude, made corrections, figured out the right steps — extract the answers from the conversation history first. The tools used, the sequence of steps, the corrections made, the inputs and outputs observed. Then confirm with the user before proceeding.

Otherwise, ask these four questions together:

1. What should this skill enable Claude to do?
2. When should this skill trigger? (specific phrases, contexts, or task types — be concrete)
3. What's the expected output? (format, structure, length, tone — show me an example if possible)
4. Do we need test cases to verify it works? Skills with objectively verifiable outputs (file transforms, data extraction, code generation, fixed multi-step workflows) benefit from test cases. Skills with subjective outputs (writing style, creative tasks) usually don't need them — suggest the appropriate default but let the user decide.

Don't move on until you have clear answers to all four. Ambiguity here is what produces skills that fail in unexpected ways.

---

## Step 2: Interview and Research

Before writing, go deeper. This is the most important step — it's what separates a skill that works on your three test cases from one that works on everything.

Ask about:

- **Edge cases** — what are the tricky inputs? What should NOT trigger this skill even if it sounds similar?
- **Input format** — what does the user actually provide when they start this task? (files, URLs, a description, a rough draft?)
- **Output format** — exactly what should the finished output look like? (ask for a real example if possible, or describe it specifically)
- **Success criteria** — how do we know it worked? What would make the user say "yes, that's it"?
- **Dependencies** — does this task need specific MCPs, tools, or reference files?

Check installed MCPs — if any are relevant to the task, note them. If there's documentation the skill should know about (an API, a library, a style guide), fetch it before writing.

Wait until this is settled before drafting anything. Jumping to writing too early is the single biggest source of imprecise skills.

---

## Step 3: Write the SKILL.md

Based on the interview, write the skill file.

### Frontmatter

```yaml
---
name: skill-name
description: [When to trigger AND what it does. This is the primary mechanism Claude uses to decide whether to use this skill. Be slightly "pushy" — lean toward using the skill when in doubt. E.g., instead of "Helps format data", write "Formats tabular data into clean structured reports. Use this whenever the user mentions data formatting, report generation, or table cleanup — even if they don't explicitly ask for a skill."]
---
```

The description field carries the most weight. Include:
- What the skill does
- Specific phrases or contexts that should trigger it
- Cases where it should trigger even if the skill isn't named explicitly
- What NOT to trigger on, if false positives are a concern

### Body

Write in imperative form: "Read the file", "Ask the user for X", "Save the output to...".

Explain the *why* behind each step. Claude understands reasoning — a well-explained "why" produces better results than a rigid "ALWAYS do X". The latter creates brittle, overfitted behavior. The former creates a model that can apply good judgment across situations you didn't anticipate.

Define the output format concretely. If the output is structured, give an exact template:

```markdown
## Report structure
Use this template exactly:
# [Title]
## Summary (2–3 sentences)
## Key findings (bullet points)
## What to do next
```

Include examples where helpful:

```markdown
## Example
Input: "summarize this article for a non-technical audience"
Output: A 3-paragraph plain-English summary, no jargon, ends with one key takeaway sentence
```

### Bundled Resources (optional)

If the skill needs reference material — a style guide, API docs, templates, scripts — put them in a subfolder:

```
skill-name/
├── SKILL.md
└── references/
    └── style-guide.md
```

Reference them clearly in the SKILL.md body with instructions on when to read them.

### Writing guidelines

**Keep the body under 500 lines.** If you're approaching that limit, move content into a `references/` subfolder and point to it from SKILL.md.

**Avoid overfitting.** Don't add narrow rules for the exact examples you tested. Write for the general case. Understand *why* something went wrong and fix the underlying reasoning — don't patch the symptom with a rigid rule.

**Keep it lean.** Remove instructions that aren't pulling their weight. If a step caused unproductive work in testing, cutting it often fixes the problem better than adding more instructions around it.

**Triggering description matters more than almost anything else.** If the skill isn't triggering when it should, the description needs work — not the body.

---

## Step 4: Test Cases

After writing the draft, create 2–3 realistic test prompts — the kind of thing a real user would say, not an abstract description of the task.

Good test prompts are concrete and specific:
> "ok so I just finished a research session on TypeScript decorators and I want to turn the whole approach we worked out into a skill I can reuse. Can you save it?"

Not:
> "Test the research-to-skill workflow"

Share the prompts with the user before running: *"Here are 2–3 prompts I'd like to test. Do these look right, or want to add anything?"*

Run each one by following the skill's instructions exactly as Claude would when triggered. Show the user the output. Ask for feedback.

---

## Step 5: Refine

Based on feedback and your own observations, improve the skill.

**Generalize from the feedback.** This skill will run thousands of times across inputs you've never seen. Don't patch the specific test case — understand why it went wrong and fix the underlying instruction. A skill that only works on the three examples you tried is not a skill.

**Explain the why.** If the feedback is "the output was too formal", don't add "NEVER use formal language". Instead: "This skill is for quick internal communication, not formal reports — write as if explaining to a colleague, not drafting a presentation."

**Look for repeated improvisation.** If every test run independently invented the same helper script or took the same multi-step workaround, that's a strong signal to bake it into the skill directly.

**When in doubt, simplify.** Remove instructions rather than adding more. Over-specified skills produce rigid, brittle behavior. Under-specified skills give Claude room to apply judgment — which is usually what you want.

After revising:
1. Run the test cases again
2. Show the user the updated outputs
3. Repeat until the user is happy or the feedback is empty (which means everything looks good)

---

## Step 6: Optimize the Description (Optional but Worth It)

After the skill body is solid, spend 5 minutes on the description field. It's what determines whether Claude actually uses this skill.

A well-tuned description:
- Names the specific task domain ("PDF conversion", "code review", "weekly digest generation")
- Lists the phrases and contexts that should trigger it — including phrasing the user might use without naming the skill
- Leans toward using the skill (slightly "pushy" is better than overly cautious)
- Clarifies what NOT to trigger on, if there's a common false-positive risk

Try 2–3 variations and ask: "If Claude saw this description alongside 10 other skills, would it know exactly when to use this one?"

Update the frontmatter with the best version.

---

## Step 7: Save

Once the user is satisfied, write the final file:

```
~/.claude/skills/<skill-name>/SKILL.md
```

For a skill with references or scripts:
```
~/.claude/skills/<skill-name>/
├── SKILL.md
└── references/
    └── reference-file.md
```

If the user wants it project-specific instead of global, save to `.claude/skills/` in the project root.

Confirm when done: *"Saved to `~/.claude/skills/<skill-name>/`. Trigger it with `/skill-name` or just describe the task — Claude will pick it up automatically."*

---

## Communicating With the User

Users who want to build skills range from non-technical (first time opening a terminal) to senior engineers. Watch for context cues and adjust:

- **Beginners:** explain what frontmatter is, keep steps concrete, avoid jargon, don't assume they know what a YAML field is
- **Technical users:** be brief, assume familiarity with file structure and CLI

When in doubt, a short inline definition is better than confusing someone. "The frontmatter (the block between `---` at the top of the file) contains..." costs one sentence and saves a lot of confusion.

---

## Source

Adapted from Anthropic's official Skill Creator skill:
[github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)

For advanced use cases — eval benchmark infrastructure, automated description optimization loop, blind A/B comparison between skill versions — see the full Anthropic version.
