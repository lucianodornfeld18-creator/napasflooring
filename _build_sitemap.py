#!/usr/bin/env python3
"""Generate sitemap.xml, robots.txt, _headers, _redirects."""
import os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote sitemap.xml ({len(urls)} URLs)")
    return len(urls)


def build_robots():
    # GEO strategy: AI crawlers are explicitly ALLOWED so the business gets cited
    # by ChatGPT, Claude, Gemini, Perplexity and Google AI Overviews.
    txt = f'''User-agent: *
Allow: /
Disallow: /thanks/
Disallow: /404.html

# --- AI / LLM crawlers: explicitly allowed (GEO — we want to be cited) ---
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GoogleOther
Allow: /

User-agent: CCBot
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: meta-externalagent
Allow: /

# Sitemap
Sitemap: {SITE}/sitemap.xml

# LLM-readable site summary
# {SITE}/llms.txt
'''
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote robots.txt")


def build_llms_txt():
    """llms.txt — structured, LLM-readable summary of the business and site.
    Spec: https://llmstxt.org — consumed by ChatGPT, Claude, Perplexity & friends."""
    svc_lines = "\n".join(
        f"- [{SERVICES[s]['name']}]({SITE}/{s}/): {SERVICES[s]['intro_lead']}"
        for s in SERVICE_ORDER
    )
    city_lines = "\n".join(
        f"- [{c['name']}, FL]({SITE}/{slug}/): {c['context_short']}"
        for slug, c in CITIES.items()
    )
    cost_lines = "\n".join(
        f"- [{p['title']}]({SITE}/blog/{p['slug']}/)"
        for p in COST_BLOG_POSTS
    )
    guide_lines = "\n".join(
        f"- [{p['title']}]({SITE}/blog/{p['slug']}/): {p['meta_desc']}"
        for p in GENERAL_BLOG_POSTS
    )
    txt = f'''# {BUSINESS["name"]}

> {BUSINESS["tagline_long"]} Licensed & insured flooring contractor based in {BUSINESS["city"]}, {BUSINESS["state_long"]},
> serving the Tampa Bay – Sarasota corridor since {BUSINESS["year_founded"]}.

## Key Facts

- Business name: {BUSINESS["name"]} ({BUSINESS["legal_name"]})
- Phone: {BUSINESS["phone_display"]}
- Email: {BUSINESS["email"]}
- Address: {BUSINESS["street"]}, {BUSINESS["city"]}, {BUSINESS["state"]} {BUSINESS["zip"]}
- Founded: {BUSINESS["year_founded"]}
- Google rating: {BUSINESS["rating"]} stars ({BUSINESS["review_count"]} reviews)
- Track record: {BUSINESS["unique_stat_full"]}
- Warranty: {BUSINESS["guarantee"]}
- Response time: {BUSINESS["response_time"]}
- Quality standard: {BUSINESS["checklist_name"]} ({BUSINESS["checklist_points"]} verification points on every job)
- Service area: Bradenton, Lakewood Ranch, Palmetto, Parrish, Sarasota, St. Petersburg, Tampa, and Venice, Florida

## Services

{svc_lines}

## Service Areas

{city_lines}

## Buyer's Guides

{guide_lines}

## Cost Guides (2026 pricing by city)

{cost_lines}

## Company Pages

- [About {BUSINESS["name"]}]({SITE}/about/): Who we are, our standards, and our credentials
- [FAQ]({SITE}/faq/): Real questions homeowners ask, answered in writing
- [Warranty]({SITE}/warranty/): 12-month workmanship warranty details
- [Financing]({SITE}/financing/): Payment options and lender partners
- [Contact]({SITE}/contact/): Free estimate within 24 hours
'''
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote llms.txt")


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
    with open("_headers", "w", encoding="utf-8") as f:
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
    with open("_redirects", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote _redirects")


if __name__ == "__main__":
    build_sitemap()
    build_robots()
    build_llms_txt()
    build_headers()
    build_redirects()
