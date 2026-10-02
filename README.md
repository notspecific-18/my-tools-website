# ToolNest

Free online tools that run entirely in the browser: Percentage, GPA and Age calculators, Word & Character Counter, Image Compressor and PDF Merger. Plain HTML, CSS and JavaScript, so it works on free static hosting.

## Folder structure
```
index.html            homepage (tools grouped by category)
404.html              custom error page
about/ privacy/ contact/
tools/<tool-name>/index.html    one page per tool
assets/css/style.css  all styling (light/dark themes)
assets/js/app.js      header, footer, search, theme toggle; list of tools (TOOLS)
assets/js/config.js   your contact email
assets/vendor/        pdf-lib (MIT licence included), used by the PDF Merger
sitemap.xml robots.txt favicon.svg set_url.py
```

## Before you publish (3 required steps)
1. **Set your site address.** Run once: `python set_url.py https://YOUR-USERNAME.github.io/toolnest` (use your real address). It updates canonical links, structured data, sitemap.xml and robots.txt.
2. **Add your contact email** in `assets/js/config.js`. Until you do, the Contact page honestly says details are not set up. Do not publish without it.
3. **Read `privacy/index.html`** and keep it true. If you add ads, analytics or affiliate links, update it first.

## Test locally
Open a terminal in this folder and run `python -m http.server 8000`, then open http://localhost:8000. (Opening files by double-click can break some features.) Try every tool on your phone too: connect to the same Wi-Fi and open `http://<your-computer-ip>:8000`.

## Publish on GitHub Pages
1. Create a free GitHub account, then a new **public** repository, e.g. `toolnest`.
2. Upload all files from this folder so `index.html` is at the top level of the repository (Add file > Upload files, or use git).
3. Go to **Settings > Pages**. Under Build and deployment choose **Deploy from a branch**, branch **main**, folder **/ (root)**, then Save.
4. After a minute or two the site is live at `https://YOUR-USERNAME.github.io/toolnest/`. If you had not run `set_url.py` yet, run it with that address and upload the changed files again.
5. Open every page and tool once on your phone to check.

## Connect a custom domain
1. Buy a domain from any registrar.
2. In **Settings > Pages > Custom domain**, enter your domain (for example `toolnest.example`) and Save. GitHub adds a `CNAME` file to the repository.
3. At your registrar's DNS settings add four **A records** for the root (`@`): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`. Optionally add the matching AAAA records listed in GitHub's docs. For `www`, add a **CNAME** record pointing to `YOUR-USERNAME.github.io`.
4. Wait for DNS to update (minutes to a few hours), then tick **Enforce HTTPS** in Settings > Pages once it becomes available.
5. Your site address changes (no `/toolnest/` sub-folder), so decide your final address first and run `python set_url.py https://toolnest.example` once. `set_url.py` only replaces the original placeholder; if you already ran it with the github.io address, search and replace that address with the new one in all `.html`, `.xml` and `.txt` files. Upload the files again. The 404 page adapts automatically.
6. Recommended: verify the domain in your GitHub account settings (Settings > Pages) to prevent others from claiming it.
Docs: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

## Submit to Google Search Console
1. Go to https://search.google.com/search-console and sign in with a Google account.
2. Add a property. For a **custom domain** choose **Domain** and add the DNS TXT record Google shows you at your registrar. For the plain **github.io** address choose **URL prefix**, enter `https://YOUR-USERNAME.github.io/toolnest/`, and verify with the HTML tag (paste the `<meta>` tag into the `<head>` of `index.html` and upload).
3. Open **Sitemaps**, enter `sitemap.xml`, and Submit. Status should become Success.
4. Open **URL Inspection**, paste your homepage address and choose **Request indexing**. Do the same for a few tool pages.
5. Check the **Pages** report after a few days. Indexing can take days or weeks and is never guaranteed. Good content, internal links and time matter more than anything else.

## About advertising
There is a hidden ad area (`.ad-slot`) and an affiliate area on pages. Add your ad code inside it and add the class `on` only after you are approved. Google AdSense has its own approval rules and requires a Privacy page and, in some regions, a cookie consent message; check its current policies before applying. No earnings are promised or implied.

## Add a new tool
Copy a folder in `tools/`, edit the page, add an entry to `TOOLS` in `assets/js/app.js` (for search), add a link on the homepage and a line in `sitemap.xml`.

## Future improvements
- Offline use of the whole site via a service worker (the tools already work offline once loaded).
- More tools: unit converter, QR code maker, text case converter, image resizer and converter, PDF split / rotate / compress.
- Drag-and-drop reordering in the PDF Merger; "download all" for the Image Compressor (as a ZIP).
- Urdu interface and right-to-left layout.
- A build step so the header and footer are plain HTML on every page (slightly better for SEO).
- Short how-to articles for each tool, plus FAQ structured data, to attract search traffic.
- Privacy-friendly analytics and a cookie-consent banner if ads are enabled.
- Automated browser tests and regular Lighthouse checks.
