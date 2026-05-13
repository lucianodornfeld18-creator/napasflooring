#!/usr/bin/env python3
"""Homepage: static hero, ticker before hero, reviews carousel 1-at-a-time, logo maior."""
import sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

OUT = "/home/claude/napas/index.html"
TITLE = "Flooring Contractor Bradenton FL · Tampa Bay · Napa's Flooring"
DESC = (f"Hardwood, vinyl plank, tile, laminate & stair tread installation across "
        f"Bradenton, Sarasota, Tampa & the Gulf Coast. "
        f"{BUSINESS['review_count']}× 5★ Google · Free estimate in 24 hrs.")[:158]
CANONICAL = f"{SITE}/"
SCHEMAS = [schema_website(), schema_organization(),
           schema_local_business(CANONICAL, "Napa's Flooring"),
           schema_breadcrumb([("Home", SITE + "/")])]

# ──────────────────────────────────────────────────────────────────
# 1) TICKER — goes BEFORE hero so it's visible above the fold
# ──────────────────────────────────────────────────────────────────
ticker = ticker_bar()   # already built in _gen.py

# ──────────────────────────────────────────────────────────────────
# 2) HERO — single static photo, no carousel, no review card
# ──────────────────────────────────────────────────────────────────
hero = f'''<section class="hero">
  <img class="hero-bg-img"
       src="/images/photo-lvp-living.jpg"
       alt="Vinyl plank flooring installed by Napa's Flooring in a Florida living room"
       loading="eager" fetchpriority="high">
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
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 3) SERVICES
# ──────────────────────────────────────────────────────────────────
svc_cards = "".join(f'''<a href="/{slug}/" class="service-card">
  <div class="service-card-num">{s["icon"]} — {s["short"]}</div>
  <h3>{s["h1_phrase"]}</h3>
  <p class="service-card-desc">{s["intro_lead"]}</p>
  <span class="service-card-cta">View work</span>
</a>''' for slug, s in [(sl, SERVICES[sl]) for sl in SERVICE_ORDER])

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

# ──────────────────────────────────────────────────────────────────
# 4) GALLERY — uniform 3×2
# ──────────────────────────────────────────────────────────────────
gallery = f'''<section style="background:var(--gray-bg);padding:60px 0">
  <div class="container-wide">
    <div style="text-align:center;margin-bottom:2rem">
      <span class="mono-label" style="justify-content:center">Our Work · Real Tampa Bay Projects</span>
      <h2 style="margin-top:.6rem;font-size:clamp(1.4rem,3vw,2rem)">Real floors. Real <em style="font-style:normal;color:var(--orange-dark)">results.</em></h2>
    </div>
    <div class="gallery-grid">
      <div class="gallery-item"><img src="/images/photo-lvp-living.jpg"        alt="Vinyl plank living room"   loading="lazy"><div class="gallery-caption">Vinyl Plank · Coastal Condo</div></div>
      <div class="gallery-item"><img src="/images/photo-hardwood-espresso.jpg" alt="Espresso hardwood"         loading="lazy"><div class="gallery-caption">Hardwood · Espresso Stain</div></div>
      <div class="gallery-item"><img src="/images/photo-tile-shower.jpg"       alt="Custom tile shower"        loading="lazy"><div class="gallery-caption">Tile · Custom Shower</div></div>
      <div class="gallery-item"><img src="/images/photo-lvp-sunroom.jpg"       alt="LVP sunroom"               loading="lazy"><div class="gallery-caption">Vinyl Plank · Sunroom</div></div>
      <div class="gallery-item"><img src="/images/photo-hardwood-dark.jpg"     alt="Dark hardwood two-tone"    loading="lazy"><div class="gallery-caption">Hardwood · Two-tone</div></div>
      <div class="gallery-item"><img src="/images/photo-tile-marble.jpg"       alt="Marble-look tile bathroom" loading="lazy"><div class="gallery-caption">Tile · Marble-look Bath</div></div>
    </div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 5) WHY US
# ──────────────────────────────────────────────────────────────────
why_items = "".join(f'''<div class="why-item">
  <div class="why-num">{w["num"]}</div>
  <div><h3>{w["title"]}</h3><p>{w["body"]}</p></div>
</div>''' for w in WHY_US_POINTS)

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

# ──────────────────────────────────────────────────────────────────
# 6) AREAS
# ──────────────────────────────────────────────────────────────────
area_cards = "".join(f'''<a href="/{slug}/" class="area-card">
  <div class="area-card-name">{c["name"]}, FL</div>
  <div class="area-card-meta">{c["county"]} · {len(c["zips"])} ZIPs</div>
  <span class="area-card-arrow">Details →</span>
</a>''' for slug, c in CITIES.items())

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

# ──────────────────────────────────────────────────────────────────
# 7) PROCESS
# ──────────────────────────────────────────────────────────────────
process_steps = "".join(
    f'<div class="process-step" data-num="{p["num"]}"><div class="process-num">{p["num"]}</div><h3>{p["title"]}</h3><p>{p["body"]}</p></div>'
    for p in PROCESS_STEPS)

process = f'''<section class="process-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">04</div>
      <div class="section-head-meta">
        <span class="mono-label">How It Works · Four Steps</span>
        <h2>Estimate to clean floor — <em>no surprises.</em></h2>
      </div>
    </div>
    <div class="process-grid">{process_steps}</div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 8) REVIEWS CAROUSEL — 1 card at a time, full width, no clipping
# ──────────────────────────────────────────────────────────────────
rv_slides = ""
rv_dots   = ""
for i, r in enumerate(REVIEWS):
    stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
    active = " rv-active" if i == 0 else ""
    rv_slides += f'''<div class="rv-slide{active}">
  <div class="rv-card">
    <div class="rv-top">
      <div class="rv-stars" aria-label="{r["rating"]} out of 5">{stars}</div>
      <span class="rv-counter">{i+1} / {len(REVIEWS)}</span>
    </div>
    <p class="rv-text">"{r["text"]}"</p>
    <div class="rv-footer">
      <div>
        <strong class="rv-name">{r["name"]}</strong>
        <span class="rv-where">{r["city"]}, FL · {r["service"]} · {r["date"]}</span>
      </div>
      <span class="rv-verified">✓ Verified Google Review</span>
    </div>
  </div>
</div>'''
    rv_dots += f'<button class="rv-dot{" rv-active" if i==0 else ""}" data-rv="{i}" aria-label="Review {i+1} of {len(REVIEWS)}"></button>'

reviews_section_html = f'''<section style="background:var(--dark);padding:80px 0">
  <div class="container">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:2rem;flex-wrap:wrap;gap:1rem">
      <div>
        <span class="mono-label on-dark">Google Reviews · Verified</span>
        <h2 style="color:var(--white);margin-top:.5rem">What homeowners <em style="color:var(--orange);font-style:normal">actually say.</em></h2>
      </div>
      <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="color:var(--orange);font-size:1.1rem;letter-spacing:2px">★★★★★</span>
          <span style="color:#fff;font-family:var(--font-head);font-size:1.3rem;font-weight:800">{BUSINESS["rating"]}</span>
          <span style="color:rgba(255,255,255,.5);font-size:.82rem">· {BUSINESS["review_count"]} reviews</span>
        </div>
        <div style="display:flex;gap:10px">
          <button id="rvPrev" class="rv-arrow" aria-label="Review anterior">&#8592;</button>
          <button id="rvNext" class="rv-arrow" aria-label="Próximo review">&#8594;</button>
        </div>
      </div>
    </div>

    <div class="rv-track-outer" id="rvOuter">
      <div class="rv-track" id="rvTrack">{rv_slides}</div>
    </div>

    <div class="rv-dots">{rv_dots}</div>

    <div style="margin-top:2rem;text-align:center">
      <a href="{BUSINESS["google_profile"]}" target="_blank" rel="noopener"
         class="btn btn-outline-light" style="display:inline-flex">
        Ver todos no Google →
      </a>
    </div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# EXTRA CSS
# ──────────────────────────────────────────────────────────────────
EXTRA_CSS = """
/* ── HERO: static single photo ── */
.hero{
  position:relative;
  height:calc(100vh - 92px - 46px); /* hero fills viewport: nav≈92 + ticker≈46 = below fold */
  min-height:480px;
  max-height:900px;
  display:flex;
  align-items:center;
  overflow:hidden;
  background:#111;
}
.hero-bg-img{
  position:absolute;inset:0;
  width:100%;height:100%;
  object-fit:cover;object-position:center;
}
.hero::after{
  content:"";position:absolute;inset:0;
  /* gradient only on left side where text is — right side shows photo clearly */
  background:linear-gradient(90deg,rgba(0,0,0,.80) 0%,rgba(0,0,0,.60) 38%,rgba(0,0,0,.20) 65%,rgba(0,0,0,.0) 100%);
  z-index:1;pointer-events:none;
}
.hero-inner{
  position:relative;z-index:2;
  max-width:var(--container);
  margin:0 auto;padding:0 28px;
  width:100%;
}
.hero-left{display:flex;flex-direction:column;max-width:680px}
.hero-label{
  display:flex;align-items:center;gap:10px;
  font-size:.76rem;font-weight:700;letter-spacing:.16em;
  text-transform:uppercase;color:#FFC84A;
  margin-bottom:16px;text-shadow:0 1px 6px rgba(0,0,0,1);
}
.hero-label::before{content:"";width:22px;height:2px;background:#FFC84A;flex-shrink:0}
.hero-h1{
  font-family:var(--font-head);font-weight:800;
  font-size:clamp(2.4rem,5vw,4rem);
  line-height:1.08;letter-spacing:-.03em;
  color:#FFFFFF;margin-bottom:1rem;
  text-shadow:0 2px 16px rgba(0,0,0,1);
}
.hero-h1 em{font-style:normal;color:#FFC84A}
.hero-sub{
  font-size:1.05rem;line-height:1.65;
  color:#FFFFFF;margin-bottom:1.6rem;
  text-shadow:0 1px 10px rgba(0,0,0,1);
  font-weight:500;
}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:1.8rem}
.hero-meta{
  display:flex;flex-wrap:wrap;gap:16px 32px;
  border-top:1px solid rgba(255,255,255,.35);
  padding-top:1.4rem;
}
.hero-meta div{display:flex;flex-direction:column;gap:3px}
.hero-meta strong{
  font-family:var(--font-head);font-size:1.5rem;
  color:#FFFFFF;font-weight:800;line-height:1;
  text-shadow:0 1px 10px rgba(0,0,0,1);
}
.hero-meta span{
  font-size:.7rem;letter-spacing:.1em;
  text-transform:uppercase;color:#FFFFFF;
  font-weight:600;text-shadow:0 1px 8px rgba(0,0,0,1);
}

/* ── SERVICES compact ── */
.home-services{padding:60px 0;background:var(--gray-bg)}
.home-services .services-grid{grid-template-columns:repeat(3,1fr);gap:14px}
.home-services .service-card{min-height:210px;padding:22px 18px}
.home-services .service-card h3{font-size:1.15rem}

/* ── GALLERY: uniform 3×2 ── */
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.gallery-item{overflow:hidden;border-radius:var(--radius);aspect-ratio:4/3;position:relative}
.gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .4s ease}
.gallery-item:hover img{transform:scale(1.06)}
.gallery-caption{
  position:absolute;bottom:0;left:0;right:0;
  background:linear-gradient(0deg,rgba(0,0,0,.65),transparent);
  color:#fff;padding:28px 14px 10px;
  font-size:.78rem;font-weight:600;letter-spacing:.04em;
  opacity:0;transition:opacity .3s;
}
.gallery-item:hover .gallery-caption{opacity:1}

/* ── REVIEWS CAROUSEL: 1 card, full width ── */
.rv-track-outer{overflow:hidden;border-radius:14px}
.rv-track{
  display:flex;
  transition:transform .5s cubic-bezier(.4,0,.2,1);
  align-items:stretch;
}
.rv-slide{
  min-width:100%;padding:0;
  box-sizing:border-box;flex-shrink:0;
}
.rv-card{
  background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.14);
  border-radius:14px;
  padding:36px 40px;
  display:flex;flex-direction:column;gap:20px;
}
.rv-top{display:flex;align-items:center;justify-content:space-between;gap:1rem}
.rv-stars{color:#FFC84A;font-size:1.2rem;letter-spacing:3px}
.rv-counter{
  font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;
  color:rgba(255,255,255,.4);font-family:var(--font-head);
}
.rv-text{
  color:#FFFFFF;font-size:1.1rem;line-height:1.7;
  font-style:italic;margin:0;max-width:900px;
}
.rv-footer{
  display:flex;align-items:flex-end;justify-content:space-between;
  flex-wrap:wrap;gap:12px;
  border-top:1px solid rgba(255,255,255,.14);
  padding-top:20px;
}
.rv-name{color:#fff;font-size:1rem;font-weight:700;font-style:normal;display:block;margin-bottom:4px}
.rv-where{font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.55)}
.rv-verified{
  font-size:.74rem;font-weight:700;letter-spacing:.1em;
  text-transform:uppercase;color:#FFC84A;white-space:nowrap;
}
.rv-arrow{
  background:rgba(255,255,255,.12);
  border:1px solid rgba(255,255,255,.22);
  color:#fff;width:42px;height:42px;border-radius:50%;
  font-size:1.1rem;cursor:pointer;transition:all .22s;
}
.rv-arrow:hover{background:var(--orange);border-color:var(--orange);color:var(--dark)}
.rv-dots{display:flex;gap:8px;justify-content:center;margin-top:18px}
.rv-dot{
  width:8px;height:8px;border-radius:50%;border:none;
  background:rgba(255,255,255,.2);cursor:pointer;padding:0;transition:all .22s;
}
.rv-dot.rv-active{background:var(--orange);transform:scale(1.35)}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .hero{height:calc(100vh - 80px - 44px);min-height:440px}
  .hero-h1{font-size:clamp(2rem,6vw,3rem)}
  .gallery-grid{grid-template-columns:1fr 1fr}
  .rv-card{padding:24px 20px}
  .rv-text{font-size:.97rem}
}
@media(max-width:520px){
  .hero{height:calc(100vh - 72px - 44px);min-height:400px}
  .hero-inner{padding:0 16px}
  .rv-card{padding:20px 16px}
  .gallery-grid{grid-template-columns:1fr 1fr}
}
"""

# ──────────────────────────────────────────────────────────────────
# JS — only reviews carousel now (no hero carousel needed)
# ──────────────────────────────────────────────────────────────────
SCRIPTS = f"""<script>
(function(){{
  var track = document.getElementById('rvTrack');
  if (!track) return;
  var slides = track.querySelectorAll('.rv-slide');
  var dots   = document.querySelectorAll('.rv-dot');
  var total  = slides.length;
  var cur    = 0, timer;

  function go(n){{
    cur = ((n % total) + total) % total;
    track.style.transform = 'translateX(-' + (cur * 100) + '%)';
    dots.forEach(function(d,i){{ d.classList.toggle('rv-active', i===cur); }});
  }}
  function next(){{ go(cur + 1); }}

  timer = setInterval(next, 5000);

  document.getElementById('rvPrev').addEventListener('click', function(){{
    go(cur - 1); clearInterval(timer); timer = setInterval(next, 5000);
  }});
  document.getElementById('rvNext').addEventListener('click', function(){{
    go(cur + 1); clearInterval(timer); timer = setInterval(next, 5000);
  }});
  dots.forEach(function(d){{
    d.addEventListener('click', function(){{
      go(+this.dataset.rv); clearInterval(timer); timer = setInterval(next, 5000);
    }});
  }});

  track.parentElement.addEventListener('mouseenter', function(){{ clearInterval(timer); }});
  track.parentElement.addEventListener('mouseleave', function(){{ timer = setInterval(next, 5000); }});
}})();
</script>"""

# ──────────────────────────────────────────────────────────────────
# ASSEMBLE — ticker BEFORE hero
# ──────────────────────────────────────────────────────────────────
final_cta_html = final_cta(
    "Free estimate on your Tampa Bay floor.",
    "In-home measure, transparent pricing, written quote within 24 hours.")

body = "\n".join([
    hero,            # hero fills (100vh - nav - ticker height)
    ticker,          # ← ticker sits at bottom of viewport, fully visible
    services,
    gallery,
    why,
    areas,
    process,
    reviews_section_html,
    f'<div class="container">{contact_banner()}</div>',
    final_cta_html,
    SCRIPTS,
])

extra = (f'<style>{EXTRA_CSS}</style>'
         '<link rel="preload" href="/images/photo-lvp-living.jpg" as="image">')

head_html = head(TITLE, DESC, CANONICAL, json_ld=SCHEMAS, extra_meta=extra)
write_page(OUT, head_html, header(active="home"), body)
print(f"✓ {OUT} — {open(OUT).read().count(chr(10))} lines")
