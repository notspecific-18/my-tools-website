"""Replace the placeholder site address everywhere. Run ONCE, e.g.:
   python set_url.py https://alice.github.io/toolnest
   python set_url.py https://toolnest.example        (custom domain, no sub-folder)"""
import sys, pathlib
OLD = "https://YOUR-USERNAME.github.io/toolnest"
if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
    sys.exit("Usage: python set_url.py https://your-site-address")
new = sys.argv[1].rstrip("/"); n = 0
for p in pathlib.Path(__file__).parent.rglob("*"):
    if p.is_file() and p.suffix in (".html", ".xml", ".txt"):
        t = p.read_text(encoding="utf-8")
        if OLD in t:
            p.write_text(t.replace(OLD, new), encoding="utf-8"); n += 1
print(f"Updated {n} files to {new}")
