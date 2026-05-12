#!/usr/bin/env python3
"""Generate /index.html — the homepage. Bold editorial showcase."""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

OUT = "/home/claude/napas/index.html"

# ============================================================================
# SEO META — title 50–65 chars, desc 130–158 chars
# ============================================================================
TITLE = f"Flooring Contractor Bradenton FL · Tampa Bay · Napa's Flooring"  # 62 chars
DESC = (
    f"Hardwood, vinyl plank, tile, laminate &amp; stair tread installation across "
    f"Bradenton, Sarasota, Tampa &amp; the Gulf Coast. {BUSINESS['review_count']}× 5★ Google · Free estimate in 24 hrs."
)  # ~158 chars
CANONICAL = f"{SITE}/"

# ============================================================================
# SCHEMAS — homepage carries Org + Website + LocalBusiness
# ============================================================================
SCHEMAS = [
    schema_website(),
    schema_organization(),
    schema_local_business(CANONICAL, "Napa's Flooring — Tampa Bay flooring contractor"),
    schema_breadcrumb([("Home", SITE + "/")]),
]

# ============================================================================
# HERO
# ============================================================================
hero = f'''<section class="hero">
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-label">Issue 06 · 2026 — A Tampa Bay Flooring Journal</div>
      <h1 class="hero-h1">Floors built<br>for <em>Florida<span class="stop">.</span></em></h1>
      <p class="hero-sub">Napa&rsquo;s is a small, craft-first flooring crew working out of east {BUSINESS["city"]}. We measure twice, acclimate properly, and finish the work we started — every plank, every transition, every baseboard reset. {BUSINESS["unique_stat_full"]}.</p>
      <div class="hero-cta">
        <a href="/contact/#quote" class="btn btn-orange">Get a free estimate <span class="btn-arrow"></span></a>
        <a href="{TEL_LINK}" class="btn btn-outline-light">{BUSINESS["phone_display"]}</a>
      </div>
      <div class="hero-meta">
        <div><strong>{BUSINESS["unique_stat_number"]}</strong><span>Tampa Bay floors</span></div>
        <div><strong>{BUSINESS["rating"]}★</strong><span>Google · {BUSINESS["review_count"]} reviews</span></div>
        <div><strong>{2026 - BUSINESS["year_founded"]} yrs</strong><span>Crew-led · est {BUSINESS["year_founded"]}</span></div>
        <div><strong>24h</strong><span>To written estimate</span></div>
      </div>
    </div>
    <div class="hero-art">
      <img src="https://images.unsplash.com/photo-1622372738946-62e02505feb3?auto=format&amp;fit=crop&amp;w=900&amp;q=80" alt="Wide-plank European white oak hardwood floor installed by Napa's Flooring in a Lakewood Ranch home" width="900" height="1200" loading="eager" fetchpriority="high">
      <div class="hero-art-tag">Now Installing</div>
      <div class="hero-art-caption"><span>Cover Photo</span><span>Lakewood Ranch · Engineered White Oak · 7&prime;&prime; Plank</span></div>
    </div>
  </div>
</section>'''

# ============================================================================
# TICKER (animated marquee under hero)
# ============================================================================
ticker = ticker_bar()

# ============================================================================
# SOCIAL PROOF STRIP
# ============================================================================
proof = f'''<section class="proof-strip tight" style="padding:36px 0">
  <div class="proof-grid">
    <div class="proof-item">
      <div class="proof-num">{BUSINESS["unique_stat_number"]}</div>
      <div class="proof-label">Floors finished · Tampa Bay</div>
    </div>
    <div class="proof-item">
      <div class="proof-num">{BUSINESS["rating"]}★</div>
      <div class="proof-label">Google · {BUSINESS["review_count"]} verified reviews</div>
    </div>
    <div class="proof-item">
      <div class="proof-num">47</div>
      <div class="proof-label">Point install standard</div>
    </div>
    <div class="proof-item">
      <div class="proof-num">12mo</div>
      <div class="proof-label">Workmanship warranty</div>
    </div>
    <div class="proof-item">
      <div class="proof-num">24h</div>
      <div class="proof-label">Free written estimate</div>
    </div>
  </div>
</section>'''

# ============================================================================
# SERVICES GRID — 6 service cards, magazine block layout
# ============================================================================
service_cards_html = ""
for slug in SERVICE_ORDER:
    s = SERVICES[slug]
    service_cards_html += f'''<a href="/{slug}/" class="service-card">
  <div class="service-card-num">{s["icon"]} / {s["short"]}</div>
  <h3>{s["h1_phrase"]}</h3>
  <p class="service-card-desc">{s["intro_lead"]}</p>
  <span class="service-card-cta">See {s["short"]} Work</span>
</a>'''

services = f'''<section class="services-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">The Work · Six Disciplines</span>
        <h2>Six things we install. <em>One way</em> we install them.</h2>
        <div class="section-head-text"><p>Hardwood, vinyl, tile, laminate, stair treads, repair &mdash; every one of them gets the same {CHECKLIST["points"]}-point standard, the same two installers, the same acclimation log, and the same 12-month workmanship warranty.</p></div>
      </div>
    </div>
    <div class="services-grid">{service_cards_html}</div>
  </div>
</section>'''

# ============================================================================
# WHY US — 6 numbered items
# ============================================================================
why_items_html = ""
for w in WHY_US_POINTS:
    why_items_html += f'''<div class="why-item">
  <div class="why-num">{w["num"]}</div>
  <div>
    <h3>{w["title"]}</h3>
    <p>{w["body"]}</p>
  </div>
</div>'''

why_us = f'''<section class="why-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label">Why It Costs What It Costs</span>
        <h2>The reasons we&rsquo;re <em>different</em>, in plain English.</h2>
        <div class="section-head-text"><p>Six things you should ask every flooring contractor about. We&rsquo;ve put our answers in writing here so you don&rsquo;t have to ask.</p></div>
      </div>
    </div>
    <div class="why-grid">{why_items_html}</div>
  </div>
</section>'''

# ============================================================================
# PULL QUOTE — editorial signature
# ============================================================================
pull_quote = f'''<div class="container"><blockquote class="pull-quote">
<p>A flooring job is finish carpentry pretending to be flooring. Treat it that way, and the floor lasts. Treat it like flooring, and it doesn&rsquo;t.</p>
<cite>— The Napa&rsquo;s Crew · Est. {BUSINESS["year_founded"]}</cite>
</blockquote></div>'''

# ============================================================================
# SERVICE AREAS GRID — 8 cities
# ============================================================================
area_cards_html = ""
for slug, c in CITIES.items():
    area_cards_html += f'''<a href="/{slug}/" class="area-card">
  <div class="area-card-name">{c["name"]}, FL</div>
  <div class="area-card-meta">{c["county"]} · {len(c["zips"])} ZIPs</div>
  <span class="area-card-arrow">See {c["name"]} Work →</span>
</a>'''

areas = f'''<section class="areas-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label on-dark">Service Map · Eight Cities</span>
        <h2>Eight cities. <em>One crew.</em></h2>
        <div class="section-head-text"><p>From Anna Maria Island to Hyde Park, from Snell Isle to Wellen Park &mdash; we work the Gulf Coast corridor that the locals know and the tourists don&rsquo;t. Pick your city to see the bairros and ZIPs we cover.</p></div>
      </div>
    </div>
    <div class="areas-grid">{area_cards_html}</div>
  </div>
</section>'''

# ============================================================================
# PROCESS — 4 steps
# ============================================================================
process_html = ""
for p in PROCESS_STEPS:
    process_html += f'''<div class="process-step">
  <div class="process-num">{p["num"]}</div>
  <h3>{p["title"]}</h3>
  <p>{p["body"]}</p>
</div>'''

process = f'''<section class="process-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">04</div>
      <div class="section-head-meta">
        <span class="mono-label">How It Goes · Four Stages</span>
        <h2>What happens between the call and the <em>clean floor</em>.</h2>
        <div class="section-head-text"><p>No surprises. No pressure. No subcontractors. Here&rsquo;s the entire process, from first estimate to final walkthrough.</p></div>
      </div>
    </div>
    <div class="process-grid">{process_html}</div>
  </div>
</section>'''

# ============================================================================
# REVIEWS section
# ============================================================================
reviews = reviews_section(limit=6, headline="What homeowners actually say.")

# Replace generated section number to 05 (it ships as 06 by default)
reviews = reviews.replace('<div class="section-head-num">06</div>', '<div class="section-head-num">05</div>')

# ============================================================================
# CTA BAND (between reviews and final)
# ============================================================================
cta_banner = f'''<div class="container">{contact_banner()}</div>'''

# ============================================================================
# FINAL CTA
# ============================================================================
final = final_cta(
    headline="Ready when you are.",
    sub="Send us the room, the rough size, and what you&rsquo;d like installed. We&rsquo;ll come measure, talk through options, and email you a written line-itemized quote within 24 hours."
)

# ============================================================================
# ASSEMBLE
# ============================================================================
body = "\n".join([hero, ticker, proof, services, pull_quote, why_us, areas, process, reviews, cta_banner, final])
head_html = head(TITLE, DESC, CANONICAL,
    og_image=f"{SITE}/images/og-default.jpg",
    og_type="website",
    json_ld=SCHEMAS,
)
header_html = header(active="home")

write_page(OUT, head_html, header_html, body)
print(f"Wrote {OUT}")
