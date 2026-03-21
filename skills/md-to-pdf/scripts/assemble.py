#!/usr/bin/env python3
"""
Assemble multiple .md files into a single document for pandoc conversion.
Handles: cover page, TOC placeholder, chapter ordering, image path fixing.
Usage: python assemble.py <source_dir> <output_md> [--title "..."] [--author "..."] [--subtitle "..."]
"""
import os, re, glob, argparse

def assemble(source_dir, output_md, course_title="", author="", subtitle=""):
    source_dir = os.path.abspath(source_dir)
    files = sorted(glob.glob(os.path.join(source_dir, "**/*.md"), recursive=True))

    # Priority ordering: intro/readme first
    priority_names = ("readme.md", "index.md", "00_intro.md", "00-intro.md", "intro.md", "00.md")
    priority = [f for f in files if os.path.basename(f).lower() in priority_names]
    rest = [f for f in files if f not in priority]
    ordered = priority + rest

    if not ordered:
        print(f"ERROR: No .md files found in {source_dir}")
        return None

    print(f"Found {len(ordered)} files:")
    for f in ordered:
        print(f"  {os.path.relpath(f, source_dir)}")

    parts = []

    # Cover page
    title = course_title or os.path.basename(source_dir).replace("-", " ").replace("_", " ").title()
    parts.append(f"""<div class="cover-page">
<div class="course-label">Course</div>
<h1>{title}</h1>
<div class="subtitle">{subtitle}</div>
<div class="author">{author}</div>
</div>

""")

    # Chapters
    for f in ordered:
        content = open(f, encoding="utf-8").read()

        # Fix relative image paths to absolute
        def fix_img(m):
            alt = m.group(1)
            img_path = m.group(2)
            if not img_path.startswith(("http://", "https://", "/")):
                abs_path = os.path.abspath(os.path.join(os.path.dirname(f), img_path))
                # Use forward slashes for pandoc compatibility
                img_path = abs_path.replace("\\", "/")
            return f"![{alt}]({img_path})"

        content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', fix_img, content)

        parts.append(content)
        parts.append("\n\n---\n\n")  # Separator between chapters

    # Remove last separator
    if parts and parts[-1] == "\n\n---\n\n":
        parts.pop()

    with open(output_md, "w", encoding="utf-8") as out:
        out.write("\n".join(parts))

    print(f"\nAssembled {len(ordered)} files → {output_md}")
    return output_md


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Assemble markdown files for PDF conversion")
    p.add_argument("source_dir", help="Directory containing .md files")
    p.add_argument("output_md", help="Output assembled .md file path")
    p.add_argument("--title", default="", help="Course title for cover page")
    p.add_argument("--author", default="", help="Author name")
    p.add_argument("--subtitle", default="", help="Course subtitle")
    args = p.parse_args()

    result = assemble(args.source_dir, args.output_md, args.title, args.author, args.subtitle)
    if not result:
        exit(1)
