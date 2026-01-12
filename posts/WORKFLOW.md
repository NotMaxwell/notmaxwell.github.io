# Blog Workflow

## Quick Start

Posts are kept as Markdown files in `/posts/markdown/` and converted to HTML for publishing.

### Writing a post

1. **Create a new `.md` file** in `/posts/markdown/`:
   ```
   /posts/markdown/2026-01-12-your-post-title.md
   ```

2. **Write in Markdown** (see sample post for reference):
   ```markdown
   # Your Post Title

   Opening paragraph.

   ## Section heading

   Body content with **bold** and `code`.

   - List items
   - Another item

   ## Another section

   More content.
   ```

3. **Convert to HTML** using `pandoc`:
   ```bash
   pandoc -f markdown -t html \
     /posts/markdown/2026-01-12-your-post-title.md \
     -o /posts/converted.html
   ```

   Then manually copy the HTML content into the template at `/posts/template.html`.

### Alternative: Simple Python script

Create `/convert.py` to batch-convert markdown to HTML:

```python
#!/usr/bin/env python3
import os
import subprocess
import re

md_dir = 'posts/markdown'
posts_dir = 'posts'

for md_file in sorted(os.listdir(md_dir)):
    if not md_file.endswith('.md'):
        continue
    
    md_path = os.path.join(md_dir, md_file)
    slug = md_file.replace('.md', '')
    html_filename = f'{slug}.html'
    html_path = os.path.join(posts_dir, html_filename)
    
    # Convert markdown to HTML
    result = subprocess.run(
        ['pandoc', '-f', 'markdown', '-t', 'html', md_path],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        print(f'Error converting {md_file}')
        continue
    
    # Read template and insert content
    with open('posts/template.html', 'r') as f:
        template = f.read()
    
    # Extract title from markdown (first h1)
    title_match = re.search(r'^# (.+)$', result.stdout, re.MULTILINE)
    title = title_match.group(1) if title_match else 'Post'
    
    # Insert converted content and title
    output = template.replace(
        '<main class="post-content">',
        f'<main class="post-content">\n{result.stdout}'
    ).replace(
        '<h1>Post Title Goes Here</h1>',
        f'<h1>{title}</h1>'
    )
    
    # Write to posts directory
    with open(html_path, 'w') as f:
        f.write(output)
    
    print(f'Created {html_path}')
```

Run it:
```bash
python3 convert.py
```

### Publishing

1. Edit `/posts/index.html` to add a link to your new post
2. Commit and push:
   ```bash
   git add posts/markdown/ posts/*.html
   git commit -m "Add new post: your title"
   git push
   ```

## Structure

```
/posts/
  ├─ index.html           ← Blog listing page
  ├─ template.html        ← Post template (copy and customize)
  ├─ 2026-01-12-post-one.html
  ├─ 2026-01-12-post-two.html
  └─ markdown/
     ├─ 2026-01-12-post-one.md
     └─ 2026-01-12-post-two.md
```

## Install pandoc (one time)

If you don't have `pandoc`:

```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Or download from https://pandoc.org/installing.html
```

That's it. Write markdown, convert to HTML, update the index.
