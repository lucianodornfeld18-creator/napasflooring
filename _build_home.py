#!/usr/bin/env python3
"""Generate /index.html — homepage with real photos and orange+white design."""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

OUT = "/home/claude/napas/index.html"

TITLE = "Flooring Contractor Bradenton FL · Tampa Bay · Napa's Flooring"
DESC = (
    "Hardwood, vinyl plank, tile, laminate & stair tread installation across "
    "Bradenton, Sarasota, Tampa & the Gulf Coast. "
    f"{BUSINESS['review_count']}× 5★ Google · Free estimate in 24 hrs."
)[:158]
CANONICAL = f"{SITE}/"

SCHEMAS = [
    schema_website(),
    schema_organization(),
    schema_local_business(CANONICAL, "Napa's Flooring — Tampa Bay flooring contractor"),
    schema_breadcrumb([("Home", SITE + "/")]),
]

# HERO — photo background + real work photos grid
hero = f'''<section class="hero">
  <img class="hero-bg" src="/images/photo-lvp-living.jpg" alt="Wood-look flooring installed in a Florida living room by Napa's Flooring" loading="eager" fetchpriority="high">
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-label">Bradenton · Sarasota · Tampa · Serving Tampa Bay Since {BUSINESS["year_founded"]}</div>
      <h1 class="hero-h1">Flooring built<br><em>right</em>, finished<br><em>proud.</em></h1>
      <p class="hero-sub">Napa&rsquo;s is a small, craft-first flooring crew based in east Bradenton. Hardwood, vinyl plank, tile, laminate, stair treads — installed by the same two people who measured your home, every time.</p>
      <div class="hero-cta">
        <a href="/contact/#quote" class="btn btn-orange">Get a Free Estimate <span class="btn-arrow"></span></a>
        <a href="{TEL_LINK}" class="btn btn-outline-light">{BUSINESS["phone_display"]}</a>
      </div>
      <div class="hero-meta">
        <div><strong>{BUSINESS["unique_stat_number"]}</strong><span>Tampa Bay Floors</span></div>
        <div><strong>{BUSINESS["rating"]}★</strong><span>Google · {BUSINESS["review_count"]} reviews</span></div>
        <div><strong>{2026 - BUSINESS["year_founded"]} yrs</strong><span>In Business</span></div>
        <div><strong>24h</strong><span>Written Estimate</span></div>
      </div>
    </div>
    <div class="hero-art">
      <div class="hero-photo">
        <img src="/images/photo-hardwood-dark.jpg" alt="Dark hardwood floor installed by Napa's Flooring" loading="eager">
      </div>
      <div class="hero-photo">
        <img src="/images/photo-tile-marble.jpg" alt="Marble-look tile bathroom by Napa's Flooring" loading="lazy">
      </div>
      <div class="hero-photo">
        <img src="/images/photo-lvp-landing.jpg" alt="LVP flooring on a stair landing by Napa's Flooring" loading="lazy">
      </div>
    </div>
  </div>
</section>'''

# TICKER
ticker = ticker_bar()

# PROOF STRIP
proof = f'''<section class="proof-strip tight">
  <div class="proof-grid">
    <div class="proof-item"><div class="proof-num">{BUSINESS["unique_stat_number"]}</div><div class="proof-label">Floors in Tampa Bay</div></div>
    <div class="proof-item"><div class="proof-num">{BUSINESS["rating"]}★</div><div class="proof-label">Google · {BUSINESS["review_count"]} reviews</div></div>
    <div class="proof-item"><div class="proof-num">47 pts</div><div class="proof-label">Install standard</div></div>
    <div class="proof-item"><div class="proof-num">12 mo</div><div class="proof-label">Workmanship warranty</div></div>
    <div class="proof-item"><div class="proof-num">24h</div><div class="proof-label">Written estimate</div></div>
  </div>
</section>'''

# SERVICES GRID
svc_cards = ""
for slug in SERVICE_ORDER:
    s = SERVICES[slug]
    svc_cards += f'''<a href="/{slug}/" class="service-card">
  <div class="service-card-num">{s["icon"]} — {s["short"]}</div>
  <h3>{s["h1_phrase"]}</h3>
  <p class="service-card-desc">{s["intro_lead"]}</p>
  <span class="service-card-cta">View {s["short"]} work</span>
</a>'''

services = f'''<section class="services-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">Six Services · Same Crew · Same Standard</span>
        <h2>Every floor we install — <em>done right</em>.</h2>
        <div class="section-head-text"><p>Hardwood, vinyl plank, tile, laminate, stair treads, and repair. Every one gets the same 47-point standard, two installers, acclimation log, and 12-month workmanship warranty.</p></div>
      </div>
    </div>
    <div class="services-grid">{svc_cards}</div>
  </div>
</section>'''

# REAL WORK GALLERY
gallery = f'''<section style="background:var(--white)">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label">Our Work · Tampa Bay Homes</span>
        <h2>Real floors. Real <em>Tampa Bay homes</em>.</h2>
        <div class="section-head-text"><p>These are jobs we installed — no stock photos, no renderings. Vinyl plank, hardwood, tile, marble-look porcelain, shower tile, backsplash. This is what Napa&rsquo;s work looks like.</p></div>
      </div>
    </div>
    <div class="gallery-grid">
      <div class="gallery-item">
        <img src="/images/photo-lvp-living.jpg" alt="Wood-look LVP in a Florida living room with water view" loading="lazy">
        <div class="gallery-caption">Vinyl Plank · Gulf Coast Condo</div>
      </div>
      <div class="gallery-item">
        <img src="/images/photo-hardwood-espresso.jpg" alt="Dark espresso hardwood floor" loading="lazy">
        <div class="gallery-caption">Hardwood · Espresso Stain</div>
      </div>
      <div class="gallery-item">
        <img src="/images/photo-tile-shower.jpg" alt="Vertical tile shower with wood mosaic floor" loading="lazy">
        <div class="gallery-caption">Tile · Custom Shower · Vertical Stack</div>
      </div>
      <div class="gallery-item">
        <img src="/images/photo-lvp-sunroom.jpg" alt="Gray LVP in a sunroom" loading="lazy">
        <div class="gallery-caption">Vinyl Plank · Sunroom Install</div>
      </div>
      <div class="gallery-item">
        <img src="/images/photo-hardwood-dark.jpg" alt="Dark and honey hardwood floor contrast" loading="lazy">
        <div class="gallery-caption">Hardwood · Two-tone Transition</div>
      </div>
      <div class="gallery-item">
        <img src="/images/photo-tile-marble.jpg" alt="Marble-look porcelain tile bathroom" loading="lazy">
        <div class="gallery-caption">Tile · Calacatta Marble-look Porcelain</div>
      </div>
    </div>
  </div>
</section>'''

# WHY US
why_items = ""
for w in WHY_US_POINTS:
    why_items += f'''<div class="why-item">
  <div class="why-num">{w["num"]}</div>
  <div>
    <h3>{w["title"]}</h3>
    <p>{w["body"]}</p>
  </div>
</div>'''

why = f'''<section class="why-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label">Why Napa&rsquo;s · Six Reasons</span>
        <h2>What makes us <em>different</em> — in plain English.</h2>
        <div class="section-head-text"><p>Six things you should ask every flooring contractor. We put our answers in writing so you don&rsquo;t have to ask.</p></div>
      </div>
    </div>
    <div class="why-grid">{why_items}</div>
  </div>
</section>'''

# AREAS
area_cards = ""
for slug, c in CITIES.items():
    area_cards += f'''<a href="/{slug}/" class="area-card">
  <div class="area-card-name">{c["name"]}, FL</div>
  <div class="area-card-meta">{c["county"]} · {len(c["zips"])} ZIPs</div>
  <span class="area-card-arrow">See {c["name"]} →</span>
</a>'''

areas = f'''<section class="areas-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">04</div>
      <div class="section-head-meta">
        <span class="mono-label on-dark">Service Map · Eight Cities</span>
        <h2 style="color:var(--white)">Eight cities. <em style="color:var(--orange);font-style:normal">One crew.</em></h2>
        <div class="section-head-text"><p style="color:rgba(255,255,255,.65)">From Anna Maria Island to Hyde Park, from Snell Isle to Wellen Park — we work the Gulf Coast corridor. Pick your city for local pricing, neighborhoods, and a tailored FAQ.</p></div>
      </div>
    </div>
    <div class="areas-grid">{area_cards}</div>
  </div>
</section>'''

# PROCESS
process_html = ""
for p in PROCESS_STEPS:
    process_html += f'<div class="process-step" data-num="{p["num"]}"><div class="process-num">{p["num"]}</div><h3>{p["title"]}</h3><p>{p["body"]}</p></div>'

process = f'''<section class="process-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">05</div>
      <div class="section-head-meta">
        <span class="mono-label">How It Works · Four Steps</span>
        <h2>Estimate to <em>clean floor</em> — no surprises.</h2>
        <div class="section-head-text"><p>No pressure, no subcontractors. Here&rsquo;s everything that happens between the first call and the final walkthrough.</p></div>
      </div>
    </div>
    <div class="process-grid">{process_html}</div>
  </div>
</section>'''

# REVIEWS
reviews = reviews_section(limit=6)
reviews = reviews.replace('<div class="section-head-num">06</div>','<div class="section-head-num">06</div>')

# ADDITIONAL GALLERY ROW
gallery2 = f'''<section style="background:var(--gray-bg)">
  <div class="container-wide">
    <div class="gallery-grid">
      <div class="gallery-item">
        <img src="/images/photo-tile-backsplash.jpg" alt="Gray glass subway tile backsplash" loading="lazy">
        <div class="gallery-caption">Tile · Glass Subway Backsplash</div>
      </div>
      <div class="gallery-item">
        <img src="/images/photo-lvp-landing.jpg" alt="Natural oak LVP on stair landing" loading="lazy">
        <div class="gallery-caption">Vinyl Plank · Stair Landing</div>
      </div>
      <div class="gallery-item">
        <img src="/images/photo-tile-marble3.jpg" alt="Warm wood-look LVP living room" loading="lazy">
        <div class="gallery-caption">Vinyl Plank · Waterfront Condo</div>
      </div>
    </div>
  </div>
</section>'''

final = final_cta(
    headline="Free estimate on your Tampa Bay floor.",
    sub=f"In-home measure, transparent pricing, written quote within 24 hours. We respond to every inquiry, every day."
)

body = "\n".join([hero, ticker, proof, services, gallery, why, areas, process, reviews, gallery2, f'<div class="container">{contact_banner()}</div>', final])

head_html = head(TITLE, DESC, CANONICAL,
    og_image=f"{SITE}/images/og-default.jpg",
    og_type="website",
    json_ld=SCHEMAS,
    extra_meta='<link rel="preload" href="/images/photo-lvp-living.jpg" as="image">'
)

write_page(OUT, head_html, header(active="home"), body)
print(f"Wrote {OUT} ({len(open(OUT).read())//1024}KB)")
