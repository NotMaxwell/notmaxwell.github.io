# notmaxwell.github.io

Personal website and blog for Maxwell McCormick. Hand-written static HTML + CSS,
hosted on GitHub Pages. No framework, no build step, no dependencies to keep alive.

Live at <https://notmaxwell.github.io/>.

## Quick commands

### Local testing

```bash
python3 serve.py        # Serves the site at http://localhost:8000
```

Changes to files show up on reload — no restart needed.

### Convert markdown posts to HTML

```bash
python3 convert.py          # Convert all posts
python3 convert.py --watch  # Auto-rebuild on save
```

Requires `pandoc` on `PATH` (`brew install pandoc`, or `choco install pandoc` on
Windows). See [posts/WORKFLOW.md](posts/WORKFLOW.md) for the post-writing flow.

## File structure

```
/
├─ index.html           ← Homepage
├─ projects/index.html  ← Full project list
├─ robots.txt           ← Crawler rules
├─ sitemap.xml          ← Update when adding a page or post
├─ serve.py             ← Local dev server
├─ convert.py           ← Markdown → HTML converter
├─ .nojekyll            ← Disables Jekyll
├─ assets/
│  ├─ favicon.svg
│  ├─ resume.docx
│  └─ css/site.css      ← Shared theme; every page links this
└─ posts/
   ├─ index.html        ← Blog listing (generated between the POSTS markers)
   ├─ template.html     ← Post template
   ├─ WORKFLOW.md       ← Blog instructions
   └─ markdown/         ← Post sources
```

### Conventions

- **One stylesheet.** `assets/css/site.css` holds everything shared. Page-specific
  rules go in a `<style>` block after the `<link>` tag — never copy the theme into a page.
- **Generated regions are marked.** `convert.py` owns the block between
  `<!-- POSTS:START -->` and `<!-- POSTS:END -->` in `posts/index.html`, and the
  title, meta description, `<h1>`, post-meta line and `<main class="post-content">`
  body of each generated post. Edit the markdown, not the generated HTML.
- The name shown in generated post titles lives in one place: `SITE_AUTHOR` in
  `convert.py`, which must match `posts/template.html`.

## Deployment

GitHub Pages builds this site with the Actions workflow in
[.github/workflows/static.yml](.github/workflows/static.yml), which runs **only on
pushes to the `production` branch**. Pushing to `main` does *not* publish anything.

Day-to-day flow:

```bash
# 1. Work on main
git add . && git commit -m "message" && git push origin main

# 2. Check it locally
python3 serve.py

# 3. Publish when you're happy with it
git checkout production
git merge main
git push origin production      # ← this is what triggers the deploy
git checkout main
```

You can also publish without a merge by running the workflow by hand from the
repository's **Actions** tab (it allows `workflow_dispatch`), but it still builds
from `production`, so the branch has to be up to date first.
