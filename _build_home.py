#!/usr/bin/env python3
"""Homepage — fullscreen carousel, project carousel in reviews slot, uniform gallery."""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

OUT = "/home/claude/napas/index.html"
TITLE = "Flooring Contractor Bradenton FL · Tampa Bay · Napa's Flooring"
DESC = (f"Hardwood, vinyl plank, tile, laminate & stair tread installation across "
        f"Bradenton, Sarasota, Tampa & the Gulf Coast. "
        f"{BUSINESS['review_count']}× 5★ Google · Free estimate in 24 hrs.")[:158]
CANONICAL = f"{SITE}/"
SCHEMAS = [schema_website(), schema_organization(),
           schema_local_business(CANONICAL, "Napa's Flooring — Tampa Bay flooring contractor"),
           schema_breadcrumb([("Home", SITE + "/")])]

# ── All photos
PHOTOS = [
    ("/images/photo-lvp-living.jpg",       "Vinyl Plank", "Coastal Living Room — Gulf View"),
    ("/images/photo-hardwood-dark.jpg",    "Hardwood",    "Two-Tone Contrast — Tampa Home"),
    ("/images/photo-tile-marble.jpg",      "Tile",        "Calacatta Marble — Master Bathroom"),
    ("/images/photo-lvp-sunroom.jpg",      "Vinyl Plank", "Gray LVP — Sunroom Install"),
    ("/images/photo-hardwood-espresso.jpg","Hardwood",    "Espresso Stain — Bedroom Suite"),
    ("/images/photo-tile-shower.jpg",      "Tile",        "Vertical Stack — Custom Shower"),
    ("/images/photo-lvp-landing.jpg",      "Vinyl Plank", "Natural Oak — Stair Landing"),
    ("/images/photo-tile-backsplash.jpg",  "Tile",        "Glass Subway — Kitchen Backsplash"),
]

# ── Hero carousel slides (background)
hero_slides = ""
hero_dots = ""
for i, (src, tag, cap) in enumerate(PHOTOS):
    active = " active" if i == 0 else ""
    eager = "loading='eager' fetchpriority='high'" if i == 0 else "loading='lazy'"
    hero_slides += f'<div class="cs-slide{active}"><img src="{src}" alt="{cap} by Napas Flooring" {eager}><span class="cs-caption">{cap}</span></div>'
    hero_dots += f'<button class="cs-dot{"  active" if i==0 else ""}" data-idx="{i}" aria-label="Slide {i+1}"></button>'

# ── Project carousel slides (portfolio section)
proj_slides = ""
proj_dots = ""
for i, (src, tag, cap) in enumerate(PHOTOS):
    active = " pj-active" if i == 0 else ""
    proj_slides += f'''<div class="pj-slide{active}">
  <img src="{src}" alt="{cap} by Napas Flooring" loading="lazy">
  <div class="pj-info"><span class="pj-tag">{tag}</span><p class="pj-cap">{cap}</p></div>
</div>'''
    proj_dots += f'<button class="pj-dot{" pj-active" if i==0 else ""}" data-pj="{i}" aria-label="Projeto {i+1}"></button>'

# ── HERO
review0 = REVIEWS[0]
hero = f'''<section class="hero">
  <div class="cs-wrap">
    {hero_slides}
    <div class="cs-arrows">
      <button id="csPrev" class="cs-arrow">&#8592;</button>
      <button id="csNext" class="cs-arrow">&#8594;</button>
    </div>
    <div class="cs-dots">{hero_dots}</div>
  </div>
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

# ── SERVICES
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

# ── GALLERY (all same size, 3×2 uniform grid)
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

# ── WHY US
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

# ── AREAS
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

# ── PROCESS
process_steps = "".join(f'<div class="process-step" data-num="{p["num"]}"><div class="process-num">{p["num"]}</div><h3>{p["title"]}</h3><p>{p["body"]}</p></div>' for p in PROCESS_STEPS)

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

# ── REVIEWS CAROUSEL
rev_slides = ""
rev_dots = ""
for i, r in enumerate(REVIEWS):
    stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
    active = " rv-active" if i == 0 else ""
    rev_slides += f'''<div class="rv-slide{active}">
  <div class="rv-card">
    <div class="rv-stars">{stars}</div>
    <p class="rv-text">"{r["text"]}"</p>
    <div class="rv-meta">
      <strong class="rv-name">{r["name"]}</strong>
      <span class="rv-where">{r["city"]}, FL · {r["service"]} · {r["date"]}</span>
      <span class="rv-verified">✓ Verified Google Review</span>
    </div>
  </div>
</div>'''
    rev_dots += f'<button class="rv-dot{" rv-active" if i==0 else ""}" data-rv="{i}" aria-label="Review {i+1}"></button>'

portfolio = f'''<section style="background:var(--dark);padding:80px 0">
  <div class="container-wide">
    <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:2rem;flex-wrap:wrap;gap:1rem">
      <div>
        <span class="mono-label on-dark">Google Reviews · Verified</span>
        <h2 style="color:var(--white);margin-top:.5rem">What homeowners <em style="color:var(--orange);font-style:normal">actually say.</em></h2>
      </div>
      <div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="color:var(--orange);font-size:1.1rem;letter-spacing:2px">★★★★★</span>
          <span style="color:#fff;font-family:var(--font-head);font-size:1.3rem;font-weight:800">{BUSINESS["rating"]}</span>
          <span style="color:rgba(255,255,255,.5);font-size:.82rem">· {BUSINESS["review_count"]} reviews</span>
        </div>
        <div style="display:flex;gap:10px">
          <button id="rvPrev" class="pj-arrow">&#8592;</button>
          <button id="rvNext" class="pj-arrow">&#8594;</button>
        </div>
      </div>
    </div>
    <div class="rv-track-wrap">
      <div class="rv-track" id="rvTrack">{rev_slides}</div>
    </div>
    <div class="rv-dots">{rev_dots}</div>
    <div style="margin-top:2rem;text-align:center">
      <a href="{BUSINESS["google_profile"]}" target="_blank" rel="noopener" class="btn btn-outline-light" style="display:inline-flex">Ver todos no Google →</a>
    </div>
  </div>
</section>'''

final = final_cta("Free estimate on your Tampa Bay floor.",
                   "In-home measure, transparent pricing, written quote within 24 hours.")

# ── CSS EXTRAS (hero carousel + project carousel)
EXTRA_CSS = """
/* HERO CAROUSEL */
.cs-wrap{position:absolute;inset:0;overflow:hidden;background:#111}
.cs-slide{position:absolute;inset:0;opacity:0;transition:opacity 1.1s ease;display:flex;align-items:stretch}
.cs-slide.active{opacity:1;z-index:1}
.cs-slide img{width:100%;height:100%;object-fit:cover}
.cs-caption{position:absolute;bottom:22px;right:28px;background:rgba(245,166,35,.92);color:#1a1a1a;font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:5px 12px;border-radius:5px}
.cs-dots{position:absolute;bottom:22px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:10}
.cs-dot{width:8px;height:8px;border-radius:50%;border:none;background:rgba(255,255,255,.35);cursor:pointer;padding:0;transition:all .22s}
.cs-dot.active{background:var(--orange);transform:scale(1.3)}
.cs-arrows{position:absolute;top:50%;transform:translateY(-50%);width:100%;display:flex;justify-content:space-between;padding:0 18px;z-index:10;pointer-events:none}
.cs-arrow{pointer-events:all;background:rgba(255,255,255,.13);border:none;color:#fff;width:42px;height:42px;border-radius:50%;font-size:1.2rem;cursor:pointer;transition:all .2s;backdrop-filter:blur(4px)}
.cs-arrow:hover{background:rgba(245,166,35,.9);color:#1a1a1a}
/* HERO LAYOUT */
.hero{position:relative;height:calc(100vh - 72px);min-height:520px;max-height:960px;display:flex;align-items:center;overflow:hidden}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(105deg,rgba(0,0,0,.82) 0%,rgba(0,0,0,.60) 50%,rgba(0,0,0,.20) 100%);z-index:2;pointer-events:none}
.hero-inner{position:relative;z-index:3;max-width:var(--container-wide);margin:0 auto;padding:0 32px;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.hero-left{display:flex;flex-direction:column}
.hero-label{display:flex;align-items:center;gap:10px;font-size:.76rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#FFC84A;margin-bottom:16px;text-shadow:0 1px 6px rgba(0,0,0,.9)}
.hero-label::before{content:"";width:22px;height:2px;background:#FFC84A;flex-shrink:0}
.hero-h1{font-family:var(--font-head);font-weight:800;font-size:clamp(2.2rem,4.5vw,3.6rem);line-height:1.08;letter-spacing:-.03em;color:#FFFFFF;margin-bottom:1rem;text-shadow:0 2px 14px rgba(0,0,0,.9)}
.hero-h1 em{font-style:normal;color:#FFC84A}
.hero-sub{font-size:1rem;line-height:1.6;color:#FFFFFF;margin-bottom:1.5rem;max-width:500px;text-shadow:0 1px 8px rgba(0,0,0,.9)}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:1.6rem}
.hero-meta{display:flex;flex-wrap:wrap;gap:16px 26px;border-top:1px solid rgba(255,255,255,.35);padding-top:1.3rem}
.hero-meta div{display:flex;flex-direction:column;gap:2px}
.hero-meta strong{font-family:var(--font-head);font-size:1.4rem;color:#FFFFFF;font-weight:800;line-height:1;text-shadow:0 1px 8px rgba(0,0,0,.9)}
.hero-meta span{font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.9);text-shadow:0 1px 6px rgba(0,0,0,.9)}
/* TRUST CARD */
.hero-trust-card{background:rgba(255,255,255,.1);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:26px 22px;display:flex;flex-direction:column;gap:14px;max-width:380px;margin-left:auto}
.htc-stars{color:var(--orange);font-size:1.1rem;letter-spacing:2px}
.htc-text{color:#fff;font-size:.95rem;line-height:1.5;font-style:italic;margin:0}
.htc-author{font-size:.76rem;color:rgba(255,255,255,.65);letter-spacing:.06em;text-transform:uppercase}
.htc-badges{display:flex;flex-direction:column;gap:10px;border-top:1px solid rgba(255,255,255,.14);padding-top:14px}
.htc-badge{display:flex;align-items:center;gap:10px;font-size:.84rem;color:rgba(255,255,255,.88);font-weight:500}
.htc-badge-icon{width:26px;height:26px;background:var(--orange);border-radius:5px;display:grid;place-items:center;font-size:.82rem;flex-shrink:0;color:var(--dark)}
/* PROJECT CAROUSEL */
.pj-track-wrap{overflow:hidden;border-radius:12px}
.pj-track{display:flex;transition:transform .5s cubic-bezier(.4,0,.2,1)}
.pj-slide{min-width:33.333%;padding:0 7px;box-sizing:border-box;position:relative;flex-shrink:0}
.pj-slide img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:10px;display:block}
.pj-info{position:absolute;bottom:0;left:7px;right:7px;background:linear-gradient(0deg,rgba(0,0,0,.75),transparent);padding:36px 14px 12px;border-radius:0 0 10px 10px}
.pj-tag{display:inline-block;background:var(--orange);color:var(--dark);font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 9px;border-radius:4px;margin-bottom:5px}
.pj-cap{color:#fff;font-size:.86rem;font-weight:600;margin:0;line-height:1.3}
.pj-arrow{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);color:#fff;width:42px;height:42px;border-radius:50%;font-size:1.1rem;cursor:pointer;transition:all .22s}
.pj-arrow:hover{background:var(--orange);border-color:var(--orange);color:var(--dark)}
.pj-dots{display:flex;gap:8px;justify-content:center;margin-top:16px}
.pj-dot{width:8px;height:8px;border-radius:50%;border:none;background:rgba(255,255,255,.25);cursor:pointer;padding:0;transition:all .22s}
.pj-dot.pj-active{background:var(--orange);transform:scale(1.3)}
/* REVIEWS CAROUSEL */
.rv-track-wrap{overflow:hidden}
.rv-track{display:flex;transition:transform .5s cubic-bezier(.4,0,.2,1)}
.rv-slide{min-width:33.333%;padding:0 8px;box-sizing:border-box;flex-shrink:0}
.rv-card{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:26px 22px;height:100%;display:flex;flex-direction:column;gap:14px}
.rv-stars{color:var(--orange);font-size:1rem;letter-spacing:2px}
.rv-text{color:rgba(255,255,255,.92);font-size:.95rem;line-height:1.62;font-style:italic;flex-grow:1;margin:0}
.rv-meta{display:flex;flex-direction:column;gap:4px;border-top:1px solid rgba(255,255,255,.12);padding-top:14px;margin-top:auto}
.rv-name{color:#fff;font-size:.9rem;font-weight:700;font-style:normal}
.rv-where{font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.5)}
.rv-verified{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--orange)}
.rv-dots{display:flex;gap:8px;justify-content:center;margin-top:18px}
.rv-dot{width:8px;height:8px;border-radius:50%;border:none;background:rgba(255,255,255,.2);cursor:pointer;padding:0;transition:all .22s}
.rv-dot.rv-active{background:var(--orange);transform:scale(1.3)}
@media(max-width:900px){.rv-slide{min-width:50%}}
@media(max-width:600px){.rv-slide{min-width:100%}}
.home-services{padding:60px 0;background:var(--gray-bg)}
.home-services .services-grid{grid-template-columns:repeat(3,1fr);gap:14px}
.home-services .service-card{min-height:220px;padding:24px 20px}
.home-services .service-card h3{font-size:1.2rem}
/* RESPONSIVE */
@media(max-width:900px){
  .hero{height:calc(100vh - 68px)}
  .hero-inner{grid-template-columns:1fr}
  .hero-trust-card{display:none}
  .hero-h1{font-size:clamp(1.9rem,6vw,3rem)}
  .pj-slide{min-width:50%}
}
@media(max-width:600px){
  .hero{height:calc(100vh - 62px);min-height:480px}
  .hero-inner{padding:0 16px}
  .pj-slide{min-width:100%}
}
"""

# ── JS (both carousels)
SCRIPTS = """<script>
(function(){
  // ── Hero carousel
  var cSlides = document.querySelectorAll('.cs-slide');
  var cDots   = document.querySelectorAll('.cs-dot');
  var cCur    = 0, cTotal = cSlides.length, cTimer;
  function cGo(n){
    cSlides[cCur].classList.remove('active'); cDots[cCur].classList.remove('active');
    cCur = (n + cTotal) % cTotal;
    cSlides[cCur].classList.add('active'); cDots[cCur].classList.add('active');
  }
  cTimer = setInterval(function(){ cGo(cCur+1); }, 4500);
  cDots.forEach(function(d){ d.addEventListener('click', function(){ cGo(+this.dataset.idx); clearInterval(cTimer); cTimer=setInterval(function(){cGo(cCur+1);},4500); }); });
  document.getElementById('csPrev').addEventListener('click', function(){ cGo(cCur-1); clearInterval(cTimer); cTimer=setInterval(function(){cGo(cCur+1);},4500); });
  document.getElementById('csNext').addEventListener('click', function(){ cGo(cCur+1); clearInterval(cTimer); cTimer=setInterval(function(){cGo(cCur+1);},4500); });

  // ── Reviews carousel
  var rvTrack = document.getElementById('rvTrack');
  if (rvTrack) {
    var rvDots = document.querySelectorAll('.rv-dot');
    var rvCur = 0, rvTotal = 15, rvTimer;
    function rvVis(){ return window.innerWidth > 900 ? 3 : window.innerWidth > 600 ? 2 : 1; }
    function rvGo(n){
      var v = rvVis();
      rvCur = Math.max(0, Math.min(n, rvTotal - v));
      rvTrack.style.transform = 'translateX(-' + (rvCur * (100/v)) + '%)';
      rvDots.forEach(function(d,i){ d.classList.toggle('rv-active', i===rvCur); });
    }
    function rvNext(){ rvGo(rvCur + rvVis() <= rvTotal - rvVis() ? rvCur + 1 : 0); }
    rvTimer = setInterval(rvNext, 4000);
    document.getElementById('rvPrev').addEventListener('click', function(){ rvGo(rvCur-1); clearInterval(rvTimer); rvTimer=setInterval(rvNext,4000); });
    document.getElementById('rvNext').addEventListener('click', function(){ rvGo(rvCur+1); clearInterval(rvTimer); rvTimer=setInterval(rvNext,4000); });
    rvDots.forEach(function(d){ d.addEventListener('click', function(){ rvGo(+this.dataset.rv); clearInterval(rvTimer); rvTimer=setInterval(rvNext,4000); }); });
    rvTrack.addEventListener('mouseenter', function(){ clearInterval(rvTimer); });
    rvTrack.addEventListener('mouseleave', function(){ rvTimer=setInterval(rvNext,4000); });
  }
})();
</script>"""

body = "\n".join([hero, ticker, services, gallery, why, areas, process, portfolio,
                  f'<div class="container">{contact_banner()}</div>', final, SCRIPTS])

extra = (f'<style>{EXTRA_CSS}</style>'
         '<link rel="preload" href="/images/photo-lvp-living.jpg" as="image">')

head_html = head(TITLE, DESC, CANONICAL, json_ld=SCHEMAS, extra_meta=extra)
write_page(OUT, head_html, header(active="home"), body)
print(f"✓ {OUT} ({open(OUT).read().count(chr(10))} lines)")
