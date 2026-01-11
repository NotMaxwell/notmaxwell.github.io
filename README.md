# notmaxwell.github.io

## Quick: site files added

I added a single-file homepage and a projects index for GitHub Pages:

- `index.html` — main homepage
- `.nojekyll` — disables Jekyll so static files are served verbatim
- `projects/index.html` — projects listing (use `/projects/<name>/` for each project)

Deploy steps (fast):

```bash
git add index.html projects/ .nojekyll README.md
git commit -m "Add homepage and projects index"
git push
```

Then enable GitHub Pages in the repo Settings → Pages → deploy from `main` branch, root.
