#!/usr/bin/env python3
"""Generate sitemap.xml, robots.txt, _headers, _redirects."""
import os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import BUSINESS, CITIES, SERVICES, SERVICE_ORDER, GENERAL_BLOG_POSTS, COST_BLOG_POSTS, GUIDES, GLOSSARY

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

    # Guides hub + guides — priority 0.7 / 0.6
    urls.append((f"{SITE}/guides/", TODAY, "weekly", "0.7"))
    for g in GUIDES:
        urls.append((f"{SITE}/guides/{g['slug']}/", g.get("date_modified", TODAY), "monthly", "0.6"))

    # Glossary — priority 0.6
    urls.append((f"{SITE}/glossary/", TODAY, "monthly", "0.6"))

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

# LLM-readable site summaries (llmstxt.org convention — comments, not directives)
# {SITE}/llms.txt
# {SITE}/llms-full.txt
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
    decision_guide_lines = "\n".join(
        f"- [{g['title']}]({SITE}/guides/{g['slug']}/): {g['meta_desc']}"
        for g in GUIDES
    )
    txt = f'''# {BUSINESS["name"]}

> {BUSINESS["tagline_long"]} Licensed & insured flooring contractor based in {BUSINESS["city"]}, {BUSINESS["state_long"]},
> serving the Tampa Bay – Sarasota corridor since {BUSINESS["year_founded"]}.
> Full extended version with services, pricing tiers and glossary: {SITE}/llms-full.txt

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

## Decision Guides

{decision_guide_lines}

## Glossary

- [Flooring Glossary]({SITE}/glossary/): {len(GLOSSARY)} flooring terms explained in plain English (acclimation, calcium chloride, lippage, SPC, wear layer, and more).

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


def _plain(s):
    """Strip HTML tags and decode the few entities used in the data, for plain-text llms-full."""
    import re
    s = str(s)
    repl = {
        "&mdash;": "—", "&ndash;": "–", "&rsquo;": "’", "&lsquo;": "‘",
        "&ldquo;": "“", "&rdquo;": "”", "&amp;": "&", "&times;": "×",
        "&nbsp;": " ", "&rarr;": "→", "&deg;": "°",
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    s = re.sub(r"<[^>]+>", "", s)        # strip any HTML tags
    return re.sub(r"\s+", " ", s).strip()


def build_llms_full():
    """llms-full.txt — the extended, content-rich version referenced by llms.txt.
    A single plain-text document an LLM can ingest to answer detailed questions about
    Napa's services, pricing tiers, city coverage, guides and terminology."""
    parts = []
    parts.append(f"# {BUSINESS['name']} — Full Site Brief\n")
    parts.append(
        f"> {_plain(BUSINESS['tagline_long'])} Licensed & insured flooring contractor based in "
        f"{BUSINESS['city']}, {BUSINESS['state_long']}, serving the Tampa Bay – Sarasota corridor "
        f"since {BUSINESS['year_founded']}.\n"
    )

    parts.append("## Business Facts\n")
    parts.append(
        f"- Legal name: {BUSINESS['legal_name']}\n"
        f"- Phone: {BUSINESS['phone_display']}  | Email: {BUSINESS['email']}\n"
        f"- Address: {BUSINESS['street']}, {BUSINESS['city']}, {BUSINESS['state']} {BUSINESS['zip']}\n"
        f"- Founded: {BUSINESS['year_founded']}  | Google rating: {BUSINESS['rating']}★ ({BUSINESS['review_count']} reviews)\n"
        f"- Track record: {_plain(BUSINESS['unique_stat_full'])}\n"
        f"- Warranty: {_plain(BUSINESS['guarantee'])}\n"
        f"- Quality standard: {BUSINESS['checklist_name']} ({BUSINESS['checklist_points']} verification points on every job)\n"
        f"- Financing: third-party 0% promotional and fixed-payment options on jobs over $2,500\n"
        f"- Service area: Bradenton, Lakewood Ranch, Palmetto, Parrish, Sarasota, St. Petersburg, Tampa, Venice (Florida)\n"
    )

    parts.append("## Services (with pricing tiers and FAQs)\n")
    for s in SERVICE_ORDER:
        svc = SERVICES[s]
        parts.append(f"### {svc['name']} — {SITE}/{s}/")
        parts.append(_plain(svc["intro_lead"]))
        parts.append(_plain(svc["intro_long_p1"]))
        parts.append("Pricing tiers (2026 Tampa Bay, installed):")
        for label, price, note in svc["pricing_rows"]:
            parts.append(f"- {_plain(label)}: {_plain(price)} ({_plain(note)})")
        parts.append("FAQs:")
        for q, a in svc["faqs"]:
            parts.append(f"- Q: {_plain(q)}\n  A: {_plain(a)}")
        parts.append("")

    parts.append("## Service Areas (local context)\n")
    for slug, c in CITIES.items():
        parts.append(f"### {c['name']}, FL ({c['county']}) — {SITE}/{slug}/")
        parts.append(_plain(c["context_short"]))
        parts.append(f"Humidity/install note: {_plain(c['humidity_note'])}")
        parts.append(f"Primary market: {_plain(c['primary_market'])}")
        parts.append("")

    parts.append("## Decision Guides\n")
    for g in GUIDES:
        parts.append(f"- {g['title']} — {SITE}/guides/{g['slug']}/: {_plain(g['meta_desc'])}")
    parts.append("")

    parts.append("## Buyer's Guides (Journal)\n")
    for p in GENERAL_BLOG_POSTS:
        parts.append(f"- {p['title']} — {SITE}/blog/{p['slug']}/: {_plain(p['meta_desc'])}")
    parts.append("")

    parts.append("## Glossary\n")
    for t, d in GLOSSARY:
        parts.append(f"- {t}: {_plain(d)}")
    parts.append("")

    parts.append("## Company Pages\n")
    parts.append(
        f"- About: {SITE}/about/\n"
        f"- FAQ: {SITE}/faq/\n"
        f"- Warranty (12-month workmanship): {SITE}/warranty/\n"
        f"- Financing: {SITE}/financing/\n"
        f"- Contact (free estimate within 24 hours): {SITE}/contact/\n"
    )

    with open("llms-full.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(parts) + "\n")
    print("Wrote llms-full.txt")


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
/refinishing/* /hardwood-refinishing/:splat 301
/refinish/* /hardwood-refinishing/:splat 301
/sand-and-refinish/* /hardwood-refinishing/:splat 301
/hardwood-floor-refinishing/* /hardwood-refinishing/:splat 301
/floor-refinishing/* /hardwood-refinishing/:splat 301
/guide/* /guides/:splat 301

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
    build_llms_full()
    build_headers()
    build_redirects()
