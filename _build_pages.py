#!/usr/bin/env python3
"""Generate /about, /contact, /faq, /financing, /warranty, /thanks and /404.html"""
import os, sys
sys.path.insert(0, '/home/claude/napas')
from _gen import *

# ============================================================================
# ABOUT
# ============================================================================
def build_about():
    URL = f"{SITE}/about/"
    TITLE = f"About Napa's Flooring · Tampa Bay's Craft-First Crew"  # 53
    DESC = (
        f"Meet Napa's — a small, craft-first flooring crew working out of east Bradenton, "
        f"serving Tampa Bay since {BUSINESS['year_founded']}. The standards we hold, the work we "
        f"refuse, the warranty in writing."
    )[:158]

    schemas = [
        schema_webpage(URL, "About Napa's Flooring", DESC),
        schema_organization(),
        schema_breadcrumb([("Home", SITE+"/"), ("About", URL)]),
    ]

    bc = breadcrumbs([("Home","/"),("About",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">About · Crew Profile</span>
    <h1>Built around <em>two installers</em>, one truck,<br>and the work that&rsquo;s in front of us.</h1>
    <p class="page-hero-sub">Napa&rsquo;s is a small, deliberately small, flooring company. We answer our own phone, we measure our own jobs, and the same two people who walk your home for the estimate are the same two who install your floor.</p>
    <div class="page-hero-trust">
      <span>Est. {BUSINESS["year_founded"]}</span>
      <span>{BUSINESS["unique_stat_full"]}</span>
      <span>{BUSINESS["rating"]}★ · {BUSINESS["review_count"]} reviews</span>
      <span>12-month warranty</span>
    </div>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">
      <p class="post-lede">Napa&rsquo;s Flooring opened in {BUSINESS["year_founded"]} for one reason and one reason only: the lead installer was tired of being the lowest paid person on a jobsite where the people doing the worst work were making the most money. The math didn&rsquo;t add up. So he stopped showing up to the bad jobs, started taking the good ones direct, and put his name on the truck.</p>

      <p>That&rsquo;s the entire founding story. There isn&rsquo;t a Silicon Valley exit, a family multi-generation legacy, or a marketing-degree backstory. There&rsquo;s a tradesman who got fed up with corners being cut on his own work, and a crew that&rsquo;s grown around him &mdash; slowly, by referral &mdash; doing flooring the way it was supposed to be done in the first place.</p>

      <h2>What we install &mdash; and what we won&rsquo;t</h2>

      <p>We install <strong>solid and engineered hardwood</strong>, <strong>luxury vinyl plank and SPC</strong>, <strong>porcelain and natural-stone tile</strong>, <strong>premium laminate</strong>, and <strong>stair treads</strong> in every species and grade those four formats come in. We also do <strong>full repair-and-restoration work</strong> &mdash; water damage, pet damage, plank lacing, sand-and-refinish on pre-war and mid-century oak.</p>

      <p>What we don&rsquo;t do is sell you the cheapest possible product to win the bid. We carry samples across every price tier, we tell you what each tier&rsquo;s honest pros and cons are, and we let you pick. If your budget points to a builder-grade laminate over a slab without a vapor barrier, we&rsquo;ll walk away from the job. There&rsquo;s no version of that floor that doesn&rsquo;t fail in five years, and we&rsquo;re not going to put our name on it.</p>

      <h2>Where we work</h2>

      <p>Our service area is the Tampa Bay &mdash; Sarasota corridor: <a href="/bradenton/">Bradenton</a>, <a href="/lakewood-ranch/">Lakewood Ranch</a>, <a href="/palmetto/">Palmetto</a>, <a href="/parrish/">Parrish</a>, <a href="/sarasota/">Sarasota</a>, <a href="/st-petersburg/">St. Petersburg</a>, <a href="/tampa/">Tampa</a>, and <a href="/venice/">Venice</a>. The crew is based in east {BUSINESS["city"]}, in the 34212 ZIP just south of SR-64, and we keep our work radius tight on purpose: we&rsquo;d rather drive 20 minutes from home and have the homeowner&rsquo;s number on speed dial during the install, than drive 90 minutes and lose half the day on logistics.</p>

      <h2>The crew, the truck, and what shows up</h2>

      <p>Most of our installs are two installers, occasionally three for tile-heavy jobs. Same two people, every day, until the work is done. The white box truck shows up in the driveway at 7:15 AM, the floor mats and runners come out first, the air filter swap on the HVAC system happens before we open a single box of material. We don&rsquo;t leave dust everywhere and we don&rsquo;t leave tools out overnight. The site is broom-clean at the end of every day &mdash; including the day we&rsquo;re installing baseboards over fresh-cut shoe mold and there&rsquo;s sawdust everywhere five minutes earlier.</p>

      <div class="post-key-takeaway">
        <strong>Our Promise — In Plain English</strong>
        We&rsquo;ll measure your floor, talk through what would actually work in your home, and email you a written, line-itemized quote within 24 hours of the visit. If we get the job, the same two installers who measured will be the ones who install. The job will be done on the date we said. The floor will pass our 47-point standard before we ask you to pay. The 12-month workmanship warranty is in writing.
      </div>

      <h2>Where the &ldquo;Napa&rdquo; came from</h2>

      <p>People assume it&rsquo;s the wine country. It isn&rsquo;t. It&rsquo;s a family nickname &mdash; <em>napa</em> &mdash; that goes back two generations on the owner&rsquo;s mother&rsquo;s side and means something approximately like &ldquo;the patient one&rdquo; in the dialect she grew up speaking. The kind of patient that lets a hardwood plank acclimate for 72 hours when the competition acclimates it for zero. The kind of patient that measures the slab flatness three times before opening a single tile box.</p>

      <p>That&rsquo;s the company.</p>

      <h2>Our credentials, in writing</h2>

      <ul>
        <li><strong>Licensed &amp; Insured</strong> &mdash; general liability and workman&rsquo;s comp in force on every job. Certificates available on request before contract signing.</li>
        <li><strong>NWFA-aligned standards</strong> &mdash; we follow National Wood Flooring Association installation guidelines for hardwood and engineered hardwood.</li>
        <li><strong>TCNA Handbook-aligned standards</strong> &mdash; we follow Tile Council of North America substrate, mortar, and crack-isolation specs on every tile install.</li>
        <li><strong>Florida Building Code compliance</strong> &mdash; for waterproofed shower assemblies, moisture-barrier installs on slab, and any framing work.</li>
        <li><strong>Manufacturer-certified installer</strong> on multiple SPC and engineered hardwood lines (we&rsquo;ll list specifics during the estimate based on the product you&rsquo;re considering).</li>
      </ul>

      <h2>How to get a quote</h2>

      <p>Three ways: <a href="{TEL_LINK}">call or text {BUSINESS["phone_display"]}</a>, <a href="mailto:{BUSINESS["email"]}">email us at {BUSINESS["email"]}</a>, or <a href="/contact/#quote">fill out the form on our contact page</a>. We respond to every inquiry within four business hours during the day, eight hours after-hours, and we&rsquo;ll schedule a free in-home measure within 24-48 hours of first contact in most cases.</p>
    </article>
  </div>
</section>

{final_cta(headline="Meet the crew. See the work.", sub="Free in-home measure. Written quote within 24 hours. No high-pressure sales, no obligation, no tricks.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas, og_type="article")
    body = body_content
    write_page("/home/claude/napas/about/index.html", head_html, header(active="about"), body, breadcrumbs_html=bc)
    print("Wrote /about/index.html")


# ============================================================================
# CONTACT
# ============================================================================
def build_contact():
    URL = f"{SITE}/contact/"
    TITLE = f"Contact Napa's Flooring · Free Quote · {BUSINESS['city']} FL"  # 60
    DESC = (
        f"Get a free, written flooring estimate within 24 hours. Call {BUSINESS['phone_display']}, "
        f"email {BUSINESS['email']}, or send your project details below. Serving all of Tampa Bay."
    )[:158]

    schemas = [
        schema_webpage(URL, "Contact Napa's Flooring", DESC),
        schema_local_business(URL, "Contact Napa's Flooring"),
        schema_breadcrumb([("Home", SITE+"/"), ("Contact", URL)]),
    ]
    bc = breadcrumbs([("Home","/"),("Contact",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Contact · Free Estimate · 24-Hour Response</span>
    <h1>Call us<span class="stop">.</span> Text us<span class="stop">.</span><br>Or send a <em>note</em>.</h1>
    <p class="page-hero-sub">Free estimates, every weekday and most weekends. We respond to every inquiry — typically within four business hours during the workday, eight hours after-hours.</p>
  </div>
</section>'''

    contact_grid = f'''<section>
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start">

      <div>
        <span class="mono-label">Direct Lines</span>
        <h2 style="font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.1;letter-spacing:-.02em;margin:.6rem 0 1.6rem">The fastest way is to <em>just call</em>.</h2>

        <div style="display:flex;flex-direction:column;gap:20px;margin-bottom:2rem">
          <a href="{TEL_LINK}" style="text-decoration:none;color:var(--ink);display:flex;align-items:baseline;gap:18px;padding-bottom:18px;border-bottom:1px solid var(--rule)">
            <span style="font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);font-weight:600">Phone / Text</span>
            <span style="font-family:var(--font-display);font-size:clamp(1.6rem,3vw,2rem);color:var(--ink);letter-spacing:-.02em;flex-grow:1;text-align:right">{BUSINESS["phone_display"]}</span>
          </a>
          <a href="mailto:{BUSINESS["email"]}" style="text-decoration:none;color:var(--ink);display:flex;align-items:baseline;gap:18px;padding-bottom:18px;border-bottom:1px solid var(--rule)">
            <span style="font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);font-weight:600">Email</span>
            <span style="font-family:var(--font-editorial);font-size:clamp(1.1rem,2vw,1.4rem);color:var(--ink);font-style:italic;flex-grow:1;text-align:right">{BUSINESS["email"]}</span>
          </a>
          <a href="{WA_LINK}" target="_blank" rel="noopener" style="text-decoration:none;color:var(--ink);display:flex;align-items:baseline;gap:18px;padding-bottom:18px;border-bottom:1px solid var(--rule)">
            <span style="font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);font-weight:600">WhatsApp</span>
            <span style="font-family:var(--font-mono);font-size:1rem;color:var(--ink);flex-grow:1;text-align:right">{BUSINESS["phone_display"]}</span>
          </a>
        </div>

        <span class="mono-label">Base of Operations</span>
        <p style="margin:.6rem 0 1.6rem;font-size:1.05rem;line-height:1.6">East {BUSINESS["city"]}, {BUSINESS["state"]} {BUSINESS["zip"]} &mdash; just south of SR-64, in the 34212 ZIP. We serve every city on our list within a 60-mile radius and travel further by quote.</p>

        <span class="mono-label">Hours</span>
        <table style="margin-top:.8rem;width:100%;font-family:var(--font-mono);font-size:.85rem;border-collapse:collapse">
          {''.join(f"<tr style='border-bottom:1px solid var(--rule)'><td style='padding:9px 0;font-weight:600'>{d}</td><td style='padding:9px 0;text-align:right;color:var(--gray)'>{o}&ndash;{c}</td></tr>" for d,o,c in BUSINESS["hours"])}
        </table>
      </div>

      <div id="quote">
        <span class="mono-label">Quote Request</span>
        <h2 style="font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.1;letter-spacing:-.02em;margin:.6rem 0 1.6rem">Or send us the <em>details</em>.</h2>
        <p style="font-size:1rem;color:var(--gray);margin-bottom:1.4rem">Tell us about the space and the rough timeline. The more detail, the better the first response. We&rsquo;ll reply within 4 business hours.</p>

        <form class="form-wrap" action="https://api.web3forms.com/submit" method="POST">
          <input type="hidden" name="access_key" value="d98ab5ee-2d5c-4932-bf67-874a4c35a5ed">
          <input type="hidden" name="subject" value="New Quote Request — napasflooring.com">
          <input type="hidden" name="from_name" value="Napa's Flooring Website">
          <input type="hidden" name="redirect" value="https://napasflooring.com/thanks/">
          <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
          <div class="form-grid">
            <label>Name<input type="text" name="name" required></label>
            <label>Phone<input type="tel" name="phone" required></label>
            <label class="full">Email<input type="email" name="email" required></label>
            <label>City<select name="city" required>
              <option value="">Select…</option>
              {''.join(f'<option value="{c["name"]}">{c["name"]}</option>' for c in CITIES.values())}
              <option value="Other">Other / Not Listed</option>
            </select></label>
            <label>Approx. Size<select name="size">
              <option value="">Select…</option>
              <option>Under 500 sq ft</option>
              <option>500 – 1,000 sq ft</option>
              <option>1,000 – 2,000 sq ft</option>
              <option>2,000 – 3,500 sq ft</option>
              <option>3,500+ sq ft</option>
              <option>Just a staircase</option>
              <option>Repair only</option>
            </select></label>
            <label class="full">Service Interest<select name="service">
              <option value="">Select…</option>
              {''.join(f'<option value="{s["name"]}">{s["name"]}</option>' for s in SERVICES.values())}
              <option>Not sure yet</option>
            </select></label>
            <label class="full">Tell us about the project<textarea name="message" placeholder="Rooms, current floor, timeline, anything else worth mentioning."></textarea></label>
            <button type="submit" class="btn btn-orange form-submit">Send Request <span class="btn-arrow"></span></button>
          </div>
        </form>
      </div>

    </div>
  </div>
</section>

{contact_banner("Prefer to talk it through?", "Call or text — same number, same person picks up.")}

{final_cta()}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("/home/claude/napas/contact/index.html", head_html, header(active="contact"), contact_grid, breadcrumbs_html=bc)
    print("Wrote /contact/index.html")


# ============================================================================
# FAQ — site-wide FAQ
# ============================================================================
def build_faq():
    URL = f"{SITE}/faq/"
    TITLE = f"Flooring FAQ · Tampa Bay · Napa's Flooring"  # 47
    DESC = (
        f"Answers to the questions Tampa Bay homeowners ask most: install costs, "
        f"timelines, warranty, what holds up to Florida humidity, and which floor fits "
        f"your room. {BUSINESS['rating']}★ rated."
    )[:158]

    site_faqs = [
        ("How quickly can you start a job?", f"Most {BUSINESS['city']}-area projects can start within 2–4 weeks of the signed estimate. Smaller jobs (single rooms, staircases, repair work) often slot in inside a week. Larger whole-home installs usually book 4–6 weeks out, depending on the season and material lead times. We&rsquo;ll give you a real timeline in the written quote, not a guess."),
        ("Do you provide free estimates?", "Yes — every estimate is free, in-home, and no-obligation. We measure on site, talk through product options at every price tier, take baseline moisture readings, and email a written line-itemized quote within 24 hours of the visit. Estimates are valid for 30 days."),
        ("What flooring works best for Florida humidity?", "Year-round: engineered hardwood (not solid), SPC luxury vinyl plank, and porcelain tile. Each one has a slot it&rsquo;s best in: SPC for primary living areas and anywhere wet, engineered hardwood for bedrooms and formal spaces where you want real wood, porcelain tile for kitchens, baths, and pool decks. We never recommend solid hardwood for slab-on-grade homes, regardless of how it&rsquo;s sealed."),
        ("Are you licensed and insured?", "Yes. Florida doesn&rsquo;t require a state license for most residential flooring under $25,000, but we carry general liability and workman&rsquo;s comp insurance on every job. Certificates of insurance (COIs) are available on request, and we&rsquo;ll provide them to your HOA, your condo association, or your home insurer before we start."),
        ("How long does an install take?", "Rough rule of thumb: a 1,000–1,500 sq ft floating LVP or laminate install runs 2–3 days. The same size engineered hardwood runs 3–4 days. Tile usually runs 5–8 days because of mortar cure time. A 14-tread staircase runs 2–3 days. Whole-home reflooring jobs (3,000+ sq ft) typically run 8–14 working days. Real timeline goes in the written quote."),
        ("Do you offer financing?", "We don&rsquo;t run financing in-house, but we work with several third-party home-improvement lenders that offer 0% promotional financing on jobs over $2,500. We can walk you through the options at the estimate. See our <a href='/financing/'>financing page</a> for details."),
        ("What&rsquo;s included in the warranty?", "Every install carries a written 12-month workmanship warranty on the labor &mdash; we cover squeaks, lippage, plank lift, grout cracks, and anything else attributable to install quality. The material itself is covered by the manufacturer&rsquo;s warranty (which varies by product and which we&rsquo;ll explain). Details on our <a href='/warranty/'>warranty page</a>."),
        ("Do you remove and haul away old flooring?", "Yes &mdash; flooring demo and haul-away is included in every estimate at a per-square-foot rate. We protect your driveway, your landscaping, and your interior trim during demo. Old carpet, sheet vinyl, tile, and laminate all get hauled to the appropriate recycling or disposal facility on the day of removal."),
        ("Can you move furniture and reset toilets / appliances?", "Yes. Toilet pull-and-reset, refrigerator and dishwasher moves, and standard furniture moves are included in the install quote. Pianos, gun safes, very heavy custom built-ins, and anything fragile or high-value (antiques, art, large aquariums) are excluded unless specifically discussed. We&rsquo;ll talk through exclusions at the estimate."),
        ("Do you work with property managers and rental owners?", "Yes &mdash; especially for short-term rentals on Anna Maria Island, Siesta Key, Lido Key, and the keys around Venice. We have a quick-turnaround SPC vinyl install standard for STR properties that fits inside a one-week vacancy window. We invoice direct to the property manager or the owner depending on preference."),
    ]

    schemas = [
        schema_faqpage(site_faqs),
        schema_breadcrumb([("Home", SITE+"/"), ("FAQ", URL)]),
        schema_local_business(URL, "Napa's Flooring FAQ"),
    ]
    bc = breadcrumbs([("Home","/"),("FAQ",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Frequently Asked · Tampa Bay Flooring</span>
    <h1>Real questions<span class="stop">.</span><br><em>Real answers</em>, in writing.</h1>
    <p class="page-hero-sub">Ten of the most common questions we get from Tampa Bay homeowners about flooring installs, materials, timelines, warranty, and process.</p>
  </div>
</section>'''

    faq_html = faq_section(site_faqs, headline="Everything we get asked, weekly.", label="Site-Wide FAQ")
    faq_html = faq_html.replace('<div class="section-head-num">07</div>', '<div class="section-head-num">01</div>')

    body = hero + faq_html + f'<div class="container">{contact_banner()}</div>' + final_cta()
    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("/home/claude/napas/faq/index.html", head_html, header(active=""), body, breadcrumbs_html=bc)
    print("Wrote /faq/index.html")


# ============================================================================
# FINANCING
# ============================================================================
def build_financing():
    URL = f"{SITE}/financing/"
    TITLE = f"Flooring Financing · 0% Options · Napa's Flooring"  # 53
    DESC = (
        f"Flooring financing options for Tampa Bay homeowners. 0% promotional periods, "
        f"fixed-payment plans, no in-house pressure. Apply through trusted third-party "
        f"lenders."
    )[:158]
    schemas = [
        schema_webpage(URL, "Flooring Financing", DESC),
        schema_breadcrumb([("Home", SITE+"/"), ("Financing", URL)]),
        schema_local_business(URL, "Napa's Flooring Financing Options"),
    ]
    bc = breadcrumbs([("Home","/"),("Financing",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Financing · Independent Third-Party Lenders</span>
    <h1>Pay over time<span class="stop">.</span><br>No <em>in-house pressure</em>.</h1>
    <p class="page-hero-sub">We don&rsquo;t run financing in-house — we don&rsquo;t want to. We work with reputable home-improvement lenders that offer 0% promotional periods and fixed-payment plans on jobs over $2,500.</p>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">
      <p class="post-lede">A good flooring contractor shouldn&rsquo;t also be your bank. We&rsquo;re tradespeople — we install floors, we don&rsquo;t process loan applications. Instead, we partner with two of the most established home-improvement lenders in the country, and we&rsquo;ll walk you through the options on the day of your estimate.</p>

      <h2>Why we don&rsquo;t do in-house financing</h2>
      <p>Most flooring companies that &ldquo;offer financing&rdquo; have a salesperson on commission who steers you toward more expensive product (and more financing) to maximize the contract. We don&rsquo;t. Our installers are paid as installers, not as salespeople, and the financing decision is yours to make with the lender directly &mdash; not with us in the middle.</p>

      <h2>The lenders we work with</h2>

      <h3>Synchrony Home Improvement</h3>
      <p>Synchrony offers 0% APR promotional periods (typically 6, 12, 18, or 24 months) for qualified borrowers on home-improvement spending over $2,500. After the promotional period, standard variable APR applies on any unpaid balance. Application is online, decision is instant in most cases, and approved customers can use the line of credit immediately.</p>

      <h3>GreenSky Financial</h3>
      <p>GreenSky offers both promotional 0% plans and fixed-payment installment loans (typically 60-, 84-, or 144-month terms) at fixed APRs. Good option for larger whole-home projects where you want a predictable monthly payment over a longer horizon. Application is online; decision typically within minutes.</p>

      <div class="post-key-takeaway">
        <strong>How to Apply</strong>
        Tell us at the estimate that you&rsquo;re interested in financing. We&rsquo;ll send you the lender&rsquo;s application link the same day. You apply directly with the lender — we don&rsquo;t collect or transmit your financial information. Once approved, the lender pays us directly for the work, and you pay the lender according to your plan&rsquo;s terms.
      </div>

      <h2>Cash, check, and card</h2>
      <p>Of course, we also accept all the usual payment forms: cash, personal check (cleared before final walkthrough), and all major credit cards (Visa, MasterCard, AmEx, Discover) via a Stripe/Square reader on-site. Credit card payments carry a 3% processing surcharge that&rsquo;s itemized in the quote — that&rsquo;s our card processor&rsquo;s fee, not a markup.</p>

      <h2>Insurance claim work</h2>
      <p>Roughly 30% of our repair work is insurance-driven: burst supply lines, dishwasher overflows, washing machine ruptures, ice maker leaks, and hurricane-related water intrusion. We document everything the adjuster needs (moisture readings, scope of damage, dated photos, pre-loss condition where determinable) in the format insurance carriers expect. We don&rsquo;t bill the insurance company directly &mdash; you do &mdash; but our paperwork has been used successfully on dozens of claims with State Farm, Citizens, Universal, USAA, Tower Hill, and others.</p>

      <h2>Standard payment schedule for cash/check jobs</h2>
      <ul>
        <li><strong>Estimate visit</strong> &mdash; free, no payment, no obligation.</li>
        <li><strong>Job signing</strong> &mdash; 10% deposit to lock the start date and order materials.</li>
        <li><strong>Material delivery</strong> &mdash; 30% due, payable on delivery to your site (typically 5–7 days before install).</li>
        <li><strong>Mid-install</strong> &mdash; 30% due at material 50% installed.</li>
        <li><strong>Final walkthrough</strong> &mdash; remaining 30% due on completion, after you&rsquo;ve walked the floor and signed off.</li>
      </ul>

      <p>For financed jobs, the lender handles disbursement to us and you pay them according to your plan&rsquo;s terms &mdash; we don&rsquo;t collect anything from you directly except the optional credit card surcharge if you choose to pay that way.</p>

      <h2>A note on financing math</h2>
      <p>If you take a 0% promotional plan, <strong>pay off the balance before the promo period ends</strong>. Most promotional plans are &ldquo;deferred interest,&rdquo; which means if you have any balance left at the end of the promo, you owe interest retroactively from day one. Set a calendar reminder. Pay it off in time. The math only works if you do.</p>
    </article>
  </div>
</section>

{final_cta(headline="Numbers work? Let&rsquo;s schedule the measure.", sub="Free estimate first. Financing conversation after, only if you want one.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("/home/claude/napas/financing/index.html", head_html, header(active=""), body_content, breadcrumbs_html=bc)
    print("Wrote /financing/index.html")


# ============================================================================
# WARRANTY
# ============================================================================
def build_warranty():
    URL = f"{SITE}/warranty/"
    TITLE = f"12-Month Workmanship Warranty · Napa's Flooring"  # 50
    DESC = (
        f"Our 12-month workmanship warranty on every Tampa Bay flooring install, in writing. "
        f"What&rsquo;s covered, what isn&rsquo;t, and how to make a claim. {BUSINESS['rating']}★ rated."
    )[:158]
    schemas = [
        schema_webpage(URL, "Workmanship Warranty", DESC),
        schema_breadcrumb([("Home", SITE+"/"), ("Warranty", URL)]),
        schema_local_business(URL, "Napa's Flooring Workmanship Warranty"),
    ]
    bc = breadcrumbs([("Home","/"),("Warranty",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Workmanship Warranty · 12 Months</span>
    <h1>If we put it in,<br><em>we stand behind it</em>.</h1>
    <p class="page-hero-sub">12 months on the labor for every install. In writing, on your invoice, with the actual install crew&rsquo;s names on it. Here&rsquo;s exactly what&rsquo;s covered, what isn&rsquo;t, and how to make a claim.</p>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">

      <p class="post-lede">Every Napa&rsquo;s install carries a written 12-month workmanship warranty on the labor, effective from the date of substantial completion (the final walkthrough). The warranty is yours as the homeowner, it transfers to the next buyer if you sell the house within the 12 months, and it&rsquo;s honored by us, in person, with the same crew that did the install.</p>

      <h2>What&rsquo;s covered</h2>

      <p>Anything attributable to the quality of our installation:</p>
      <ul>
        <li>Squeaks in floating floors or nail-down hardwood that develop within 12 months.</li>
        <li>Plank lift, gapping, or buckling on properly acclimated, properly installed product.</li>
        <li>Lippage on tile floors that develops within 12 months (we use lippage clips on every large-format install &mdash; if it shows up later, we fix it).</li>
        <li>Grout cracks not attributable to substrate movement.</li>
        <li>Transition strip lift or detachment.</li>
        <li>Baseboard or quarter-round gaps that open up on us.</li>
        <li>Stair tread or riser separation from the underlying tread platform.</li>
        <li>Any other workmanship-related failure that traces back to the install crew.</li>
      </ul>

      <h2>What isn&rsquo;t covered</h2>

      <p>Three categories, all of which we&rsquo;ll talk through on the estimate:</p>
      <ul>
        <li><strong>Material defects.</strong> Those go to the manufacturer&rsquo;s warranty, which we&rsquo;ll register on your behalf and which usually runs 15–50 years on the product itself. We&rsquo;ll help you file a manufacturer warranty claim at no charge if it comes to that.</li>
        <li><strong>Damage from misuse.</strong> Standing water for hours (a broken dishwasher line that ran overnight, an AC condensate overflow, hurricane intrusion), pet urine that wasn&rsquo;t cleaned promptly, dragging furniture across a finished floor without protection, dropping heavy objects &mdash; none of those are workmanship issues.</li>
        <li><strong>Acts of God and structural movement.</strong> Hurricane damage, settlement cracks in concrete slab, structural subfloor failure, lightning strikes &mdash; the floor isn&rsquo;t designed to withstand any of those, and our warranty doesn&rsquo;t pretend to either.</li>
      </ul>

      <div class="post-key-takeaway">
        <strong>The Honest Take</strong>
        We&rsquo;ve had to honor exactly three warranty claims since {BUSINESS["year_founded"]} — out of {BUSINESS["unique_stat_number"]} installs. Two were lippage on early tile jobs (fixed by lifting the high tile, re-bedding, and re-grouting); one was a squeak on a floating LVP over an under-prepared subfloor that we should have leveled (we lifted four planks, leveled, replaced underlayment, re-installed). None cost the homeowner a cent.
      </div>

      <h2>How to make a claim</h2>

      <p>Call or email us. That&rsquo;s it. We&rsquo;ll come out within 5 business days (often within 2), inspect the issue, and if it&rsquo;s a workmanship problem we fix it &mdash; no paperwork, no run-around, no &ldquo;sorry, that&rsquo;s out of scope.&rdquo; If we determine it&rsquo;s not a workmanship issue (a manufacturer defect, a homeowner-caused issue, or an act-of-God event), we&rsquo;ll tell you so clearly, explain why in writing, and quote the repair work separately.</p>

      <h2>What stays in your job file</h2>

      <p>Every job we complete leaves the homeowner with the following documentation, which is your warranty trigger:</p>
      <ul>
        <li>The signed install agreement showing scope and pricing.</li>
        <li>The acclimation log (digital hygrometer readings for the 72-hour pre-install window).</li>
        <li>The moisture log (subfloor calcium chloride or in-situ RH probe readings, pre-install).</li>
        <li>Pre-install and post-install photos of every room.</li>
        <li>The signed final walkthrough form with both installer signatures and homeowner sign-off.</li>
        <li>The 12-month workmanship warranty card with start and end dates.</li>
        <li>The manufacturer warranty registration confirmation for the product installed.</li>
      </ul>

      <p>Keep the file. If anything happens within the 12 months, that&rsquo;s your proof.</p>

      <h2>Transfer to next homeowner</h2>

      <p>If you sell your house during the 12-month warranty window, the warranty transfers to the buyer at closing. They get the unused balance of the 12 months from the original install date. They don&rsquo;t need to register anything; the documentation in the original homeowner&rsquo;s job file is enough proof. Just hand them the warranty card at closing.</p>

      <h2>Beyond 12 months</h2>

      <p>Most workmanship failures show up in the first 6 months &mdash; that&rsquo;s why the 12-month window is generous. Beyond that, the structural integrity of the install is established. If something does come up between month 13 and month 24, call us anyway. We&rsquo;ve fixed jobs out-of-warranty before for old clients, on our own dime, because the relationship matters more than the technicality.</p>

    </article>
  </div>
</section>

{final_cta(headline="Warranty work you&rsquo;ll never need.", sub="The best warranty claim is the one that never gets filed. That&rsquo;s the install we&rsquo;re trying to do.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("/home/claude/napas/warranty/index.html", head_html, header(active=""), body_content, breadcrumbs_html=bc)
    print("Wrote /warranty/index.html")


# ============================================================================
# THANKS (form submission landing)
# ============================================================================
def build_thanks():
    URL = f"{SITE}/thanks/"
    TITLE = "Thanks · Napa's Flooring"  # 24
    DESC = "Thanks for reaching out to Napa's Flooring. We've received your inquiry and will respond within 4 business hours."
    schemas = [schema_breadcrumb([("Home", SITE+"/"), ("Thanks", URL)])]
    bc = breadcrumbs([("Home","/"),("Thanks",None)])

    body = f'''<section class="page-hero">
  <div class="page-hero-inner" style="text-align:center;max-width:760px;margin:0 auto">
    <span class="mono-label" style="justify-content:center">● Message Received</span>
    <h1>Got it<span class="stop">.</span> <em>Talk soon</em>.</h1>
    <p class="page-hero-sub" style="margin-left:auto;margin-right:auto">We&rsquo;ve received your inquiry. Expect a response from the actual installer (not a salesperson) within 4 business hours on weekdays, 8 hours after-hours and weekends.</p>
    <div style="margin-top:2rem;display:flex;justify-content:center;gap:14px;flex-wrap:wrap">
      <a href="/" class="btn btn-outline-light">Back to Home</a>
      <a href="/blog/" class="btn btn-outline-light">Read the Journal</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <span class="mono-label" style="justify-content:center">In a hurry?</span>
      <h2 style="font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.4rem);line-height:1.1;letter-spacing:-.02em;margin:.8rem 0 1.2rem">Just call instead.</h2>
      <a href="{TEL_LINK}" style="font-family:var(--font-display);font-size:clamp(2rem,5vw,3rem);color:var(--orange-deep);letter-spacing:-.02em;text-decoration:underline;text-underline-offset:8px;text-decoration-thickness:3px">{BUSINESS["phone_display"]}</a>
    </div>
  </div>
</section>'''

    head_html = head(TITLE, DESC, URL, indexable=False, json_ld=schemas)
    write_page("/home/claude/napas/thanks/index.html", head_html, header(active=""), body, breadcrumbs_html=bc)
    print("Wrote /thanks/index.html")


# ============================================================================
# 404
# ============================================================================
def build_404():
    body = f'''<section class="page-hero">
  <div class="page-hero-inner" style="text-align:center;max-width:760px;margin:0 auto">
    <span class="mono-label" style="justify-content:center">Error 404 · Page Not Found</span>
    <h1>That&rsquo;s a <em>dead-end</em>.</h1>
    <p class="page-hero-sub" style="margin-left:auto;margin-right:auto">The page you&rsquo;re looking for doesn&rsquo;t exist, has moved, or was never there to begin with. Try one of the links below — or just call.</p>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:920px;margin:0 auto;display:grid;grid-template-columns:repeat(2,1fr);gap:14px">
      {''.join(f'<a href="/{s}/" class="neighborhood-pill">{SERVICES[s]["name"]}</a>' for s in SERVICE_ORDER)}
    </div>
    <div style="text-align:center;margin-top:3rem"><a href="/" class="btn btn-orange">Back to Home <span class="btn-arrow"></span></a></div>
  </div>
</section>'''

    head_html = head("404 · Page Not Found · Napa's Flooring", "Page not found. Try a service link or call.", f"{SITE}/404.html", indexable=False)
    out = "/home/claude/napas/404.html"
    html = wrap_page(head_html, header(active=""), body)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {out}")


if __name__ == "__main__":
    build_about()
    build_contact()
    build_faq()
    build_financing()
    build_warranty()
    build_thanks()
    build_404()
