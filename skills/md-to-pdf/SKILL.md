---
name: md-to-pdf
description: Use this skill whenever the user wants to convert Markdown files (.md) into a professional-grade PDF — especially for courses, books, reports, or structured documents. Triggers when the user mentions .md files + PDF output, course creation, "convert my course", "build PDF from markdown", or asks to design/format a document into PDF. Handles the complete pipeline: dependency setup, design reference analysis, CSS templating, image embedding, TOC, chapter ordering, and final rendering — all autonomously.
argument-hint: [source_dir] [output_pdf] [design_reference]
allowed-tools: Bash, Read, Write, Edit, Glob
---

# MD to PDF Converter — Course Writer

Convert one or more Markdown files into a professionally designed, print-ready PDF. The user provides content (.md files) and optionally a design reference. Claude does everything else.

**Arguments (all optional):**
- `$ARGUMENTS` may contain: source directory, output filename, and/or a design reference path/description

---

## Workflow Overview

```
1. Discover .md files + understand structure
2. Parse design reference (image, PDF, or description)
3. Install dependencies if missing
4. Build CSS template matching the design
5. Assemble final Markdown (cover + TOC + chapters)
6. Run pandoc → PDF
7. Verify output, report result
```

---

## Step 1 — Discover Source Files

Parse `$ARGUMENTS` for a source directory. If not provided, ask the user or default to current directory.

```bash
# Find all .md files
find "$SOURCE_DIR" -name "*.md" | sort
```

Identify the structure:
- Is there a single file or multiple chapters?
- Is there a `README.md` or `index.md` to use as intro/cover?
- Are there subdirectories (chapters)?
- Are there image files (`.png`, `.jpg`, `.svg`)?

Report what you found before proceeding.

---

## Step 2 — Analyze Design Reference

The user may provide:
- A screenshot or PDF path → read it with the Read tool and describe the visual style
- A URL → note the design elements
- A text description → parse directly
- Nothing → use the **default professional course template** below

Extract and note:
- Color scheme (primary, accent, background, text colors)
- Font choices (serif vs sans-serif, heading vs body)
- Page layout (margins, sidebar, single/double column)
- Header/footer style
- Code block appearance
- Chapter heading style
- Cover page design

---

## Step 3 — Install Dependencies

Check and install what's needed:

```bash
# Check pandoc
pandoc --version 2>/dev/null || winget install JohnMacFarlane.Pandoc

# Check weasyprint
python -c "import weasyprint" 2>/dev/null || pip install weasyprint

# Check python-markdown (for preprocessing if needed)
python -c "import markdown" 2>/dev/null || pip install markdown

# Check Pillow (for image handling)
python -c "import PIL" 2>/dev/null || pip install Pillow

# On Windows, weasyprint may need GTK — check:
python -c "import weasyprint; weasyprint.HTML(string='<p>test</p>').write_pdf('/tmp/test.pdf')" 2>&1
```

If weasyprint fails on Windows, fall back to `--pdf-engine=pdflatex` or `--pdf-engine=wkhtmltopdf`:
```bash
wkhtmltopdf --version 2>/dev/null || echo "Install from: https://wkhtmltopdf.org/downloads.html"
```

---

## Step 4 — Build CSS Template

Write the CSS to `~/.claude/skills/md-to-pdf/scripts/course.css` (or a project-local copy).

### Default Professional Course Template

```css
/* ============================================================
   MD-TO-PDF COURSE TEMPLATE
   Professional course/book layout
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&family=JetBrains+Mono:wght@400;500&display=swap');

/* --- Page Setup --- */
@page {
  size: A4;
  margin: 25mm 20mm 25mm 25mm;

  @top-center {
    content: string(chapter-title);
    font-family: 'Inter', sans-serif;
    font-size: 9pt;
    color: #888;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 4mm;
  }

  @bottom-right {
    content: counter(page);
    font-family: 'Inter', sans-serif;
    font-size: 9pt;
    color: #888;
  }

  @bottom-left {
    content: string(course-title);
    font-family: 'Inter', sans-serif;
    font-size: 9pt;
    color: #888;
  }
}

@page :first {
  margin: 0;
  @top-center { content: none; }
  @bottom-right { content: none; }
  @bottom-left { content: none; }
}

/* --- Typography --- */
:root {
  --primary: #1a1a2e;
  --accent: #4f46e5;
  --accent-light: #818cf8;
  --bg-code: #f4f4f8;
  --bg-callout: #eef2ff;
  --border: #e2e8f0;
  --text: #1e293b;
  --text-muted: #64748b;
}

body {
  font-family: 'Merriweather', serif;
  font-size: 11pt;
  line-height: 1.8;
  color: var(--text);
  background: white;
  margin: 0;
  padding: 0;
}

/* --- Cover Page --- */
.cover-page {
  page: :first;
  width: 100vw;
  height: 100vh;
  background: linear-gradient(135deg, var(--primary) 0%, #16213e 50%, #0f3460 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: white;
  padding: 60px;
  box-sizing: border-box;
}

.cover-page h1 {
  font-family: 'Inter', sans-serif;
  font-size: 36pt;
  font-weight: 700;
  line-height: 1.2;
  margin: 0 0 20px 0;
  color: white;
  border: none;
  padding: 0;
}

/* --- Chapter Headings --- */
h1 {
  font-family: 'Inter', sans-serif;
  font-size: 24pt;
  font-weight: 700;
  color: var(--primary);
  margin-top: 0;
  margin-bottom: 8mm;
  padding-bottom: 4mm;
  border-bottom: 3px solid var(--accent);
  page-break-before: always;
  string-set: chapter-title content();
}

h2 {
  font-family: 'Inter', sans-serif;
  font-size: 16pt;
  font-weight: 600;
  color: var(--primary);
  margin-top: 10mm;
  margin-bottom: 4mm;
  padding-left: 10px;
  border-left: 4px solid var(--accent);
}

h3 {
  font-family: 'Inter', sans-serif;
  font-size: 13pt;
  font-weight: 600;
  color: var(--text);
  margin-top: 6mm;
  margin-bottom: 3mm;
}

/* --- Body Text --- */
p {
  margin: 0 0 5mm 0;
  text-align: justify;
  hyphens: auto;
}

/* --- Code --- */
code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9.5pt;
  background: var(--bg-code);
  padding: 2px 6px;
  border-radius: 3px;
  color: #c7254e;
}

pre {
  background: #1e1e2e;
  color: #cdd6f4;
  padding: 6mm;
  border-radius: 6px;
  overflow-x: auto;
  margin: 5mm 0;
  border-left: 4px solid var(--accent);
  page-break-inside: avoid;
}

pre code {
  background: none;
  color: inherit;
  padding: 0;
  font-size: 9pt;
  line-height: 1.6;
}

/* --- Tables --- */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 5mm 0;
  font-family: 'Inter', sans-serif;
  font-size: 10pt;
  page-break-inside: avoid;
}

thead tr {
  background: var(--primary);
  color: white;
}

thead th {
  padding: 3mm 4mm;
  text-align: left;
  font-weight: 600;
}

tbody tr:nth-child(even) { background: #f8fafc; }

tbody td {
  padding: 2.5mm 4mm;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}

/* --- Callouts --- */
blockquote {
  background: var(--bg-callout);
  border-left: 5px solid var(--accent);
  margin: 5mm 0;
  padding: 4mm 6mm;
  border-radius: 0 6px 6px 0;
  page-break-inside: avoid;
}

blockquote p {
  margin: 0;
  font-style: italic;
  color: var(--primary);
}

/* --- Lists --- */
ul, ol {
  padding-left: 6mm;
  margin: 3mm 0 5mm 0;
}

li {
  margin-bottom: 2mm;
  line-height: 1.7;
}

ul li::marker { color: var(--accent); }
```

---

## Step 5 — Assemble Final Markdown

Write a Python assembly script to `~/.claude/skills/md-to-pdf/scripts/assemble.py`:

```python
#!/usr/bin/env python3
"""
Assemble multiple .md files into a single document for pandoc conversion.
Handles: cover page, TOC placeholder, chapter ordering, image path fixing.
"""
import os, re, sys, glob, shutil

def assemble(source_dir, output_md, course_title="", author="", subtitle=""):
    source_dir = os.path.abspath(source_dir)
    files = sorted(glob.glob(os.path.join(source_dir, "**/*.md"), recursive=True))
    priority = [f for f in files if os.path.basename(f).lower() in ("readme.md","index.md","00_intro.md","00-intro.md","intro.md")]
    rest = [f for f in files if f not in priority]
    ordered = priority + rest

    parts = []

    parts.append(f"""<div class="cover-page">
<h1>{course_title or os.path.basename(source_dir)}</h1>
<div class="subtitle">{subtitle}</div>
<div class="author">{author}</div>
</div>

""")

    for f in ordered:
        content = open(f, encoding="utf-8").read()
        def fix_img(m):
            img_path = m.group(1)
            if not img_path.startswith(("http","/")):
                img_path = os.path.join(os.path.dirname(f), img_path)
                img_path = os.path.abspath(img_path)
            return f"![]({img_path})"
        content = re.sub(r'!\[.*?\]\((.+?)\)', fix_img, content)
        parts.append(content)
        parts.append("\n\n")

    with open(output_md, "w", encoding="utf-8") as out:
        out.write("\n".join(parts))

    print(f"Assembled {len(ordered)} files → {output_md}")
    return output_md

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("source_dir")
    p.add_argument("output_md")
    p.add_argument("--title", default="")
    p.add_argument("--author", default="")
    p.add_argument("--subtitle", default="")
    args = p.parse_args()
    assemble(args.source_dir, args.output_md, args.title, args.author, args.subtitle)
```

---

## Step 6 — Run the Conversion

```bash
# 1. Assemble all .md files into one
python ~/.claude/skills/md-to-pdf/scripts/assemble.py \
  "$SOURCE_DIR" \
  /tmp/course_assembled.md \
  --title "YOUR COURSE TITLE" \
  --author "Your Name" \
  --subtitle "Course Subtitle"

# 2. Convert to PDF with pandoc + weasyprint
pandoc /tmp/course_assembled.md \
  -o "$OUTPUT_PDF" \
  --pdf-engine=weasyprint \
  --css=~/.claude/skills/md-to-pdf/scripts/course.css \
  --toc \
  --toc-depth=3 \
  --highlight-style=zenburn \
  --metadata title="$COURSE_TITLE" \
  --metadata author="$AUTHOR" \
  --standalone \
  -f markdown+smart+fenced_divs+native_divs
```

### If weasyprint fails on Windows, use wkhtmltopdf:
```bash
pandoc /tmp/course_assembled.md \
  -o "$OUTPUT_PDF" \
  --pdf-engine=wkhtmltopdf \
  --css=~/.claude/skills/md-to-pdf/scripts/course.css \
  --toc \
  --toc-depth=3 \
  --standalone \
  -V margin-top=25mm -V margin-bottom=25mm \
  -V margin-left=25mm -V margin-right=20mm
```

---

## Step 7 — Verify and Report

```bash
ls -lh "$OUTPUT_PDF"
pdfinfo "$OUTPUT_PDF" 2>/dev/null | grep Pages
```

Report to the user:
- PDF created at: `$OUTPUT_PDF`
- Page count
- File size
- Images embedded: N
- Chapters included: N

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Fonts not loading | Use local fonts or `--embed-resources` flag |
| Images missing | Ensure absolute paths; run assemble.py first |
| weasyprint GTK error on Windows | Use wkhtmltopdf fallback |
| TOC page numbers wrong | Use `--toc` flag with pandoc only |
| Code blocks overflow | Add `overflow-x: auto` or reduce font size |
| Cover page not full-bleed | Ensure `@page :first { margin: 0; }` in CSS |
