#!/usr/bin/env python3
"""
Napa's Flooring — Shared Page Generator
Bold/Editorial design system: ink black + paper cream + orange accent.
Used by every _build_*.py script.
"""
import json
from _data import BUSINESS, CITIES, SERVICES, SERVICE_ORDER, CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, SMS_LINK, WHY_US_POINTS, PROCESS_STEPS, HERO_TRUST_BADGES, GENERAL_BLOG_POSTS, COST_BLOG_POSTS

DOMAIN = BUSINESS["domain"]
SITE = f"https://{DOMAIN}"

# ============================================================================
# CSS — Bold/Editorial design system
# ============================================================================
CSS = r"""
:root{
  --ink:#0A0A0A;
  --ink-soft:#1A1A1A;
  --paper:#F5F2EC;
  --paper-deep:#EDE8DE;
  --orange:#F5A623;
  --orange-deep:#D68A0A;
  --white:#FFFFFF;
  --rule:#D9D2C3;
  --gray:#525252;
  --muted:#8A8A8A;
  --success:#16A34A;
  --whatsapp:#25D366;
  --font-display:'Archivo Black','Inter',sans-serif;
  --font-editorial:'Fraunces','Georgia',serif;
  --font-body:'Inter','Helvetica Neue',Arial,sans-serif;
  --font-mono:'JetBrains Mono','Menlo',monospace;
  --container:1240px;
  --container-wide:1400px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;scroll-padding-top:110px}
body{font-family:var(--font-body);font-size:17px;line-height:1.6;color:var(--ink);background:var(--paper);overflow-x:hidden;font-feature-settings:"ss01","ss02";text-rendering:optimizeLegibility}
img{max-width:100%;height:auto;display:block}
a{color:var(--ink);text-decoration:none;transition:color .2s}
a:hover{color:var(--orange-deep)}
h1,h2,h3,h4,h5{font-family:var(--font-editorial);font-weight:600;line-height:1.05;letter-spacing:-.02em;color:var(--ink)}
p{margin:0 0 1.1rem}
button{font-family:inherit}
hr{border:none;border-top:1px solid var(--rule);margin:3rem 0}
.container{max-width:var(--container);margin:0 auto;padding:0 28px}
.container-wide{max-width:var(--container-wide);margin:0 auto;padding:0 28px}

/* MONO LABEL — editorial tag (Issue 06, By-line, etc) */
.mono-label{font-family:var(--font-mono);font-size:.74rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);display:inline-flex;align-items:center;gap:10px}
.mono-label::before{content:"";width:18px;height:1px;background:var(--orange);display:inline-block}
.mono-label.no-bar::before{display:none}
.mono-label.on-dark{color:rgba(255,255,255,.6)}

/* SECTION NUMBER — huge editorial */
.section-num{font-family:var(--font-display);font-size:clamp(2.4rem,7vw,4.5rem);color:var(--orange);line-height:1;letter-spacing:-.04em;display:inline-block;margin-bottom:.3rem}
.section-num.on-dark{color:var(--orange)}

/* SECTION KICKER bar */
.kicker{display:flex;align-items:baseline;gap:18px;margin-bottom:1.6rem;padding-bottom:1rem;border-bottom:2px solid var(--ink)}
.kicker-num{font-family:var(--font-display);font-size:clamp(1.6rem,4vw,2.4rem);color:var(--orange);line-height:1}
.kicker-label{font-family:var(--font-mono);font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink);font-weight:500}

/* BUTTONS — editorial style: sharp corners, arrow */
.btn{display:inline-flex;align-items:center;gap:10px;padding:16px 28px;font-family:var(--font-body);font-weight:600;font-size:.95rem;letter-spacing:.02em;text-decoration:none;cursor:pointer;border:none;transition:all .25s cubic-bezier(.2,.8,.2,1);position:relative;white-space:nowrap}
.btn-ink{background:var(--ink);color:var(--paper)}
.btn-ink:hover{background:var(--orange);color:var(--ink);transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink)}
.btn-orange{background:var(--orange);color:var(--ink);font-weight:700}
.btn-orange:hover{background:var(--ink);color:var(--orange);transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--orange)}
.btn-outline{background:transparent;color:var(--ink);border:2px solid var(--ink)}
.btn-outline:hover{background:var(--ink);color:var(--paper)}
.btn-outline-light{background:transparent;color:var(--paper);border:2px solid var(--paper)}
.btn-outline-light:hover{background:var(--paper);color:var(--ink)}
.btn-arrow::after{content:"→";font-family:var(--font-body);font-size:1.05rem;transition:transform .25s}
.btn:hover .btn-arrow::after,.btn-arrow:hover::after{transform:translateX(4px)}

/* TOP BANNER (very thin, above header) */
.top-bar{background:var(--ink);color:var(--paper);padding:9px 0;font-family:var(--font-mono);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase}
.top-bar-inner{max-width:var(--container-wide);margin:0 auto;padding:0 28px;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}
.top-bar a{color:var(--paper)}
.top-bar a:hover{color:var(--orange)}
.top-bar-edition{color:rgba(245,242,236,.5)}

/* MAIN HEADER */
.site-header{position:sticky;top:0;z-index:100;background:var(--paper);border-bottom:1px solid var(--rule);transition:padding .25s}
.nav-bar{display:flex;align-items:center;justify-content:space-between;padding:18px 28px;max-width:var(--container-wide);margin:0 auto;gap:1.4rem}
.brand{display:flex;align-items:center;gap:14px;text-decoration:none;flex-shrink:0}
.brand-mark{width:46px;height:46px;background:var(--ink);display:grid;place-items:center;flex-shrink:0}
.brand-mark span{color:var(--orange);font-family:var(--font-display);font-size:1.2rem;line-height:1;letter-spacing:-.02em}
.brand-text{display:flex;flex-direction:column;line-height:1.05}
.brand-name{font-family:var(--font-display);font-weight:400;font-size:1.32rem;color:var(--ink);letter-spacing:-.025em;white-space:nowrap}
.brand-tag{font-family:var(--font-mono);font-size:.66rem;letter-spacing:.18em;color:var(--orange);text-transform:uppercase;margin-top:5px;white-space:nowrap}
.nav-menu{display:flex;align-items:center;gap:2rem;list-style:none;flex-wrap:nowrap}
.nav-menu li{position:relative}
.nav-menu>li>a{font-family:var(--font-body);font-weight:500;color:var(--ink);font-size:.92rem;padding:10px 0;letter-spacing:.02em;position:relative;white-space:nowrap}
.nav-menu>li>a::after{content:"";position:absolute;bottom:4px;left:0;width:0;height:2px;background:var(--orange);transition:width .25s}
.nav-menu>li:hover>a::after,.nav-menu>li.active>a::after{width:100%}
.dropdown{position:absolute;top:calc(100% + 8px);left:0;background:var(--ink);min-width:260px;padding:14px 0;opacity:0;visibility:hidden;transform:translateY(-8px);transition:all .25s;z-index:99;box-shadow:8px 8px 0 var(--orange)}
.nav-menu li:hover .dropdown{opacity:1;visibility:visible;transform:translateY(0)}
.dropdown a{display:block;padding:9px 22px;font-size:.88rem;color:var(--paper);font-weight:400;letter-spacing:.01em}
.dropdown a:hover{background:var(--orange);color:var(--ink)}
.dropdown a .dot{color:var(--orange);font-family:var(--font-mono);font-size:.7rem;margin-right:8px}
.dropdown a:hover .dot{color:var(--ink)}
.nav-cta{display:flex;align-items:center;gap:18px;flex-shrink:0}
.nav-phone{display:flex;align-items:center;gap:8px;color:var(--ink);font-family:var(--font-mono);font-weight:500;font-size:.85rem;letter-spacing:.05em;white-space:nowrap}
.nav-phone:hover{color:var(--orange-deep)}
.nav-phone svg{width:16px;height:16px;flex-shrink:0;color:var(--orange)}
.menu-toggle{display:none;background:transparent;border:none;cursor:pointer;padding:8px;color:var(--ink)}
.menu-toggle svg{width:28px;height:28px}

/* BREADCRUMBS — editorial style */
.breadcrumbs{background:var(--paper);padding:18px 0 0;border-bottom:1px solid var(--rule)}
.breadcrumbs ol{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-family:var(--font-mono);font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);padding-bottom:16px}
.breadcrumbs li{display:flex;align-items:center;gap:8px}
.breadcrumbs li::after{content:"/";color:var(--rule)}
.breadcrumbs li:last-child::after{display:none}
.breadcrumbs a{color:var(--muted)}
.breadcrumbs a:hover{color:var(--orange-deep)}
.breadcrumbs li:last-child{color:var(--ink);font-weight:600}

/* HOMEPAGE HERO — split editorial */
.hero{background:var(--ink);color:var(--paper);padding:90px 0 70px;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 80% 30%,rgba(245,166,35,.08),transparent 60%);pointer-events:none}
.hero-inner{max-width:var(--container-wide);margin:0 auto;padding:0 28px;display:grid;grid-template-columns:1.15fr .85fr;gap:60px;align-items:center;position:relative;z-index:1}
.hero-label{display:flex;align-items:center;gap:14px;font-family:var(--font-mono);font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,242,236,.55);margin-bottom:34px}
.hero-label::before{content:"";width:38px;height:1px;background:var(--orange)}
.hero-h1{font-family:var(--font-editorial);font-weight:500;font-size:clamp(2.6rem,7vw,6rem);line-height:1;letter-spacing:-.035em;color:var(--paper);margin-bottom:2rem}
.hero-h1 em{font-style:italic;color:var(--orange);font-weight:400;display:inline-block}
.hero-h1 .stop{color:var(--orange);font-style:normal;font-weight:600}
.hero-sub{font-family:var(--font-body);font-size:1.12rem;line-height:1.5;color:rgba(245,242,236,.78);margin-bottom:2.4rem;max-width:560px;font-weight:400}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:2.6rem}
.hero-meta{display:flex;flex-wrap:wrap;gap:30px 40px;font-family:var(--font-mono);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(245,242,236,.6);padding-top:2rem;border-top:1px solid rgba(245,242,236,.14)}
.hero-meta div{display:flex;flex-direction:column;gap:4px}
.hero-meta strong{font-family:var(--font-display);font-size:1.7rem;color:var(--paper);letter-spacing:-.02em;line-height:1}
.hero-art{position:relative;aspect-ratio:4/5;background:var(--ink-soft);border:1px solid rgba(245,242,236,.12);overflow:hidden}
.hero-art img{width:100%;height:100%;object-fit:cover;filter:saturate(.85) brightness(.92)}
.hero-art::after{content:"";position:absolute;inset:0;background:linear-gradient(135deg,transparent 50%,rgba(10,10,10,.4) 100%);pointer-events:none}
.hero-art-tag{position:absolute;top:24px;left:24px;background:var(--orange);color:var(--ink);padding:8px 14px;font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;z-index:1}
.hero-art-caption{position:absolute;bottom:24px;left:24px;right:24px;color:var(--paper);font-family:var(--font-mono);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;z-index:1;display:flex;justify-content:space-between;gap:1rem}

/* PAGE HERO (interior) */
.page-hero{background:var(--ink);color:var(--paper);padding:60px 0 70px;position:relative;overflow:hidden}
.page-hero::before{content:"";position:absolute;top:0;right:-100px;width:400px;height:400px;background:radial-gradient(circle,rgba(245,166,35,.08),transparent 70%);pointer-events:none}
.page-hero-inner{max-width:var(--container);margin:0 auto;padding:0 28px;position:relative;z-index:1}
.page-hero .mono-label{color:rgba(245,242,236,.55)}
.page-hero h1{font-family:var(--font-editorial);font-weight:500;font-size:clamp(2.2rem,5.5vw,4.6rem);line-height:1.02;letter-spacing:-.025em;color:var(--paper);margin:18px 0 1.6rem;max-width:980px}
.page-hero h1 em{font-style:italic;color:var(--orange);font-weight:400}
.page-hero h1 .stop{color:var(--orange);font-weight:600}
.page-hero-sub{font-family:var(--font-body);font-size:1.1rem;line-height:1.55;color:rgba(245,242,236,.78);max-width:760px;margin-bottom:2.4rem}
.page-hero-trust{display:flex;flex-wrap:wrap;gap:22px 40px;font-family:var(--font-mono);font-size:.76rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(245,242,236,.6);padding-top:1.6rem;border-top:1px solid rgba(245,242,236,.14)}
.page-hero-trust span::before{content:"●";color:var(--orange);margin-right:8px;font-size:.6rem}

/* TICKER BAR (between hero and main content) */
.ticker{background:var(--orange);color:var(--ink);overflow:hidden;border-top:1px solid var(--orange-deep);border-bottom:1px solid var(--orange-deep)}
.ticker-inner{display:flex;animation:tickerScroll 50s linear infinite;font-family:var(--font-mono);font-size:.82rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;padding:14px 0;white-space:nowrap}
.ticker-inner span{padding:0 30px;flex-shrink:0;position:relative}
.ticker-inner span::after{content:"●";color:var(--ink);margin-left:30px;font-size:.5rem;vertical-align:middle}
@keyframes tickerScroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* SECTION BASE */
section{padding:90px 0;position:relative}
section.tight{padding:50px 0}
.section-head{margin-bottom:3.5rem;display:grid;grid-template-columns:1fr 1.4fr;gap:60px;align-items:end;border-bottom:2px solid var(--ink);padding-bottom:1.8rem}
.section-head-num{font-family:var(--font-display);font-size:clamp(3rem,8vw,5.5rem);color:var(--orange);line-height:1;letter-spacing:-.04em;align-self:start}
.section-head-meta{display:flex;flex-direction:column;gap:8px}
.section-head h2{font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.9rem,4vw,3.2rem);line-height:1.05;letter-spacing:-.025em}
.section-head h2 em{font-style:italic;color:var(--orange-deep)}
.section-head-text{max-width:680px}
.section-head-text p{font-size:1.02rem;color:var(--gray);margin:0}

/* INTRO COPY — drop cap */
.intro-prose{max-width:780px;margin:0 auto;font-family:var(--font-body);font-size:1.12rem;line-height:1.7;color:var(--ink)}
.intro-prose p:first-child::first-letter{font-family:var(--font-display);font-size:5.2rem;float:left;line-height:.88;padding:6px 14px 0 0;color:var(--orange)}
.intro-prose p{margin-bottom:1.25rem}
.intro-prose strong{font-weight:600;color:var(--ink)}

/* SOCIAL PROOF STRIP — newspaper style */
.proof-strip{background:var(--paper);padding:36px 0;border-top:3px solid var(--ink);border-bottom:1px solid var(--rule)}
.proof-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:36px;max-width:var(--container-wide);margin:0 auto;padding:0 28px}
.proof-item{display:flex;flex-direction:column;gap:4px;border-left:2px solid var(--orange);padding-left:18px}
.proof-num{font-family:var(--font-display);font-size:clamp(1.6rem,3.5vw,2.4rem);color:var(--ink);line-height:1;letter-spacing:-.02em}
.proof-label{font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gray);font-weight:500}

/* SERVICES GRID — magazine cards */
.services-section{background:var(--paper-deep)}
.services-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:1rem;border-top:2px solid var(--ink);border-left:2px solid var(--ink)}
.service-card{background:var(--paper);border-right:2px solid var(--ink);border-bottom:2px solid var(--ink);padding:36px 30px 30px;text-decoration:none;color:var(--ink);transition:background .25s;display:flex;flex-direction:column;min-height:360px;position:relative}
.service-card:hover{background:var(--ink);color:var(--paper)}
.service-card-num{font-family:var(--font-mono);font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);margin-bottom:1.2rem}
.service-card h3{font-family:var(--font-editorial);font-weight:500;font-size:1.85rem;line-height:1.04;letter-spacing:-.02em;color:inherit;margin:0 0 .9rem}
.service-card-desc{font-size:.95rem;color:var(--gray);line-height:1.55;flex-grow:1;margin-bottom:1.4rem;transition:color .25s}
.service-card:hover .service-card-desc{color:rgba(245,242,236,.7)}
.service-card-cta{font-family:var(--font-mono);font-size:.76rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink);font-weight:600;display:flex;align-items:center;gap:10px;transition:color .25s}
.service-card-cta::after{content:"→";font-family:var(--font-body);font-size:1.1rem;transition:transform .3s}
.service-card:hover .service-card-cta{color:var(--orange)}
.service-card:hover .service-card-cta::after{transform:translateX(6px)}

/* WHY US — numbered editorial */
.why-section{background:var(--paper)}
.why-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:0;margin-top:1rem;border-top:1px solid var(--ink)}
.why-item{padding:36px 0;border-bottom:1px solid var(--rule);display:grid;grid-template-columns:80px 1fr;gap:30px;align-items:start}
.why-item:nth-child(even){padding-left:40px;border-left:1px solid var(--rule)}
.why-item:nth-child(odd){padding-right:40px}
.why-num{font-family:var(--font-display);font-size:clamp(2.4rem,4vw,3.4rem);color:var(--orange);line-height:1;letter-spacing:-.04em}
.why-item h3{font-family:var(--font-editorial);font-weight:500;font-size:1.4rem;line-height:1.15;letter-spacing:-.015em;margin-bottom:.8rem}
.why-item p{font-size:.97rem;color:var(--gray);line-height:1.6;margin:0}

/* AREAS — black band with photo bg accent */
.areas-section{background:var(--ink);color:var(--paper);position:relative}
.areas-section h2{color:var(--paper)}
.areas-section h2 em{color:var(--orange)}
.areas-section .section-head{border-bottom-color:var(--paper)}
.areas-section .section-head-text p{color:rgba(245,242,236,.7)}
.areas-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:1rem;border:1px solid rgba(245,242,236,.16)}
.area-card{padding:26px 24px;border-right:1px solid rgba(245,242,236,.16);border-bottom:1px solid rgba(245,242,236,.16);text-decoration:none;color:var(--paper);transition:background .25s;display:flex;flex-direction:column;gap:8px}
.area-card:hover{background:var(--orange);color:var(--ink)}
.area-card-name{font-family:var(--font-editorial);font-weight:500;font-size:1.35rem;line-height:1.05;letter-spacing:-.02em;color:inherit}
.area-card-meta{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,242,236,.55);transition:color .25s}
.area-card:hover .area-card-meta{color:rgba(10,10,10,.7)}
.area-card-arrow{margin-top:auto;align-self:flex-start;font-family:var(--font-mono);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);display:inline-flex;align-items:center;gap:8px;font-weight:600}
.area-card:hover .area-card-arrow{color:var(--ink)}

/* PROCESS — horizontal timeline */
.process-section{background:var(--paper-deep)}
.process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:1rem;position:relative;border-top:2px solid var(--ink)}
.process-step{padding:36px 28px 30px;background:var(--paper);border-right:1px solid var(--rule);position:relative;border-bottom:2px solid var(--ink)}
.process-step:last-child{border-right:none}
.process-num{font-family:var(--font-display);font-size:clamp(2.6rem,5vw,3.6rem);color:var(--orange);line-height:.9;letter-spacing:-.04em;margin-bottom:1rem}
.process-step h3{font-family:var(--font-editorial);font-weight:500;font-size:1.35rem;margin-bottom:.6rem;line-height:1.12}
.process-step p{font-size:.92rem;color:var(--gray);line-height:1.55;margin:0}

/* REVIEWS — pull-quote style */
.reviews-section{background:var(--paper)}
.reviews-rating-bar{display:flex;align-items:center;gap:14px;padding:14px 24px;background:var(--ink);color:var(--paper);font-family:var(--font-mono);font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3rem;justify-content:space-between;flex-wrap:wrap}
.reviews-rating-bar strong{font-family:var(--font-display);color:var(--orange);font-size:1.4rem;letter-spacing:-.02em}
.reviews-rating-bar .stars{color:var(--orange);font-size:1rem;letter-spacing:2px}
.reviews-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--ink);border-left:1px solid var(--ink)}
.review-card{padding:36px 28px;border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);background:var(--paper);display:flex;flex-direction:column;gap:1rem;position:relative}
.review-quote-mark{font-family:var(--font-editorial);font-size:4rem;line-height:.7;color:var(--orange);position:absolute;top:24px;right:24px;font-weight:600;opacity:.4}
.review-stars{color:var(--orange);font-size:.95rem;letter-spacing:2px}
.review-text{font-family:var(--font-editorial);font-style:italic;font-size:1.04rem;line-height:1.5;color:var(--ink);margin:0;font-weight:400}
.review-meta{margin-top:auto;padding-top:1.2rem;border-top:1px solid var(--rule);display:flex;flex-direction:column;gap:4px}
.review-author{font-family:var(--font-body);font-weight:600;font-size:.92rem;color:var(--ink)}
.review-where{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.review-verified{font-family:var(--font-mono);font-size:.65rem;letter-spacing:.14em;text-transform:uppercase;color:var(--success);font-weight:600;display:inline-flex;align-items:center;gap:5px}

/* CHECKLIST — editorial card grid */
.checklist-section{background:var(--paper-deep)}
.checklist-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:1rem}
.checklist-card{background:var(--paper);border:2px solid var(--ink);position:relative}
.checklist-card-head{background:var(--ink);color:var(--paper);padding:18px 22px;display:flex;align-items:baseline;justify-content:space-between;gap:14px}
.checklist-card-head strong{font-family:var(--font-editorial);font-weight:500;font-size:1.15rem;letter-spacing:-.015em}
.checklist-card-head .ck-num{font-family:var(--font-display);color:var(--orange);font-size:1.1rem;line-height:1}
.checklist-card-head .ck-count{font-family:var(--font-mono);color:rgba(245,242,236,.6);font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;margin-left:auto}
.checklist-card ol{padding:20px 24px 22px 44px;list-style:decimal;font-size:.92rem;line-height:1.55;color:var(--ink)}
.checklist-card ol li{margin-bottom:.5rem;padding-left:6px}
.checklist-card ol li::marker{color:var(--orange);font-family:var(--font-mono);font-weight:700;font-size:.85rem}

/* NEIGHBORHOODS — pill chip grid */
.neighborhoods-section{background:var(--paper)}
.neighborhood-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;margin:1rem 0 2rem}
.neighborhood-pill{padding:13px 18px;background:var(--paper);border:1.5px solid var(--ink);color:var(--ink);font-family:var(--font-body);font-weight:500;font-size:.92rem;letter-spacing:.01em;display:flex;align-items:center;gap:10px;transition:all .2s}
.neighborhood-pill::before{content:"";width:6px;height:6px;background:var(--orange);flex-shrink:0;display:block}
.neighborhood-pill:hover{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.neighborhood-pill:hover::before{background:var(--orange)}
.zips-bar{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-top:2rem;padding-top:1.5rem;border-top:1px solid var(--rule)}
.zips-bar-label{font-family:var(--font-mono);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gray);font-weight:600;margin-right:10px}
.zip-tag{padding:6px 11px;background:var(--ink);color:var(--paper);font-family:var(--font-mono);font-size:.78rem;letter-spacing:.04em;font-weight:500}

/* PRICING TABLE — newspaper accounting style */
.pricing-section{background:var(--paper-deep)}
.pricing-wrap{margin-top:1.4rem;background:var(--paper);border:2px solid var(--ink);overflow:hidden}
.pricing-head-bar{background:var(--ink);color:var(--paper);padding:18px 26px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem}
.pricing-head-bar h3{font-family:var(--font-editorial);font-weight:500;color:var(--paper);font-size:1.4rem;margin:0;letter-spacing:-.015em}
.pricing-head-bar h3 em{color:var(--orange);font-style:italic}
.pricing-head-meta{font-family:var(--font-mono);font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,242,236,.7)}
table.pricing-table{width:100%;border-collapse:collapse;font-size:.95rem}
.pricing-table thead{background:var(--paper-deep);border-bottom:2px solid var(--ink)}
.pricing-table th{padding:14px 22px;text-align:left;font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink);font-weight:600}
.pricing-table th:last-child,.pricing-table td:last-child{text-align:right}
.pricing-table td{padding:16px 22px;border-bottom:1px solid var(--rule);color:var(--ink);vertical-align:top}
.pricing-table td:first-child{font-weight:600;font-family:var(--font-body)}
.pricing-table .price{font-family:var(--font-display);color:var(--orange-deep);white-space:nowrap;font-size:.95rem;letter-spacing:-.01em}
.pricing-table tr:last-child td{border-bottom:none}
.pricing-table tr:hover td{background:var(--paper-deep)}
.pricing-note{padding:14px 26px;background:var(--paper-deep);font-family:var(--font-mono);font-size:.74rem;letter-spacing:.08em;color:var(--gray);text-transform:uppercase;border-top:1px solid var(--rule)}
.pricing-note a{color:var(--orange-deep);font-weight:600}

/* STAT BADGE — editorial signature block */
.stat-badge{margin:2rem 0;padding:22px 28px;background:var(--ink);color:var(--paper);display:flex;align-items:center;gap:24px;border-left:6px solid var(--orange);position:relative}
.stat-badge-num{font-family:var(--font-display);font-size:clamp(2rem,5vw,3rem);color:var(--orange);line-height:1;letter-spacing:-.03em;flex-shrink:0}
.stat-badge-body{flex-grow:1}
.stat-badge-body strong{font-family:var(--font-editorial);font-weight:500;font-size:1.15rem;color:var(--paper);display:block;margin-bottom:4px;letter-spacing:-.01em}
.stat-badge-body small{font-family:var(--font-mono);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,242,236,.7)}

/* PULL QUOTE — magazine signature */
.pull-quote{max-width:820px;margin:3rem auto;padding:2rem 1rem;text-align:center;border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);position:relative}
.pull-quote p{font-family:var(--font-editorial);font-style:italic;font-size:clamp(1.4rem,3vw,2rem);line-height:1.25;color:var(--ink);font-weight:400;margin:0;letter-spacing:-.01em}
.pull-quote p::before{content:"\201C";font-size:1em;color:var(--orange);font-weight:600;margin-right:6px}
.pull-quote p::after{content:"\201D";font-size:1em;color:var(--orange);font-weight:600;margin-left:6px}
.pull-quote cite{display:block;margin-top:1rem;font-family:var(--font-mono);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;font-style:normal;color:var(--muted)}

/* MISTAKES LIST — editorial numbered features */
.features-list{display:flex;flex-direction:column;gap:0;max-width:920px;margin:0 auto;border-top:1px solid var(--ink)}
.feature-row{padding:30px 0;border-bottom:1px solid var(--rule);display:grid;grid-template-columns:80px 1fr;gap:32px;align-items:start}
.feature-row:hover .feature-num{color:var(--orange-deep)}
.feature-num{font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);color:var(--orange);line-height:1;letter-spacing:-.03em}
.feature-body h3{font-family:var(--font-editorial);font-weight:500;font-size:1.45rem;margin-bottom:.7rem;line-height:1.12;letter-spacing:-.015em}
.feature-body p{font-size:1rem;color:var(--gray);line-height:1.6;margin:0}

/* FAQ — editorial details/summary */
.faq-section{background:var(--paper)}
.faq-list{max-width:880px;margin:0 auto;border-top:2px solid var(--ink)}
.faq-list details{border-bottom:1px solid var(--rule);padding:0}
.faq-list summary{padding:28px 0;cursor:pointer;list-style:none;display:flex;align-items:flex-start;gap:20px;font-family:var(--font-editorial);font-weight:500;font-size:1.15rem;line-height:1.3;letter-spacing:-.015em;color:var(--ink);position:relative}
.faq-list summary::-webkit-details-marker{display:none}
.faq-list summary::before{content:"+";font-family:var(--font-display);color:var(--orange);font-size:1.4rem;font-weight:400;line-height:1;flex-shrink:0;width:28px;transition:transform .25s}
.faq-list details[open] summary::before{content:"−"}
.faq-list .faq-body{padding:0 0 28px 48px;font-size:1rem;line-height:1.65;color:var(--gray)}
.faq-list .faq-body p{margin-bottom:.9rem}
.faq-list .faq-body p:last-child{margin-bottom:0}

/* INTERNAL LINK BOX — newspaper style */
.related-box{background:var(--ink);color:var(--paper);padding:38px 32px;margin:3rem 0}
.related-box-label{font-family:var(--font-mono);font-size:.74rem;letter-spacing:.18em;text-transform:uppercase;color:var(--orange);margin-bottom:1rem;font-weight:600}
.related-box h3{font-family:var(--font-editorial);font-weight:500;color:var(--paper);font-size:1.5rem;margin-bottom:1.6rem;letter-spacing:-.015em}
.related-box ul{list-style:none;display:grid;grid-template-columns:repeat(2,1fr);gap:8px 32px}
.related-box li a{color:var(--paper);font-family:var(--font-body);font-size:.96rem;border-bottom:1px solid rgba(245,242,236,.18);padding:8px 0;display:block;transition:all .2s}
.related-box li a:hover{color:var(--orange);border-bottom-color:var(--orange);padding-left:8px}

/* WHATSAPP INLINE BANNER (de-emphasized — phone is primary) */
.contact-banner{background:var(--ink);color:var(--paper);padding:28px 32px;margin:3rem 0;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;border-left:6px solid var(--orange)}
.contact-banner-text strong{font-family:var(--font-editorial);font-weight:500;font-size:1.4rem;color:var(--paper);display:block;letter-spacing:-.015em;margin-bottom:4px}
.contact-banner-text span{font-family:var(--font-mono);font-size:.78rem;letter-spacing:.12em;color:rgba(245,242,236,.65);text-transform:uppercase}
.contact-banner-cta{display:flex;gap:10px;flex-wrap:wrap}

/* FINAL CTA */
.final-cta{background:var(--orange);color:var(--ink);padding:80px 0;text-align:center;border-top:6px solid var(--ink);border-bottom:6px solid var(--ink)}
.final-cta .mono-label{color:var(--ink)}
.final-cta .mono-label::before{background:var(--ink)}
.final-cta h2{font-family:var(--font-editorial);font-weight:500;font-size:clamp(2rem,5vw,3.4rem);line-height:1.05;letter-spacing:-.025em;color:var(--ink);margin:1rem 0 1.4rem;max-width:760px;margin-left:auto;margin-right:auto}
.final-cta h2 em{font-style:italic;color:var(--ink)}
.final-cta-sub{font-family:var(--font-body);font-size:1.08rem;color:var(--ink);max-width:560px;margin:0 auto 2rem;opacity:.8}
.final-cta-phone{font-family:var(--font-display);font-size:clamp(2rem,5vw,3rem);color:var(--ink);letter-spacing:-.02em;display:inline-block;margin-bottom:1.4rem;text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:8px}
.final-cta-phone:hover{color:var(--paper)}
.final-cta-buttons{display:flex;justify-content:center;gap:14px;flex-wrap:wrap}

/* FOOTER */
footer{background:var(--ink);color:rgba(245,242,236,.78);padding:80px 0 0;border-top:6px solid var(--orange)}
.footer-grid{max-width:var(--container-wide);margin:0 auto;padding:0 28px;display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:50px;margin-bottom:3.5rem}
.footer-col h4{font-family:var(--font-mono);color:var(--orange);font-size:.74rem;font-weight:600;text-transform:uppercase;letter-spacing:.18em;margin-bottom:1.2rem}
.footer-brand-bar{display:flex;align-items:center;gap:14px;margin-bottom:1.3rem}
.footer-brand-mark{width:46px;height:46px;background:var(--orange);display:grid;place-items:center}
.footer-brand-mark span{color:var(--ink);font-family:var(--font-display);font-size:1.2rem;letter-spacing:-.02em}
.footer-brand strong{font-family:var(--font-display);font-weight:400;font-size:1.4rem;color:var(--paper);letter-spacing:-.02em}
.footer-col p{color:rgba(245,242,236,.62);line-height:1.65;font-size:.94rem;margin-bottom:.8rem}
.footer-col ul{list-style:none}
.footer-col li{margin-bottom:.55rem}
.footer-col a{color:rgba(245,242,236,.72);font-size:.93rem}
.footer-col a:hover{color:var(--orange)}
.footer-contact-item{display:flex;gap:10px;margin-bottom:.7rem;font-size:.92rem;color:rgba(245,242,236,.72);align-items:flex-start}
.footer-contact-item svg{width:15px;height:15px;color:var(--orange);flex-shrink:0;margin-top:4px}
.footer-hours{font-family:var(--font-mono);font-size:.78rem;letter-spacing:.04em;color:rgba(245,242,236,.6);line-height:1.7;margin-top:1rem}
.footer-bottom{border-top:1px solid rgba(245,242,236,.14);padding:1.6rem 0;max-width:var(--container-wide);margin:0 auto;padding-left:28px;padding-right:28px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:1rem;font-family:var(--font-mono);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(245,242,236,.5)}
.footer-bottom a{color:rgba(245,242,236,.55)}
.footer-bottom a:hover{color:var(--orange)}
.footer-bigtype{padding:2.4rem 28px 1.6rem;text-align:center;border-top:1px solid rgba(245,242,236,.14);max-width:var(--container-wide);margin:0 auto}
.footer-bigtype span{font-family:var(--font-display);font-size:clamp(2.6rem,8vw,5.4rem);color:var(--orange);letter-spacing:-.04em;line-height:.9;display:block;opacity:.92}

/* WHATSAPP FLOAT (compact, secondary CTA) */
.contact-float{position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;flex-direction:column;gap:10px;align-items:flex-end}
.contact-float-btn{display:inline-flex;align-items:center;gap:9px;background:var(--ink);color:var(--paper);padding:13px 20px;font-family:var(--font-mono);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;text-decoration:none;box-shadow:6px 6px 0 var(--orange);transition:all .25s}
.contact-float-btn:hover{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--orange);color:var(--orange)}
.contact-float-btn svg{width:16px;height:16px}
.contact-float-btn.wa{background:var(--whatsapp);color:var(--white);box-shadow:6px 6px 0 var(--ink)}
.contact-float-btn.wa:hover{box-shadow:8px 8px 0 var(--ink);color:var(--white)}

/* CONTACT FORM */
.form-wrap{background:var(--paper);border:2px solid var(--ink);padding:36px;margin:2rem 0}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.form-grid label{grid-column:span 1;display:flex;flex-direction:column;gap:6px;font-family:var(--font-mono);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);font-weight:600}
.form-grid label.full{grid-column:span 2}
.form-grid input,.form-grid select,.form-grid textarea{font-family:var(--font-body);font-size:1rem;color:var(--ink);background:var(--paper);border:1.5px solid var(--ink);padding:14px 16px;transition:all .2s}
.form-grid input:focus,.form-grid select:focus,.form-grid textarea:focus{outline:none;border-color:var(--orange);box-shadow:4px 4px 0 var(--orange)}
.form-grid textarea{min-height:140px;resize:vertical}
.form-submit{grid-column:span 2;justify-self:start}

/* BLOG INDEX cards */
.blog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:2px solid var(--ink);border-left:2px solid var(--ink)}
.blog-card{padding:34px 28px;background:var(--paper);border-right:2px solid var(--ink);border-bottom:2px solid var(--ink);text-decoration:none;color:var(--ink);transition:background .25s;display:flex;flex-direction:column;min-height:260px}
.blog-card:hover{background:var(--ink);color:var(--paper)}
.blog-card-meta{font-family:var(--font-mono);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--orange);margin-bottom:1rem;display:flex;justify-content:space-between;gap:1rem}
.blog-card h3{font-family:var(--font-editorial);font-weight:500;font-size:1.32rem;line-height:1.15;letter-spacing:-.015em;color:inherit;margin:0 0 .9rem;flex-grow:1}
.blog-card-cta{font-family:var(--font-mono);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink);font-weight:600;margin-top:auto}
.blog-card:hover .blog-card-cta{color:var(--orange)}
.blog-card-cta::after{content:"→";margin-left:8px;display:inline-block;transition:transform .25s}
.blog-card:hover .blog-card-cta::after{transform:translateX(5px)}

/* BLOG POST article body */
.post-article{max-width:760px;margin:0 auto;padding:60px 0}
.post-meta-bar{font-family:var(--font-mono);font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gray);display:flex;flex-wrap:wrap;gap:24px;margin-bottom:1.6rem}
.post-meta-bar .cat{color:var(--orange-deep);font-weight:600}
.post-article h1{font-family:var(--font-editorial);font-weight:500;font-size:clamp(2rem,5vw,3.4rem);line-height:1.06;letter-spacing:-.025em;margin-bottom:1.5rem;color:var(--ink)}
.post-lede{font-family:var(--font-editorial);font-size:1.3rem;line-height:1.45;color:var(--gray);font-style:italic;font-weight:400;margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid var(--rule)}
.post-article h2{font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.1rem);line-height:1.15;margin:2.5rem 0 1.1rem;letter-spacing:-.02em;border-top:2px solid var(--ink);padding-top:2.2rem}
.post-article h3{font-family:var(--font-editorial);font-weight:500;font-size:1.35rem;line-height:1.2;margin:1.8rem 0 .9rem;color:var(--ink)}
.post-article p{font-size:1.08rem;line-height:1.72;color:var(--ink);margin-bottom:1.2rem}
.post-article p strong{font-weight:600}
.post-article ul,.post-article ol{padding-left:1.5rem;margin-bottom:1.4rem}
.post-article li{margin-bottom:.6rem;font-size:1.05rem;line-height:1.65}
.post-article li::marker{color:var(--orange);font-weight:700}
.post-article blockquote{border-left:4px solid var(--orange);padding:.6rem 0 .6rem 1.6rem;font-family:var(--font-editorial);font-style:italic;font-size:1.2rem;line-height:1.4;color:var(--ink);margin:2rem 0}
.post-article .post-table{width:100%;border-collapse:collapse;margin:2rem 0;font-size:.94rem;border:2px solid var(--ink)}
.post-article .post-table th{background:var(--ink);color:var(--paper);padding:12px 16px;text-align:left;font-family:var(--font-mono);font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.post-article .post-table td{padding:12px 16px;border-bottom:1px solid var(--rule);color:var(--ink)}
.post-article .post-table tr:nth-child(even) td{background:var(--paper-deep)}
.post-article .post-key-takeaway{background:var(--paper-deep);border-left:4px solid var(--orange);padding:1.3rem 1.6rem;margin:2rem 0;font-family:var(--font-body)}
.post-article .post-key-takeaway strong{font-family:var(--font-mono);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange-deep);display:block;margin-bottom:.5rem;font-weight:600}
.post-author{margin:3rem 0 0;padding:2rem 0;border-top:2px solid var(--ink);display:flex;align-items:center;gap:18px}
.post-author-avatar{width:60px;height:60px;background:var(--orange);display:grid;place-items:center;color:var(--ink);font-family:var(--font-display);font-size:1.4rem;letter-spacing:-.02em;flex-shrink:0}
.post-author-info strong{display:block;font-family:var(--font-editorial);font-weight:500;font-size:1.1rem;color:var(--ink);margin-bottom:2px}
.post-author-info span{font-family:var(--font-mono);font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gray)}

/* GENERIC ARTICLE PAGE (about, financing, etc) */
.page-article{max-width:820px;margin:0 auto;padding:50px 0}
.page-article p{font-size:1.08rem;line-height:1.7;color:var(--ink);margin-bottom:1.1rem}
.page-article h2{font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.2rem);margin:2.4rem 0 1rem;line-height:1.1;letter-spacing:-.02em;border-top:2px solid var(--ink);padding-top:2rem}
.page-article h3{font-family:var(--font-editorial);font-weight:500;font-size:1.35rem;margin:1.6rem 0 .8rem;line-height:1.18}
.page-article ul,.page-article ol{padding-left:1.5rem;margin-bottom:1.4rem}
.page-article li{margin-bottom:.55rem;font-size:1.04rem;line-height:1.65}
.page-article li::marker{color:var(--orange);font-weight:700}

/* MOBILE */
@media(max-width:1100px){
  .hero-inner{grid-template-columns:1fr;gap:40px}
  .hero-art{aspect-ratio:16/10;max-width:520px;margin:0 auto}
  .section-head{grid-template-columns:1fr;gap:18px}
  .services-grid,.areas-grid,.process-grid,.reviews-grid,.blog-grid{grid-template-columns:repeat(2,1fr)}
  .why-grid{grid-template-columns:1fr}
  .why-item:nth-child(even){padding-left:0;border-left:none}
  .why-item:nth-child(odd){padding-right:0}
  .checklist-grid{grid-template-columns:repeat(2,1fr)}
  .footer-grid{grid-template-columns:1fr 1fr;gap:36px}
}
@media(max-width:768px){
  .top-bar-inner{justify-content:center;gap:14px}
  .top-bar-edition{display:none}
  .nav-menu{display:none;position:absolute;top:100%;left:0;right:0;flex-direction:column;background:var(--paper);padding:14px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);align-items:stretch;gap:0;max-height:calc(100vh - 110px);overflow-y:auto;box-shadow:0 12px 32px rgba(10,10,10,.12)}
  .nav-menu.open{display:flex}
  .nav-menu>li{width:100%;border-bottom:1px solid var(--rule)}
  .nav-menu>li:last-child{border-bottom:none}
  .nav-menu>li>a{display:block;padding:14px 28px;font-size:1rem}
  .dropdown{position:static;opacity:1;visibility:visible;transform:none;background:var(--paper-deep);box-shadow:none;padding:8px 0}
  .dropdown a{padding:10px 44px;color:var(--ink);font-size:.92rem}
  .menu-toggle{display:block}
  .nav-phone span{display:none}
  .brand-tag{display:none}
  .hero{padding:50px 0 40px}
  .page-hero{padding:36px 0 50px}
  section{padding:55px 0}
  .proof-grid{grid-template-columns:repeat(2,1fr);gap:22px}
  .proof-item:nth-child(5){display:none}
  .services-grid,.areas-grid,.process-grid,.reviews-grid,.blog-grid,.checklist-grid{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr;gap:32px}
  .related-box ul{grid-template-columns:1fr}
  .form-grid{grid-template-columns:1fr}
  .form-grid label.full,.form-submit{grid-column:span 1}
  .contact-banner{grid-template-columns:1fr;text-align:left}
  .feature-row{grid-template-columns:60px 1fr;gap:18px}
  .why-item{grid-template-columns:60px 1fr;gap:18px;padding:24px 0}
  .pricing-table th,.pricing-table td{padding:10px 14px;font-size:.86rem}
  .reviews-rating-bar{font-size:.7rem}
  .faq-list summary{font-size:1.02rem}
}
@media(max-width:520px){
  .container,.container-wide{padding:0 18px}
  .nav-bar{padding:14px 18px}
  .top-bar-inner{padding:0 18px;font-size:.66rem}
  .hero-meta{gap:18px 28px}
  .hero-meta strong{font-size:1.35rem}
  .stat-badge{flex-direction:column;align-items:flex-start;text-align:left;gap:10px;padding:18px}
  .pricing-table{display:block;overflow-x:auto}
  .pricing-table table{min-width:540px}
  .form-wrap{padding:24px 20px}
}
"""

# ============================================================================
# HEAD — page <head> builder
# ============================================================================
def head(title, desc, canonical, og_image=None, og_type="website", indexable=True, json_ld=None, extra_meta=""):
    """Builds the <head> section with all SEO meta, OG, fonts, CSS, and JSON-LD."""
    og_image = og_image or f"{SITE}/images/og-default.jpg"
    robots = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" if indexable else "noindex, nofollow"
    schemas_html = ""
    if json_ld:
        if isinstance(json_ld, list):
            for s in json_ld:
                schemas_html += f'<script type="application/ld+json">{json.dumps(s, separators=(",",":"))}</script>\n'
        else:
            schemas_html = f'<script type="application/ld+json">{json.dumps(json_ld, separators=(",",":"))}</script>\n'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="author" content="{BUSINESS["name"]}">
<meta name="geo.region" content="US-{BUSINESS["state"]}">
<meta name="geo.placename" content="{BUSINESS["city"]}, {BUSINESS["state_long"]}">
<meta name="geo.position" content="{BUSINESS["lat"]};{BUSINESS["lng"]}">
<meta name="ICBM" content="{BUSINESS["lat"]}, {BUSINESS["lng"]}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{BUSINESS["name"]} — {BUSINESS["tagline"]}">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{BUSINESS["name"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
{extra_meta}
<style>{CSS}</style>
{schemas_html}</head>
'''

# ============================================================================
# HEADER — site nav (consistent across all pages)
# ============================================================================
def header(active=""):
    svc_links = "".join(
        f'<a href="/{slug}/"><span class="dot">{SERVICES[slug]["icon"]}</span>{SERVICES[slug]["name"]}</a>'
        for slug in SERVICE_ORDER
    )
    city_links = "".join(
        f'<a href="/{slug}/"><span class="dot">●</span>{CITIES[slug]["name"]}, FL</a>'
        for slug in CITIES
    )
    nav_active = {
        "home":"", "services":"active", "areas":"active",
        "blog":"active", "about":"active", "contact":"active", "":""
    }
    a_serv = nav_active.get("services","") if active in ("services","service","service-city") else ""
    a_area = nav_active.get("areas","") if active in ("areas","city") else ""
    a_blog = nav_active.get("blog","") if active == "blog" else ""
    a_about = nav_active.get("about","") if active == "about" else ""
    a_cont = nav_active.get("contact","") if active == "contact" else ""

    return f'''<div class="top-bar"><div class="top-bar-inner">
<a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a>
<span class="top-bar-edition">Edition 06 · 2026 · {BUSINESS["city"]} · {BUSINESS["state"]}</span>
<a href="mailto:{BUSINESS["email"]}">{BUSINESS["email"]}</a>
</div></div>
<header class="site-header">
  <nav class="nav-bar" aria-label="Main">
    <a href="/" class="brand" aria-label="{BUSINESS["name"]} home">
      <span class="brand-mark"><span>N</span></span>
      <span class="brand-text">
        <span class="brand-name">NAPA&rsquo;S</span>
        <span class="brand-tag">Flooring · Est. {BUSINESS["year_founded"]}</span>
      </span>
    </a>
    <ul class="nav-menu" id="navMenu">
      <li{' class="active"' if active=="home" else ''}><a href="/">Home</a></li>
      <li{' class="' + a_serv + '"' if a_serv else ''}><a href="/hardwood-flooring/">Services</a>
        <div class="dropdown">{svc_links}</div>
      </li>
      <li{' class="' + a_area + '"' if a_area else ''}><a href="/bradenton/">Service Areas</a>
        <div class="dropdown">{city_links}</div>
      </li>
      <li{' class="' + a_blog + '"' if a_blog else ''}><a href="/blog/">Journal</a></li>
      <li{' class="' + a_about + '"' if a_about else ''}><a href="/about/">About</a></li>
      <li{' class="' + a_cont + '"' if a_cont else ''}><a href="/contact/">Contact</a></li>
    </ul>
    <div class="nav-cta">
      <a href="{TEL_LINK}" class="nav-phone" aria-label="Call {BUSINESS["name"]}">
        <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        <span>{BUSINESS["phone_display"]}</span>
      </a>
      <a href="/contact/#quote" class="btn btn-orange">Free Quote <span class="btn-arrow"></span></a>
      <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu" aria-expanded="false">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </nav>
</header>'''

# ============================================================================
# BREADCRUMBS
# ============================================================================
def breadcrumbs(items):
    """items: list of (label, href|None). Last item href should be None."""
    lis = ""
    for label, href in items:
        if href:
            lis += f'<li><a href="{href}">{label}</a></li>'
        else:
            lis += f'<li>{label}</li>'
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><div class="container"><ol>{lis}</ol></div></nav>'

# ============================================================================
# FOOTER
# ============================================================================
def footer():
    svc_links = "".join(
        f'<li><a href="/{slug}/">{SERVICES[slug]["name"]}</a></li>'
        for slug in SERVICE_ORDER
    )
    area_links = "".join(
        f'<li><a href="/{slug}/">{CITIES[slug]["name"]}, FL</a></li>'
        for slug in CITIES
    )
    hours_html = "<br>".join(
        f'<span>{day[:3].upper()}</span> &nbsp; {o}–{c}'
        for day, o, c in BUSINESS["hours"]
    )
    return f'''<footer>
  <div class="footer-grid">
    <div class="footer-col footer-brand">
      <div class="footer-brand-bar">
        <span class="footer-brand-mark"><span>N</span></span>
        <strong>Napa&rsquo;s Flooring</strong>
      </div>
      <p>{BUSINESS["tagline_long"]}</p>
      <p style="font-family:var(--font-mono);font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--orange);margin-top:1rem">{BUSINESS["unique_stat_full"]}</p>
    </div>
    <div class="footer-col">
      <h4>Services</h4>
      <ul>{svc_links}</ul>
    </div>
    <div class="footer-col">
      <h4>Service Areas</h4>
      <ul>{area_links}</ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <div class="footer-contact-item">
        <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        <a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a>
      </div>
      <div class="footer-contact-item">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        <a href="mailto:{BUSINESS["email"]}">{BUSINESS["email"]}</a>
      </div>
      <div class="footer-contact-item">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        <span>{BUSINESS["city"]}, {BUSINESS["state"]} {BUSINESS["zip"]}</span>
      </div>
      <p class="footer-hours">{hours_html}</p>
    </div>
  </div>
  <div class="footer-bigtype"><span>NAPA&rsquo;S FLOORING.</span></div>
  <div class="footer-bottom">
    <span>© {BUSINESS["year_founded"]}–2026 {BUSINESS["legal_name"]} · Licensed &amp; Insured</span>
    <span><a href="/about/">About</a> &nbsp;·&nbsp; <a href="/warranty/">Warranty</a> &nbsp;·&nbsp; <a href="/financing/">Financing</a> &nbsp;·&nbsp; <a href="/faq/">FAQ</a></span>
  </div>
</footer>'''

# ============================================================================
# WhatsApp / Contact floats
# ============================================================================
FLOAT_CONTACT = f'''<div class="contact-float">
  <a href="{TEL_LINK}" class="contact-float-btn" aria-label="Call {BUSINESS["name"]}">
    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
    Call Now
  </a>
  <a href="{WA_LINK}" target="_blank" rel="noopener" class="contact-float-btn wa" aria-label="Message us on WhatsApp">
    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.157 5.335 5.495 0 12.05 0a11.817 11.817 0 018.413 3.488 11.824 11.824 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.888-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.743-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413z"/></svg>
    WhatsApp
  </a>
</div>'''

# Compact MENU script — toggle hamburger
MENU_JS = '''<script>
(function(){var t=document.getElementById("menuToggle"),m=document.getElementById("navMenu");if(t&&m){t.addEventListener("click",function(){var o=m.classList.toggle("open");t.setAttribute("aria-expanded",o)})}})();
</script>'''

# Inline contact banner (used in long pages)
def contact_banner(message="Free, no-pressure estimate within 24 hours.", subtitle="Call, text, or email — your floor, your call."):
    return f'''<aside class="contact-banner">
  <div class="contact-banner-text">
    <strong>{message}</strong>
    <span>{subtitle}</span>
  </div>
  <div class="contact-banner-cta">
    <a href="{TEL_LINK}" class="btn btn-orange">Call {BUSINESS["phone_display"]}</a>
    <a href="/contact/" class="btn btn-outline-light">Email Us</a>
  </div>
</aside>'''

# Stat badge (used on service/city pages)
def stat_badge():
    return f'''<div class="stat-badge">
  <div class="stat-badge-num">{BUSINESS["unique_stat_number"]}</div>
  <div class="stat-badge-body">
    <strong>{BUSINESS["unique_stat_full"]}.</strong>
    <small>{BUSINESS["review_count"]} verified reviews · {BUSINESS["rating"]}★ Google · Licensed &amp; Insured</small>
  </div>
</div>'''

# Final CTA (most pages end with this)
def final_cta(headline=None, sub=None):
    headline = headline or "Get a real estimate from a real installer."
    sub = sub or f"Free, written, line-itemized — within 24 hours. We respond to every inquiry, every day."
    return f'''<section class="final-cta">
  <div class="container">
    <span class="mono-label">Free Estimate · No Pressure</span>
    <h2>{headline}</h2>
    <p class="final-cta-sub">{sub}</p>
    <a href="{TEL_LINK}" class="final-cta-phone">{BUSINESS["phone_display"]}</a>
    <div class="final-cta-buttons">
      <a href="/contact/#quote" class="btn btn-ink btn-arrow">Email Us</a>
      <a href="{SMS_LINK}" class="btn btn-outline">Text Us</a>
    </div>
  </div>
</section>'''

# Ticker scrolling bar (animated, used after hero)
def ticker_bar():
    items = [
        f"{BUSINESS['unique_stat_full']}",
        f"{BUSINESS['review_count']} × 5★ Google reviews",
        f"Free estimate in 24 hrs",
        f"Licensed &amp; Insured",
        f"12-month workmanship warranty",
        f"Two installers · same crew · start to finish",
        f"TCNA-spec tile · IRC-spec framing",
        f"Acclimation log on every install",
    ]
    # Repeat for seamless scroll
    items2 = "".join(f"<span>{x}</span>" for x in (items*2))
    return f'<div class="ticker"><div class="ticker-inner">{items2}</div></div>'

# Reviews section (drop in any page)
def reviews_section(limit=6, headline=None):
    headline = headline or "What homeowners actually say."
    cards = ""
    for r in REVIEWS[:limit]:
        stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
        cards += f'''<article class="review-card">
  <div class="review-quote-mark">&ldquo;</div>
  <div class="review-stars" aria-label="{r["rating"]} out of 5 stars">{stars}</div>
  <p class="review-text">{r["text"]}</p>
  <div class="review-meta">
    <span class="review-author">{r["name"]}</span>
    <span class="review-where">{r["city"]}, FL · {r["service"]}</span>
    <span class="review-verified">● Verified Google Review · {r["date"]}</span>
  </div>
</article>'''
    return f'''<section class="reviews-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">06</div>
      <div class="section-head-meta">
        <span class="mono-label">Reviews · Tampa Bay Homeowners</span>
        <h2>{headline}</h2>
      </div>
    </div>
    <div class="reviews-rating-bar">
      <span>● Google Verified</span>
      <span class="stars">★★★★★</span>
      <strong>{BUSINESS["rating"]}</strong>
      <span>from {BUSINESS["review_count"]} reviews · 100% 5-star</span>
      <a href="{BUSINESS["google_profile"]}" target="_blank" rel="noopener" style="color:var(--orange);text-decoration:underline">View on Google →</a>
    </div>
    <div class="reviews-grid">{cards}</div>
  </div>
</section>'''

# 47-point checklist section (used on every service-city page + service hub)
def checklist_section(city_name=None, service_name=None):
    title_city = f" for {city_name} Homes" if city_name else ""
    if service_name:
        intro_text = f"Every {service_name.lower()} install passes all 47 points before we sign off. You get a printed copy at handover."
    else:
        intro_text = "Every install passes all 47 points before we sign off. You get a printed copy at handover."
    cards = ""
    for c in CHECKLIST["categories"]:
        items_html = "".join(f"<li>{it}</li>" for it in c["items"])
        cards += f'''<article class="checklist-card">
  <header class="checklist-card-head">
    <span class="ck-num">{c["icon"]}</span>
    <strong>{c["title"]}</strong>
    <span class="ck-count">{len(c["items"])} pts</span>
  </header>
  <ol>{items_html}</ol>
</article>'''
    return f'''<section class="checklist-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">04</div>
      <div class="section-head-meta">
        <span class="mono-label">The Napa&rsquo;s Standard</span>
        <h2>Our 47-Point Installation Checklist<em>{title_city}</em></h2>
        <div class="section-head-text"><p>{intro_text}</p></div>
      </div>
    </div>
    <div class="checklist-grid">{cards}</div>
  </div>
</section>'''

# Neighborhood + ZIP grid section
def neighborhoods_section(city):
    pills = "".join(f'<div class="neighborhood-pill">{n}</div>' for n in city["neighborhoods"])
    zips = "".join(f'<span class="zip-tag">{z}</span>' for z in city["zips"])
    return f'''<section class="neighborhoods-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">05</div>
      <div class="section-head-meta">
        <span class="mono-label">Local Coverage · {city["county"]}</span>
        <h2>Where we work in <em>{city["name"]}</em>.</h2>
        <div class="section-head-text"><p>We serve every neighborhood, subdivision, and ZIP code in {city["name"]} and the surrounding {city["county"]} corridor. If your community isn&rsquo;t listed below, it just means we haven&rsquo;t worked there yet — call and we&rsquo;ll quote it.</p></div>
      </div>
    </div>
    <div class="neighborhood-grid">{pills}</div>
    <div class="zips-bar">
      <span class="zips-bar-label">ZIPs served</span>
      {zips}
    </div>
  </div>
</section>'''

# FAQ section with details/summary
def faq_section(faqs, headline=None, label="FAQ · Frequently Asked"):
    headline = headline or "Questions homeowners actually ask."
    items = ""
    for q, a in faqs:
        items += f'<details><summary>{q}</summary><div class="faq-body"><p>{a}</p></div></details>'
    return f'''<section class="faq-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">07</div>
      <div class="section-head-meta">
        <span class="mono-label">{label}</span>
        <h2>{headline}</h2>
      </div>
    </div>
    <div class="faq-list">{items}</div>
  </div>
</section>'''

# ============================================================================
# JSON-LD SCHEMA builders
# ============================================================================
def schema_organization():
    same_as = [x for x in [BUSINESS["google_profile"], BUSINESS["facebook"], BUSINESS["instagram"], BUSINESS["yelp"], BUSINESS["thumbtack"], BUSINESS["angi"], BUSINESS["houzz"], BUSINESS["bbb"]] if x]
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": BUSINESS["name"],
        "alternateName": BUSINESS["legal_name"],
        "url": SITE,
        "logo": {"@type":"ImageObject","url":f"{SITE}/images/logo.png","width":600,"height":400},
        "image": f"{SITE}/images/og-default.jpg",
        "telephone": BUSINESS["phone"],
        "email": BUSINESS["email"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": BUSINESS["city"],
            "addressRegion": BUSINESS["state"],
            "postalCode": BUSINESS["zip"],
            "addressCountry": BUSINESS["country"],
        },
        "geo": {"@type":"GeoCoordinates","latitude":BUSINESS["lat"],"longitude":BUSINESS["lng"]},
        "areaServed": [{"@type":"City","name":c["name"]} for c in CITIES.values()],
        "sameAs": same_as,
        "aggregateRating": {
            "@type":"AggregateRating",
            "ratingValue":BUSINESS["rating"],
            "reviewCount":str(BUSINESS["review_count"]),
            "bestRating":"5",
            "worstRating":"1",
        },
        "openingHoursSpecification": [
            {"@type":"OpeningHoursSpecification","dayOfWeek":d,"opens":o,"closes":c}
            for d,o,c in BUSINESS["hours"]
        ],
        "priceRange": "$$",
        "foundingDate": str(BUSINESS["year_founded"]),
        "description": BUSINESS["tagline_long"],
    }

def schema_local_business(page_url, page_name, city=None, service=None, image=None):
    image = image or f"{SITE}/images/og-default.jpg"
    desc = page_name
    if service and city:
        desc = f"{service} contractor in {city}, FL. {BUSINESS['tagline_long']}"
    elif service:
        desc = f"{service} services across Tampa Bay and Sarasota. {BUSINESS['tagline_long']}"
    elif city:
        desc = f"Flooring contractor in {city}, FL. {BUSINESS['tagline_long']}"
    return {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": page_url + "#business",
        "name": BUSINESS["name"],
        "url": page_url,
        "telephone": BUSINESS["phone"],
        "email": BUSINESS["email"],
        "image": image,
        "description": desc,
        "address": {
            "@type":"PostalAddress",
            "addressLocality": city or BUSINESS["city"],
            "addressRegion": BUSINESS["state"],
            "postalCode": BUSINESS["zip"] if not city else "",
            "addressCountry": BUSINESS["country"],
        },
        "geo": {"@type":"GeoCoordinates","latitude":BUSINESS["lat"],"longitude":BUSINESS["lng"]},
        "areaServed": {"@type":"City","name":city} if city else [{"@type":"City","name":c["name"]} for c in CITIES.values()],
        "aggregateRating":{"@type":"AggregateRating","ratingValue":BUSINESS["rating"],"reviewCount":str(BUSINESS["review_count"]),"bestRating":"5"},
        "priceRange":"$$",
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":d,"opens":o,"closes":c} for d,o,c in BUSINESS["hours"]],
    }

def schema_breadcrumb(items):
    """items: list of (name, url). LAST one's url is page url."""
    return {
        "@context":"https://schema.org",
        "@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":i+1,"name":name,"item":url}
            for i,(name,url) in enumerate(items)
        ],
    }

def schema_faqpage(faqs):
    return {
        "@context":"https://schema.org",
        "@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
            for q,a in faqs
        ],
    }

def schema_article(post, canonical):
    return {
        "@context":"https://schema.org",
        "@type":"Article",
        "headline": post["title"],
        "description": post["meta_desc"],
        "image": f"{SITE}/images/og-default.jpg",
        "datePublished": post["date_published"],
        "dateModified": post["date_modified"],
        "author":{"@type":"Organization","name":BUSINESS["name"]},
        "publisher":{
            "@type":"Organization",
            "name":BUSINESS["name"],
            "logo":{"@type":"ImageObject","url":f"{SITE}/images/logo.png"},
        },
        "mainEntityOfPage":{"@type":"WebPage","@id":canonical},
        "articleSection":post.get("category","Flooring"),
    }

def schema_webpage(canonical, name, desc):
    return {
        "@context":"https://schema.org",
        "@type":"WebPage",
        "@id":canonical,
        "url":canonical,
        "name":name,
        "description":desc,
        "isPartOf":{"@id":f"{SITE}/#website"},
    }

def schema_website():
    return {
        "@context":"https://schema.org",
        "@type":"WebSite",
        "@id":f"{SITE}/#website",
        "url":SITE,
        "name":BUSINESS["name"],
        "publisher":{"@id":f"{SITE}/#organization"},
        "inLanguage":"en-US",
    }

def schema_service(service, city=None, canonical=None):
    desc = service["intro_lead"]
    name = service["name"]
    if city:
        name = f"{service['name']} in {city}, FL"
    return {
        "@context":"https://schema.org",
        "@type":"Service",
        "serviceType": service["name"],
        "name": name,
        "description": desc,
        "provider":{"@id":f"{SITE}/#organization"},
        "areaServed": {"@type":"City","name":city} if city else [{"@type":"City","name":c["name"]} for c in CITIES.values()],
        "url": canonical or SITE,
    }

# ============================================================================
# WRAPPER — full HTML page (combines everything)
# ============================================================================
def wrap_page(head_html, header_html, body_html, footer_html=None, breadcrumbs_html="", float_html=None):
    footer_html = footer_html if footer_html is not None else footer()
    float_html = float_html if float_html is not None else FLOAT_CONTACT
    return f'''{head_html}<body>
{header_html}
{breadcrumbs_html}
<main>
{body_html}
</main>
{footer_html}
{float_html}
{MENU_JS}
</body>
</html>'''

# Convenience: full page builder for the homepage and most pages
def write_page(filepath, head_html, header_html, body_html, footer_html=None, breadcrumbs_html="", float_html=None):
    import os
    html = wrap_page(head_html, header_html, body_html, footer_html=footer_html, breadcrumbs_html=breadcrumbs_html, float_html=float_html)
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath
