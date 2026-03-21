---
name: svg-diagram
description: >
  Generates clean, styled SVG architecture and flow diagrams directly in the terminal
  or as saved .svg files. Use this skill whenever the user wants to visualize a system,
  workflow, agent loop, data pipeline, decision tree, or any box-and-arrow diagram.
  Trigger on phrases like: "draw a diagram", "make a flow", "visualize this architecture",
  "show me how X works", "create a diagram like this", "turn this into a diagram",
  "make a chart of this process", or whenever the user shares a screenshot of a diagram
  and asks to reproduce or adapt it. Also trigger if the user describes components and
  relationships between them — even without explicitly asking for a diagram.
---

# SVG Diagram Skill

You are an expert at producing clean, professional SVG diagrams from a description or
from structured information the user provides. Your output is always a valid `.svg` file
that renders beautifully in any browser or SVG viewer.

Read `references/svg-diagram-reference.md` before generating any diagram. It contains
the full design system: color palette, layout rules, typography, arrow patterns, and
annotated examples. Always follow it precisely.

---

## Workflow

### Step 0 — Collect a visual reference (MANDATORY — do not skip)

**Before doing anything else**, you must establish the visual style. STOP and ask:

```
Before I generate the diagram, I need a visual reference to match the correct
font, color palette, sizing, and style. Please provide one of the following:

  A) A screenshot or image of an existing diagram to match
  B) A file path to a reference image or SVG already in the project
  C) A path to a reference folder (e.g. screenshots/references/)
  D) An explicit style description covering:
       - Font family (e.g. Georgia serif, Arial sans-serif)
       - Color palette (e.g. warm earth tones, cool blues, greyscale)
       - Box corner style (rounded / sharp)
       - Any wordmark or footnote to include

If you have reference diagrams already in the project, tell me where they are
and I will read them before generating.
```

**Do not proceed to Step 1 until you have received one of A, B, C, or D.**

Once a reference is provided:
- If it is an image/screenshot → read it visually and extract: font family, font sizes,
  fill colors, stroke colors, corner radii, arrow style, label style, footnote style.
- If it is a file path → read the file and extract the same properties.
- If it is a style description → map it to the design system tokens in
  `references/svg-diagram-reference.md`.

Confirm the extracted style back to the user in one line before generating:
```
Style locked: [font] · [palette name] · [corner style] · [any wordmark]
→ Generating now.
```

---

### Step 1 — Understand the diagram

Ask yourself (and the user if needed):

1. **What are the components?** (boxes, nodes, actors, systems)
2. **What are the connections?** (arrows, flows, bidirectional links)
3. **Is there a grouping / container?** (a boundary box like "Assistant" in the example)
4. **Are there labels on the diagram itself?** (italic section labels, footnotes, a wordmark)
5. **What is the flow direction?** (left-to-right, top-to-bottom, or mixed)
6. **What color style?** (confirmed in Step 0 — do not re-ask)

If the user has given you enough to proceed, do not ask — just generate. If critical
information is missing (e.g. you don't know what the nodes are), ask 1–2 focused
questions only.

### Step 2 — Plan the layout on paper (mentally)

Before writing any SVG code:

- Decide the `viewBox` width × height. Start with `820 × 460` for landscape, `500 × 600`
  for portrait. Adjust after placing elements.
- Sketch the rough grid: left region, center region, right region (or top/bottom).
- Assign coordinates to each box. Leave ≥ 30px padding between boxes.
- Plan arrow routes (straight lines preferred; use `path` curves only when lines would
  overlap boxes).

### Step 3 — Write the SVG

Follow the structure in `references/svg-diagram-reference.md` exactly:

1. `<svg>` root with `viewBox`, `xmlns`, font stack, transparent background
2. `<defs>` with arrow markers first
3. Group elements logically with `<!-- comments -->` per region
4. Draw container boxes before their children
5. Draw arrows after all boxes
6. Draw text labels last (they must sit on top)

### Step 4 — Validate mentally

Before outputting, check:
- [ ] Every `<text>` has an explicit `fill` color
- [ ] Every arrow `marker-end` references a defined marker id
- [ ] No element is placed outside the `viewBox`
- [ ] Container boxes visually enclose their children
- [ ] Font sizes: titles 15–18px, body 12–14px, footnotes 11–12px
- [ ] `font-family` set on root `<svg>` element
- [ ] `background: transparent` set via inline style on root

### Step 5 — Save and present

Save the SVG to the path the user specifies, or default to `./diagram.svg`.

```bash
# Example: write the SVG to a file
cat > diagram.svg << 'EOF'
<svg ...>...</svg>
EOF
```

Then open it for the user if possible:
```bash
open diagram.svg          # macOS
xdg-open diagram.svg      # Linux
start diagram.svg         # Windows
```

If the user is in a Claude.ai chat (not terminal), output the raw SVG inline so it
renders in the conversation.

---

## Accepting user input

The user may describe their diagram in many formats. Handle all of them:

### Natural language description
> "Draw a diagram showing a user sending a request to an API gateway, which routes to
> either a fast path or slow path service, both returning to a response aggregator."

→ Extract nodes and arrows, assign layout, generate.

### Bullet list of components
> Components: User, API Gateway, Fast Service, Slow Service, Aggregator
> Connections: User→Gateway, Gateway→Fast, Gateway→Slow, Fast→Aggregator, Slow→Aggregator

→ Map directly to boxes and arrows.

### Screenshot or image of an existing diagram
> (User uploads a photo / screenshot)

→ Identify all boxes, labels, arrows, groupings, colors, and italic labels from the
image. Reproduce faithfully using the design system.

### Structured data (JSON / YAML)
```json
{
  "nodes": ["A","B","C"],
  "edges": [["A","B"],["B","C"]],
  "container": "My System"
}
```
→ Parse and render.

---

## Iterating on a diagram

If the user says "change X", "add Y", "make Z bigger", etc.:

1. Re-read the last generated SVG from the saved file (or from context)
2. Apply the change with surgical precision — do not regenerate from scratch
3. Re-save and re-open

Common change requests and how to handle them:

| Request | Action |
|---|---|
| "Add a node" | Insert a new `<rect>` + `<text>` group; re-route nearby arrows |
| "Change color" | Update `fill` on the target element(s) |
| "Flip direction" | Swap x/y coordinates; adjust arrow markers |
| "Make it wider" | Increase `viewBox` width; spread x coordinates |
| "Add a label to an arrow" | Insert `<text>` at midpoint of the line |
| "Add footnotes" | Append `<circle>` + `<text>` pairs in the bottom region |

---

## Reference

Read `references/svg-diagram-reference.md` for:
- Full color palette (earth tones + semantic colors)
- Box styles (filled, outlined, container)
- Arrow marker definitions (one-way, bidirectional)
- Typography rules
- Annotated full example (the Claude Code agent loop diagram)
- Common mistakes to avoid
