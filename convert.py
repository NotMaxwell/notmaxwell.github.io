#!/usr/bin/env python3
"""
Convert markdown posts to HTML.

Usage:
    python3 convert.py                 # Convert all markdown files
    python3 convert.py --watch         # Watch for changes and rebuild
"""

import os
import sys
import re
import subprocess
from pathlib import Path
from datetime import datetime

# Directories
MARKDOWN_DIR = Path("posts/markdown")
POSTS_DIR = Path("posts")
TEMPLATE_PATH = POSTS_DIR / "template.html"
INDEX_PATH = POSTS_DIR / "index.html"

def extract_metadata(md_content):
    """Extract title and description from markdown."""
    title_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Untitled"
    
    # Get first paragraph as description
    desc_match = re.search(r'^(?!#)(.{0,150})', md_content, re.MULTILINE)
    description = desc_match.group(1).strip() if desc_match else "Blog post"
    
    return title, description.replace('\n', ' ')

def markdown_to_html(md_path):
    """Convert markdown file to HTML using pandoc."""
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'markdown', '-t', 'html', str(md_path)],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except FileNotFoundError:
        print("ERROR: pandoc not found. Install with: brew install pandoc")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"ERROR converting {md_path}: {e.stderr}")
        return None

def get_date_from_filename(filename):
    """Extract date from filename (e.g., 2026-01-12-title.md -> 2026-01-12)."""
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return match.group(1) if match else datetime.now().strftime('%Y-%m-%d')

def format_date(date_str):
    """Format YYYY-MM-DD to 'Jan 12, 2026'."""
    try:
        d = datetime.strptime(date_str, '%Y-%m-%d')
        return d.strftime('%b %d, %Y')
    except:
        return date_str

def estimate_read_time(html_content):
    """Rough estimate of read time in minutes."""
    # Count words (roughly)
    word_count = len(re.findall(r'\w+', html_content))
    read_time = max(1, round(word_count / 200))  # ~200 words per minute
    return read_time

def convert_post(md_path):
    """Convert a single markdown file to HTML post."""
    md_file = md_path.name
    slug = md_file.replace('.md', '')
    html_filename = f"{slug}.html"
    html_path = POSTS_DIR / html_filename
    
    print(f"Converting {md_file}...")
    
    # Read markdown
    with open(md_path, 'r') as f:
        md_content = f.read()
    
    # Extract metadata
    title, description = extract_metadata(md_content)
    date_str = get_date_from_filename(md_file)
    formatted_date = format_date(date_str)
    
    # Convert to HTML
    html_content = markdown_to_html(md_path)
    if html_content is None:
        return None
    
    # Estimate read time
    read_time = estimate_read_time(html_content)
    
    # Read template
    with open(TEMPLATE_PATH, 'r') as f:
        template = f.read()
    
    # Build final HTML
    output = template.replace(
        '<h1>Post Title Goes Here</h1>',
        f'<h1>{title}</h1>'
    ).replace(
        '<p class="post-meta">Jan 12, 2026 · 5 min read</p>',
        f'<p class="post-meta">{formatted_date} · {read_time} min read</p>'
    ).replace(
        '<main class="post-content">\n',
        f'<main class="post-content">\n{html_content}'
    )
    
    # Write output
    with open(html_path, 'w') as f:
        f.write(output)
    
    print(f"  ✓ Created {html_filename}")
    
    return {
        'slug': slug,
        'title': title,
        'description': description,
        'date': date_str,
        'formatted_date': formatted_date,
        'read_time': read_time,
        'html_filename': html_filename
    }

def update_blog_index(posts_metadata):
    """Update posts/index.html with links to all posts."""
    if not posts_metadata:
        return
    
    # Sort by date descending (newest first)
    sorted_posts = sorted(posts_metadata, key=lambda x: x['date'], reverse=True)
    
    # Generate post list HTML
    post_links = []
    for post in sorted_posts:
        link = f"""      <article class="post">
        <h2><a href="/posts/{post['html_filename']}">{post['title']}</a></h2>
        <p class="meta">{post['formatted_date']} · {post['read_time']} min read</p>
        <p>{post['description']}</p>
      </article>"""
        post_links.append(link)
    
    post_list_html = "\n\n".join(post_links)
    
    # Read current index
    with open(INDEX_PATH, 'r') as f:
        index_content = f.read()
    
    # Find and replace the post list section
    # Look for: <article class="post"> ... </article> patterns and replace them
    pattern = r'(<main>\s*).*?(<p style="margin-top:22px">)'
    replacement = f'\\1{post_list_html}\n\n      \\2'
    
    updated_index = re.sub(pattern, replacement, index_content, flags=re.DOTALL)
    
    # Write updated index
    with open(INDEX_PATH, 'w') as f:
        f.write(updated_index)
    
    print(f"\n✓ Updated {INDEX_PATH} with {len(sorted_posts)} post(s)")

def convert_all():
    """Convert all markdown files."""
    if not MARKDOWN_DIR.exists():
        print(f"ERROR: {MARKDOWN_DIR} not found")
        sys.exit(1)
    
    if not TEMPLATE_PATH.exists():
        print(f"ERROR: {TEMPLATE_PATH} not found")
        sys.exit(1)
    
    # Find all markdown files
    md_files = sorted(MARKDOWN_DIR.glob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {MARKDOWN_DIR}")
        return
    
    posts_metadata = []
    
    for md_path in md_files:
        metadata = convert_post(md_path)
        if metadata:
            posts_metadata.append(metadata)
    
    # Update index
    if posts_metadata:
        update_blog_index(posts_metadata)
    
    print(f"\n✓ Done! Converted {len(posts_metadata)} post(s)")

def watch_and_convert():
    """Watch markdown directory for changes and rebuild."""
    try:
        import time
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        
        class MarkdownHandler(FileSystemEventHandler):
            def on_modified(self, event):
                if event.src_path.endswith('.md'):
                    print(f"\nDetected change: {event.src_path}")
                    convert_all()
        
        observer = Observer()
        observer.schedule(MarkdownHandler(), str(MARKDOWN_DIR))
        observer.start()
        
        print(f"Watching {MARKDOWN_DIR} for changes (Ctrl+C to stop)...")
        while True:
            time.sleep(1)
    except ImportError:
        print("ERROR: watchdog not installed. Install with: pip install watchdog")
        sys.exit(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        print("\nStopped watching")

if __name__ == "__main__":
    if "--watch" in sys.argv:
        watch_and_convert()
    else:
        convert_all()
