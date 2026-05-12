#!/usr/bin/env python3
"""Homepage — fullscreen carousel, no top-bar, above-fold design."""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

OUT = "/home/claude/napas/index.html"
TITLE = "Flooring Contractor Bradenton FL · Tampa Bay · Napa's Flooring"
DESC = (
    f"Hardwood, vinyl plank, tile, laminate & stair tread installation across "
    f"Bradenton, Sarasota, Tampa & the Gulf Coast. "
    f"{BUSINESS['review_count']}× 5★ Google · Free estimate in 24 hrs."
)[:158]
CANONICAL = f"{SITE}/"

SCHEMAS = [
    schema_website(), schema_organization(),
    schema_local_business(CANONICAL, "Napa's Flooring — Tampa Bay flooring contractor"),
    schema_breadcrumb([("Home", SITE + "/")]),
]

# ── Photos for carousel (all 9 real photos)
CAROUSEL_PHOTOS = [
    ("/images/photo-lvp-living.jpg",      "Vinyl Plank — Coastal Living Room"),
    ("/images/photo-hardwood-dark.jpg",   "Hardwood — Two-Tone Contrast"),
    ("/images/photo-tile-marble.jpg",     "Tile — Calacatta Marble Bathroom"),
    ("/images/photo-lvp-sunroom.jpg",     "Vinyl Plank — Sunroom Install"),
    ("/images/photo-hardwood-espresso.jpg","Hardwood — Espresso Stain"),
    ("/images/photo-tile-shower.jpg",     "Tile — Custom Shower"),
    ("/images/photo-lvp-landing.jpg",     "Vinyl Plank — Stair Landing"),
    ("/images/photo-tile-backsplash.jpg", "Tile — Glass Subway Backsplash"),
]

slides_html = ""
dots_html = ""
for i, (src, caption) in enumerate(CAROUSEL_PHOTOS):
    active = " active" if i == 0 else ""
    slides_html += f'''<div class="cs-slide{active}">
  <img src="{src}" alt="{caption} by Napa's Flooring" {"loading='eager' fetchpriority='high'" if i==0 else "loading='lazy'"}>
  <span class="cs-caption">{caption}</span>
</div>'''
    dots_html += f'<button class="cs-dot{" active" if i==0 else ""}" data-idx="{i}" aria-label="Slide {i+1}"></button>'

CAROUSEL_CSS = """
/* CAROUSEL */
.cs-wrap{position:absolute;inset:0;overflow:hidden;background:#111}
.cs-slide{position:absolute;inset:0;opacity:0;transition:opacity 1.1s ease;display:flex;align-items:stretch}
.cs-slide.active{opacity:1;z-index:1}
.cs-slide img{width:100%;height:100%;object-fit:cover;object-position:center}
.cs-caption{position:absolute;bottom:22px;right:28px;background:rgba(245,166,35,.92);color:#1a1a1a;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:6px 14px;border-radius:6px}
.cs-dots{position:absolute;bottom:22px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:10}
.cs-dot{width:8px;height:8px;border-radius:50%;border:none;background:rgba(255,255,255,.4);cursor:pointer;padding:0;transition:all .25s}
.cs-dot.active{background:var(--orange);transform:scale(1.25)}
.cs-arrows{position:absolute;top:50%;transform:translateY(-50%);width:100%;display:flex;justify-content:space-between;padding:0 20px;z-index:10;pointer-events:none}
.cs-arrow{pointer-events:all;background:rgba(255,255,255,.15);border:none;color:#fff;width:42px;height:42px;border-radius:50%;font-size:1.3rem;cursor:pointer;transition:background .2s;backdrop-filter:blur(4px)}
.cs-arrow:hover{background:rgba(245,166,35,.9);color:#1a1a1a}

/* FULLSCREEN HERO */
.hero{position:relative;height:calc(100vh - 72px);min-height:520px;max-height:960px;display:flex;align-items:center;overflow:hidden}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(100deg,rgba(10,10,10,.80) 0%,rgba(10,10,10,.55) 50%,rgba(10,10,10,.15) 100%);z-index:2;pointer-events:none}
.hero-inner{position:relative;z-index:3;max-width:var(--container-wide);margin:0 auto;padding:0 32px;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.hero-left{display:flex;flex-direction:column;gap:0}
.hero-label{display:flex;align-items:center;gap:10px;font-size:.78rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);margin-bottom:18px}
.hero-label::before{content:"";width:24px;height:2px;background:var(--orange);flex-shrink:0}
.hero-h1{font-family:var(--font-head);font-weight:800;font-size:clamp(2.2rem,4.5vw,3.6rem);line-height:1.08;letter-spacing:-.03em;color:#fff;margin-bottom:1.1rem}
.hero-h1 em{font-style:normal;color:var(--orange)}
.hero-sub{font-size:1rem;line-height:1.6;color:rgba(255,255,255,.82);margin-bottom:1.6rem;max-width:500px}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:1.8rem}
.hero-meta{display:flex;flex-wrap:wrap;gap:18px 28px;border-top:1px solid rgba(255,255,255,.18);padding-top:1.4rem}
.hero-meta div{display:flex;flex-direction:column;gap:2px}
.hero-meta strong{font-family:var(--font-head);font-size:1.5rem;color:#fff;font-weight:800;line-height:1}
.hero-meta span{font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.55)}

/* RIGHT SIDE — trust card over the photo */
.hero-trust-card{background:rgba(255,255,255,.1);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:28px 24px;display:flex;flex-direction:column;gap:16px;max-width:380px;margin-left:auto}
.htc-stars{color:var(--orange);font-size:1.1rem;letter-spacing:2px}
.htc-text{color:#fff;font-size:1rem;line-height:1.5;font-style:italic}
.htc-author{font-size:.78rem;color:rgba(255,255,255,.7);letter-spacing:.06em;text-transform:uppercase}
.htc-badges{display:flex;flex-direction:column;gap:10px;border-top:1px solid rgba(255,255,255,.15);padding-top:16px}
.htc-badge{display:flex;align-items:center;gap:10px;font-size:.85rem;color:rgba(255,255,255,.9);font-weight:500}
.htc-badge-icon{width:28px;height:28px;background:var(--orange);border-radius:6px;display:grid;place-items:center;font-size:.9rem;flex-shrink:0}

/* HIDE ORIGINAL HERO ART on this page */
.hero-art{display:none!important}

/* BELOW-HERO: compact sections */
.home-services{padding:60px 0;background:var(--gray-bg)}
.home-services .services-grid{grid-template-columns:repeat(3,1fr);gap:14px}
.home-services .service-card{min-height:220px;padding:24px 20px}
.home-services .service-card h3{font-size:1.2rem}

/* RESPONSIVE */
@media(max-width:900px){
  .hero{height:calc(100vh - 68px);max-height:800px}
  .hero-inner{grid-template-columns:1fr;gap:24px}
  .hero-trust-card{display:none}
  .hero-h1{font-size:clamp(1.9rem,6vw,3rem)}
}
@media(max-width:600px){
  .hero{height:calc(100vh - 62px);min-height:480px}
  .hero-inner{padding:0 18px}
  .hero-label{font-size:.7rem}
}
"""

CAROUSEL_JS = f"""<script>
(function(){{
  var slides = document.querySelectorAll('.cs-slide');
  var dots = document.querySelectorAll('.cs-dot');
  var cur = 0, total = slides.length, timer;

  function go(n){{
    slides[cur].classList.remove('active');
    dots[cur].classList.remove('active');
    cur = (n + total) % total;
    slides[cur].classList.add('active');
    dots[cur].classList.add('active');
  }}
  function autoPlay(){{ timer = setInterval(function(){{ go(cur+1); }}, 4500); }}
  function reset(){{ clearInterval(timer); autoPlay(); }}

  // dots
  dots.forEach(function(d){{
    d.addEventListener('click', function(){{ go(+this.dataset.idx); reset(); }});
  }});
  // arrows
  document.getElementById('csPrev').addEventListener('click', function(){{ go(cur-1); reset(); }});
  document.getElementById('csNext').addEventListener('click', function(){{ go(cur+1); reset(); }});

  autoPlay();
}})();
</script>"""

# ── HERO SECTION
review0 = REVIEWS[0]
hero = f'''<section class="hero">
  <!-- Carousel Background -->
  <div class="cs-wrap">
    {slides_html}
    <div class="cs-arrows">
      <button id="csPrev" class="cs-arrow">&#8592;</button>
      <button id="csNext" class="cs-arrow">&#8594;</button>
    </div>
    <div class="cs-dots">{dots_html}</div>
  </div>

  <!-- Overlay Content -->
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-label">Bradenton · Sarasota · Tampa · Since {BUSINESS["year_founded"]}</div>
      <h1 class="hero-h1">Flooring built <em>right</em>,<br>finished <em>proud.</em></h1>
      <p class="hero-sub">A small, craft-first crew based in east Bradenton. Hardwood, vinyl plank, tile, laminate &amp; stair treads — installed by the same people who measured your home.</p>
      <div class="hero-cta">
        <a href="/contact/#quote" class="btn btn-orange">Free Estimate <span class="btn-arrow"></span></a>
        <a href="{TEL_LINK}" class="btn btn-outline-light">{BUSINESS["phone_display"]}</a>
      </div>
      <div class="hero-meta">
        <div><strong>{BUSINESS["unique_stat_number"]}</strong><span>Tampa Bay Floors</span></div>
        <div><strong>{BUSINESS["rating"]}★</strong><span>{BUSINESS["review_count"]} Reviews</span></div>
        <div><strong>{2026 - BUSINESS["year_founded"]} yrs</strong><span>In Business</span></div>
        <div><strong>24h</strong><span>Written Estimate</span></div>
        <div><strong>12mo</strong><span>Warranty</span></div>
      </div>
    </div>

    <!-- Trust card on right -->
    <div class="hero-trust-card">
      <div class="htc-stars">★★★★★</div>
      <p class="htc-text">&ldquo;{review0["text"][:160]}…&rdquo;</p>
      <p class="htc-author">— {review0["name"]} · {review0["city"]}, FL · {review0["date"]}</p>
      <div class="htc-badges">
        <div class="htc-badge"><div class="htc-badge-icon">✓</div>Licensed &amp; Insured</div>
        <div class="htc-badge"><div class="htc-badge-icon">✓</div>47-Point Install Standard</div>
        <div class="htc-badge"><div class="htc-badge-icon">✓</div>12-Month Workmanship Warranty</div>
        <div class="htc-badge"><div class="htc-badge-icon">✓</div>Free Written Estimate in 24h</div>
      </div>
    </div>
  </div>
</section>'''

# ── TICKER
ticker = ticker_bar()

# ── SERVICES (compact, 2-row of 3)
svc_cards = ""
for slug in SERVICE_ORDER:
    s = SERVICES[slug]
    svc_cards += f'''<a href="/{slug}/" class="service-card">
  <div class="service-card-num">{s["icon"]} — {s["short"]}</div>
  <h3>{s["h1_phrase"]}</h3>
  <p class="service-card-desc">{s["intro_lead"]}</p>
  <span class="service-card-cta">View work</span>
</a>'''

services = f'''<section class="home-services">
  <div class="container-wide">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:2rem;flex-wrap:wrap;gap:1rem">
      <div>
        <span class="mono-label">Six Services · Tampa Bay</span>
        <h2 style="margin-top:.5rem;font-size:clamp(1.4rem,3vw,2rem)">Every floor we install — <em style="font-style:normal;color:var(--orange-dark)">done right.</em></h2>
      </div>
      <a href="/contact/#quote" class="btn btn-orange" style="flex-shrink:0">Get Free Estimate <span class="btn-arrow"></span></a>
    </div>
    <div class="services-grid">{svc_cards}</div>
  </div>
</section>'''

# ── WHY US (compact)
why_items = ""
for w in WHY_US_POINTS:
    why_items += f'''<div class="why-item">
  <div class="why-num">{w["num"]}</div>
  <div><h3>{w["title"]}</h3><p>{w["body"]}</p></div>
</div>'''

why = f'''<section class="why-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label">Why Napa&rsquo;s · Six Reasons</span>
        <h2>What makes us different — <em>in plain English.</em></h2>
      </div>
    </div>
    <div class="why-grid">{why_items}</div>
  </div>
</section>'''

# ── AREAS
area_cards = ""
for slug, c in CITIES.items():
    area_cards += f'''<a href="/{slug}/" class="area-card">
  <div class="area-card-name">{c["name"]}, FL</div>
  <div class="area-card-meta">{c["county"]} · {len(c["zips"])} ZIPs</div>
  <span class="area-card-arrow">Details →</span>
</a>'''

areas = f'''<section class="areas-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label on-dark">Eight Cities · Tampa Bay</span>
        <h2 style="color:var(--white)">Eight cities. <em style="color:var(--orange);font-style:normal">One crew.</em></h2>
      </div>
    </div>
    <div class="areas-grid">{area_cards}</div>
  </div>
</section>'''

# ── PROCESS
process_html = ""
for p in PROCESS_STEPS:
    process_html += f'<div class="process-step" data-num="{p["num"]}"><div class="process-num">{p["num"]}</div><h3>{p["title"]}</h3><p>{p["body"]}</p></div>'

process = f'''<section class="process-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">04</div>
      <div class="section-head-meta">
        <span class="mono-label">How It Works · Four Steps</span>
        <h2>Estimate to clean floor — <em>no surprises.</em></h2>
      </div>
    </div>
    <div class="process-grid">{process_html}</div>
  </div>
</section>'''

# ── REVIEWS
reviews = reviews_section(limit=6)

# ── GALLERY (real photos)
gallery = f'''<section style="background:var(--gray-bg);padding:60px 0">
  <div class="container-wide">
    <div style="text-align:center;margin-bottom:2rem">
      <span class="mono-label" style="justify-content:center">Our Work · Tampa Bay Homes</span>
      <h2 style="margin-top:.6rem;font-size:clamp(1.4rem,3vw,2rem)">Real floors. Real <em style="font-style:normal;color:var(--orange-dark)">results.</em></h2>
    </div>
    <div class="gallery-grid">
      <div class="gallery-item"><img src="/images/photo-lvp-living.jpg" alt="Vinyl plank living room" loading="lazy"><div class="gallery-caption">Vinyl Plank · Coastal Condo</div></div>
      <div class="gallery-item"><img src="/images/photo-hardwood-espresso.jpg" alt="Espresso hardwood" loading="lazy"><div class="gallery-caption">Hardwood · Espresso Stain</div></div>
      <div class="gallery-item"><img src="/images/photo-tile-shower.jpg" alt="Custom tile shower" loading="lazy"><div class="gallery-caption">Tile · Custom Shower</div></div>
      <div class="gallery-item"><img src="/images/photo-lvp-sunroom.jpg" alt="LVP sunroom" loading="lazy"><div class="gallery-caption">Vinyl Plank · Sunroom</div></div>
      <div class="gallery-item"><img src="/images/photo-hardwood-dark.jpg" alt="Dark hardwood contrast" loading="lazy"><div class="gallery-caption">Hardwood · Two-tone</div></div>
      <div class="gallery-item"><img src="/images/photo-tile-marble.jpg" alt="Marble tile bathroom" loading="lazy"><div class="gallery-caption">Tile · Marble-look Bath</div></div>
    </div>
  </div>
</section>'''

final = final_cta(
    headline="Free estimate on your Tampa Bay floor.",
    sub="In-home measure, transparent pricing, written quote within 24 hours."
)

body = "\n".join([
    hero, ticker, services, gallery, why, areas, process, reviews,
    f'<div class="container">{contact_banner()}</div>', final,
    CAROUSEL_JS
])

# Inject carousel CSS into head via extra_meta
extra = f'<style>{CAROUSEL_CSS}</style><link rel="preload" href="/images/photo-lvp-living.jpg" as="image">'

head_html = head(TITLE, DESC, CANONICAL,
    og_image=f"{SITE}/images/og-default.jpg",
    og_type="website",
    json_ld=SCHEMAS,
    extra_meta=extra
)

write_page(OUT, head_html, header(active="home"), body)
lines = open(OUT).read().count('\n')
print(f"✓ Homepage: {lines} lines")
