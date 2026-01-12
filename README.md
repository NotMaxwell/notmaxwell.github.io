# notmaxwell.github.io

Personal website & blog. Static HTML + CSS hosted on GitHub Pages.

## Quick commands

### Local testing

```bash
python3 serve.py        # Start at localhost:8000
```

Then open `http://localhost:8000` in your browser. Changes to files are reflected immediately.

### Convert markdown posts to HTML

```bash
python3 convert.py      # Convert all posts
python3 convert.py --watch  # Auto-rebuild on save
```

See [posts/WORKFLOW.md](posts/WORKFLOW.md) for details.

## File structure

```
/
├─ index.html           ← Main homepage
├─ serve.py             ← Local dev server
├─ convert.py           ← Markdown → HTML converter
├─ .nojekyll            ← Disables Jekyll
├─ assets/
│  └─ css/
│     └─ site.css       ← Shared theme
├─ posts/
│  ├─ index.html        ← Blog listing
│  ├─ template.html     ← Post template
│  ├─ WORKFLOW.md       ← Blog instructions
│  └─ markdown/
│     └─ 2026-01-12-*.md
└─ projects/
   └─ index.html        ← Projects listing
```

## Workflow

1. Make changes locally
2. Test with `python3 serve.py`
3. For blog posts: write `.md` in `posts/markdown/`, then `python3 convert.py`
4. Commit and push: `git add . && git commit -m "message" && git push`

## Deployment

GitHub Pages automatically deploys from the `main` branch root directory.

No build step needed—just plain HTML + CSS.
