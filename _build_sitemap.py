#!/usr/bin/env python3
"""Generate sitemap.xml, robots.txt, _headers, _redirects."""
import os, sys
from datetime import date
sys.path.insert(0, '/home/claude/napas')
from _data import BUSINESS, CITIES, SERVICES, SERVICE_ORDER, GENERAL_BLOG_POSTS, COST_BLOG_POSTS

DOMAIN = BUSINESS["domain"]
SITE = f"https://{DOMAIN}"
TODAY = date.today().isoformat()


def build_sitemap():
    """Build sitemap.xml with all 124 URLs and priorities."""
    urls = []

    # Homepage — priority 1.0
    urls.append((f"{SITE}/", TODAY, "weekly", "1.0"))

    # Service hubs — priority 0.9
    for s in SERVICE_ORDER:
        urls.append((f"{SITE}/{s}/", TODAY, "weekly", "0.9"))

    # City hubs — priority 0.8
    for c in CITIES:
        urls.append((f"{SITE}/{c}/", TODAY, "weekly", "0.8"))

    # Service-city pages — priority 0.7
    for s in SERVICE_ORDER:
        for c in CITIES:
            urls.append((f"{SITE}/{s}/{c}/", TODAY, "monthly", "0.7"))

    # Blog index — priority 0.7
    urls.append((f"{SITE}/blog/", TODAY, "weekly", "0.7"))

    # Blog posts — priority 0.6
    for p in GENERAL_BLOG_POSTS:
        urls.append((f"{SITE}/blog/{p['slug']}/", p.get("date_modified", TODAY), "monthly", "0.6"))
    for p in COST_BLOG_POSTS:
        urls.append((f"{SITE}/blog/{p['slug']}/", p.get("date_modified", TODAY), "monthly", "0.6"))

    # Secondary pages — priority 0.5
    for path in ["about", "contact", "faq", "financing", "warranty"]:
        urls.append((f"{SITE}/{path}/", TODAY, "monthly", "0.5"))

    # Build XML
    rows = "\n".join(
        f'  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{p}</priority></url>'
        for loc, lm, cf, p in urls
    )
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{rows}
</urlset>
'''
    with open("/home/claude/napas/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote sitemap.xml ({len(urls)} URLs)")
    return len(urls)


def build_robots():
    txt = f'''User-agent: *
Allow: /
Disallow: /thanks/
Disallow: /404.html

# Block AI scrapers that don't respect attribution
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Allow: /

User-agent: Google-Extended
Disallow: /

# Sitemap
Sitemap: {SITE}/sitemap.xml
'''
    with open("/home/claude/napas/robots.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote robots.txt")


def build_headers():
    """Cloudflare Pages _headers file — security + cache rules."""
    txt = '''/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  X-XSS-Protection: 1; mode=block

# HTML files — short cache, must revalidate
/*.html
  Cache-Control: public, max-age=3600, must-revalidate

# Images — long cache (immutable assets)
/images/*
  Cache-Control: public, max-age=31536000, immutable

# Fonts — long cache
*.woff2
  Cache-Control: public, max-age=31536000, immutable

# Sitemap & robots — moderate cache
/sitemap.xml
  Cache-Control: public, max-age=86400

/robots.txt
  Cache-Control: public, max-age=86400
'''
    with open("/home/claude/napas/_headers", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote _headers")


def build_redirects():
    """Cloudflare Pages _redirects file — common URL normalizations."""
    txt = '''# Force HTTPS (Cloudflare typically handles this already, but explicit)
http://napasflooring.com/* https://napasflooring.com/:splat 301!
http://www.napasflooring.com/* https://napasflooring.com/:splat 301!
https://www.napasflooring.com/* https://napasflooring.com/:splat 301!

# Common typos / variations
/services/* /:splat 301
/service-areas/* /:splat 301
/areas/* /:splat 301

# Service slug variations
/hardwood/* /hardwood-flooring/:splat 301
/wood-floor/* /hardwood-flooring/:splat 301
/wood-flooring/* /hardwood-flooring/:splat 301
/vinyl/* /vinyl-plank-flooring/:splat 301
/lvp/* /vinyl-plank-flooring/:splat 301
/spc/* /vinyl-plank-flooring/:splat 301
/luxury-vinyl/* /vinyl-plank-flooring/:splat 301
/tile/* /tile-installation/:splat 301
/porcelain/* /tile-installation/:splat 301
/ceramic/* /tile-installation/:splat 301
/laminate/* /laminate-flooring/:splat 301
/stairs/* /stair-treads/:splat 301
/staircase/* /stair-treads/:splat 301
/repair/* /floor-repair/:splat 301
/floor-installation/* /:splat 301

# City variations
/st-pete/* /st-petersburg/:splat 301
/saint-petersburg/* /st-petersburg/:splat 301
/saint-pete/* /st-petersburg/:splat 301
/lakewoodranch/* /lakewood-ranch/:splat 301
/lakewood/* /lakewood-ranch/:splat 301

# 404 fallback
/* /404.html 404
'''
    with open("/home/claude/napas/_redirects", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote _redirects")


if __name__ == "__main__":
    build_sitemap()
    build_robots()
    build_headers()
    build_redirects()
