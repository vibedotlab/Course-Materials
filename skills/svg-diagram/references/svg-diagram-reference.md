# SVG Diagram Reference

Complete design system for generating architecture and flow diagrams in SVG.

---

## Table of Contents

1. [SVG Root Template](#1-svg-root-template)
2. [Arrow Marker Definitions](#2-arrow-marker-definitions)
3. [Color Palette](#3-color-palette)
4. [Box Styles](#4-box-styles)
5. [Text Rules](#5-text-rules)
6. [Arrow / Connector Rules](#6-arrow--connector-rules)
7. [Layout System](#7-layout-system)
8. [Grouping & Container Boxes](#8-grouping--container-boxes)
9. [Labels, Annotations & Footnotes](#9-labels-annotations--footnotes)
10. [Full Annotated Example](#10-full-annotated-example)
11. [Common Mistakes](#11-common-mistakes)

---

## 1. SVG Root Template

Always start every diagram with this exact root element:

```svg
<svg
  viewBox="0 0 820 460"
  xmlns="http://www.w3.org/2000/svg"
  style="width:100%;font-family:Georgia,serif;background:transparent;"
>
```

**Rules:**
- `viewBox` defines the internal coordinate space. Width × Height.
  - Landscape default: `820 460`
  - Portrait default: `500 640`
  - Adjust to fit your content — never leave more than 40px empty margin on any side.
- `width:100%` makes it responsive in any container.
- `font-family:Georgia,serif` gives the warm editorial look matching the reference design.
  Use `Arial,sans-serif` for a more technical / neutral aesthetic.
- `background:transparent` — never set a background color on the root. The page/host
  provides the background.

---

## 2. Arrow Marker Definitions

Always place these in `<defs>` as the very first thing inside `<svg>`.
Define all markers you need upfront, even if not all are used — it's harmless.

```svg
<defs>
  <!-- Standard one-way arrowhead (dark gray, pointing right by default) -->
  <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L0,6 L8,3 z" fill="#888"/>
  </marker>

  <!-- Reverse arrowhead for bidirectional lines (tail end) -->
  <marker id="arrb" markerWidth="8" markerHeight="8" refX="2" refY="3" orient="auto">
    <path d="M8,0 L8,6 L0,3 z" fill="#888"/>
  </marker>

  <!-- Darker arrowhead for emphasis -->
  <marker id="arr-dark" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L0,6 L8,3 z" fill="#444"/>
  </marker>
</defs>
```

**Usage:**
- One-way arrow: `<line ... marker-end="url(#arr)"/>`
- Bidirectional:  `<line ... marker-end="url(#arr)" marker-start="url(#arrb)"/>`

---

## 3. Color Palette

### Earth Tone Palette (default)

| Role | Fill | Stroke | Text |
|---|---|---|---|
| Page background | `#eae7df` | — | — |
| Light box (neutral) | `#f5f0e8` | `#b0a898` | `#2e2a26` |
| Light warm accent | `#ebe8e0` | `#b0a898` | `#3d3530` |
| Tan / khaki | `#d6cba0` | `#b8a866` | `#2e2a26` |
| Medium brown | `#b87a50` | `#9a6038` | `#f5ede4` |
| Deep rust / terracotta | `#8f3e28` | `#7a3020` | `#f5ede4` |
| Container outline | `none` | `#b0a898` | — |
| Italic label | — | — | `#5a5347` |
| Body text | — | — | `#3d3530` |
| Arrow / line | — | `#888888` | — |
| Footnote bullet | `#3d3530` | — | — |

### Gradient Progression (for sequenced steps)

```
Stage 1 (lightest): fill="#d6cba0"  stroke="#b8a866"  text="#2e2a26"
Stage 2 (mid):      fill="#b87a50"  stroke="#9a6038"  text="#f5ede4"
Stage 3 (darkest):  fill="#8f3e28"  stroke="#7a3020"  text="#f5ede4"
```

### Alternative: Cool Blue Technical Palette

| Role | Fill | Stroke | Text |
|---|---|---|---|
| Light box | `#f0f4ff` | `#8899cc` | `#1a2040` |
| Medium box | `#4a6fa5` | `#3a5585` | `#ffffff` |
| Dark box | `#1a2e5a` | `#0f1e3d` | `#e8eeff` |
| Container | `none` | `#8899cc` | — |
| Arrow | — | `#6677aa` | — |

### Alternative: Greyscale Minimal

| Role | Fill | Stroke | Text |
|---|---|---|---|
| Light box | `#f5f5f5` | `#cccccc` | `#222222` |
| Medium box | `#888888` | `#666666` | `#ffffff` |
| Dark box | `#333333` | `#111111` | `#f0f0f0` |
| Container | `none` | `#cccccc` | — |
| Arrow | — | `#888888` | — |

---

## 4. Box Styles

### Standard filled box

```svg
<rect x="530" y="90" width="210" height="60" rx="10"
      fill="#d6cba0" stroke="#b8a866" stroke-width="1.2"/>
<text x="635" y="126" text-anchor="middle"
      font-size="15" font-weight="bold" fill="#2e2a26">Box label</text>
```

**Rules:**
- `rx="10"` — standard corner radius. Use `rx="14"` for larger/prominent boxes.
- `stroke-width="1.2"` for most boxes. Use `2` for highlighted/featured boxes.
- Text `x` = center of box (`box_x + box_width / 2`).
- Text `y` = vertical center. For single-line: `box_y + box_height * 0.6`.
  For two-line text: first line at `box_y + box_height * 0.45`, second at `+ 22`.

### Two-line box label

```svg
<rect x="295" y="155" width="160" height="110" rx="14"
      fill="#f5f0e8" stroke="#b8705a" stroke-width="2"/>
<text x="375" y="202" text-anchor="middle"
      font-size="16" font-weight="bold" fill="#2e2a26">Language</text>
<text x="375" y="224" text-anchor="middle"
      font-size="16" font-weight="bold" fill="#2e2a26">Model</text>
```

### Container / grouping box (boundary)

```svg
<!-- Draw this BEFORE the child boxes it encloses -->
<rect x="270" y="60" width="520" height="340" rx="16"
      fill="none" stroke="#b0a898" stroke-width="1.2"/>
<!-- Label sits ABOVE the container box, centered -->
<text x="530" y="50" text-anchor="middle"
      font-style="italic" font-size="16" fill="#5a5347">Assistant</text>
```

**Critical:** Draw the container `<rect>` before child elements so they visually
sit on top of the border, not behind it.

---

## 5. Text Rules

| Text type | font-size | font-weight | font-style | fill |
|---|---|---|---|---|
| Section label (italic) | 15–16px | normal | italic | `#5a5347` |
| Box title (bold) | 14–18px | bold | normal | Depends on box fill |
| Body text in box | 12–13px | normal | normal | `#3d3530` |
| Arrow label | 12–13px | normal | italic | `#5a5347` |
| Footnote text | 11–12px | normal | normal | `#3d3530` |
| Wordmark | 10–11px | bold | normal | `#5a5347` |

**Alignment:**
- Always use `text-anchor="middle"` for centered box labels.
- Use `text-anchor="start"` for left-aligned body text and footnotes.
- Always set `fill` explicitly on every `<text>` element. Never omit it.

**Vertical centering formula:**
```
single line:  y = rect_y + (rect_height / 2) + (font_size * 0.35)
two lines:    line1_y = rect_y + (rect_height / 2) - (font_size * 0.3)
              line2_y = line1_y + font_size + 4
```

---

## 6. Arrow / Connector Rules

### Straight horizontal arrow

```svg
<line x1="191" y1="210" x2="262" y2="210"
      stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
```

**Tip:** End the line 2–4px before the target box edge so the arrowhead doesn't
overlap the box stroke.

### Bidirectional arrow

```svg
<line x1="375" y1="266" x2="375" y2="294"
      stroke="#888" stroke-width="1.5"
      marker-end="url(#arr)" marker-start="url(#arrb)"/>
```

### Curved loop arrow (iterate / cycle back)

```svg
<path d="M 741 300 C 790 300 790 120 741 120"
      fill="none" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
<text x="798" y="215" text-anchor="middle"
      font-style="italic" font-size="13" fill="#5a5347">Iterate</text>
```

**Path syntax:** `M startX startY C cp1x cp1y cp2x cp2y endX endY`

---

## 7. Layout System

### 3-column landscape layout (820 × 460 viewBox)

```
Col 1: x=20–190    (Task / Input region)
Col 2: x=270–465   (Core processing region)
Col 3: x=530–760   (Action steps region)

Rows:
Top:    y=60–150
Middle: y=150–270
Bottom: y=270–380
Footer: y=390–460
```

### Spacing rules

- Minimum gap between sibling boxes: **30px**
- Minimum gap between a box and its container: **20px on each side**
- Minimum gap between a box and the viewBox edge: **20px**
- Preferred gap between connected boxes: **40–60px**

---

## 8. Grouping & Container Boxes

1. **Draw the container `<rect>` FIRST** — children render on top.
2. Container always has `fill="none"`.
3. Container stroke: `stroke-width="1.2"`.
4. Container label goes **outside** (above or below), in italic.
5. Container `rx` should be larger than child box `rx` (e.g., `rx="16"` if children use `rx="10"`).
6. Leave at least 20px padding between container edge and children.

---

## 9. Labels, Annotations & Footnotes

### Italic section label

```svg
<text x="95" y="155" text-anchor="middle"
      font-style="italic" font-size="15" fill="#5a5347">Task</text>
```

Place 10–15px above the top edge of the box or container it labels.

### Arrow label (mid-arrow)

```svg
<text x="235" y="202" text-anchor="middle"
      font-style="italic" font-size="12" fill="#5a5347">request</text>
```

Offset the label 8px above the arrow line.

### Footnote bullets

```svg
<circle cx="460" cy="410" r="3" fill="#3d3530"/>
<text x="472" y="414" font-size="12" fill="#3d3530">First footnote text here</text>

<circle cx="460" cy="432" r="3" fill="#3d3530"/>
<text x="472" y="436" font-size="12" fill="#3d3530">Second footnote text here</text>
```

Spacing between footnote lines: **22px**.

### Wordmark (bottom-left)

```svg
<text x="30" y="455" font-size="11" font-weight="bold"
      letter-spacing="2" fill="#5a5347">COMPANYNAME</text>
```

---

## 10. Full Annotated Example

Complete SVG for a Claude Code agent loop diagram — demonstrates every pattern in this guide.

```svg
<svg viewBox="0 0 820 460" xmlns="http://www.w3.org/2000/svg"
     style="width:100%;font-family:Georgia,serif;background:transparent;">

  <!-- ① ARROW MARKERS — always first in <defs> -->
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#888"/>
    </marker>
    <marker id="arrb" markerWidth="8" markerHeight="8" refX="2" refY="3" orient="auto">
      <path d="M8,0 L8,6 L0,3 z" fill="#888"/>
    </marker>
  </defs>

  <!-- ② COLUMN 1: Task input box -->
  <text x="95" y="122" text-anchor="middle"
        font-style="italic" font-size="15" fill="#5a5347">Task</text>
  <rect x="20" y="130" width="170" height="160" rx="14"
        fill="#ebe8e0" stroke="#b0a898" stroke-width="1.2"/>
  <text x="95" y="210" text-anchor="middle" font-size="13" fill="#3d3530">Your prompt here</text>

  <!-- ③ ARROW: Task → Language Model -->
  <line x1="191" y1="210" x2="262" y2="210"
        stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- ④ COLUMN 2+3: Assistant container — draw BEFORE children -->
  <rect x="270" y="60" width="520" height="340" rx="16"
        fill="none" stroke="#b0a898" stroke-width="1.2"/>
  <text x="530" y="50" text-anchor="middle"
        font-style="italic" font-size="16" fill="#5a5347">Assistant</text>

  <!-- ⑤ COLUMN 2: Language Model box (featured) -->
  <rect x="295" y="155" width="160" height="110" rx="14"
        fill="#f5f0e8" stroke="#b8705a" stroke-width="2"/>
  <text x="375" y="202" text-anchor="middle"
        font-size="16" font-weight="bold" fill="#2e2a26">Language</text>
  <text x="375" y="224" text-anchor="middle"
        font-size="16" font-weight="bold" fill="#2e2a26">Model</text>

  <!-- ⑥ COLUMN 2: Set of tools box -->
  <rect x="295" y="295" width="160" height="82" rx="14"
        fill="#f5f0e8" stroke="#c8b87a" stroke-width="1.8"/>
  <text x="375" y="331" text-anchor="middle"
        font-size="16" font-weight="bold" fill="#2e2a26">Set of</text>
  <text x="375" y="353" text-anchor="middle"
        font-size="16" font-weight="bold" fill="#2e2a26">tools</text>

  <!-- ⑦ Bidirectional arrow: Language Model ↔ tools -->
  <line x1="375" y1="266" x2="375" y2="294"
        stroke="#888" stroke-width="1.5"
        marker-end="url(#arr)" marker-start="url(#arrb)"/>

  <!-- ⑧ Diagonal arrows: Language Model → each action box -->
  <line x1="456" y1="185" x2="530" y2="130"
        stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="456" y1="210" x2="530" y2="210"
        stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="456" y1="235" x2="530" y2="300"
        stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- ⑨ COLUMN 3: Action boxes (gradient progression) -->
  <rect x="530" y="90" width="210" height="60" rx="10"
        fill="#d6cba0" stroke="#b8a866" stroke-width="1.2"/>
  <text x="635" y="126" text-anchor="middle"
        font-size="15" font-weight="bold" fill="#2e2a26">Gather context</text>

  <rect x="530" y="180" width="210" height="60" rx="10"
        fill="#b87a50" stroke="#9a6038" stroke-width="1.2"/>
  <text x="635" y="216" text-anchor="middle"
        font-size="15" font-weight="bold" fill="#f5ede4">Formulate a plan</text>

  <rect x="530" y="270" width="210" height="60" rx="10"
        fill="#8f3e28" stroke="#7a3020" stroke-width="1.2"/>
  <text x="635" y="306" text-anchor="middle"
        font-size="15" font-weight="bold" fill="#f5ede4">Take an action</text>

  <!-- ⑩ Vertical arrows between action boxes -->
  <line x1="635" y1="151" x2="635" y2="179"
        stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="635" y1="241" x2="635" y2="269"
        stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- ⑪ Curved loop arrow + label -->
  <path d="M 741 300 C 790 300 790 120 741 120"
        fill="none" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="798" y="215" text-anchor="middle"
        font-style="italic" font-size="13" fill="#5a5347">Iterate</text>

  <!-- ⑫ FOOTER: footnotes -->
  <circle cx="460" cy="410" r="3" fill="#3d3530"/>
  <text x="472" y="414" font-size="12" fill="#3d3530">First footnote text</text>
  <circle cx="460" cy="432" r="3" fill="#3d3530"/>
  <text x="472" y="436" font-size="12" fill="#3d3530">Second footnote text</text>

  <!-- ⑬ WORDMARK -->
  <text x="30" y="455" font-size="11" font-weight="bold"
        letter-spacing="2" fill="#5a5347">YOURNAME</text>

</svg>
```

---

## 11. Common Mistakes

| Mistake | Fix |
|---|---|
| Text invisible on dark box | Set `fill="#f5ede4"` on text inside dark boxes |
| Arrowhead floats off the line | Check `refX` in marker definition |
| Text outside box bounds | Recalculate `y` using the vertical centering formula in §5 |
| Container border hides children | Draw container `<rect>` before child elements |
| Arrow overlaps a box | Subtract 3–4px from endpoint so line ends just before the box edge |
| Diagram cut off | Expand `viewBox` width/height |
| Inconsistent corner radii | Containers `rx="16"`, primary boxes `rx="14"`, small boxes `rx="10"` |
| Missing `fill` on text | Always set `fill` explicitly — never omit it |
| Font too small to read | Minimum 11px. Prefer 12–13px for body, 14–16px for titles |
