# Blog Workflow

## Quick Start

Posts are written as Markdown files in `/posts/markdown/` and automatically converted to HTML.

### Writing a post

1. **Create a new `.md` file** in `/posts/markdown/`:
   ```
   /posts/markdown/2026-01-12-your-post-title.md
   ```

2. **Write in Markdown**:
   ```markdown
   # Your Post Title

   Opening paragraph.

   ## Section heading

   Body content with **bold** and `code`.

   - List items
   - Another item
   ```

3. **Convert all markdown to HTML**:
   ```bash
   python3 convert.py
   ```

That's it. The script will:
- Convert all `.md` files in `/posts/markdown/` to HTML
- Use your post template automatically
- Update `/posts/index.html` with links to all posts (newest first)
- Estimate read time

### Watch mode (auto-rebuild)

For live editing, watch the markdown directory:

```bash
python3 convert.py --watch
```

Or use the shell wrapper:

```bash
## Setup (one time)

### 1. Install pandoc

```bash
brew install pandoc
```

### 2. (Optional) Install watchdog for watch mode

```bash
pip install watchdog
```

## Publishing

After converting posts:

```bash
git add posts/markdown/ posts/*.html posts/index.html
git commit -m "Update blog posts"
git push
```

## Structure

```
/posts/
  ├─ index.html           ← Blog listing (auto-updated)
  ├─ template.html        ← Post template (used for all posts)
  ├─ convert.py           ← Conversion script
  ├─ WORKFLOW.md          ← This file
  ├─ 2026-01-12-post-one.html
  ├─ 2026-01-12-post-two.html
  └─ markdown/
     ├─ 2026-01-12-post-one.md
     └─ 2026-01-12-post-two.md
```

## Metadata Extraction

The conversion script automatically:

- **Extracts title** from the first `# Heading` in your markdown
- **Extracts description** from the first paragraph (used in blog index)
- **Extracts date** from filename (e.g., `2026-01-12` in `2026-01-12-title.md`)
- **Estimates read time** based on word count

You don't need to add any frontmatter—just write markdown the normal way.

## Tips

- Use `# Title` for the main heading
- Use `## Sections` for subsections
- Use `### Subsections` for nested headings
- Use `**bold**` and `_italic_` for emphasis
- Use `` `code` `` for inline code
- Use triple backticks for code blocks

That's it. Write your post, run `python3 convert.py`, and you're done.

