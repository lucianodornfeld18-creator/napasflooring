#!/usr/bin/env python3
"""Generate /[service]/ hub pages + /[service]/[city]/ pages."""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

# ============================================================================
# 5 COMMON MISTAKES — one set per service (unique wording, used across cities)
# ============================================================================
MISTAKES_BY_SERVICE = {
    "hardwood-flooring": [
        ("Buying solid hardwood for a slab home.",
         "Solid hardwood needs to be nailed or stapled to a wood subfloor. Most Florida homes built after 1980 sit on a concrete slab &mdash; full stop, no exceptions. Installing solid hardwood on a slab requires either a sleeper system (3/4-inch plywood floated over the slab, gluing down to that), or a glue-down floor that the manufacturer doesn&rsquo;t actually warrant. The honest answer in Florida is engineered hardwood, almost always. We&rsquo;ll show you side-by-side samples of solid and engineered at the estimate and you genuinely cannot tell them apart after install."),
        ("Skipping the acclimation period.",
         "Outdoor Florida humidity in summer averages 75&ndash;85% RH; your air-conditioned home interior averages 45&ndash;55% RH. Hardwood that&rsquo;s installed straight off the delivery truck &mdash; without 48&ndash;72 hours of on-site acclimation in your conditioned space &mdash; is going to lose moisture, shrink, and gap by month four. We acclimate every plank for at least 72 hours with a digital hygrometer running, and we hand you the printed log on closeout."),
        ("Trusting a finisher who skips the moisture meter.",
         "Every plank gets a pin-meter reading before install, every subfloor gets a calcium chloride or in-situ RH probe, and both numbers go on the install record. The number-one cause of hardwood floor failure in Florida isn&rsquo;t the wood &mdash; it&rsquo;s the substrate. A finisher who can&rsquo;t show you moisture readings isn&rsquo;t a finisher; he&rsquo;s an installer who hopes the moisture problem stays hidden."),
        ("Picking species without considering hardness.",
         "Florida homes get sand-tracked-in traffic constantly, especially Gulf Coast homes within a few miles of the beach. Softer species (American walnut, hickory&rsquo;s softer cousins like alder) scratch easily. White oak, red oak, and hard maple all rate 1,290&ndash;1,450 on the Janka scale &mdash; harder than most species, and what we install most often for Tampa Bay primary residences. Beauty is half of it; the other half is whether the floor still looks like you wanted it to in year three."),
        ("Buying labor on price alone.",
         "Hardwood installation labor varies wildly because installation quality varies wildly. The lowest bid almost always means subcontracted labor, no real acclimation, no documented moisture readings, and no warranty. The same hardwood floor installed badly versus installed properly can have a ten-year vs. thirty-year lifespan. We&rsquo;ve been hired to redo at least a dozen hardwood floors that were installed by lowest-bid crews within the previous 24 months. Pay for the install, save on the rework you don&rsquo;t have to do."),
    ],
    "vinyl-plank-flooring": [
        ("Buying the cheapest LVP at the big-box.",
         "There are two kinds of LVP at retail: $1.50&ndash;$2.50 per square foot product (thin wear layer, repeating visuals, soft core that telegraphs every imperfection in the subfloor below) and $4&ndash;$7 per square foot product (20&ndash;22 mil wear layer, dozens of unique plank visuals, dense SPC core that hides minor subfloor imperfections). The first one looks fake from 6 feet, scratches when your dog walks across it in nail guards, and shows seam separation by year three. The second one reads as real wood from 10 feet and lasts the warranty. Spend the extra $2&ndash;$3 per square foot. It&rsquo;s the same labor either way."),
        ("Glue-down on a slab with no moisture barrier.",
         "Concrete slabs in Florida can pull moisture from the soil below them at rates above 5 lbs per 1,000 sq ft per 24 hours &mdash; well above what most LVP glue can tolerate long-term. If you&rsquo;re glue-down installing on a slab, the slab needs a documented calcium chloride moisture reading, and a vapor barrier under the adhesive if the reading is borderline. Skip that step, and you&rsquo;re looking at adhesive failure, plank lift, and bubbles at the 3-year mark. Every glue-down slab job we do gets a calcium chloride test before adhesive touches the floor."),
        ("Skipping the underlayment on a click-lock install.",
         "Cheap click-lock LVP without an underlayment over a slab telegraphs every imperfection: that minor dip you can&rsquo;t even see with the naked eye will sound hollow underfoot, the plank edges will deflect when you step on them, and over 18&ndash;24 months the click-lock joints will wear out at the high-traffic spots. A 1.5mm closed-cell foam underlayment costs $0.40&ndash;$0.75 per square foot, lasts the life of the floor, and is the difference between a floor that feels solid and a floor that feels cheap. Always include it on slab installs."),
        ("Believing &lsquo;waterproof&rsquo; means &lsquo;flood-proof&rsquo;.",
         "LVP is genuinely waterproof through the core &mdash; you can submerge a plank for days and it won&rsquo;t swell. What it isn&rsquo;t is flood-proof: standing water against a baseboard for 24+ hours will still get into the wall cavity behind the floor through the expansion gap. The plank itself stays fine; the structure behind it doesn&rsquo;t. Treat &lsquo;waterproof flooring&rsquo; as a forgiveness factor against minor spills and pet accidents, not as a license to ignore an active leak."),
        ("Installing over an old floor without removing the old floor.",
         "Two scenarios where this looks tempting: existing sheet vinyl that&rsquo;s flat, or existing ceramic tile that&rsquo;s relatively flat. Skipping the removal saves a day of labor and several hundred dollars. It also locks you in: the new floor height adds 5&ndash;6mm to every doorway transition, every appliance kickplate, every toilet flange. We pull old flooring on almost every install, all the way down to the subfloor, because that&rsquo;s how the new floor ends up at the height it was supposed to be."),
    ],
    "tile-installation": [
        ("Using the wrong setting mortar for the tile size.",
         "TCNA spec is explicit: tile under 15 inches uses standard modified thinset mortar (medium bed at most); tile 15 inches and larger requires a large-format / medium-bed (LFT/MB) mortar applied at 1/4-inch trowel notch minimum, back-buttered. Using standard thinset under a 24x48 large-format tile is the number-one cause of hollow spots and lippage on premium tile installs. The mortar matters more than the brand of tile."),
        ("Skipping the crack-isolation membrane on a slab.",
         "Florida slabs crack. They always do, eventually &mdash; from settlement, from temperature cycling, from the soil shifting underneath. A tile floor installed directly on a slab will crack along the same lines as the slab below it. A Schluter Ditra or equivalent crack-isolation membrane decouples the tile floor from the slab, so a hairline crack in the concrete doesn&rsquo;t telegraph through to a $15 per square foot porcelain tile. Skipping the membrane saves $2.50&ndash;$4 per square foot. Re-tiling the floor after a crack costs $12&ndash;$18 per square foot."),
        ("Letting the original installer build the shower waterproofing.",
         "The old-school method (tar paper plus wire-lath mud bed plus a clamping drain) still passes code in some jurisdictions but has dozens of failure points. We exclusively install bonded sheet-membrane systems (Schluter Kerdi) or foam-panel systems (Wedi). Both are dramatically more reliable, easier to inspect, and what we put on every shower job. The vast majority of catastrophic bathroom failures we get called to fix trace back to a shower that was waterproofed with the old method, badly, by someone who didn&rsquo;t know what they were doing."),
        ("Choosing tile that&rsquo;s rated for walls in a floor application.",
         "Tile carries a PEI rating (Porcelain Enamel Institute) for surface hardness. PEI 1 is wall-only. PEI 2 is light residential floor traffic. PEI 3 and 4 are most residential floor applications. PEI 5 is commercial. Florida sand is abrasive; we recommend PEI 4 minimum for any floor application. A pretty wall tile installed on a floor will scratch and dull in the high-traffic lines within 12&ndash;18 months."),
        ("Picking grout without thinking about maintenance.",
         "Cement-based sanded grout is cheap, easy to install, and stains permanently with any prolonged moisture contact. Urethane grout (Bostik TruColor, Mapei Flexcolor CQ) is stain-resistant, flexible, and costs about 3&times; per pound &mdash; but you spend nothing on grout sealing for the life of the floor. Epoxy grout is the gold standard for kitchens, bathrooms, and any wet-area floor. For premium tile jobs (over $10 per square foot installed), we almost always specify urethane or epoxy. The grout outlives the tile if you pick the right one."),
    ],
    "laminate-flooring": [
        ("Buying AC3 laminate for high-traffic residential.",
         "Laminate carries an AC rating (Abrasion Class) from AC1 (light residential, hallways) through AC5 (commercial). AC3 is the standard at most retail price points, and it&rsquo;s rated for moderate residential traffic &mdash; bedrooms, dens, light-use living rooms. For high-traffic residential (kitchens, mudrooms, anywhere a pet runs daily), step up to AC4 or AC5. The cost difference is $0.50&ndash;$1.50 per square foot; the lifespan difference is roughly double. We specify AC4 minimum for any primary living-area install."),
        ("Installing without a vapor barrier on a slab.",
         "Laminate is wood-based at the core (high-density fiberboard, HDF) &mdash; which means it swells if it absorbs moisture. Florida slabs always carry some moisture, even when they look dry. A 6-mil polyethylene vapor barrier underlayment (or an underlayment with an attached vapor barrier) is non-negotiable on slab installs. Skipping it isn&rsquo;t a money-saver; it&rsquo;s a 5-year guarantee that your floor will lift and gap."),
        ("Picking laminate for kitchens or full baths.",
         "Modern laminate is humidity-tolerant up to a point; it isn&rsquo;t waterproof. A dishwasher leak that runs for 4 hours, a clogged sink that overflows, a child&rsquo;s bath that splashes water onto the floor for weeks &mdash; any of those will swell the HDF core at the seams. For kitchens and full baths in Florida, we recommend SPC vinyl plank instead. For bedrooms, living rooms, and home offices on plywood subfloors, AC4 laminate is fine."),
        ("Skipping the 3/8-inch expansion gap.",
         "Every floating floor needs an expansion gap at every wall, every fixed object, every doorway transition. Laminate manufacturers spec 3/8-inch minimum &mdash; not 1/4-inch, not &lsquo;just snug.&rsquo; Skipping the gap means the floor can&rsquo;t expand when seasonal humidity rises, and it buckles in the middle of the room. We measure and maintain the gap on every wall, every install, no exceptions."),
        ("Confusing &lsquo;laminate&rsquo; with &lsquo;LVP&rsquo; at the showroom.",
         "Half the customers walking into a flooring showroom are talking about laminate when they mean LVP, or LVP when they mean laminate. They&rsquo;re completely different products. Laminate has an HDF wood core, isn&rsquo;t waterproof, costs less, and feels more like real wood underfoot. LVP has a plastic or stone-plastic composite core, is fully waterproof, costs slightly more, and is more forgiving on uneven subfloors. We&rsquo;ll bring samples of both to your estimate and let you feel the difference before you commit."),
    ],
    "stair-treads": [
        ("Trying to refinish carpet-stained pine treads.",
         "Most older homes have construction-grade pine or fir stair treads under the carpet, intended to be hidden permanently. They&rsquo;ll often be stained from carpet adhesive, sticker residue, and pet accidents. Refinishing them looks tempting but rarely produces a result you&rsquo;re happy with. Replacement with proper 5/4 hardwood or LVP treads is almost always the right call &mdash; better finish, longer life, dramatically better look."),
        ("Skipping the riser detail.",
         "A riser is the vertical face between each tread. White-painted poplar risers are the cheapest option ($35&ndash;$55 each installed) and the default we recommend for most jobs. Stain-matched hardwood risers (matching the tread species) cost more ($60&ndash;$95 each) and look spectacular, but only make visual sense on certain stair designs &mdash; primarily open staircases visible from below. Mid-traffic staircases against a wall almost always look best with white risers."),
        ("Ignoring the return-nose detail on open-side stairs.",
         "An &lsquo;open-side&rsquo; staircase has at least one side that&rsquo;s visible (not against a wall). The tread on that side needs a 1-inch return-nose detail where the nosing wraps the open side &mdash; otherwise you see raw end-grain at every tread, which looks unfinished. Return-nose work is meticulous carpentry; we charge an extra $20&ndash;$40 per open-side tread for it, and it&rsquo;s worth every penny on a staircase that&rsquo;s visible from the living room."),
        ("Picking pet-unfriendly finishes.",
         "Pre-finished hardwood and LVP treads are smooth, which means dogs (especially older ones) can slip on them. We install clear silicone grip strips 1 inch back from the tread nose on request &mdash; nearly invisible from standing height, and a real difference for pets&rsquo; traction. Specify this at the estimate if you have pets and we&rsquo;ll include them at no extra labor charge."),
        ("Mismatching the tread species to the existing floor.",
         "If your downstairs floor is engineered hardwood from a specific manufacturer, source matching treads from that manufacturer. If your floor is site-finished solid hardwood, we&rsquo;ll bring sample treads in the same species and stain-match on-site. The transition between a $9 per square foot engineered floor and an off-the-shelf prefinished tread is the giveaway on a budget stair-tread job. We always specify treads to match."),
    ],
    "floor-repair": [
        ("Waiting to call after water damage.",
         "Water damage in flooring is a clock-running problem. Within 24 hours, the subfloor begins absorbing moisture from above and below; within 48 hours, mold growth typically starts in the right humidity conditions; within 72 hours, the structural integrity of plywood subfloor sheathing can be compromised. Call us within 24 hours of any active water issue &mdash; we&rsquo;ll come out same-day or next-day to assess, take baseline moisture readings, document for insurance, and start drying."),
        ("Letting the wrong contractor &lsquo;match&rsquo; replacement planks.",
         "A bad plank-replacement match (wrong species, wrong width, wrong sheen, wrong cut) is visible from across the room and ruins the look of an otherwise good floor. We source matching planks from the original manufacturer when possible, from period-correct alternates when not, and we feather the install (staggering joints into the existing field, lacing planks two rows deep) so the transition is invisible. Most plank repairs we do can&rsquo;t be found visually after we&rsquo;re done."),
        ("Trying to refinish over old finish without proper sanding.",
         "A &lsquo;screen and recoat&rsquo; (lightly abrading the existing finish and adding a fresh coat) is appropriate for floors with only surface wear and no deep scratches or stain damage. For floors with real wear, repeated scratches, pet damage, or graying around water exposure points, a full sand-and-refinish is required &mdash; three sandings (coarse, medium, fine), proper grain-raise, and three fresh poly coats. Skipping the full sand on a floor that needs it leaves visible wear lines under the new finish."),
        ("Treating a sagging subfloor as a finish-floor problem.",
         "A floor that bounces underfoot or shows a visible dip across a room isn&rsquo;t a finish-flooring problem &mdash; it&rsquo;s a structural subfloor problem. Pulling the finish floor and re-laying it over the same sagging subfloor produces the same problem in 12 months. The right repair is to lift the finish floor, sister the underlying joists or patch the subfloor plywood, and then re-lay. We&rsquo;ll do this on repair calls when it&rsquo;s the right call &mdash; even though it doubles the labor."),
        ("Ignoring the squeak.",
         "Floor squeaks are caused by relative movement between the finish floor and the subfloor, or between the subfloor and the underlying framing. They almost never &lsquo;heal&rsquo; on their own; they get worse over time as the gap that&rsquo;s producing the friction widens. A &lsquo;squeak survey&rsquo; (walking the floor in a grid, marking every squeak with a piece of painter&rsquo;s tape, and screwing through the finish floor into the framing from above) takes a half-day on a typical home and resolves 90%+ of squeaks permanently. Don&rsquo;t live with the squeak."),
    ],
}

# ============================================================================
# Pricing table builder
# ============================================================================
def pricing_table_html(svc, city_name=None):
    rows = ""
    for label, price, note in svc["pricing_rows"]:
        rows += f'<tr><td>{label}</td><td>{note}</td><td class="price">{price}</td></tr>'
    city_note = f" for {city_name} homes" if city_name else ""
    head_h3 = f'2026 {svc["name"]} pricing<em>{city_note}</em>.'
    return f'''<section class="pricing-section">
  <div class="container">
    <div class="pricing-wrap">
      <header class="pricing-head-bar">
        <h3>{head_h3}</h3>
        <span class="pricing-head-meta">Updated for 2026 · Tampa Bay rates</span>
      </header>
      <table class="pricing-table">
        <thead><tr><th>Tier</th><th>What it&rsquo;s best for</th><th>Installed cost</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
      <div class="pricing-note">All prices include labor, prep, and standard transition trim. Old-floor removal $1.50&ndash;$3/sq ft. <a href="/contact/#quote">Free written quote within 24 hrs →</a></div>
    </div>
  </div>
</section>'''

# ============================================================================
# Scope items list
# ============================================================================
def scope_section(svc):
    items = "".join(f"<li>{x}</li>" for x in svc["scope_items"])
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label">Scope of Work · What&rsquo;s Included</span>
        <h2>What every <em>{svc["name"].lower()}</em> install includes.</h2>
        <div class="section-head-text"><p>Itemized in your quote, executed on the job, signed off at handover. No surprise change orders mid-install.</p></div>
      </div>
    </div>
    <ul style="list-style:none;display:grid;grid-template-columns:repeat(2,1fr);gap:14px 30px;max-width:1080px;margin:0 auto;padding:0;font-size:1rem;line-height:1.5">
      {"".join(f'<li style="display:flex;gap:14px;align-items:flex-start;padding-bottom:14px;border-bottom:1px solid var(--rule)"><span style="font-family:var(--font-display);color:var(--orange);font-size:1.1rem;line-height:1;flex-shrink:0">●</span><span>{x}</span></li>' for x in svc["scope_items"])}
    </ul>
  </div>
</section>'''

# ============================================================================
# 5 MISTAKES section
# ============================================================================
def mistakes_section(service_slug, city_name=None):
    items = MISTAKES_BY_SERVICE.get(service_slug, [])
    rows = ""
    for i, (h, body) in enumerate(items, 1):
        rows += f'''<div class="feature-row">
  <div class="feature-num">{i:02d}</div>
  <div class="feature-body">
    <h3>{h}</h3>
    <p>{body}</p>
  </div>
</div>'''
    title_city = f" in {city_name}" if city_name else ""
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">06</div>
      <div class="section-head-meta">
        <span class="mono-label">After {BUSINESS["unique_stat_number"]} Installs · Hard-Won Lessons</span>
        <h2>Five expensive mistakes flooring buyers make<em>{title_city}</em>.</h2>
        <div class="section-head-text"><p>Every one of these has cost a homeowner real money on a redo. None of them are obvious in advance. All of them are avoidable.</p></div>
      </div>
    </div>
    <div class="features-list">{rows}</div>
  </div>
</section>'''

# ============================================================================
# SERVICE-CITY page builder
# ============================================================================
def build_service_city(service_slug, city_slug):
    svc = SERVICES[service_slug]
    city = CITIES[city_slug]
    URL = f"{SITE}/{service_slug}/{city_slug}/"

    # SEO: Title <65 chars, keyword-first
    short = svc["short"]
    city_name = city["name"]
    TITLE_RAW = f"{short} {city_name} FL | Napa's Flooring 5★"
    TITLE = TITLE_RAW[:65]
    DESC = (
        f"{svc['name']} in {city_name}, FL. Installed by hand · "
        f"acclimated · 47-point standard. {len(city['neighborhoods'])}+ neighborhoods. "
        f"5★ Google · 12-month warranty · free estimate in 24 hrs."
    )[:158]

    schemas = [
        schema_local_business(URL, f"{svc['name']} in {city_name}, FL", city=city_name, service=svc["name"]),
        schema_service(svc, city=city_name, canonical=URL),
        schema_faqpage(svc["faqs"]),
        schema_breadcrumb([
            ("Home", SITE+"/"),
            (svc["name"], f"{SITE}/{service_slug}/"),
            (city_name, URL),
        ]),
    ]
    bc = breadcrumbs([
        ("Home","/"),
        (svc["name"], f"/{service_slug}/"),
        (city_name, None),
    ])

    # HERO
    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">{city["county"]} · {svc["name"]} · {len(city["neighborhoods"])}+ neighborhoods</span>
    <h1>{svc["h1_phrase"]}<br>in <em>{city_name}<span class="stop">,</span></em> FL.</h1>
    <p class="page-hero-sub">{svc["intro_lead"]}</p>
    <div class="page-hero-trust">
      <span>{len(city["neighborhoods"])}+ {city_name} neighborhoods</span>
      <span>{BUSINESS["unique_stat_full"]}</span>
      <span>47-point install standard</span>
      <span>12-month workmanship warranty</span>
    </div>
  </div>
</section>'''

    # CITY-SPECIFIC LEAD (01)
    lead = f'''<section style="background:var(--paper-deep)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">{svc["name"]} · {city_name} Service Profile</span>
        <h2>{svc["short"]} in {city_name}, done <em>the long way</em>.</h2>
      </div>
    </div>
    <div class="intro-prose">
      <p><strong>{svc["name"]} in {city_name}, Florida</strong> is one of our most-requested services across {city["county"]}. {city["context_short"]} The {svc["name"].lower()} market in {city_name} is shaped by three things: {city["primary_market"].lower()}, the year-round humidity profile we share with the rest of Tampa Bay, and the volume of new construction (or aging housing stock) in the neighborhoods we serve here.</p>

      <p>{svc["intro_long_p1"]}</p>

      <p>{svc["intro_long_p2"]}</p>

      <p><strong>The local angle for {city_name}:</strong> {city["humidity_note"]} For {svc["name"].lower()} specifically, that means we acclimate every shipment of material for the full manufacturer-spec window (72 hours for hardwood and engineered, 48 hours for laminate, 24 hours for LVP and SPC), and we always pull a moisture reading on the subfloor before we start. Most {city_name} installs we do are in {city["neighborhoods"][0]}, {city["neighborhoods"][1]}, or one of the surrounding subdivisions; we&rsquo;ve worked all of them, we know the HOA rules, and we know what the city building department actually looks for if a permit is involved.</p>

      {stat_badge()}
    </div>
  </div>
</section>'''

    # SCOPE (03)
    scope_html = scope_section(svc)

    # CHECKLIST (04)
    checklist_html = checklist_section(city_name=city_name, service_name=svc["name"])

    # NEIGHBORHOODS (05)
    neigh_html = neighborhoods_section(city)
    # rebadge as section 05
    neigh_html = neigh_html.replace('<div class="section-head-num">05</div>', '<div class="section-head-num">05</div>')

    # MISTAKES (06)
    mistakes_html = mistakes_section(service_slug, city_name=city_name)

    # PRICING TABLE
    pricing_html = pricing_table_html(svc, city_name=city_name)

    # REVIEWS — filter for this city's matches first
    matched = [r for r in REVIEWS if r["city"] == city_name][:3]
    others = [r for r in REVIEWS if r["city"] != city_name][:3]
    reviews_combined = matched + others
    review_cards = ""
    for r in reviews_combined[:6]:
        stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
        review_cards += f'''<article class="review-card">
  <div class="review-quote-mark">&ldquo;</div>
  <div class="review-stars">{stars}</div>
  <p class="review-text">{r["text"]}</p>
  <div class="review-meta">
    <span class="review-author">{r["name"]}</span>
    <span class="review-where">{r["city"]}, FL · {r["service"]}</span>
    <span class="review-verified">● Verified Google Review · {r["date"]}</span>
  </div>
</article>'''
    reviews_html = f'''<section class="reviews-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">07</div>
      <div class="section-head-meta">
        <span class="mono-label">Reviews · {svc["short"]} · {city_name} &amp; Tampa Bay</span>
        <h2>What {svc["short"].lower()} buyers in <em>{city_name}</em> actually say.</h2>
      </div>
    </div>
    <div class="reviews-rating-bar">
      <span>● Google Verified</span>
      <span class="stars">★★★★★</span>
      <strong>{BUSINESS["rating"]}</strong>
      <span>from {BUSINESS["review_count"]} reviews</span>
      <a href="{BUSINESS["google_profile"]}" target="_blank" rel="noopener" style="color:var(--orange);text-decoration:underline">View on Google →</a>
    </div>
    <div class="reviews-grid">{review_cards}</div>
  </div>
</section>'''

    # FAQ (08)
    faq_html = faq_section(svc["faqs"], headline=f"{svc['short']} in {city_name} &mdash; the real questions.", label=f"FAQ · {svc['name']} · {city_name}")

    # RELATED — other services in this city + same service in other cities
    other_svcs = [s for s in SERVICE_ORDER if s != service_slug]
    other_svcs_links = "".join(
        f'<li><a href="/{s}/{city_slug}/">{SERVICES[s]["short"]} in {city_name}</a></li>'
        for s in other_svcs
    )
    other_cities = [c for c in CITIES if c != city_slug]
    other_cities_links = "".join(
        f'<li><a href="/{service_slug}/{c}/">{svc["short"]} in {CITIES[c]["name"]}</a></li>'
        for c in other_cities
    )
    related_html = f'''<section style="background:var(--paper)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px">
      <div class="related-box">
        <div class="related-box-label">Read Next · Other {city_name} Services</div>
        <h3>{city_name} homeowners also book.</h3>
        <ul>{other_svcs_links}</ul>
      </div>
      <div class="related-box">
        <div class="related-box-label">Read Next · {svc["short"]} in Other Cities</div>
        <h3>{svc["short"]} across Tampa Bay.</h3>
        <ul>{other_cities_links}</ul>
      </div>
    </div>
  </div>
</section>'''

    # FINAL CTA
    final_html = final_cta(
        headline=f"Ready for a real estimate on {svc['short'].lower()} in {city_name}?",
        sub=f"Free in-home measure. Written quote within 24 hours. {svc['short']} for {city_name} homes done to the {BUSINESS['checklist_points']}-point Napa&rsquo;s standard."
    )

    body = "\n".join([hero, lead, scope_html, checklist_html, neigh_html, mistakes_html, pricing_html, reviews_html, faq_html, related_html, f'<div class="container">{contact_banner()}</div>', final_html])

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    out = f"/home/claude/napas/{service_slug}/{city_slug}/index.html"
    write_page(out, head_html, header(active="services"), body, breadcrumbs_html=bc)


# ============================================================================
# SERVICE HUB page builder
# ============================================================================
def build_service_hub(service_slug):
    svc = SERVICES[service_slug]
    URL = f"{SITE}/{service_slug}/"

    TITLE_RAW = f"{svc['name']} · Tampa Bay & Sarasota · Napa's Flooring"
    TITLE = TITLE_RAW[:65]
    DESC = (
        f"{svc['name']} across Bradenton, Sarasota, Tampa &amp; Gulf Coast. "
        f"Installed by hand, acclimated, 47-point standard. 5★ Google · "
        f"12-month warranty · free quote in 24 hrs."
    )[:158]

    schemas = [
        schema_local_business(URL, f"{svc['name']} contractor", service=svc["name"]),
        schema_service(svc, canonical=URL),
        schema_faqpage(svc["faqs"]),
        schema_breadcrumb([
            ("Home", SITE+"/"),
            (svc["name"], URL),
        ]),
    ]
    bc = breadcrumbs([("Home","/"), (svc["name"], None)])

    # HERO
    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Service · {svc["name"]} · 8 Tampa Bay Cities</span>
    <h1>{svc["h1_phrase"]}.<br>Tampa Bay &amp; <em>Sarasota</em>.</h1>
    <p class="page-hero-sub">{svc["intro_lead"]}</p>
    <div class="page-hero-trust">
      <span>8 cities served</span>
      <span>{BUSINESS["unique_stat_full"]}</span>
      <span>{BUSINESS["rating"]}★ · {BUSINESS["review_count"]} reviews</span>
      <span>47-point install standard</span>
    </div>
  </div>
</section>'''

    # INTRO (01)
    lead = f'''<section style="background:var(--paper-deep)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">Service · Overview</span>
        <h2>{svc["name"]}, the <em>long way</em>.</h2>
      </div>
    </div>
    <div class="intro-prose">
      <p>{svc["intro_long_p1"]}</p>
      <p>{svc["intro_long_p2"]}</p>
      {stat_badge()}
      <p>This service is available in all eight cities we cover &mdash; pick the city closest to you below for {svc["short"].lower()}-specific pricing, FAQ, and a local-context page tailored to that market.</p>
    </div>
  </div>
</section>'''

    # SCOPE (02)
    scope_html = scope_section(svc)
    scope_html = scope_html.replace('<div class="section-head-num">03</div>', '<div class="section-head-num">02</div>')

    # CHECKLIST (03)
    checklist_html = checklist_section(service_name=svc["name"])
    checklist_html = checklist_html.replace('<div class="section-head-num">04</div>', '<div class="section-head-num">03</div>')

    # MISTAKES (04)
    mistakes_html = mistakes_section(service_slug)
    mistakes_html = mistakes_html.replace('<div class="section-head-num">06</div>', '<div class="section-head-num">04</div>')

    # PRICING (05)
    pricing_html = pricing_table_html(svc)

    # CITIES GRID (06)
    city_cards = ""
    for cslug, c in CITIES.items():
        city_cards += f'''<a href="/{service_slug}/{cslug}/" class="area-card">
  <div class="area-card-name">{svc["short"]} · {c["name"]}, FL</div>
  <div class="area-card-meta">{c["county"]} · {len(c["zips"])} ZIPs</div>
  <span class="area-card-arrow">See {c["name"]} →</span>
</a>'''
    cities_html = f'''<section class="areas-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">06</div>
      <div class="section-head-meta">
        <span class="mono-label on-dark">Cities Served · {svc["short"]}</span>
        <h2>{svc["short"]} in eight <em>Tampa Bay cities</em>.</h2>
        <div class="section-head-text"><p>Each city has its own page with local pricing, neighborhoods, and a {svc["short"].lower()} FAQ tailored to that market.</p></div>
      </div>
    </div>
    <div class="areas-grid">{city_cards}</div>
  </div>
</section>'''

    # REVIEWS (07)
    reviews_html = reviews_section(limit=6, headline=f"What {svc['short'].lower()} clients say.")
    reviews_html = reviews_html.replace('<div class="section-head-num">06</div>', '<div class="section-head-num">07</div>')

    # FAQ (08)
    faq_html = faq_section(svc["faqs"], headline=f"{svc['short']} questions, honestly answered.", label=f"FAQ · {svc['name']}")

    final_html = final_cta(
        headline=f"Get a real {svc['short'].lower()} estimate.",
        sub=f"Free in-home measure. Written, line-itemized quote within 24 hours. {svc['short']} done to the {BUSINESS['checklist_points']}-point Napa&rsquo;s standard."
    )

    body = "\n".join([hero, lead, scope_html, checklist_html, mistakes_html, pricing_html, cities_html, reviews_html, faq_html, f'<div class="container">{contact_banner()}</div>', final_html])

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    out = f"/home/claude/napas/{service_slug}/index.html"
    write_page(out, head_html, header(active="services"), body, breadcrumbs_html=bc)


if __name__ == "__main__":
    print("Building 6 service hub pages…")
    for s in SERVICE_ORDER:
        build_service_hub(s)
        print(f"  ✓ /{s}/")
    print(f"\nBuilding {len(SERVICE_ORDER)*len(CITIES)} service-city pages…")
    count = 0
    for s in SERVICE_ORDER:
        for c in CITIES:
            build_service_city(s, c)
            count += 1
    print(f"  ✓ Built {count} service-city pages.")
