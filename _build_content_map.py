#!/usr/bin/env python3
"""Generate _content_map.json — the anti-cannibalization ledger.

Every (service × city) head term is targeted by TWO pages on this site:
  • a TRANSACTIONAL hub  /[service]/[city]/         (intent: hire / get a quote)
  • an INFORMATIONAL post /blog/[service]-cost-[city]/ (intent: research the price)

Search engines can treat near-duplicate intent as cannibalization. This ledger
documents the deliberate split: distinct primary keyword, distinct intent, a
single canonical owner of the head term, and the cross-link direction — so the
two pages reinforce each other instead of competing. It also maps the decision
guides and the floor-repair vs. hardwood-refinishing overlap."""
import os, sys, json
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import CITIES, SERVICES, SERVICE_ORDER, COST_BLOG_POSTS, GUIDES, GENERAL_BLOG_POSTS

DOMAIN = "napasflooring.com"
SITE = f"https://{DOMAIN}"

cost_by_pair = {(p["service_slug"], p["city_slug"]): p for p in COST_BLOG_POSTS}

pairs = []
for s in SERVICE_ORDER:
    svc = SERVICES[s]
    for cslug, city in CITIES.items():
        cost = cost_by_pair.get((s, cslug))
        kw = cost["keyword"] if cost else svc["short"].lower()
        pairs.append({
            "service": s,
            "city": cslug,
            "head_term": f"{kw} {city['name'].lower()}",
            "transactional": {
                "url": f"/{s}/{cslug}/",
                "intent": "transactional (hire / request a quote)",
                "primary_keyword": f"{kw} {city['name'].lower()} fl",
                "title_pattern": f"{svc['short']} {city['name']} FL",
            },
            "informational": {
                "url": f"/blog/{cost['slug']}/" if cost else None,
                "intent": "informational (research cost / what it includes)",
                "primary_keyword": f"{kw} cost {city['name'].lower()}",
                "title_pattern": f"{svc['short']} Cost in {city['name']}, FL (2026)",
            },
            "canonical_owner_of_head_term": "transactional",
            "internal_links": {
                "informational_to_transactional": "CTA + related box → the service-city hub (capture the booking)",
                "transactional_to_informational": "pricing section → the cost post (deep-dive on numbers)",
            },
        })

# Guides are top-of-funnel decision content; they must not target the same
# head terms as the transactional hubs or the cost posts.
guides = [{
    "url": f"/guides/{g['slug']}/",
    "intent": "decision / consideration (top-of-funnel)",
    "title": g["title"],
    "does_not_target": "any [service] [city] head term or [service] cost [city] term",
} for g in GUIDES]

ledger = {
    "site": DOMAIN,
    "generated": date.today().isoformat(),
    "purpose": "Anti-cannibalization ledger. Documents the intent split between transactional "
               "service-city hubs and informational blog-cost posts so the two pages targeting "
               "each head term reinforce rather than compete.",
    "policy": {
        "head_term_canonical_owner": "transactional service-city hub",
        "cost_post_role": "informational long-tail ('... cost ...' modifier) — never duplicates the hub's intent",
        "title_must_differ": True,
        "meta_desc_must_differ": True,
        "one_h1_keyword_owner_per_head_term": True,
        "cross_link": "bidirectional (hub <-> cost post), no orphan pages",
        "guides_rule": "decision guides stay top-of-funnel; they never target a [service]/[city] or cost head term",
    },
    "overlap_resolutions": [
        {
            "topic": "Hardwood refinishing vs. floor repair",
            "note": "Sand-and-refinish appears as a line item under /floor-repair/ (repair context) but the "
                    "canonical hub for the 'hardwood floor refinishing [city]' head term is /hardwood-refinishing/. "
                    "floor-repair pages link to hardwood-refinishing for refinish-led intent.",
            "canonical": "/hardwood-refinishing/",
        },
        {
            "topic": "Refinish blog guide vs. refinishing service",
            "note": "/blog/refinishing-old-oak-floors-tampa-bay/ is the informational restoration guide; "
                    "/hardwood-refinishing/ is the transactional hub. Guide links to the hub for booking.",
            "canonical_for_booking": "/hardwood-refinishing/",
        },
    ],
    "counts": {
        "services": len(SERVICE_ORDER),
        "cities": len(CITIES),
        "transactional_hubs": len(SERVICE_ORDER) * len(CITIES) + len(SERVICE_ORDER),
        "cost_posts": len(COST_BLOG_POSTS),
        "decision_guides": len(GUIDES),
        "general_posts": len(GENERAL_BLOG_POSTS),
        "pairs_mapped": len(pairs),
    },
    "pairs": pairs,
    "guides": guides,
}

with open("_content_map.json", "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

print(f"Wrote _content_map.json — {len(pairs)} service×city pairs, {len(guides)} guides mapped.")
