#!/usr/bin/env python3
"""Generate /blog/ index + ~53 blog posts (5 general + 48 cost-per-service-per-city)."""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

ALL_POSTS = []  # we'll assemble as we go for the index

# ============================================================================
# Helper: render a post's article body
# ============================================================================
def post_shell(post, lede, sections_html, faqs=None, related_links=None, has_table=False):
    """Common wrapper for any blog post."""
    URL = f"{SITE}/blog/{post['slug']}/"
    TITLE = post["title"][:65]
    DESC = post["meta_desc"]
    cat = post.get("category", "Flooring")
    date_pretty = post["date_published"][:10]

    schemas = [
        schema_article(post, URL),
        schema_breadcrumb([
            ("Home", SITE+"/"),
            ("Journal", f"{SITE}/blog/"),
            (post["title"], URL),
        ]),
    ]
    if faqs:
        schemas.append(schema_faqpage(faqs))

    bc = breadcrumbs([
        ("Home","/"),
        ("Journal","/blog/"),
        (post["title"][:50] + ("..." if len(post["title"]) > 50 else ""), None),
    ])

    # Hero block (header-style for posts, smaller than page-hero)
    article_hero = f'''<section class="page-hero" style="padding:60px 0 50px">
  <div class="page-hero-inner">
    <div class="post-meta-bar" style="color:rgba(245,242,236,.6)">
      <span class="cat" style="color:var(--orange)">● {cat}</span>
      <span>Published {date_pretty}</span>
      <span>By Napa&rsquo;s Crew</span>
    </div>
    <h1 style="margin-top:14px">{post["title"]}</h1>
    <p class="page-hero-sub" style="font-style:italic">{post["meta_desc"]}</p>
  </div>
</section>'''

    related_block = ""
    if related_links:
        items = "".join(f'<li><a href="{url}">{label}</a></li>' for url, label in related_links)
        related_block = f'''<div class="related-box">
  <div class="related-box-label">Read Next · Related Reading</div>
  <h3>If this helped, also read.</h3>
  <ul>{items}</ul>
</div>'''

    faq_html = ""
    if faqs:
        faq_html = faq_section(faqs, headline="Common questions on this topic.", label="FAQ · Quick Answers")

    author_block = f'''<div class="post-author">
  <div class="post-author-avatar">N</div>
  <div class="post-author-info">
    <strong>The Napa&rsquo;s Crew</strong>
    <span>{BUSINESS["city"]}, FL · Est. {BUSINESS["year_founded"]} · {BUSINESS["unique_stat_full"]}</span>
  </div>
</div>'''

    body = f'''{article_hero}
<section>
  <div class="container">
    <article class="post-article">
      <p class="post-lede">{lede}</p>
      {sections_html}
      {author_block}
      {related_block}
    </article>
  </div>
</section>

{faq_html}

{f'<div class="container">{contact_banner()}</div>'}

{final_cta(headline=post.get("cta_headline", "Got a project this article would help with?"), sub="Free in-home measure. Written quote within 24 hours.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas, og_type="article")
    out = f"/home/claude/napas/blog/{post['slug']}/index.html"
    write_page(out, head_html, header(active="blog"), body, breadcrumbs_html=bc)
    ALL_POSTS.append(post)


# ============================================================================
# 5 GENERAL POSTS — handcrafted unique content
# ============================================================================
def build_general_posts():

    # ============================================================================
    # POST 1: Humidity guide
    # ============================================================================
    p1 = GENERAL_BLOG_POSTS[0]  # best-flooring-gulf-coast-humidity
    lede = (
        "Florida flooring is its own engineering problem. Year-round dew points "
        "in the high 60s and low 70s, slab-on-grade construction in most homes "
        "built after 1980, salt air on every coastal mile of the Gulf, and an "
        "indoor-outdoor humidity differential that bends materials in predictable, "
        "expensive ways. Here&rsquo;s what actually holds up &mdash; and what we&rsquo;ve "
        "stopped installing on the Gulf Coast even when customers ask for it."
    )
    sections = '''
<h2>What humidity actually does to flooring</h2>

<p>Materials don&rsquo;t fail because of the average humidity. They fail because of the <em>swing</em> &mdash; the difference between the highest moisture the material absorbs (typically July through September outdoor exposure or during a hurricane closure) and the lowest moisture it dries down to (typically February through April in a heavily air-conditioned home). A wood-based product that absorbs 4% moisture at peak and dries down to 1% moisture in the dry months will expand and contract enough to gap, cup, or buckle. The wider the swing, the worse the failure.</p>

<p>Most Florida homes operate at indoor relative humidity between 45 and 60 percent year-round, which translates to wood equilibrium moisture content (EMC) between 8% and 11%. Outdoor air on a typical August afternoon hits 78&ndash;85% RH, which translates to wood EMC between 16% and 18%. That&rsquo;s a 5&ndash;7 point swing if the material gets any meaningful outdoor exposure &mdash; from open windows, from a porch transition, from a snowbird closure where the AC is off for months.</p>

<blockquote>Solid hardwood was designed in the Northeast for the Northeast. It works in Florida only when you control humidity the way the Northeast does, which most Florida homes don&rsquo;t.</blockquote>

<h2>What we install most for Gulf Coast humidity</h2>

<h3>1. Engineered hardwood (the only "real wood" we recommend on slabs)</h3>

<p>Engineered hardwood has a top-layer of real hardwood (typically 2&ndash;6mm thick) glued to a stable plywood or HDF substrate. The cross-grain construction of the substrate prevents the directional swelling that wreaks havoc with solid hardwood. We install it almost exclusively in the 7&ndash;9 inch wide-plank format, in European white oak (most-installed), American white oak, and hickory.</p>

<p>What to look for: a substrate that&rsquo;s 7+ layers (not 3-layer cheap engineered), a wear layer of 3mm or more on premium product (4&ndash;6mm on the high end), and a finish that&rsquo;s aluminum-oxide-cured (most premium European brands) or oil-finished (more authentic, more maintenance). Cost-installed: $7&ndash;$14 per square foot most of the time, $14&ndash;$22 for high-end European brands.</p>

<h3>2. SPC luxury vinyl plank (the all-around winner for most Florida homes)</h3>

<p>SPC stands for &ldquo;stone-plastic composite&rdquo; &mdash; a rigid-core vinyl plank with a stone-aggregate-and-thermoplastic core that&rsquo;s essentially dimensionally stable across the full humidity range a Florida home will ever see. It&rsquo;s 100% waterproof through the core, has wear layers up to 22 mil (premium), and the visuals have improved dramatically in the last 5 years to where mid-tier SPC ($4&ndash;$7 installed) reads as real wood from 10 feet away.</p>

<p>What to look for: a wear layer of 20 mil or more (anything thinner wears through within 5&ndash;8 years on high-traffic floors), a plank thickness of 6mm or more (thinner planks telegraph subfloor imperfections), and an attached underlayment (most premium SPC includes it). Cost-installed: $4&ndash;$7 most of the time, $7&ndash;$9 for the wide-plank premium tier.</p>

<h3>3. Porcelain tile (the only realistic option for full bathrooms and kitchens with islands)</h3>

<p>Porcelain doesn&rsquo;t care about humidity. It doesn&rsquo;t care about water. It doesn&rsquo;t care about pets. It will outlive the structure it&rsquo;s installed in. The constraints are aesthetic (some homeowners don&rsquo;t love the feel underfoot), thermal (cold in winter unless you install radiant heat under it), and structural (the substrate has to be dramatically flatter for large-format tile than for any other flooring).</p>

<p>For Florida kitchens, full baths, mudrooms, laundry rooms, and pool-deck-adjacent rooms, porcelain is the right answer almost every time. Cost-installed: $7&ndash;$11 for standard 12&times;24 and 18&times;18 formats, $10&ndash;$15 for 24&times;48 large format, $14&ndash;$22 for marble-look slab and natural-stone product.</p>

<h2>What we&rsquo;ve stopped recommending</h2>

<h3>Solid hardwood on slabs</h3>
<p>It works for about 8 years on average in Florida before the gapping, cupping, or buckling becomes visible enough to require a re-sand-and-refinish or a full replacement. The exception: solid hardwood over a properly installed sleeper system (3/4-inch plywood subfloor floated over the slab with a 6-mil vapor barrier and adhesive). That works long-term, but costs an extra $2.50&ndash;$4 per square foot just for the sleeper install, which usually makes engineered hardwood the better economic choice anyway.</p>

<h3>Laminate in kitchens and full baths</h3>
<p>Modern AC4 and AC5 laminate is wonderful in bedrooms, living rooms, and home offices. It is wood-based at the core, and that core will swell at the seams if liquid water sits on the floor for hours. For kitchens (dishwasher leaks, refrigerator condensate, ice maker lines) and full baths, we&rsquo;ve stopped installing laminate. SPC vinyl plank does the same job, costs about the same, and doesn&rsquo;t fail when something leaks.</p>

<h3>Glue-down LVP without a moisture test</h3>
<p>Florida concrete slabs can carry moisture from the soil below them at rates that exceed what most LVP adhesives can tolerate over time. A glue-down install without a documented calcium chloride moisture test (or in-situ RH probe reading) is a 5-year warranty waiting to fail. We test on every glue-down job, every time.</p>

<h2>Pricing for Gulf Coast humidity-tolerant flooring (2026)</h2>

<table class="post-table">
<thead><tr><th>Product Tier</th><th>Installed Cost</th><th>Best Use</th></tr></thead>
<tbody>
<tr><td>Budget SPC LVP (6mm, 12-mil)</td><td><strong>$2.50&ndash;$3.50</strong></td><td>Rentals, secondary spaces</td></tr>
<tr><td>Mid-range SPC LVP (6mm, 20-mil)</td><td><strong>$4&ndash;$6</strong></td><td>Most primary residences</td></tr>
<tr><td>Premium SPC LVP (8mm, 22-mil)</td><td><strong>$6&ndash;$9</strong></td><td>Pet-heavy primary residences</td></tr>
<tr><td>Engineered Hardwood (3-layer)</td><td><strong>$7&ndash;$10</strong></td><td>Builder-grade upgrade</td></tr>
<tr><td>Engineered Hardwood (7+ layer, 4mm wear)</td><td><strong>$10&ndash;$14</strong></td><td>Premium primary residence</td></tr>
<tr><td>European Engineered (wide plank, oil finish)</td><td><strong>$14&ndash;$22</strong></td><td>High-end whole-home install</td></tr>
<tr><td>Porcelain Tile (12&times;24, 18&times;18)</td><td><strong>$7&ndash;$11</strong></td><td>Kitchens, baths, laundry</td></tr>
<tr><td>Large-format Porcelain (24&times;48)</td><td><strong>$10&ndash;$15</strong></td><td>Open-plan main floors</td></tr>
<tr><td>Marble-look Porcelain Slab (48&times;48+)</td><td><strong>$14&ndash;$22</strong></td><td>Foyers, premium kitchens</td></tr>
</tbody>
</table>

<div class="post-key-takeaway">
<strong>The Bottom Line for Gulf Coast Homes</strong>
For most Florida primary residences in 2026, the best whole-home flooring combination is mid-range to premium SPC vinyl plank in living areas and bedrooms ($4&ndash;$6 per square foot installed), porcelain tile in kitchens and bathrooms ($7&ndash;$11), and engineered hardwood only where you really want real wood and you accept the higher cost ($10&ndash;$14). That combo handles humidity, water, pets, and Florida living without compromise &mdash; and it&rsquo;s what we install most often, across all eight cities we serve.
</div>

<h2>How to choose, in order</h2>

<ol>
<li><strong>Decide if you want real wood</strong> in the living areas. If yes, engineered hardwood ($10&ndash;$14 installed). If no, SPC vinyl plank ($4&ndash;$6 installed).</li>
<li><strong>Decide on a tile for wet rooms.</strong> Standard porcelain for budget ($7&ndash;$11), large-format for design statement ($10&ndash;$15), natural stone for premium ($14&ndash;$22).</li>
<li><strong>Decide on stairs.</strong> Match the downstairs floor &mdash; hardwood treads if downstairs is hardwood, LVP treads with matching nosing if downstairs is LVP.</li>
<li><strong>Plan transitions.</strong> Every flooring-to-flooring transition needs a strip; budget $30&ndash;$60 per transition in the install quote.</li>
</ol>

<p>Three product categories. One per use case. We&rsquo;ll bring samples of all three to the estimate and let you compare them in your home, in your lighting, against your existing trim. The hour at the dining table is the most-important hour of the entire job.</p>
'''
    related = [
        ("/blog/short-term-rental-flooring-tampa-bay/", "STR Flooring Playbook for Tampa Bay Rentals"),
        ("/blog/engineered-hardwood-vs-spc-lakewood-ranch/", "Engineered Hardwood vs. SPC: Field Test"),
        ("/hardwood-flooring/", "Hardwood Flooring · Service Page"),
        ("/vinyl-plank-flooring/", "Luxury Vinyl Plank · Service Page"),
    ]
    faqs = [
        ("Is engineered hardwood really &lsquo;real wood&rsquo;?",
         "Yes &mdash; the top wear-layer of engineered hardwood is the same species, same cut, same finish as solid hardwood. The difference is what&rsquo;s underneath: solid hardwood is wood all the way down, engineered hardwood has a cross-grain plywood or HDF substrate. The look is identical; the dimensional stability is dramatically better. We can&rsquo;t tell solid from engineered standing on it after install &mdash; you definitely can&rsquo;t."),
        ("Is SPC actually waterproof or just water-resistant?",
         "SPC is genuinely waterproof through the core &mdash; you can submerge a plank for days and it won&rsquo;t swell, warp, or delaminate. The seams between planks are tight enough that surface water won&rsquo;t penetrate to the subfloor for hours. What it isn&rsquo;t is flood-proof &mdash; standing water at a baseboard for 24+ hours can still get into the wall cavity through the expansion gap. Treat &lsquo;waterproof&rsquo; as a forgiveness factor for spills and pet accidents, not as a license to ignore an active leak."),
        ("Will porcelain tile feel cold in winter?",
         "Yes, somewhat. Porcelain conducts thermal energy more efficiently than wood-based or vinyl-based floors, so it feels cool underfoot. Most Florida winters this is welcome; some homeowners in St. Petersburg and Tampa where January nights dip to the 40s prefer not to walk on tile bare-foot. The solution is radiant heating mat under the tile (Schluter Ditra-Heat or equivalent), which adds about $4&ndash;$6 per square foot and is genuinely transformative on tile bathroom floors."),
    ]
    post_shell(p1, lede, sections, faqs=faqs, related_links=related)

    # ============================================================================
    # POST 2: STR / Short-term rental guide
    # ============================================================================
    p2 = GENERAL_BLOG_POSTS[1]
    lede = (
        "Short-term rentals chew through flooring at 3&ndash;5&times; the rate of "
        "owner-occupied homes. Guest turnovers, suitcase wheels, beach sand, pets, "
        "kids, the &lsquo;take everything off the floor&rsquo; cleaning crew &mdash; nothing "
        "stays nice forever, but some floors stay nice long enough to be a real "
        "investment. Here&rsquo;s what we install in Anna Maria, Siesta, Lido, "
        "Wellen Park, Channelside, and Snell Isle rentals, and what we don&rsquo;t."
    )
    sections = '''
<h2>The economic argument for the right floor</h2>

<p>A typical Tampa Bay short-term rental sees 40&ndash;120 guest turnovers per year, depending on size, location, and pricing strategy. Each turnover is a cleaning crew sweeping, vacuuming, mopping, and occasionally dragging suitcases across the floor. Beach rentals on Anna Maria, Lido, Siesta, and the keys around Venice add fine quartz sand to the mix &mdash; the same sand that goes between the planks of any wood-floor installation and gradually grinds the finish away from below.</p>

<p>A cheap LVP that&rsquo;s rated for &ldquo;light residential&rdquo; will show visible wear in the high-traffic lines (front door to bedroom, kitchen to dining) within 18&ndash;24 months of STR use. A premium SPC with a 22-mil wear layer rated for &ldquo;commercial&rdquo; use will look identical at the 5-year mark. The difference is roughly $1,500&ndash;$3,500 on a 1,200 sq ft rental &mdash; less than two months of rental income on most properties. The math is obvious.</p>

<h2>What we install in Tampa Bay STRs (in order of how often)</h2>

<h3>1. Glue-down SPC with 22-mil wear layer (the workhorse)</h3>

<p>Glue-down (not floating) SPC at the premium tier is what we install in roughly 70% of the STR projects we do. The glue-down install costs about $1.50 per square foot more in labor than a floating install, but the floor doesn&rsquo;t move under suitcase wheels, the seams stay tight under the constant pivoting of a cleaning crew, and the lifespan in STR use roughly doubles relative to a floating install of the same product.</p>

<p>The product specs we look for: <strong>22-mil wear layer minimum</strong> (anything thinner shows wear too fast), <strong>commercial-grade rating</strong>, <strong>EVA-style adhesive</strong> compatible with concrete slabs and minor moisture, and a <strong>visual that doesn&rsquo;t repeat obviously</strong> (some cheap LVP shows the same plank pattern every 4 boards, which guests notice). Premium brands we trust: COREtec, Mannington Adura Max, Shaw Resilient.</p>

<h3>2. Large-format porcelain in beach rentals (sand-proof)</h3>

<p>For ground-floor beach rentals on Anna Maria, Lido, Siesta, and the Venice barrier islands, we increasingly install large-format porcelain throughout the entire ground floor instead of LVP. The reason: sand. Sand is abrasive, it travels in on every guest&rsquo;s feet, and it&rsquo;s the single biggest enemy of any wood-look flooring &mdash; including premium SPC. Porcelain doesn&rsquo;t care about sand. You sweep it up, you move on. The floor is identical in year 10.</p>

<p>Cost is competitive: $7&ndash;$11 per square foot installed for standard porcelain matches the mid-tier SPC range, and the lifespan is roughly 2&ndash;3&times; longer in beach-house use. The downside is the install timeline (5&ndash;8 days vs. 2&ndash;3 for LVP), which matters during a vacancy window.</p>

<h3>3. Premium engineered hardwood in luxury rentals only</h3>

<p>For high-end luxury rentals (Siesta Key beachfront, Longboat Key, Casey Key, premium Old Northeast historic homes, Hyde Park bungalow rentals at the top of the market), wide-plank European white oak engineered hardwood remains the right choice on aesthetics alone &mdash; guests notice the difference, reviews mention it, and it justifies the per-night premium. The constraint is maintenance: hardwood in STR use requires a full sand-and-refinish every 4&ndash;6 years to stay in luxury condition. Budget for it.</p>

<h2>What we don&rsquo;t install in STRs</h2>

<ul>
<li><strong>Solid hardwood.</strong> The maintenance cycle is too aggressive for STR economics, and the dimensional movement on a slab is too unpredictable for a remotely-managed property.</li>
<li><strong>Cheap laminate.</strong> AC3 laminate (the standard at most retail price points) doesn&rsquo;t hold up to STR traffic, and the seams swell from the first dishwasher leak or guest-spilled drink.</li>
<li><strong>Cheap LVP.</strong> $1.50&ndash;$2.50 per square foot LVP looks ok for the first year, mediocre by year two, and unacceptable by year three. Spend the extra $2&ndash;$3 per square foot and forget about the floor for a decade.</li>
<li><strong>Floating floors in high-traffic STRs.</strong> Even premium SPC, when installed as a floating floor, will eventually show seam separation at the high-pivot points (front door, kitchen island, bedroom doorways) in heavy STR use. Glue it down.</li>
</ul>

<h2>STR turnover timeline: how to install during a one-week vacancy</h2>

<p>The hardest constraint in STR flooring isn&rsquo;t the product or the price; it&rsquo;s the schedule. Owners typically have a 5&ndash;10 day window between bookings, and a missed deadline costs real money in refunded nights or unhappy guests.</p>

<p>Our STR install standard for a typical 1,000&ndash;1,400 sq ft property:</p>

<ul>
<li><strong>Day 1 morning:</strong> Final cleaning crew exits. Owner&rsquo;s team removes all furniture, art, and decor to a holding location (we don&rsquo;t typically handle this).</li>
<li><strong>Day 1 afternoon:</strong> We arrive. Demo of existing flooring, haul-away, subfloor inspection.</li>
<li><strong>Day 2:</strong> Subfloor prep &mdash; self-level any dips, install vapor barrier where needed, moisture readings logged.</li>
<li><strong>Day 3&ndash;4:</strong> SPC glue-down install. Two installers, full days.</li>
<li><strong>Day 5:</strong> Transitions, trim, baseboard reset, final clean.</li>
<li><strong>Day 6:</strong> Owner&rsquo;s team moves furniture back, cleaning crew returns for guest-ready clean.</li>
<li><strong>Day 7:</strong> Next guest arrives.</li>
</ul>

<p>That&rsquo;s the standard. We&rsquo;ve done it in 4 days when the vacancy was tight, with three installers instead of two, on a Saturday-through-Tuesday schedule.</p>

<div class="post-key-takeaway">
<strong>STR Owner&rsquo;s Bottom Line</strong>
Spend the extra $1.50&ndash;$3 per square foot for premium glue-down SPC (22-mil wear, commercial-grade, 6mm+ thickness). The math pays back inside the first 24 months of ownership in reduced replacement frequency. For ground-floor beach rentals on Anna Maria, Lido, Siesta, or the Venice islands, strongly consider large-format porcelain instead &mdash; sand is the silent killer of every wood-look flooring product, and porcelain is the only floor that genuinely doesn&rsquo;t care.
</div>

<h2>STR-tested products we install most</h2>

<table class="post-table">
<thead><tr><th>Product</th><th>Cost Installed</th><th>STR Lifespan</th></tr></thead>
<tbody>
<tr><td>Premium SPC glue-down (22-mil, commercial)</td><td><strong>$5&ndash;$7</strong></td><td>8&ndash;12 years</td></tr>
<tr><td>Large-format porcelain (12&times;24, 18&times;18)</td><td><strong>$7&ndash;$11</strong></td><td>20+ years</td></tr>
<tr><td>Large-format porcelain (24&times;48)</td><td><strong>$10&ndash;$15</strong></td><td>20+ years</td></tr>
<tr><td>European engineered hardwood (oil-finish)</td><td><strong>$14&ndash;$22</strong></td><td>15+ yrs with periodic refinish</td></tr>
</tbody>
</table>
'''
    related = [
        ("/blog/best-flooring-gulf-coast-humidity/", "What Flooring Holds Up to Gulf Coast Humidity"),
        ("/vinyl-plank-flooring/sarasota/", "Vinyl Plank Flooring in Sarasota"),
        ("/tile-installation/", "Tile Installation · Service Page"),
    ]
    faqs = [
        ("Can you install flooring during my one-week vacancy?",
         "Yes &mdash; we&rsquo;ve done dozens of one-week STR turnover installs across Anna Maria Island, Siesta Key, Wellen Park, Channelside, and the keys around Venice. The standard is 5 working days for a typical 1,000&ndash;1,400 sq ft install; we&rsquo;ve done 4 days with 3 installers when the vacancy was tight. Schedule needs to be locked at least 3 weeks in advance for guaranteed availability."),
        ("Do you bill the property manager or the owner?",
         "Either &mdash; depends on what you prefer. About 60% of our STR work is billed direct to the property manager (Vacasa, Evolve, AvantStay, and several local Tampa Bay PMs), and the manager invoices the owner. About 40% is billed direct to the owner. Either way, we provide itemized written quotes and detailed invoices."),
    ]
    post_shell(p2, lede, sections, faqs=faqs, related_links=related)

    # ============================================================================
    # POST 3: Refinish guide
    # ============================================================================
    p3 = GENERAL_BLOG_POSTS[2]
    lede = (
        "Tampa Bay has a remarkable inventory of pre-war and mid-century homes with "
        "original oak floors hiding under decades of carpet, vinyl, or tile. The "
        "instinct is to refinish and reveal them. The reality is more complicated. "
        "Here&rsquo;s how we evaluate, price, and execute oak refinish projects in "
        "{city_one}, {city_two}, {city_three}, and {city_four} in 2026."
    ).format(
        city_one="Bradenton",
        city_two="Sarasota",
        city_three="Tampa",
        city_four="St. Pete",
    )
    sections = '''
<h2>Can your floor actually be refinished?</h2>

<p>The first question, asked before any other. A solid hardwood floor can typically be sand-and-refinished 4&ndash;6 times in its life &mdash; each sanding removes about 1/32-inch of material, and most solid hardwood has 5/16-inch of wood above the tongue (the structural part that can&rsquo;t be sanded). Floors that have been sanded 4&ndash;5 times already are often too thin to do safely; one more pass exposes the tongue and the floor delaminates.</p>

<p>We use a slim probe driven into a small drilled hole at an inconspicuous spot (under a piece of trim, in a closet) to measure the remaining wood thickness above the tongue. The reading tells us whether a full sand is realistic, a screen-and-recoat is the right call, or a partial sand with section-replacement of the worst areas is the better answer.</p>

<h3>Refinish vs. screen-and-recoat vs. replace</h3>

<ul>
<li><strong>Full sand-and-refinish</strong> ($3.50&ndash;$6 per square foot) &mdash; for floors with deep scratches, water staining, pet damage, or visible wear-through of the original finish. Three full sandings (coarse, medium, fine), three coats of polyurethane (water-based or oil-based), 5&ndash;8 days of cure time. The floor will look new.</li>
<li><strong>Screen-and-recoat</strong> ($1.50&ndash;$2.50 per square foot) &mdash; for floors with only surface wear, no stain damage, and a finish that&rsquo;s simply faded. We lightly abrade the existing finish with a 120-grit screen, vacuum twice, apply one or two coats of new poly. 2&ndash;3 days. Brings back the sheen but doesn&rsquo;t remove anything below the original finish.</li>
<li><strong>Partial sand with section replacement</strong> &mdash; for floors with localized damage (water at a leak point, a damaged plank or two, a section that was repaired badly). We replace the bad section with new planks &mdash; either matching the original species or feathering with similar-character salvaged stock &mdash; and refinish everything to blend.</li>
<li><strong>Full replacement</strong> &mdash; when the remaining wood thickness is too thin to safely sand, when the structural subfloor has issues, or when the cost of restoration exceeds what new engineered hardwood would cost (which it often does on small old floors with extensive damage).</li>
</ul>

<h2>Realistic cost expectations in 2026 (Tampa Bay rates)</h2>

<table class="post-table">
<thead><tr><th>Scope</th><th>Cost / Square Foot</th><th>Timeline</th></tr></thead>
<tbody>
<tr><td>Screen-and-recoat (no sand)</td><td><strong>$1.50&ndash;$2.50</strong></td><td>2&ndash;3 days</td></tr>
<tr><td>Full sand &amp; refinish (water-based poly)</td><td><strong>$3.50&ndash;$5</strong></td><td>5&ndash;7 days</td></tr>
<tr><td>Full sand &amp; refinish (oil-based poly)</td><td><strong>$4&ndash;$6</strong></td><td>7&ndash;10 days</td></tr>
<tr><td>Partial sand + section replacement</td><td><strong>$5&ndash;$8</strong></td><td>5&ndash;9 days</td></tr>
<tr><td>Dust-containment system (premium)</td><td><strong>+$1 per sq ft</strong></td><td>same</td></tr>
<tr><td>Stain change (light to dark or v.v.)</td><td><strong>+$0.80&ndash;$1.50</strong></td><td>+1 day</td></tr>
</tbody>
</table>

<h2>Water-based vs. oil-based polyurethane</h2>

<p>Two common finish systems, and they look genuinely different.</p>

<h3>Water-based poly (Bona Traffic HD, Vermeister Aqua, Loba 2K Supra)</h3>
<p>Cures in 8&ndash;12 hours per coat, almost no odor, dries crystal-clear and stays that way (no amber over time). Better for white-oak floors where you want to preserve the natural color. Modern premium water-based polys are as durable as oil &mdash; the old stereotype that &lsquo;water-based wears out faster&rsquo; hasn&rsquo;t been true for at least a decade. Slightly more expensive material; same labor.</p>

<h3>Oil-based poly (Bona Mega ONE, traditional oil-modified)</h3>
<p>Cures in 24 hours per coat, has the distinctive solvent smell during cure (we evacuate the home for the cure window), ambers warmly over time. Better for red oak and walnut where you want the wood to deepen and richen with age. The traditional choice for pre-war and mid-century oak floors, and what we recommend for restoration projects that want to keep the period look.</p>

<h2>The Tampa Bay reality: 1925&ndash;1965 oak floors</h2>

<p>The Tampa Bay area has a large inventory of homes from this era with original oak floors:</p>

<ul>
<li><strong>Hyde Park and Bayshore (Tampa)</strong> &mdash; 1910s&ndash;1930s bungalows with 2-1/4 inch red oak, often carpeted over decades ago.</li>
<li><strong>Old Northeast and Snell Isle (St. Petersburg)</strong> &mdash; 1920s&ndash;1940s Mediterranean-revival homes with red oak and occasionally heart pine.</li>
<li><strong>Cherokee Park and Southside Village (Sarasota)</strong> &mdash; 1940s&ndash;1960s ranches with 2-1/4 and 3-1/4 inch red oak.</li>
<li><strong>West Bradenton and Palma Sola (Bradenton)</strong> &mdash; 1950s&ndash;1970s block homes with mid-century oak and occasional period parquet.</li>
</ul>

<p>Many of these floors are eminently salvageable &mdash; even when the carpet has been down for 40 years and the wood looks shocking when first exposed. The carpet adhesive, the staples, the cushion residue all scrape off in the first sanding. The wood underneath is almost always sound.</p>

<div class="post-key-takeaway">
<strong>The Restoration Reality Check</strong>
A full sand-and-refinish on 1,200 square feet of original oak runs $4,800&ndash;$7,200 in 2026 Tampa Bay rates. New premium engineered hardwood installed in the same space runs $11,000&ndash;$18,000. The math heavily favors restoration when the floor is genuinely sound. We&rsquo;ll evaluate honestly and tell you when restoration is not the right call.
</div>

<h2>What we won&rsquo;t recommend</h2>

<ul>
<li><strong>Refinishing engineered hardwood you don&rsquo;t know the wear-layer thickness on.</strong> Many builder-grade engineered floors have a 1mm or 2mm wear layer that can be sanded zero times safely. We can&rsquo;t tell from the surface; we have to drill a probe hole or pull a sample plank.</li>
<li><strong>Sanding parquet with a flat-pad sander.</strong> Period parquet (especially Versailles patterns and herringbone) requires hand-scraping or a small orbital sander to avoid blowing through the wood at the grain transitions. We use small machines and slow passes.</li>
<li><strong>Staining floors a color the species can&rsquo;t hold.</strong> Red oak takes stain very differently than white oak; pine takes stain very poorly; maple is famously stain-resistant. We bring stain samples and we test on a hidden spot before we commit a whole floor to a color that may not work.</li>
</ul>
'''
    related = [
        ("/floor-repair/", "Floor Repair · Service Page"),
        ("/floor-repair/tampa/", "Floor Repair in Tampa, FL"),
        ("/blog/best-flooring-gulf-coast-humidity/", "Gulf Coast Humidity Guide"),
    ]
    faqs = [
        ("How do I know if my old hardwood is solid or engineered?",
         "Three checks. First, look at the edge of a plank under a transition strip or at a doorway &mdash; solid hardwood is the same wood all the way through; engineered shows visible plywood layers. Second, the plank width &mdash; almost all engineered hardwood is 5 inches or wider; almost all pre-1970s solid hardwood is 2-1/4 or 3-1/4 inches wide. Third, the age of the home &mdash; almost all engineered hardwood post-dates 1985; pre-war floors are almost certainly solid. We confirm at the estimate with a probe sample."),
        ("How disruptive is a sand-and-refinish?",
         "Moderately. We use a HEPA-filtered dust containment system on every job, but there&rsquo;s residual dust and the polyurethane cure window requires the room to be unoccupied for 8&ndash;24 hours per coat. Most owners stay elsewhere for the 5&ndash;8 days of the job. The dust containment system is a +$1 per square foot upgrade that&rsquo;s worth every cent &mdash; it keeps the rest of the house clean during the work."),
    ]
    post_shell(p3, lede, sections, faqs=faqs, related_links=related)

    # ============================================================================
    # POST 4: Stair tread guide
    # ============================================================================
    p4 = GENERAL_BLOG_POSTS[3]
    lede = (
        "Stair tread replacement is the highest-impact, lowest-disruption flooring "
        "upgrade in any two-story home. Two days, one staircase, and the most "
        "visible carpentry detail in the entire house gets transformed. Here&rsquo;s "
        "exactly how we do it, what it actually costs in 2026, and what goes wrong "
        "when it&rsquo;s done badly."
    )
    sections = '''
<h2>What &lsquo;stair tread replacement&rsquo; actually means</h2>

<p>A staircase has three visible elements: <strong>treads</strong> (the horizontal surface you step on), <strong>risers</strong> (the vertical face between treads), and <strong>nosing</strong> (the rounded or square edge that protrudes from the front of each tread). When most people say &lsquo;stair tread replacement,&rsquo; they mean replacing all three &mdash; pulling up the existing carpet, removing the original construction-grade pine treads underneath, and installing finished hardwood, LVP, or laminate treads with matching risers and nosing detail.</p>

<p>Most existing stair builds have pine or fir treads under the carpet, intended to be hidden permanently. They&rsquo;re usually stained from carpet adhesive and pad residue, sometimes warped from age, and rarely finished to a quality you&rsquo;d want to live with. Refinishing them is occasionally an option; replacement is the default we recommend.</p>

<h2>Tread material options &mdash; in order of how often we install</h2>

<h3>1. Solid hardwood (most popular)</h3>

<p>The traditional choice. We install 5/4-inch solid hardwood treads in oak, hickory, walnut, or maple &mdash; matched to the downstairs floor, site-finished to match the stain and sheen of the existing flooring, with hardwood return-nose detail on open-side staircases. Cost: $130&ndash;$200 per tread installed. Lifespan: indefinite, with occasional refinishing every 8&ndash;12 years.</p>

<h3>2. Engineered hardwood treads (when matching engineered floor)</h3>

<p>For homes with engineered hardwood downstairs, we source factory-pre-finished engineered treads from the same manufacturer, with matching nosing pieces. The match is perfect, no site finishing required, and the install is faster. Cost: $110&ndash;$160 per tread installed. Lifespan: matches the manufacturer warranty on the floor (typically 25&ndash;50 years).</p>

<h3>3. LVP and laminate treads</h3>

<p>The most cost-effective option, and a very common pairing with downstairs SPC vinyl plank installs. Manufacturer-matched nosing pieces tie the tread visually to the field plank. Cost: $60&ndash;$95 per tread (LVP) and $70&ndash;$110 per tread (laminate) installed. Lifespan: matches the warranty on the flooring (typically 15&ndash;30 years residential).</p>

<h2>Cost breakdown for a typical 14-tread staircase</h2>

<table class="post-table">
<thead><tr><th>Component</th><th>Per Tread/Riser</th><th>Total for 14 treads</th></tr></thead>
<tbody>
<tr><td>LVP treads + LVP risers</td><td><strong>$95&ndash;$150</strong></td><td><strong>$1,330&ndash;$2,100</strong></td></tr>
<tr><td>Engineered hardwood treads + poplar risers</td><td><strong>$145&ndash;$215</strong></td><td><strong>$2,030&ndash;$3,010</strong></td></tr>
<tr><td>Solid hardwood treads + poplar risers</td><td><strong>$165&ndash;$255</strong></td><td><strong>$2,310&ndash;$3,570</strong></td></tr>
<tr><td>Solid hardwood treads + matching hardwood risers</td><td><strong>$190&ndash;$295</strong></td><td><strong>$2,660&ndash;$4,130</strong></td></tr>
<tr><td>Return-nose detail (open-side stairs)</td><td><strong>+$20&ndash;$40 each</strong></td><td><strong>+$140&ndash;$280 (open-side treads only)</strong></td></tr>
<tr><td>Iron baluster install through new treads</td><td><strong>+$45&ndash;$75 each</strong></td><td><strong>+$630&ndash;$1,050 (if applicable)</strong></td></tr>
</tbody>
</table>

<h2>What a 2-day install actually looks like</h2>

<p>Day 1, morning: Carpet removal, staple pull, sub-tread inspection. We strip the staircase down to the original pine or fir tread platforms, vacuum twice, and inspect each tread for soundness. Any soft spots or excessive crowning gets noted for replacement.</p>

<p>Day 1, afternoon: Old tread removal where required (which is most of them on a full-tread-replacement job). Subflooring is checked for squeaks; any movement gets screwed through into the framing.</p>

<p>Day 2, morning: New tread install starts at the top of the stairs and works down. Each tread is shim-leveled if needed (slight pitch differences are corrected at this stage), construction-adhesived to the platform, and screwed through into the framing from above (concealed under the riser above).</p>

<p>Day 2, afternoon: Risers installed, transitions and quarter-rounds nailed at the bottom and top tread, return-nose details mitered and installed on open-side stairs. Final caulk lines at the riser-to-tread joints, touch-up paint on the risers.</p>

<p>For site-finished solid hardwood treads (not pre-finished), add a day or two for stain application and polyurethane cure.</p>

<h2>What can go wrong (and what we&rsquo;ve fixed)</h2>

<h3>Uneven tread depth</h3>
<p>Different treads in the same staircase can vary by 1/8 to 1/4 inch in depth because of original construction tolerances. A good installer notices this on day one and cuts each new tread to fit its specific position. A bad installer cuts all 14 treads to the same dimension and you get gaps at the back wall or at the open-side return. We&rsquo;ve fixed this twice on staircases that were installed by other contractors before us.</p>

<h3>Non-matching nosing profiles</h3>
<p>Some homeowners try to mix-and-match: a solid hardwood tread with an off-the-shelf LVP nosing piece, or an LVP tread with a stock pine nosing. The mismatch is visible from across the room. We source the tread, riser, and nosing from a coordinated system &mdash; either all from the same manufacturer (for engineered and LVP) or all custom-milled and finished together (for solid hardwood).</p>

<h3>Pet traction issues</h3>
<p>Pre-finished hardwood and LVP treads are smoother than carpet, and older dogs (especially larger breeds) can lose traction going down them. The fix is clear silicone grip strips applied 1 inch back from the tread nose &mdash; nearly invisible from standing height, transformative for pet traction. We install them on request at no additional labor charge.</p>

<div class="post-key-takeaway">
<strong>The Stair Replacement Bottom Line</strong>
A 14-tread staircase replacement in 2026 Tampa Bay runs $1,330 (entry-level LVP) to $4,130 (full custom solid hardwood with matching risers and iron-baluster integration). The mid-tier sweet spot &mdash; matching engineered hardwood treads with white poplar risers &mdash; lands at $2,030&ndash;$3,010 and looks indistinguishable from a $4,000 custom job to anyone but the builder. Done in 2&ndash;3 days. The single highest-impact, lowest-disruption upgrade in any two-story home.
</div>
'''
    related = [
        ("/stair-treads/", "Stair Treads · Service Page"),
        ("/blog/refinishing-old-oak-floors-tampa-bay/", "Refinishing Old Oak Floors"),
    ]
    faqs = [
        ("Can you match new treads to my existing downstairs hardwood?",
         "Yes &mdash; this is our most common stair-tread scenario. We bring sample treads in your floor&rsquo;s species and stain, hold them up to your existing floor in natural light, and stain-match on-site if the floor is site-finished or source factory-matching if the floor is pre-finished engineered hardwood. The transition between downstairs and stairs reads as intentional in normal light."),
        ("How long does the staircase need to be unusable?",
         "Realistically 2&ndash;3 days for a typical 14-tread staircase. We work top-down on day 2 so the bottom of the staircase remains accessible during the install. The whole staircase is usable again by end of day 2 in most cases. For site-finished hardwood treads (with stain and poly), the poly cure adds 24&ndash;48 hours of stay-off-the-stairs time."),
    ]
    post_shell(p4, lede, sections, faqs=faqs, related_links=related)

    # ============================================================================
    # POST 5: Hardwood vs SPC comparison
    # ============================================================================
    p5 = GENERAL_BLOG_POSTS[4]
    lede = (
        "We installed premium engineered hardwood and 22-mil SPC vinyl plank in two "
        "side-by-side Lakewood Ranch homes within the same six-month window: same "
        "neighborhood, same builder, same family configuration, identical square "
        "footage. Three years later, we walked both floors back to see what "
        "actually happened. Here&rsquo;s the field-test result."
    )
    sections = '''
<h2>The two homes</h2>

<p>Both homes are single-family two-story builds in Country Club East at Lakewood Ranch, completed in 2021 by the same regional builder. Both families are 2 adults plus 2 school-age children, both have one medium-sized dog, and both run the AC at 74 degrees year-round. The only meaningful difference: <strong>Home A installed premium European engineered white oak hardwood</strong> (7-inch wide-plank, 4mm wear layer, oil-finished) throughout the main floor in 2022; <strong>Home B installed premium 22-mil SPC vinyl plank</strong> (7-inch wide-plank, wood-look visual, glue-down) in the same footprint, same year.</p>

<p>We installed both. Both homeowners have authorized us to write up the comparison without naming the brands.</p>

<h2>Install cost (2022 dollars)</h2>

<ul>
<li><strong>Home A (engineered hardwood):</strong> $13.50/sq ft installed × 1,800 sq ft = $24,300.</li>
<li><strong>Home B (SPC vinyl plank glue-down):</strong> $6.25/sq ft installed × 1,800 sq ft = $11,250.</li>
<li><strong>Differential:</strong> $13,050. The hardwood floor cost roughly 2.2&times; the SPC floor.</li>
</ul>

<h2>Year-3 condition assessment</h2>

<h3>Home A &mdash; engineered hardwood</h3>
<p>Visible wear at the entry hallway and the dining-to-kitchen transition: light scratches running with the grain in the highest-traffic lines, visible only in raked light from a low angle. The matte oil finish has a slightly burnished look in the same areas &mdash; closer to a satin sheen than the original matte. No gapping, no cupping, no buckling. One spot near the kitchen island where a dropped pan caused a 3/4-inch dent in the wood; the rest of the floor is otherwise unmarked. The homeowner is happy and reports zero maintenance issues. We&rsquo;ll likely recommend a recoat (light buff with a screen and one coat of oil finish) at year 6 or 7.</p>

<h3>Home B &mdash; SPC vinyl plank</h3>
<p>No visible wear in any traffic line. No scratches. No dents from dropped objects. The visual is unchanged from install day. The dog&rsquo;s nails leave no marks. The kids&rsquo; toys leave no marks. The floor looks exactly like the day we glued it down. The homeowner reports zero maintenance issues, sweeps and damp-mops once a week, and has never paid attention to the floor.</p>

<h2>What this tells us</h2>

<p>The SPC floor is, on every measurable durability metric, the more practical floor for a family with kids and a dog. The hardwood floor is, on every aesthetic metric, the more beautiful floor &mdash; reads as real wood from every angle, in every light, at every distance, and has a tactile warmth underfoot that no vinyl plank can match.</p>

<p>Your decision depends almost entirely on which one matters more to you. Both floors will last 15&ndash;25 years in this kind of family use. The hardwood will need one refinish during that span, costing $4&ndash;$6 per square foot or roughly $8,000 on this 1,800 sq ft footprint. The SPC will need zero maintenance beyond cleaning.</p>

<blockquote>The right question isn&rsquo;t &lsquo;which is better.&rsquo; It&rsquo;s &lsquo;which one&rsquo;s downsides can I live with.&rsquo; Hardwood&rsquo;s downsides are wear marks and the eventual refinish. SPC&rsquo;s downsides are the fact that it isn&rsquo;t wood, no matter how good the visual.</blockquote>

<h2>Cost comparison over 20 years</h2>

<table class="post-table">
<thead><tr><th>Cost Item</th><th>Engineered Hardwood</th><th>SPC Vinyl Plank</th></tr></thead>
<tbody>
<tr><td>Install (2022 pricing, 1,800 sq ft)</td><td><strong>$24,300</strong></td><td><strong>$11,250</strong></td></tr>
<tr><td>Annual maintenance (cleaning)</td><td><strong>$0</strong></td><td><strong>$0</strong></td></tr>
<tr><td>Recoat at year 7&ndash;8 ($2 per sq ft)</td><td><strong>$3,600</strong></td><td><strong>$0</strong></td></tr>
<tr><td>Full sand-and-refinish at year 14&ndash;15 ($4.50/sq ft)</td><td><strong>$8,100</strong></td><td><strong>$0</strong></td></tr>
<tr><td>20-year total cost of ownership</td><td><strong>$36,000</strong></td><td><strong>$11,250</strong></td></tr>
<tr><td>Estimated value at year 20</td><td><strong>Still original wood, refinishable</strong></td><td><strong>Likely replacement needed</strong></td></tr>
</tbody>
</table>

<h2>When we recommend each</h2>

<h3>Recommend hardwood when</h3>
<ul>
<li>The aesthetic of real wood matters to the homeowner more than the maintenance schedule.</li>
<li>The home is upper-mid-range or higher, where flooring authenticity affects resale value.</li>
<li>No pets, or only well-behaved pets that don&rsquo;t scratch the floor.</li>
<li>The home is a long-term residence (10+ years), where the refinish cycle is just part of ownership.</li>
</ul>

<h3>Recommend SPC vinyl plank when</h3>
<ul>
<li>The home has young children, multiple pets, or any factor that creates intense day-to-day floor traffic.</li>
<li>Budget matters and the per-square-foot differential affects the project.</li>
<li>The home is on a slab and the moisture readings are borderline (SPC handles slab moisture better than even properly-installed engineered hardwood).</li>
<li>The home is a short-term rental, an investment property, or a secondary residence with closure cycles.</li>
<li>Anywhere a kitchen, full bath, or laundry adjoins (SPC handles water without question; even engineered hardwood doesn&rsquo;t).</li>
</ul>

<div class="post-key-takeaway">
<strong>The Bottom Line, From Three Years of Field Data</strong>
SPC vinyl plank at the premium tier ($5&ndash;$7 per square foot installed) is the more practical floor for almost every Tampa Bay family with kids, pets, or budget constraints. Engineered hardwood at the premium tier ($10&ndash;$14 per square foot installed) is the more beautiful floor for owners who value real wood and accept the 7-year recoat / 14-year refinish cycle. Both are great. Pick the trade-off you can live with for two decades.
</div>
'''
    related = [
        ("/hardwood-flooring/lakewood-ranch/", "Hardwood Flooring in Lakewood Ranch"),
        ("/vinyl-plank-flooring/lakewood-ranch/", "Vinyl Plank in Lakewood Ranch"),
        ("/blog/best-flooring-gulf-coast-humidity/", "Gulf Coast Humidity Guide"),
    ]
    faqs = [
        ("Does engineered hardwood help home resale value more than SPC?",
         "Marginally, yes, in upper-bracket homes where buyers value authenticity. In starter homes and most mid-range homes, well-installed premium SPC reads as &lsquo;new flooring&rsquo; and the resale impact is identical. The exception: in $1M+ luxury homes in Tampa Bay (downtown St. Petersburg, Bayshore, Hyde Park, Siesta Key, Longboat Key), authentic engineered hardwood is the expectation and SPC is recognized as a downgrade even when it&rsquo;s beautifully installed."),
        ("Can I install SPC and hardwood in the same house, in different rooms?",
         "Yes &mdash; this is actually one of our most-recommended approaches: engineered hardwood in formal living, dining, and bedroom areas; SPC vinyl plank in kitchens, mudrooms, and laundry rooms. The transition strip between the two materials is the entire visible difference. Pick a transition strip color that bridges the two products and the transition reads as intentional design rather than budget compromise."),
    ]
    post_shell(p5, lede, sections, faqs=faqs, related_links=related)


# ============================================================================
# 48 COST POSTS — one per service x city combination
# ============================================================================
def build_cost_posts():
    for post in COST_BLOG_POSTS:
        svc = SERVICES[post["service_slug"]]
        city = CITIES[post["city_slug"]]
        kw = post["keyword"]
        city_name = city["name"]
        svc_name = svc["name"]
        svc_short = svc["short"]

        lede = (
            f"What does {kw} actually cost in {city_name}, FL in 2026? "
            f"After {BUSINESS['unique_stat_number']} installs across Tampa Bay, here&rsquo;s the honest "
            f"pricing &mdash; by material tier, by install type, with the {city_name}-specific factors "
            f"that drive the numbers up or down."
        )

        # Body sections (assembled to hit 2000+ words)
        sections = f'''
<h2>The honest cost ranges for {kw} in {city_name}</h2>

<p>{svc["intro_long_p1"]}</p>

<p><strong>What that translates to in {city_name} dollar terms:</strong> for a typical 1,200&ndash;1,500 sq ft install at the most-common tier, expect to budget <strong>$5&ndash;$9 per square foot installed</strong> &mdash; or roughly <strong>$6,000&ndash;$13,500 total</strong> for the typical {city_name} living-area install. Premium options run higher; budget options run lower; the table below has the full range.</p>

<table class="post-table">
<thead><tr><th>{svc_short} Tier</th><th>Installed Cost / Sq Ft</th><th>Typical Use</th></tr></thead>
<tbody>
{''.join(f"<tr><td>{label}</td><td><strong>{price}</strong></td><td>{note}</td></tr>" for label, price, note in svc["pricing_rows"])}
</tbody>
</table>

<h2>Why pricing varies in {city_name} specifically</h2>

<p>{city["context_short"]} That market profile drives the local cost dynamics in three specific ways:</p>

<ul>
<li><strong>Property type and age.</strong> {city["primary_market"]}. Each property type has its own prep requirements &mdash; older homes often need self-leveling, subfloor repair, or vapor-barrier installation that newer homes don&rsquo;t. Budget extra for the first &mdash; $0.50&ndash;$2 per square foot in additional prep depending on what we find.</li>

<li><strong>Humidity exposure.</strong> {city["humidity_note"]} For {kw} specifically, this affects which products we&rsquo;ll recommend (some products genuinely don&rsquo;t belong in this market) and what the install timeline includes &mdash; full manufacturer-spec acclimation isn&rsquo;t optional, and we never skip it.</li>

<li><strong>Access and HOA logistics.</strong> Many of {city_name}&rsquo;s gated communities ({city["neighborhoods"][0]}, {city["neighborhoods"][1] if len(city["neighborhoods"])>1 else city["neighborhoods"][0]}, {city["neighborhoods"][2] if len(city["neighborhoods"])>2 else city["neighborhoods"][0]}) have HOA flooring rules that affect both the schedule (weekday-only work, quiet hours) and the materials (sound-attenuation underlayment required in second-floor condos, fire-rated assemblies in some buildings). We handle the HOA communication, but the requirements affect the quote.</li>
</ul>

<h2>What your money buys at each tier (in {city_name})</h2>

<h3>Budget tier ({svc["pricing_rows"][0][1]})</h3>
<p>{svc["pricing_rows"][0][2]}. This is the entry point we recommend for rental properties, secondary spaces (bonus rooms, dens, guest bedrooms), and value-engineered primary installs where the budget genuinely doesn&rsquo;t allow the mid-tier. The quality is real &mdash; this isn&rsquo;t bait-and-switch &mdash; but the visuals and the longevity step up dramatically as you move up tiers.</p>

<h3>Mid-range tier (the most-installed)</h3>
<p>Most {city_name} primary residences land here. The visuals are excellent, the durability is appropriate for family use, and the warranty terms from the manufacturer are generous. This is where the value-per-dollar curve hits its sweet spot for most homes.</p>

<h3>Premium tier</h3>
<p>For homeowners who want the best material the category offers, or who have specific requirements (premium aesthetics, top-tier durability, lifetime warranty terms, specific brand alignment). Premium-tier {svc_short.lower()} in {city_name} is most-installed in the gated communities along {city["neighborhoods"][0]} and the higher-end neighborhoods in {city["county"]}.</p>

<h2>What the install timeline looks like in {city_name}</h2>

<p>Typical {city_name} install schedule for a 1,200&ndash;1,500 sq ft {svc_short.lower()} project:</p>

<ul>
<li><strong>Day 0 (3&ndash;7 days before install):</strong> Material delivery to site. Boxes opened for acclimation. Digital hygrometer running.</li>
<li><strong>Day 1:</strong> Final acclimation reading. Furniture move-out by you or by us (if scoped). Floor protection runners laid in non-work areas. Demolition of existing flooring begins.</li>
<li><strong>Day 2:</strong> Subfloor inspection, moisture readings, self-leveling where needed. Vapor barrier on slab installs.</li>
<li><strong>Day 3&ndash;4:</strong> Install of new flooring. Two installers, same crew, full days.</li>
<li><strong>Day 5:</strong> Transitions, trim, baseboard reset, final clean, walk-through. 47-point checklist signed off.</li>
</ul>

<p>Larger installs scale roughly linearly: a 2,500&ndash;3,500 sq ft whole-home {svc_short.lower()} install typically runs 8&ndash;12 working days. Tile installs add 2&ndash;3 days for mortar cure time. Site-finished hardwood adds 2&ndash;3 days for stain and polyurethane cure.</p>

<h2>The {city_name} neighborhoods where we install most {svc_short.lower()}</h2>

<p>We&rsquo;ve installed {svc_short.lower()} across most {city_name} neighborhoods, but the highest concentration in 2025&ndash;2026 has been in:</p>

<ul>
{''.join(f"<li><strong>{n}</strong></li>" for n in city["neighborhoods"][:6])}
</ul>

<p>Plus dozens of other neighborhoods, subdivisions, and historic districts across {city["county"]}. If your neighborhood isn&rsquo;t on this list, we&rsquo;ve almost certainly worked it &mdash; we just haven&rsquo;t logged it as a top-6 for the year.</p>

<h2>What can change your {city_name} quote &mdash; up or down</h2>

<h3>Drives the price up</h3>
<ul>
<li>Subfloor that needs self-leveling (common in older {city_name} homes built before 1985) &mdash; +$200&ndash;$600 per affected room.</li>
<li>Vapor barrier on slab where moisture readings warrant &mdash; +$0.40&ndash;$1 per square foot.</li>
<li>Old flooring removal (carpet, tile, sheet vinyl) &mdash; +$1.50&ndash;$3 per square foot.</li>
<li>HVAC ducting cleanout and reinstall (more common in older homes) &mdash; +$200&ndash;$500.</li>
<li>Stair-tread installation as part of the same project &mdash; per-tread pricing as noted in our stair-tread tier table.</li>
</ul>

<h3>Drives the price down</h3>
<ul>
<li>Whole-home installs (2,500+ sq ft) typically get a 5&ndash;10% per-square-foot discount because of efficiency in scheduling and material delivery.</li>
<li>Schedule flexibility &mdash; if we can install during a slower week (typically June&ndash;August or January&ndash;February), we sometimes offer modest schedule-flexibility pricing.</li>
<li>Bring-your-own-material installs &mdash; we can install material you&rsquo;ve purchased separately at a labor-only rate, though we encourage you to source through our supplier network for warranty alignment and quality control.</li>
</ul>

<div class="post-key-takeaway">
<strong>The Honest Answer for {city_name}, FL in 2026</strong>
A typical 1,200&ndash;1,500 sq ft {kw} install in {city_name} costs $6,000&ndash;$13,500 at the most-common tiers, all-in. The premium tier runs higher (up to $20,000+ on the same footprint for top-end product); the budget tier runs lower ($3,500&ndash;$6,000) but with real trade-offs in longevity. Most {city_name} homeowners we work with land in the mid-tier and stay there for 10&ndash;15 years before they think about replacement.
</div>

<h2>How to get a quote that&rsquo;s actually useful</h2>

<p>Three things make a {city_name} {kw} quote useful:</p>

<ol>
<li><strong>An in-home measure.</strong> Tape-measure-on-photos doesn&rsquo;t work. We measure on site, in your home, in roughly 30&ndash;45 minutes for most jobs.</li>
<li><strong>A baseline moisture reading on your subfloor.</strong> We pull one during the measure, on slab and plywood alike. The reading affects what we can and can&rsquo;t recommend &mdash; for some products it&rsquo;s a make-or-break number.</li>
<li><strong>A line-itemized written quote.</strong> Material, labor, demo, transitions, baseboards, prep, waste percentage &mdash; all itemized separately. Anyone giving you a one-number quote is hiding something or has bad accounting.</li>
</ol>

<p>We send written quotes within 24 hours of the in-home measure, and they&rsquo;re valid for 30 days. <a href="/contact/#quote">Request a {city_name} {kw} estimate</a> or call <a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a>.</p>
'''
        related = [
            (f"/{post['service_slug']}/{post['city_slug']}/", f"{svc_short} in {city_name} · Service Page"),
            (f"/{post['city_slug']}/", f"All Flooring in {city_name}, FL"),
        ]
        # Add 1 other cost post in same city
        other_in_city = [p for p in COST_BLOG_POSTS if p["city_slug"] == post["city_slug"] and p["slug"] != post["slug"]]
        if other_in_city:
            related.append((f"/blog/{other_in_city[0]['slug']}/", other_in_city[0]["title"]))

        faqs = svc["faqs"][:2]  # use first 2 service FAQs
        # Add a city-specific FAQ
        faqs = list(faqs) + [
            (f"Do you do quotes specifically for {city_name}?",
             f"Yes &mdash; every {city_name} project gets an in-home measure, a baseline moisture reading on the subfloor, and a written line-itemized quote within 24 hours. We&rsquo;re based in east {BUSINESS['city']} and work {city_name} every week, so the schedule turnaround is fast."),
        ]
        post_shell(post, lede, sections, faqs=faqs, related_links=related)


# ============================================================================
# BLOG INDEX
# ============================================================================
def build_blog_index():
    URL = f"{SITE}/blog/"
    TITLE = f"Tampa Bay Flooring Journal · Napa's Flooring"  # 47
    DESC = (
        f"Practical Tampa Bay flooring guides: cost-by-city, humidity-tolerant products, "
        f"hardwood-vs-LVP, short-term-rental playbook, refinishing reality check. "
        f"Written by installers."
    )[:158]

    schemas = [
        schema_breadcrumb([("Home", SITE+"/"), ("Journal", URL)]),
        schema_webpage(URL, TITLE, DESC),
        schema_local_business(URL, "Napa's Flooring Journal"),
    ]
    bc = breadcrumbs([("Home","/"), ("Journal", None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">The Napa&rsquo;s Journal · Updated Monthly</span>
    <h1>Field notes from <em>under the floor</em>.</h1>
    <p class="page-hero-sub">Practical guides for Tampa Bay flooring buyers &mdash; written by installers, not by SEO writers. Cost data, humidity guides, the brutal honest comparisons. {len(GENERAL_BLOG_POSTS) + len(COST_BLOG_POSTS)} articles and counting.</p>
  </div>
</section>'''

    # Combine all posts, sorted by date desc
    combined = list(GENERAL_BLOG_POSTS) + list(COST_BLOG_POSTS)
    combined.sort(key=lambda p: p["date_published"], reverse=True)

    # FEATURED: 5 general posts
    featured_html = ""
    for p in GENERAL_BLOG_POSTS:
        featured_html += f'''<a href="/blog/{p["slug"]}/" class="blog-card">
  <div class="blog-card-meta">
    <span>● {p["category"]}</span>
    <span>{p["date_published"][:7]}</span>
  </div>
  <h3>{p["title"]}</h3>
  <span class="blog-card-cta">Read Field Notes</span>
</a>'''

    featured = f'''<section class="services-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">Featured Reading</span>
        <h2>Five long-form pieces, <em>read-them-first</em>.</h2>
        <div class="section-head-text"><p>The handful of articles that cover the biggest decisions Tampa Bay flooring buyers face. Start here.</p></div>
      </div>
    </div>
    <div class="blog-grid">{featured_html}</div>
  </div>
</section>'''

    # COST POSTS BY CITY
    by_city_html = ""
    for cslug, c in CITIES.items():
        city_posts = [p for p in COST_BLOG_POSTS if p["city_slug"] == cslug]
        items = "".join(f'<li><a href="/blog/{p["slug"]}/">{p["title"]}</a></li>' for p in city_posts)
        by_city_html += f'''<div class="related-box" style="margin:0">
  <div class="related-box-label">Cost Guides · {c["name"]}, FL</div>
  <h3>{svc_count_label(cslug)}</h3>
  <ul>{items}</ul>
</div>'''

    cost_section = f'''<section style="background:var(--paper-deep)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label">Cost Guides · 48 Articles · 6 Services × 8 Cities</span>
        <h2>What it actually costs<em>, by city</em>.</h2>
        <div class="section-head-text"><p>One cost guide per service, per city &mdash; with real {2026} Tampa Bay pricing, city-specific factors, and what changes the number up or down.</p></div>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px">{by_city_html}</div>
  </div>
</section>'''

    body = "\n".join([hero, featured, cost_section, f'<div class="container">{contact_banner()}</div>', final_cta()])

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("/home/claude/napas/blog/index.html", head_html, header(active="blog"), body, breadcrumbs_html=bc)
    print("Wrote /blog/index.html")


def svc_count_label(city_slug):
    """Small helper for the city cost-guide block heading."""
    name = CITIES[city_slug]["name"]
    return f"{name} pricing · 6 services."


if __name__ == "__main__":
    print("Building 5 general blog posts…")
    build_general_posts()
    print(f"  ✓ Built {len(GENERAL_BLOG_POSTS)} general posts")
    print(f"\nBuilding {len(COST_BLOG_POSTS)} cost posts…")
    build_cost_posts()
    print(f"  ✓ Built {len(COST_BLOG_POSTS)} cost posts")
    print("\nBuilding blog index…")
    build_blog_index()
    print(f"\nTotal blog pages: {len(ALL_POSTS) + 1}")
