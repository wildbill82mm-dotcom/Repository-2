"""Build Skypoint.

Embeds the sky catalog (data/skydata.json) into src/app.html and writes:
  index.html          - full page for any web host (e.g. GitHub Pages)
  dist/artifact.html  - page fragment (no <html>/<head> wrapper) for Claude artifacts
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ROOT, "src", "app.html"), encoding="utf-8").read()
data = open(os.path.join(ROOT, "data", "skydata.json"), encoding="utf-8").read()
page = src.replace("__SKYDATA__", data.replace("</", "<\\/"))

head = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    "</head>\n<body>\n"
)
with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(head + page + "\n</body>\n</html>\n")

os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
with open(os.path.join(ROOT, "dist", "artifact.html"), "w", encoding="utf-8") as f:
    f.write(page)
print("built index.html and dist/artifact.html", len(page) // 1024, "KB")
