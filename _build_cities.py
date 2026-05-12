#!/usr/bin/env python3
"""Generate /[city]/ hub pages — one per city in CITIES."""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

# ============================================================================
# City-specific FAQ generator
# ============================================================================
def city_faqs(city):
    """Returns a list of (q, a) tuples — 6 city-specific Q&As."""
    name = city["name"]
    cnty = city["county"]
    neigh_sample = city["neighborhoods"][:3]
    primary = city["primary_market"]
    humid = city["humidity_note"]

    return [
        (f"How much does flooring installation cost in {name}, FL?",
         f"Pricing in {name} runs the same range as the rest of our Tampa Bay service area: budget LVP and laminate jobs land in the $2&ndash;$4 per square foot installed range, mid-range engineered hardwood and premium SPC vinyl plank in the $5&ndash;$9 range, and high-end European white oak hardwood, large-format porcelain, and natural stone in the $10&ndash;$22 range. {name}-specific factors that affect pricing are travel time from our {BUSINESS['city']} home base (minimal, since we serve {cnty} regularly), subfloor condition (older homes in {name} sometimes require self-leveling; newer slab homes typically don&rsquo;t), and material delivery logistics. You&rsquo;ll get a written, line-itemized quote within 24 hours of the in-home measure &mdash; no &lsquo;starting at&rsquo; language, no hidden change orders."),
        (f"How long does an install take in {name}?",
         f"Typical timelines for {name} homes: 2&ndash;3 working days for a 1,000&ndash;1,500 sq ft floating LVP or laminate install; 3&ndash;4 days for the same size engineered hardwood; 5&ndash;8 days for tile (mortar cure time is the long pole); 2&ndash;3 days for a standard 14-tread staircase. Whole-home reflooring jobs in 2,500&ndash;4,000 sq ft homes in {name} (common in {neigh_sample[0]} and {neigh_sample[1]}) typically run 8&ndash;14 working days. The real schedule lives in your written quote, not in this paragraph."),
        (f"Do you actually live and work in {name}?",
         f"Our crew is based in east {BUSINESS['city']}, in the 34212 ZIP just south of SR-64 &mdash; about a 10&ndash;25 minute drive from anywhere in {name}, depending on which neighborhood. We work {name} every week. We know the gated-community access protocols at {neigh_sample[0]}, the HOA flooring rules at {neigh_sample[1]}, and the dumpster restrictions for {neigh_sample[2]}. We&rsquo;re not driving in from Tampa or Sarasota for the work &mdash; we&rsquo;re local."),
        (f"Why does {name} need different prep than other Florida cities?",
         f"{humid} The bigger picture: {primary.lower()}. That dictates the products we recommend, the prep we do, and the timeline we quote. The same square footage in two different {name} neighborhoods can have completely different prep requirements &mdash; a 1965 ranch in {city['neighborhoods'][-2] if len(city['neighborhoods']) > 1 else city['neighborhoods'][0]} needs subfloor leveling and a vapor barrier; a 2022 build in {neigh_sample[0]} usually needs neither. We catch all of that at the in-home measure."),
        (f"Do you handle HOA-managed communities in {name}?",
         f"Yes. Most of the gated and master-planned communities in {name} (including {neigh_sample[0]}, {neigh_sample[1]}, and {neigh_sample[2]}) have specific HOA rules around flooring installs &mdash; weekday-only work, quiet hours, dumpster placement, access through gate codes, and floor-type restrictions in second-floor condos. We&rsquo;ve worked in most of them and we know the playbook. We&rsquo;ll handle the HOA communication if you want us to, or just give us the gate code and we&rsquo;ll work within the rules."),
        (f"Can you start a {name} job within the week?",
         f"Sometimes &mdash; depends on the size of the job and our current schedule. Small jobs (single rooms, staircases, repair work) can often start within 5&ndash;7 days of the signed estimate, especially during the slower summer season. Larger whole-home installs typically book 3&ndash;6 weeks out, sometimes more during peak season (November through April). Material lead times are the other variable: most LVP and laminate is in stock at our suppliers within 48 hours; engineered hardwood from European mills can be 2&ndash;6 weeks. We&rsquo;ll give you the real start date in the quote."),
    ]

# ============================================================================
# City-specific "why this city" content section
# ============================================================================
def city_why_here(city):
    name = city["name"]
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label">{city["county"]} · {city["population"]}</span>
        <h2>Why flooring in <em>{name}</em> isn&rsquo;t the same as anywhere else.</h2>
        <div class="section-head-text"><p>{city["growth"]}. The flooring market here has its own dynamics.</p></div>
      </div>
    </div>

    <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:50px;align-items:start;max-width:1100px;margin:0 auto">
      <div class="intro-prose" style="margin:0">
        <p>{city["context"]}</p>

        <p><strong>Humidity reality:</strong> {city["humidity_note"]}</p>

        <p><strong>Primary market we serve:</strong> {city["primary_market"]}. Most {name} flooring conversations are some version of one of those scenarios &mdash; and the right product, the right prep, and the right timeline depend on which one your home falls into.</p>

        <p><strong>Trade and permitting:</strong> {city["trade_class"]}. We work this jurisdiction every week and we know what passes, what flags, and what the inspectors actually look for.</p>
      </div>

      <aside style="background:var(--paper-deep);padding:32px 28px;border-left:6px solid var(--orange)">
        <span class="mono-label">{name} Quick Facts</span>
        <dl style="margin-top:1.2rem;display:flex;flex-direction:column;gap:.8rem;font-family:var(--font-mono);font-size:.85rem">
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">County</dt><dd style="font-weight:600;text-align:right">{city["county"]}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">Population</dt><dd style="font-weight:600;text-align:right">{city["population"]}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">Growth</dt><dd style="font-weight:600;text-align:right">{city["growth"]}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">ZIPs Served</dt><dd style="font-weight:600;text-align:right">{len(city["zips"])}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">Coordinates</dt><dd style="font-weight:600;text-align:right;font-size:.78rem">{city["lat"]}, {city["lng"]}</dd></div>
        </dl>
        <p style="margin-top:1.4rem;font-family:var(--font-body);font-size:.92rem;color:var(--gray);line-height:1.55;font-style:normal"><em>Landmarks nearby:</em> {city["landmarks"]}.</p>
      </aside>
    </div>
  </div>
</section>'''

# ============================================================================
# Services grid filtered by city (each links to /service/city/)
# ============================================================================
def city_services_grid(city):
    name = city["name"]
    slug = city["slug"]
    cards = ""
    for sslug in SERVICE_ORDER:
        s = SERVICES[sslug]
        cards += f'''<a href="/{sslug}/{slug}/" class="service-card">
  <div class="service-card-num">{s["icon"]} / {s["short"]}</div>
  <h3>{s["short"]} in {name}</h3>
  <p class="service-card-desc">{s["intro_lead"]}</p>
  <span class="service-card-cta">See {s["short"]} · {name}</span>
</a>'''
    return f'''<section class="services-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label">Six services · {name}, FL</span>
        <h2>Every floor we install,<br><em>installed in {name}</em>.</h2>
        <div class="section-head-text"><p>Hardwood, vinyl plank, tile, laminate, stair treads, repair &mdash; pick what you&rsquo;re after. Each service page has {name}-specific pricing, scope, and FAQ.</p></div>
      </div>
    </div>
    <div class="services-grid">{cards}</div>
  </div>
</section>'''

# ============================================================================
# Filter reviews for city (best matches first)
# ============================================================================
def city_reviews(city, count=6):
    name = city["name"]
    matched = [r for r in REVIEWS if r["city"] == name]
    others = [r for r in REVIEWS if r["city"] != name]
    final = matched + others
    cards = ""
    for r in final[:count]:
        stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
        cards += f'''<article class="review-card">
  <div class="review-quote-mark">&ldquo;</div>
  <div class="review-stars" aria-label="{r["rating"]} of 5 stars">{stars}</div>
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
        <span class="mono-label">Reviews · {name} &amp; Tampa Bay</span>
        <h2>From {name} homeowners and their <em>neighbors</em>.</h2>
      </div>
    </div>
    <div class="reviews-rating-bar">
      <span>● Google Verified</span>
      <span class="stars">★★★★★</span>
      <strong>{BUSINESS["rating"]}</strong>
      <span>from {BUSINESS["review_count"]} reviews</span>
      <a href="{BUSINESS["google_profile"]}" target="_blank" rel="noopener" style="color:var(--orange);text-decoration:underline">View on Google →</a>
    </div>
    <div class="reviews-grid">{cards}</div>
  </div>
</section>'''

# ============================================================================
# Related city links + related posts (cross-link)
# ============================================================================
def city_related_box(city):
    slug = city["slug"]
    name = city["name"]
    # Other cities
    other_links = "".join(
        f'<li><a href="/{s}/">{c["name"]}, FL</a></li>'
        for s, c in CITIES.items() if s != slug
    )
    # Cost blog posts for this city
    cost_posts = [p for p in COST_BLOG_POSTS if p["city_slug"] == slug]
    blog_links = "".join(
        f'<li><a href="/blog/{p["slug"]}/">{p["title"]}</a></li>'
        for p in cost_posts
    )
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px">
      <div class="related-box">
        <div class="related-box-label">Read Next · Other Cities</div>
        <h3>We also work nearby.</h3>
        <ul>{other_links}</ul>
      </div>
      <div class="related-box">
        <div class="related-box-label">Read Next · {name} Cost Guides</div>
        <h3>What it actually costs in {name}.</h3>
        <ul>{blog_links}</ul>
      </div>
    </div>
  </div>
</section>'''

# ============================================================================
# Build one city page
# ============================================================================
def build_city(slug):
    city = CITIES[slug]
    name = city["name"]
    URL = f"{SITE}/{slug}/"

    # SEO
    TITLE_RAW = f"Flooring Contractor {name} FL · Napa's Flooring 5★"
    TITLE = TITLE_RAW[:65]
    DESC = (
        f"Flooring installation in {name}, FL — hardwood, vinyl plank, tile, laminate, "
        f"stair treads. {len(city['neighborhoods'])}+ neighborhoods served. "
        f"5★ Google · 47-point standard · 12-month warranty."
    )[:158]

    faqs = city_faqs(city)
    schemas = [
        schema_local_business(URL, f"Flooring in {name}, FL", city=name),
        schema_faqpage(faqs),
        schema_breadcrumb([("Home", SITE+"/"), (f"{name}, FL", URL)]),
        schema_webpage(URL, TITLE, DESC),
    ]
    bc = breadcrumbs([("Home","/"), (f"{name}, FL", None)])

    # HERO
    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">{city["county"]} · {len(city["zips"])} ZIPs · {len(city["neighborhoods"])}+ neighborhoods</span>
    <h1>Flooring contractor.<br><em>{name}<span class="stop">,</span></em> Florida.</h1>
    <p class="page-hero-sub">Hardwood, vinyl plank, tile, laminate &amp; stair treads &mdash; installed by hand, acclimated for Florida humidity, finished to spec. {city["context_short"]}</p>
    <div class="page-hero-trust">
      <span>{len(city["neighborhoods"])}+ {name} neighborhoods</span>
      <span>{BUSINESS["unique_stat_full"]}</span>
      <span>{BUSINESS["rating"]}★ · {BUSINESS["review_count"]} reviews</span>
      <span>Free estimate in 24 hrs</span>
    </div>
  </div>
</section>'''

    # INTRO (numbered 01)
    intro = f'''<section style="background:var(--paper-deep)" id="intro">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">{name} · Service Profile</span>
        <h2>Local flooring crew. <em>Real {name} addresses.</em></h2>
      </div>
    </div>
    <div class="intro-prose">
      <p><strong>Napa&rsquo;s Flooring</strong> has been installing floors in {name} since {BUSINESS["year_founded"]} &mdash; from the gated golf communities along {city["neighborhoods"][0]} and {city["neighborhoods"][1] if len(city["neighborhoods"]) > 1 else city["neighborhoods"][0]}, to the older single-family homes off the main corridors, to the new construction in {city["neighborhoods"][-1]}. We are a small, deliberately small crew based in east {BUSINESS["city"]}, in the 34212 ZIP, with a tight Tampa Bay service radius that includes every part of {name}, {city["county"]}, and the surrounding corridor.</p>

      <p>Our specialty in {name} is the same as everywhere we work: <strong>installation done to manufacturer spec, on subfloors that are actually prepared, by the same two installers from estimate to walkthrough.</strong> We don&rsquo;t subcontract, we don&rsquo;t outsource the demo crew, we don&rsquo;t hire a 1099 finish crew at the end &mdash; the two people who measure your {name} home for the estimate are the two people who finish the work, including the final coat of caulk on the baseboard.</p>

      {stat_badge()}

      <p>Every install in {name} passes our <a href="#checklist">47-point installation standard</a> &mdash; published, printed, signed off, and handed to you on closeout. {city["humidity_note"]} The 47 points are how we make sure that doesn&rsquo;t happen on a Napa&rsquo;s job.</p>
    </div>
  </div>
</section>'''

    # WHY THIS CITY (02)
    why_here = city_why_here(city)

    # SERVICES GRID (03)
    services_grid_html = city_services_grid(city)

    # CHECKLIST (04)
    checklist_html = checklist_section(city_name=name)

    # NEIGHBORHOODS (05)
    neigh_html = neighborhoods_section(city)

    # REVIEWS (06)
    reviews_html = city_reviews(city, count=6)

    # FAQ (07)
    faq_html = faq_section(faqs, headline=f"Questions {name} homeowners ask, weekly.", label=f"FAQ · {name}, FL")

    # RELATED LINKS
    related_html = city_related_box(city)

    # FINAL CTA
    final_html = final_cta(
        headline=f"Ready for a real estimate, on a real {name} home?",
        sub=f"Free in-home measure within 24&ndash;48 hours. Written, line-itemized quote within 24 hours of the visit. No high-pressure sales, no obligation."
    )

    body = "\n".join([hero, intro, why_here, services_grid_html, checklist_html, neigh_html, reviews_html, faq_html, related_html, f'<div class="container">{contact_banner()}</div>', final_html])

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page(f"/home/claude/napas/{slug}/index.html", head_html, header(active="areas"), body, breadcrumbs_html=bc)
    print(f"Wrote /{slug}/index.html")


if __name__ == "__main__":
    for slug in CITIES:
        build_city(slug)
    print(f"\nBuilt {len(CITIES)} city hub pages.")
