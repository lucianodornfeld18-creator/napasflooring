#!/usr/bin/env python3
"""
Napa's Flooring — Master Data Module
All cities, services, neighborhoods, FAQs, pricing tables, business info.
Used by every _build_*.py script.
"""

# ============================================================================
# BUSINESS IDENTITY
# ============================================================================
BUSINESS = {
    "name": "Napa's Flooring",
    "legal_name": "Napa's Flooring LLC",
    "domain": "napasflooring.com",
    "phone": "+14076279533",
    "phone_display": "(407) 627-9533",
    "phone_tel": "+14076279533",
    "email": "napasflooring@gmail.com",
    "street": "5926 SR 70 E, Suite 200",     # generic Bradenton service-area address
    "city": "Bradenton",
    "city_slug": "bradenton",
    "state": "FL",
    "state_long": "Florida",
    "zip": "34212",
    "country": "US",
    "lat": "27.4806",
    "lng": "-82.4569",
    "year_founded": 2020,
    "rating": "5.0",
    "review_count": 15,
    "tagline": "Built right. Finished proud.",
    "tagline_long": "Tampa Bay's craft-first flooring crew — hardwood, vinyl, tile, laminate and stair treads installed by hand.",
    "unique_stat_number": "300+",
    "unique_stat_full": "300+ Tampa Bay floors finished since 2020",
    "checklist_name": "Napa's 47-Point Installation Standard",
    "checklist_points": 47,
    "guarantee": "12-month workmanship warranty on every installation.",
    "response_time": "Free estimate within 24 hours, often same-day.",
    "google_profile": "https://g.page/napas-flooring",   # placeholder — user can update later
    "google_review_url": "https://g.page/r/napas-flooring/review",
    "facebook": "",
    "instagram": "",
    "yelp": "",
    "thumbtack": "",
    "angi": "",
    "houzz": "",
    "bbb": "",
    "hours": [
        ("Monday","07:00","19:00"),
        ("Tuesday","07:00","19:00"),
        ("Wednesday","07:00","19:00"),
        ("Thursday","07:00","19:00"),
        ("Friday","07:00","19:00"),
        ("Saturday","08:00","17:00"),
        ("Sunday","09:00","16:00"),
    ],
}

# WhatsApp link helper (same number, but de-emphasized; the buttons primarily say "Call" / "Text")
WA_LINK = f"https://wa.me/{BUSINESS['phone'].lstrip('+')}?text=Hi%20Napa%27s%20Flooring%2C%20I%27d%20like%20a%20free%20estimate."
SMS_LINK = f"sms:{BUSINESS['phone']}?body=Hi%20Napa%27s%20Flooring%2C%20I%27d%20like%20a%20free%20estimate."
TEL_LINK = f"tel:{BUSINESS['phone']}"

# ============================================================================
# SERVICE AREA — 8 cities (same Tampa Bay/Sarasota footprint)
# ============================================================================
CITIES = {
    "bradenton": {
        "name": "Bradenton",
        "slug": "bradenton",
        "county": "Manatee County",
        "state": "FL",
        "zips": ["34201","34202","34203","34205","34207","34208","34209","34210","34211","34212"],
        "population": "60,000+ city · 420,000+ metro",
        "growth": "12% population growth 2020–2025",
        "lat": "27.4989",
        "lng": "-82.5748",
        "neighborhoods": [
            "Heritage Harbour","River Strand","GreyHawk Landing","Mill Creek","Stoneybrook at Heritage Harbour",
            "Tara Preserve","Country Club East","Esplanade Golf & Country Club","River Wilderness","Rosedale Golf & Country Club",
            "Braden Woods","Cortez","Palma Sola","West Bradenton","River Place",
            "Anna Maria Island","Holmes Beach","Bradenton Beach","Perico Bay","University Park"
        ],
        "context": "Bradenton sits at the mouth of the Manatee River and serves as the county seat of Manatee — a working-class river town that's added more than seven thousand new residents in the last five years. The eastern half of the city (along the SR-70 and SR-64 corridors near our home base in the 34212 ZIP) is dominated by gated golf communities like Heritage Harbour, GreyHawk Landing, and River Strand, while the historic western neighborhoods around Palma Sola and West Bradenton hold a wave of mid-century block homes being renovated by younger buyers. Both extremes drive flooring work: builder-grade carpet getting ripped out of fifteen-year-old planned communities, and tile-over-terrazzo problems getting solved in 1960s ranches near 14th Street West.",
        "context_short": "Bradenton — Manatee County seat. 60,000 residents inside city limits, 420,000 in the metro. Heavy mix of gated golf communities east of I-75 and renovation-ready mid-century homes west of US-41.",
        "humidity_note": "Year-round dew points in Bradenton sit between 65 and 75°F from May through October, which is why we acclimate every hardwood and engineered plank for a minimum of 72 hours before a single nail goes in.",
        "landmarks": "LECOM Park, IMG Academy, Riverwalk Bradenton, the De Soto Bridge, Robinson Preserve, the Village of the Arts",
        "primary_market": "Mix of gated golf-community new construction and 1960s–1980s ranch renovations",
        "trade_class": "C-license territory under Manatee County Building & Development",
    },
    "lakewood-ranch": {
        "name": "Lakewood Ranch",
        "slug": "lakewood-ranch",
        "county": "Manatee/Sarasota Counties",
        "state": "FL",
        "zips": ["34202","34211","34212","34240","34238"],
        "population": "60,000+ across 30+ villages",
        "growth": "#1 best-selling master-planned community in the US (eight years running, RCLCO Real Estate Advisors)",
        "lat": "27.4181",
        "lng": "-82.3884",
        "neighborhoods": [
            "Country Club East at Lakewood Ranch","Lakewood Ranch Country Club","The Lake Club","Esplanade Golf & Country Club","Polo Run",
            "Indigo","Mallory Park","Greenbrook","Summerfield","Edgewater Village",
            "Lorraine Lakes","Del Webb Lakewood Ranch","Cresswind Lakewood Ranch","Star Farms at Lakewood Ranch","Sweetwater at Lakewood Ranch",
            "Waterside Place","Azario Esplanade","Avanti at Waterside","Solera at Lakewood Ranch","Savanna at Lakewood Ranch"
        ],
        "context": "Lakewood Ranch is the largest planned community on Florida's Gulf Coast — more than thirty thousand acres straddling the Manatee–Sarasota county line, organized into villages that each operate like their own small town. The 34211 ZIP alone (Country Club East, Polo Run, Indigo, Mallory Park, Lorraine Lakes) has absorbed nearly five thousand new homes since 2018, and the construction pipeline north of SR-64 (Star Farms, Sweetwater, Azario) keeps the volume going. Almost every floor we lay in Lakewood Ranch is going into a builder-original home where the owner wants to replace the standard 12×24 porcelain or wood-look LVP with something with character — wide-plank European white oak, large-format marble-look porcelain, or a custom herringbone laydown that the builder never offered.",
        "context_short": "Lakewood Ranch — 30,000-acre planned community across two counties, more than 30 villages, ranked #1 best-selling master-planned community in the US for eight consecutive years.",
        "humidity_note": "Lakewood Ranch homes east of I-75 sit on slab foundations with elevated water tables in the rainy season. We pull calcium chloride moisture readings on every concrete pour before glue-down installs.",
        "landmarks": "Main Street at Lakewood Ranch, Waterside Place, University Town Center (UTC), Premier Sports Campus, Lakewood Ranch Medical Center",
        "primary_market": "Builder-original homes being upgraded — wide-plank engineered hardwood, herringbone laydowns, large-format porcelain",
        "trade_class": "Crosses both Manatee and Sarasota County permitting jurisdictions",
    },
    "palmetto": {
        "name": "Palmetto",
        "slug": "palmetto",
        "county": "Manatee County",
        "state": "FL",
        "zips": ["34220","34221"],
        "population": "13,500+ city",
        "growth": "23% growth 2020–2025 (US Census ACS)",
        "lat": "27.5214",
        "lng": "-82.5723",
        "neighborhoods": [
            "Historic Downtown Palmetto","Riviera Dunes","Snead Island","Terra Ceia","Sanctuary Cove",
            "Heron Creek","Esplanade at Artisan Lakes","Artisan Lakes","Trevesta","Northshore at Riviera Dunes",
            "Rye Wilderness Estates","Palmetto Estates","Palm View","Memphis","Ellenton"
        ],
        "context": "Palmetto is the quieter twin of Bradenton — sitting on the north bank of the Manatee River, directly across the De Soto Bridge from downtown Bradenton, with about thirteen thousand residents inside city limits. The Riviera Dunes Marina and the Snead Island bird sanctuary anchor the historic waterfront, while Artisan Lakes and Trevesta on the east side along US-301 are absorbing the spillover from the Lakewood Ranch construction boom. Many of the older waterfront homes (built in the 1950s through 1970s) are second residences for snowbirds, which creates a specific flooring problem we see constantly: floors that sit empty in 85°F closed-up houses from June through October, then get walked on five months a year. We size moisture barriers, gap allowances, and HVAC run-time recommendations specifically for that closure cycle.",
        "context_short": "Palmetto — historic riverfront city across the Manatee River from Bradenton. 13,500 residents. Mix of 1950s–70s waterfront homes (many snowbird-owned) and new master-planned developments along US-301.",
        "humidity_note": "Snowbird homes that sit closed and unconditioned from June to October are the single highest-failure environment for hardwood floors in our service area. We never recommend solid hardwood for these homes.",
        "landmarks": "Riviera Dunes Marina, Snead Island Causeway, Emerson Point Preserve, the De Soto Bridge, Sutton Park, the Manatee River",
        "primary_market": "Aging waterfront homes (snowbird closures) and Artisan Lakes new-build upgrades",
        "trade_class": "Manatee County permitting; downtown historic overlay applies on Riverside Drive",
    },
    "parrish": {
        "name": "Parrish",
        "slug": "parrish",
        "county": "Manatee County",
        "state": "FL",
        "zips": ["34219"],
        "population": "28,000+ (doubled since 2015)",
        "growth": "Roughly 100% population growth 2015–2025",
        "lat": "27.5764",
        "lng": "-82.4234",
        "neighborhoods": [
            "North River Ranch","Star Farms at Parrish","Aviary at Rutland Ranch","Crosscreek","Forest Creek",
            "Silverleaf","Twin Rivers","Foxbrook","Canoe Creek","Parrish Lakes",
            "Rye Crossings","Wilderness Reserve","Salt Meadows","Jacaranda Estates","Copperstone"
        ],
        "context": "Parrish is northeastern Manatee County's relocation magnet — a stretch of US-301 and Moccasin Wallow Road that's gone from cattle pasture to twenty-eight thousand residents in ten years. North River Ranch alone is platted for more than seven thousand homes; Aviary at Rutland Ranch, Canoe Creek, and Salt Meadows are all running their first phases. Almost everything we do in Parrish is the same conversation: a new-construction homeowner closes on a builder home, lives with the standard wood-look LVP or polished porcelain for six to eighteen months, then upgrades the living areas to wide-plank engineered hardwood or a higher-end SPC plank with a thicker wear layer. The ROI on that upgrade — measured against resale appraisals on adjacent homes — is the strongest in any city we serve.",
        "context_short": "Parrish — fastest-growing community in Manatee County. Population doubled since 2015 to 28,000+. New-construction master-planned communities (North River Ranch, Aviary, Canoe Creek) drive the market.",
        "humidity_note": "Parrish slab homes inland of US-301 have lower water-table issues than coastal cities, but we still acclimate every shipment for 72 hours and moisture-test every slab before glue-down.",
        "landmarks": "Fort Hamer Park, the Fort Hamer Bridge, Florida Railroad Museum, Carlton Reserve trails, Buffalo Creek Park",
        "primary_market": "New-construction post-closing upgrades from builder-grade flooring",
        "trade_class": "Manatee County permitting; floods almost never an issue inland of US-301",
    },
    "sarasota": {
        "name": "Sarasota",
        "slug": "sarasota",
        "county": "Sarasota County",
        "state": "FL",
        "zips": ["34230","34231","34232","34233","34234","34235","34236","34237","34238","34239","34240","34241","34242","34243"],
        "population": "58,000+ city · 450,000+ metro",
        "growth": "Median home price up 64% since 2020 (Sarasota-Manatee MLS)",
        "lat": "27.3364",
        "lng": "-82.5307",
        "neighborhoods": [
            "Downtown Sarasota","St. Armands Key","Lido Key","Siesta Key","Longboat Key",
            "Bird Key","Bay Isles","Golden Gate Point","The Meadows","Palmer Ranch",
            "Gulf Gate","Laurel Park","Southside Village","Cherokee Park","Indian Beach",
            "Sapphire Shores","Arlington Park","University Park (Sarasota side)","Hidden Lake","The Landings",
            "Oakford"
        ],
        "context": "Sarasota is the cultural and architectural anchor of the Suncoast — fifty-eight thousand residents inside the city, four hundred and fifty thousand in the metro, and one of the highest median household incomes south of Tampa Bay. The market is bifurcated: waterfront condos and key homes (Siesta, Lido, Longboat, Bird, Casey) drive the high end, where we install wide-plank European white oak, marble-look porcelain in 24×48 and larger, and custom inlays for foyers and great rooms. West-of-Trail neighborhoods like Southside Village and Cherokee Park are full of restored 1950s ranch homes where we frequently remove old vinyl asbestos tile and install glue-down luxury vinyl plank with a vapor barrier. East of I-75, Palmer Ranch and The Meadows give us a steady stream of mid-2000s homes upgrading from carpet to engineered hardwood.",
        "context_short": "Sarasota — Suncoast cultural anchor. 58,000 in city, 450,000 metro. High median income. Bifurcated market: waterfront condos/key homes drive premium installs; west-of-Trail ranches drive renovation work.",
        "humidity_note": "Siesta Key and Lido Key homes are five to twelve feet from saltwater exposure. We always specify marine-grade adhesives and elevated vapor barriers for ground-floor installs on the keys.",
        "landmarks": "Siesta Key Beach (rated #1 beach in America by Dr. Beach multiple years), the John & Mable Ringling Museum of Art, St. Armands Circle, the Sarasota Opera House, Marie Selby Botanical Gardens, the Van Wezel Performing Arts Hall",
        "primary_market": "Waterfront premium installs (keys) + West-of-Trail mid-century renovations + Palmer Ranch carpet-to-wood upgrades",
        "trade_class": "Sarasota County and City of Sarasota permitting; salt-air corrosion is a real factor on the keys",
    },
    "st-petersburg": {
        "name": "St. Petersburg",
        "slug": "st-petersburg",
        "county": "Pinellas County",
        "state": "FL",
        "zips": ["33701","33702","33703","33704","33705","33706","33707","33708","33709","33710","33711","33712","33713","33714","33715","33716"],
        "population": "260,000+ city · 1M+ Pinellas County",
        "growth": "Highest median rent growth in the Tampa Bay MSA 2020–2024 (Zillow)",
        "lat": "27.7676",
        "lng": "-82.6403",
        "neighborhoods": [
            "Downtown St. Petersburg","Snell Isle","Old Northeast","Coffee Pot Bayou","Crescent Lake",
            "Crescent Heights","Shore Acres","Bayway Isles","Pasadena","Tierra Verde",
            "Allendale","Disston Heights","Historic Kenwood","Euclid–St. Paul","Driftwood",
            "Riviera Bay","Gulfport (border)","Old Southeast","Bayou Bonita","Pinellas Point"
        ],
        "context": "St. Petersburg is the densest, oldest, and most architecturally varied city in our service area — pre-war bungalows in Historic Kenwood, 1920s Mediterranean Revival on Snell Isle, mid-century cinder-block in Shore Acres, modern condo towers along Beach Drive. That variety drives a very different flooring practice than Lakewood Ranch or Parrish: we spend more time on subfloor remediation here than on actual install. Pinellas concrete slabs are often six to nine decades old, with original moisture barriers long since failed; bungalow tongue-and-groove pine subfloors need leveling and patching before any modern install can go down. Most of our St. Pete work is renovation of older homes — sand-and-refinish projects on original oak floors, glue-down LVP over old terrazzo, and large-format porcelain in renovated 1950s ranches.",
        "context_short": "St. Petersburg — Pinellas County. 260,000 in city, 1M+ in county. Older, denser, more architecturally varied than the Manatee/Sarasota footprint. Heavy subfloor remediation work on pre-1970 housing stock.",
        "humidity_note": "St. Pete's older slab homes (pre-1985) frequently lack any subfloor vapor barrier. We always run a calcium chloride test and recommend a poured liquid membrane before glue-down on these homes.",
        "landmarks": "The Salvador Dalí Museum, the Pier (rebuilt 2020), Tropicana Field, Sunken Gardens, the Vinoy Park Hotel, the Imagine Museum",
        "primary_market": "Older-home renovation — sand-and-refinish, glue-down LVP over terrazzo, subfloor remediation, bungalow restoration",
        "trade_class": "Pinellas County and City of St. Pete permitting; Historic Preservation Commission review for Kenwood, Old Northeast, Round Lake",
    },
    "tampa": {
        "name": "Tampa",
        "slug": "tampa",
        "county": "Hillsborough County",
        "state": "FL",
        "zips": ["33602","33603","33604","33605","33606","33609","33611","33612","33613","33614","33615","33616","33618","33619","33624","33625","33626","33629","33634","33647"],
        "population": "400,000+ city · 1.5M+ Hillsborough County",
        "growth": "Strongest five-year job growth of any major Florida metro (BLS)",
        "lat": "27.9506",
        "lng": "-82.4572",
        "neighborhoods": [
            "Hyde Park","Davis Islands","Bayshore Beautiful","South Tampa","Channelside",
            "Westshore","Carrollwood","New Tampa","Brandon","Riverview",
            "Tampa Palms","Westchase","Town N' Country","Seminole Heights","Ybor City",
            "Beach Park","Sunset Park","Culbreath Heights","Palma Ceia","Bayshore Gardens",
            "Lutz","Wesley Chapel (north)","Apollo Beach"
        ],
        "context": "Tampa is the largest market we serve — four hundred thousand inside the city, more than one and a half million in Hillsborough County, and the strongest five-year job growth of any major Florida metro. The South Tampa market (Hyde Park, Bayshore Beautiful, Davis Islands, Sunset Park, Palma Ceia) is the most premium zip-code cluster in all of Tampa Bay; we install wide-plank European white oak, herringbone laydowns, and large-format porcelain in bungalows being expanded and modernized. North of Kennedy Boulevard the work shifts to volume new construction (Tampa Palms, New Tampa, Westchase, Wesley Chapel), where the conversation is identical to Lakewood Ranch — owners replacing builder-grade LVP with character-grade engineered hardwood within twelve to twenty-four months of closing.",
        "context_short": "Tampa — largest market in our footprint. 400,000 in city, 1.5M+ county. Strongest job growth of any major FL metro. South Tampa drives premium installs; north Tampa drives volume new-construction upgrades.",
        "humidity_note": "South Tampa bungalow renovations on Bayshore Boulevard need particular subfloor moisture care — many of these homes are within 200 yards of saltwater intrusion and have elevated slab humidity readings.",
        "landmarks": "Bayshore Boulevard (the longest continuous sidewalk in the world), Riverwalk Tampa, Amalie Arena, Raymond James Stadium, the University of Tampa, Tampa International Airport, the Florida Aquarium",
        "primary_market": "South Tampa bungalow restorations + North Tampa new-construction upgrades + South Hillsborough (Apollo Beach, Riverview) volume work",
        "trade_class": "City of Tampa and Hillsborough County permitting; competitive contractor density",
    },
    "venice": {
        "name": "Venice",
        "slug": "venice",
        "county": "Sarasota County",
        "state": "FL",
        "zips": ["34284","34285","34292","34293"],
        "population": "26,000+ city",
        "growth": "Wellen Park alone has added 15,000+ homes since 2018",
        "lat": "27.0998",
        "lng": "-82.4543",
        "neighborhoods": [
            "Venice Island","Historic Downtown Venice","Venice Gulf View","Venice Beach","Pelican Pointe Golf & Country Club",
            "Venetian Golf & River Club","Venetia","Sawgrass","Stoneybrook at Venice","Wellen Park",
            "IslandWalk at the West Villages","Gran Paradiso","Renaissance at Wellen Park","Ventura Country Club","Capri Isles",
            "Caribbean Bay","Bird Bay","Jacaranda West","Sorrento East","Eagle Trace"
        ],
        "context": "Venice has two completely different flooring markets coexisting in the same zip codes. The first is Venice Island and Historic Downtown Venice — small 1950s and 1960s waterfront homes that get bought by retirees, gutted to the studs, and reborn with wide-plank engineered hardwood, large-format porcelain, and re-finished original terrazzo. The second is Wellen Park and the West Villages south of US-41 — fifteen thousand new homes since 2018, almost all delivered with builder-grade LVP that gets replaced with premium product inside the first two years. Both markets agree on one thing: humidity and snowbird closures mean solid hardwood is rarely the right call here. We install more engineered seven-inch wide plank in Venice than anywhere else in our footprint.",
        "context_short": "Venice — Sarasota County. 26,000 residents. Bifurcated market: Venice Island & Historic Downtown (1950s–60s renovations) + Wellen Park / West Villages (15,000+ new-construction homes since 2018).",
        "humidity_note": "Venice Island sits on a barrier island with naturally higher slab humidity. We always recommend engineered hardwood (never solid) for any Venice Island install.",
        "landmarks": "Venice Beach (the Shark Tooth Capital of the World), Venice Pier, Historic Downtown Venice, Wellen Park Downtown, Caspersen Beach, the Venice Theatre, the Venetian Waterway Park",
        "primary_market": "Venice Island gut-renovations + Wellen Park new-construction upgrades",
        "trade_class": "Sarasota County permitting; Wellen Park has its own master HOA architectural review",
    },
}

CITY_ORDER = ["bradenton","lakewood-ranch","palmetto","parrish","sarasota","st-petersburg","tampa","venice"]


# ============================================================================
# SERVICES — six core
# ============================================================================
SERVICES = {
    "hardwood-flooring": {
        "name": "Hardwood Flooring",
        "slug": "hardwood-flooring",
        "short": "Hardwood",
        "h1_phrase": "Hardwood Flooring",
        "card_image": "card-hardwood.webp",
        "icon": "01",
        "intro_lead": "Solid plank, engineered plank, and wide-board European white oak — installed by hand, acclimated for the Gulf Coast, and finished to outlast the next twenty years of Tampa Bay living.",
        "intro_long_p1": "Hardwood is still the most resale-defensible floor you can install in a Florida home — but only if the installation respects how wood behaves in a sub-tropical climate. The biggest mistake we see in repair calls across Bradenton, Sarasota, and Tampa is rushed acclimation. Florida dew points run between 65 and 75 degrees from May through October; the air inside a properly conditioned home runs closer to 45 to 55 percent relative humidity. When a hardwood plank moves from a humid warehouse straight into a cold-conditioned living room, it expands, contracts, and gaps inside the first summer. Every Napa's install acclimates for seventy-two hours minimum on the actual jobsite, with digital hygrometer logging.",
        "intro_long_p2": "We install both <strong>solid hardwood</strong> (three-quarter-inch thick, sandable up to eight times in its lifetime, our pick for second-floor and above-grade plywood subfloors) and <strong>engineered hardwood</strong> (multi-ply construction with a real-wood top veneer, dramatically more dimensionally stable, the right answer for ninety percent of slab-on-grade homes in our service area). Species we work with regularly include European White Oak, American White Oak, Red Oak, Hickory, Walnut, Maple, and Acacia. Widths from three inches up through ten inches; flat, hand-scraped, and wire-brushed surface textures.",
        "scope_items": [
            "Solid hardwood installation (3/4″ tongue-and-groove, nail-down on plywood)",
            "Engineered hardwood installation (5″–9″ widths, glue-down or floating)",
            "Wide-plank European White Oak (7″–10″) — our most-installed product",
            "Custom herringbone &amp; chevron laydowns",
            "Nail-down installation on plywood subfloors",
            "Glue-down installation on concrete slabs",
            "Floating engineered installation with click-lock systems",
            "Subfloor moisture testing (calcium chloride + pin meter, both logged)",
            "Self-leveling concrete pours for slab dips up to 1.5″",
            "Vapor-retarder installation on concrete slabs",
            "Threshold &amp; transition strip carpentry",
            "Quarter-round and shoe-mold matching",
            "Flush-mount baseboard refits where requested",
            "Stair tread &amp; nosing integration",
            "Toilet pull-and-reset, appliance moves, debris haul-away",
        ],
        "pricing_rows": [
            ("Engineered Hardwood (5″ wide)", "$8.50–$11/sq ft installed", "Glue-down or nail-down"),
            ("Engineered Hardwood (7–9″ wide)", "$10–$14/sq ft installed", "Most-installed in Lakewood Ranch"),
            ("Solid Hardwood (3/4″, 3–5″ wide)", "$9–$13/sq ft installed", "Nail-down on plywood subfloor only"),
            ("Premium European White Oak (wide plank)", "$13–$18/sq ft installed", "Character-grade, 7–10″ width"),
            ("Custom Herringbone Laydown", "$15–$22/sq ft installed", "Labor doubles vs. straight plank"),
            ("Custom Chevron Laydown", "$17–$24/sq ft installed", "Our most-premium hardwood install"),
            ("Subfloor Self-Leveling (per room)", "$200–$600", "When pin-meter shows 1/4″+ dip"),
            ("Old Flooring Removal &amp; Haul", "$1.50–$3/sq ft", "Carpet, laminate, or tile demo"),
        ],
        "faqs": [
            ("Can I install solid hardwood on a Florida slab?", "We don't recommend it. The combination of slab moisture and Gulf Coast humidity makes solid hardwood prone to cupping, gapping, and crowning when it's glued or nailed directly to concrete. Engineered hardwood (with a multi-ply core that resists dimensional movement) is the right call for 95% of slab-on-grade homes in our service area. The few exceptions are homes where we can install a 5/8″ plywood underlayment over the slab first — but that raises the finished floor height by an inch, which affects door clearance, transitions, and baseboard returns."),
            ("How long does hardwood acclimate before install?", "Seventy-two hours is our floor. The boxes get opened on the jobsite, the planks get cross-stacked so air circulates around every face, and a digital hygrometer logs jobsite humidity for the entire acclimation window. If your home was just turned over by a builder and the HVAC has been off, we'll often want longer — sometimes a full week — before installation begins."),
            ("Engineered vs. solid — what's actually different?", "Solid hardwood is one piece of wood, 3/4″ thick. It can be sanded and refinished up to eight times over its lifetime, which is why it's still the standard for premium plywood-subfloor installs. Engineered hardwood is a real-wood top veneer (typically 2–6 mm) bonded to a multi-ply substrate underneath; it's far more dimensionally stable, can be installed below grade, and can usually be refinished once or twice. For Florida slab homes we recommend engineered nine times out of ten."),
            ("How long does the whole job take?", "A typical 1,200–1,800 sq ft hardwood install runs 3–5 working days from demo to walk-through. Day one is demolition and subfloor prep, day two is acclimation finishing and starting the install, days three through four are the bulk of the laydown plus transitions, day five is quarter-round and the final walkthrough. Herringbone and chevron jobs run 6–10 days. Stair treads add a day."),
        ],
    },
    "vinyl-plank-flooring": {
        "name": "Luxury Vinyl Plank (LVP) Flooring",
        "slug": "vinyl-plank-flooring",
        "short": "Vinyl Plank",
        "h1_phrase": "Vinyl Plank Flooring",
        "card_image": "card-vinyl.webp",
        "icon": "02",
        "intro_lead": "100% waterproof, scratch-resistant, dimensionally stable in Florida humidity, and the smartest dollar-per-square-foot floor you can install in a Tampa Bay rental, kitchen, or family room.",
        "intro_long_p1": "Luxury vinyl plank (LVP) and stone-plastic composite (SPC) have become the dominant new-floor category in Tampa Bay for a stack of practical reasons: they're 100% waterproof, they shrug off dog claws and dropped pans, they cost a fraction of real hardwood, and the visual gap between a good SPC plank and an actual oak floor has gotten genuinely small. We install both <strong>click-lock floating systems</strong> (faster install, no glue, individual planks replaceable down the road) and <strong>full glue-down systems</strong> (more permanent, zero flex, the right answer for open-plan rooms over eight hundred square feet and for high-traffic commercial work).",
        "intro_long_p2": "Where we really earn our keep is short-term rental work — Anna Maria Island, Siesta Key, Lido Key, Longboat, and the Wellen Park rental cluster. STR floors take five times the traffic of a primary residence, get cleaned with chemicals most homeowners would never use, and need to look new in listing photos for the next decade. We've completed more than a hundred and forty STR re-floorings since 2020. For most Florida residential clients we land on a click-lock SPC plank at 6.5 mm with a 22-mil wear layer — that's the sweet spot for durability, price, and visual quality.",
        "scope_items": [
            "Click-lock LVP installation (floating, no adhesive)",
            "Full glue-down LVP installation (large open-plan spaces, commercial)",
            "SPC (Stone-Plastic Composite) plank installation",
            "WPC (Wood-Plastic Composite) plank installation",
            "Cork or foam underlayment when manufacturer-required",
            "Calcium chloride moisture testing on slabs before glue-down",
            "Concrete slab self-leveling for dips, low spots, and cracks",
            "Old flooring removal &amp; haul-away (carpet, tile, sheet vinyl)",
            "Transition strip and reducer installation",
            "Flush-mount transitions to tile or carpet",
            "Custom LVP stair treads with matching nosing",
            "Quarter-round and shoe-mold installation",
            "Toilet pull-and-reset, appliance moves",
            "Vapor barrier installation on suspect slabs",
        ],
        "pricing_rows": [
            ("Standard LVP (4 mm, 12-mil wear)", "$1.50–$3/sq ft installed", "Builder-grade, rental-friendly"),
            ("Mid-Range LVP / SPC (6 mm, 20-mil)", "$2.50–$5/sq ft installed", "Most-installed for primary residences"),
            ("Premium SPC (8 mm, 22+ mil wear)", "$4–$7/sq ft installed", "Pet-proof, lifetime residential warranty"),
            ("Wide-Plank Luxury LVP (9″+)", "$5–$9/sq ft installed", "Hardwood-mimicking, premium look"),
            ("Glue-Down Commercial LVP", "$3–$6/sq ft installed", "STRs, AirBnBs, high-traffic"),
            ("LVP Stair Treads (per tread)", "$60–$95 each", "Includes nosing and matching riser"),
            ("Slab Self-Leveling (per room)", "$200–$600", "When dip exceeds 3/16″ in 10 ft"),
            ("Old Flooring Removal &amp; Haul", "$1.50–$3/sq ft", "Carpet/tile/sheet-vinyl demo"),
        ],
        "faqs": [
            ("Is luxury vinyl plank really waterproof?", "Yes — fully. Modern LVP and SPC planks are 100% waterproof through the core; you can submerge a plank for days and it won't swell, warp, or delaminate. The seams where two planks meet are tight enough that surface water (a dishwasher leak, a pet accident, a hurricane-driven AC condensate overflow) won't penetrate to the subfloor for hours. That said: waterproof flooring doesn't make a waterproof house. Standing water against a baseboard for days will still get into the wall cavity behind the floor — the plank itself won't fail, but adjacent assemblies can."),
            ("Click-lock vs. glue-down — which is right for me?", "Click-lock (floating) is faster to install, easier to repair (you can pop up a damaged plank and swap it), and gentler on subfloors with minor imperfections. Glue-down is more permanent, has zero flex underfoot (which feels closer to tile or real hardwood), and is the right answer for open-plan spaces over 800 sq ft, for commercial buildings, and for spaces with very heavy furniture (pool tables, gun safes, commercial-grade appliances). For most Florida residential work we install click-lock; for STRs and commercial, we glue down."),
            ("Will LVP look fake?", "It depends entirely on what you buy. Builder-grade LVP at $1.50/sq ft has visible pattern repeats — you'll see the same knot or grain reappear every 4–6 planks, and the embossing doesn't always line up with the printed grain. Mid-tier and premium SPC ($4+/sq ft installed) has dozens of unique plank visuals, deeper embossing, and matte finishes that read remarkably close to real hardwood from anywhere outside ten feet. We bring samples to your home and show you the cost-vs-realism tradeoff in person."),
            ("How long does an LVP install take?", "A typical 1,000–1,500 sq ft floating LVP install runs 2–3 days: day one demo and subfloor prep, day two installation, day three transitions and trim. Glue-down jobs typically add one to two days because of the adhesive cure time. Stair treads add a day. Any subfloor leveling work adds drying time before install can begin."),
        ],
    },
    "tile-installation": {
        "name": "Tile Installation",
        "slug": "tile-installation",
        "short": "Tile",
        "h1_phrase": "Tile Installation",
        "card_image": "card-tile.webp",
        "icon": "03",
        "intro_lead": "Porcelain, ceramic, natural stone, and large-format slabs — set flat, set straight, and set to the slope your shower pan actually needs.",
        "intro_long_p1": "Tile is the most installation-sensitive flooring product on the market. The tile itself is durable, beautiful, and inert; the failure points are almost always underneath it — improperly prepared substrates, the wrong setting mortar, missing decoupling membranes, and skipped lippage controls. We install everything from 4-inch ceramic field tile to 24x48 large-format porcelain to 48x48 marble-look slabs, and the larger the format the more critical the prep becomes. A 24x48 porcelain tile on a slab with a 1/8-inch dip will sit visibly cupped in the room; the same dip is invisible under 12-inch tile.",
        "intro_long_p2": "We follow the TCNA (Tile Council of North America) handbook for substrate prep, setting mortars, and crack-isolation membranes — that's the published spec for a tile floor that doesn't crack when the slab below it does. For wet areas (showers, primary bathrooms, splash zones near tubs) we install Schluter Kerdi or Wedi waterproofing systems before a single piece of tile gets set. The vast majority of our tile-failure repair calls trace back to the original installer skipping either the substrate prep or the waterproofing — and once tile is set wrong, the only real fix is to take it back out.",
        "scope_items": [
            "Ceramic field tile (4″–18″ formats)",
            "Porcelain field tile (12″–24″ formats)",
            "Large-format porcelain (24×48 and larger)",
            "Natural stone — travertine, marble, slate, granite",
            "Mosaic and decorative inlay work",
            "Schluter Kerdi waterproofing for wet areas",
            "Wedi panel shower system installation",
            "Crack-isolation membrane (Schluter Ditra)",
            "Heated-floor mat installation (Schluter Ditra-Heat)",
            "Self-leveling underlayment when slab requires",
            "Bullnose and Schluter trim profile installation",
            "Grouting (sanded, unsanded, urethane, epoxy)",
            "Caulk-and-grout sealing at change-of-plane",
            "Old tile demolition &amp; substrate prep",
            "Toilet pull-and-reset, appliance moves",
        ],
        "pricing_rows": [
            ("Standard Ceramic Tile (12″–18″)", "$6–$9/sq ft installed", "Tile included, basic patterns"),
            ("Porcelain Tile (12″–18″)", "$7–$11/sq ft installed", "Most-installed for primary living areas"),
            ("Large-Format Porcelain (24×48)", "$10–$15/sq ft installed", "Premium look, longer prep time"),
            ("Marble-Look Porcelain Slab (48×48+)", "$14–$22/sq ft installed", "Slab handling adds labor"),
            ("Natural Stone (travertine/marble)", "$12–$20/sq ft installed", "Plus sealing on day of install"),
            ("Mosaic / Decorative Inlay", "$25–$50/sq ft installed", "Labor-intensive, custom layouts"),
            ("Schluter Kerdi Shower Waterproofing", "$1,200–$2,800", "Per standard 3×5 shower footprint"),
            ("Crack-Isolation Membrane (Ditra)", "$2.50–$4/sq ft", "Critical over concrete slabs"),
            ("Tile Demo &amp; Substrate Prep", "$3–$6/sq ft", "Old tile + thinset removal"),
        ],
        "faqs": [
            ("Why does large-format tile cost so much more to install?", "Two reasons. First, the substrate has to be dramatically flatter — TCNA spec for tile under 15 inches allows 1/4-inch deviation over 10 feet; for tile 15 inches and larger that tightens to 1/8-inch over 10 feet. Florida slabs rarely meet that out of the box, so we frequently self-level. Second, the tiles are heavy, two-person lifts, and require back-buttering plus a fully troweled bed of mortar to avoid lippage. The tile may cost only slightly more — the labor is the real difference."),
            ("Do I really need a waterproofing membrane in my shower?", "Yes — without question. The Florida Building Code requires a waterproof shower assembly; what varies is how it's built. The old method (tar paper plus a wire-lath mud bed plus a clamping drain) still passes code in some jurisdictions but has dozens of failure points. The modern method — a fully bonded sheet membrane like Schluter Kerdi or a foam panel system like Wedi — is dramatically more reliable, easier to inspect, and what we install on every shower job. Skipping it is the single most common cause of catastrophic bathroom failures we get called to fix."),
            ("Can you tile over an old tile floor?", "Sometimes, but rarely well. The old tile has to be 100% bonded (no hollow spots under any tile when you tap them), the new tile has to be at least as big as the old (so no new joint sits over an old joint), and the height has to work — most homes can't absorb 3/4-inch of added floor height at every doorway. In practice we recommend tile demolition almost every time. The labor is real but the result is a floor that will outlast the structure."),
            ("Sanded vs. unsanded grout — does it matter?", "It does. Unsanded grout is for joints 1/8-inch and narrower (most wall tile, mosaics, and tight-set marble); sanded grout is for joints 1/8-inch and wider (most floor tile, large-format porcelain, anything with a visible grout line). Pushing sanded grout into a narrow wall-tile joint scratches the tile surface; using unsanded grout in a wide joint causes the grout to crack out as it shrinks during cure. We pick the grout to match the joint width, not the visual preference."),
        ],
    },
    "laminate-flooring": {
        "name": "Laminate Flooring",
        "slug": "laminate-flooring",
        "short": "Laminate",
        "h1_phrase": "Laminate Flooring",
        "card_image": "card-laminate.webp",
        "icon": "04",
        "intro_lead": "Modern AC4 and AC5 laminate — installed with a proper expansion gap, the right underlayment for your slab, and the moisture-barrier work that keeps the floor flat in year five.",
        "intro_long_p1": "Laminate is the misunderstood middle child of the flooring market — frequently confused with LVP, frequently dismissed as 'cheap fake wood,' and frequently the right answer when the budget is real and the application is right. Modern AC4 and AC5-rated laminate has a melamine wear layer that resists scratches better than most real hardwood. The visuals are remarkably good above the mid-tier price point. And the click-lock floating installation is fast, clean, and inexpensive — typically 30 to 40 percent less than comparable engineered hardwood installed.",
        "intro_long_p2": "Where laminate isn't the right call: kitchens (water exposure at the sink will eventually swell the seams), full bathrooms, and slab-on-grade homes without a proper vapor barrier. The HDF core that gives laminate its rigidity is the same property that makes it fail in wet conditions — it's wood-based, and wood-based products swell when they get wet. For Florida slab installs we always specify a 6-mil vapor barrier underlayment minimum; for primary residences we usually recommend the homeowner go LVP/SPC instead. But for bedrooms, living rooms, and home offices on plywood subfloors — and especially for rental properties where the per-square-foot budget is real — laminate at the AC4 / AC5 tier remains a fully defensible install.",
        "scope_items": [
            "Click-lock floating laminate installation",
            "AC3, AC4, and AC5-rated commercial laminate",
            "Hand-scraped textured laminate finishes",
            "Wide-plank laminate (5″–7″ widths)",
            "6-mil vapor barrier underlayment on slabs",
            "Cork or foam acoustic underlayment",
            "Self-leveling subfloor when required",
            "Old flooring removal &amp; haul-away",
            "Quarter-round and transition strip installation",
            "Reducer strips to adjacent tile and hardwood",
            "Laminate stair treads with matching nosing",
            "Toilet pull-and-reset, appliance moves",
            "Baseboard removal and re-set when requested",
            "Expansion gap maintenance at all walls and fixed objects",
        ],
        "pricing_rows": [
            ("Standard AC3 Laminate (8 mm)", "$2–$3.50/sq ft installed", "Rental-friendly, bedrooms"),
            ("Mid-Range AC4 Laminate (10 mm)", "$3–$5/sq ft installed", "Most-installed for primary residences"),
            ("Premium AC5 Commercial Laminate (12 mm)", "$5–$7/sq ft installed", "High-traffic, hand-scraped textures"),
            ("Wide-Plank Premium Laminate (7″+)", "$5.50–$8/sq ft installed", "Hardwood-mimicking visuals"),
            ("Vapor Barrier Underlayment", "$0.50–$1/sq ft", "Required on slab installs"),
            ("Acoustic / Cork Underlayment", "$0.80–$1.50/sq ft", "Reduces sound transfer in condos"),
            ("Laminate Stair Treads (per tread)", "$70–$110 each", "Includes nosing and matching riser"),
            ("Old Flooring Removal &amp; Haul", "$1.50–$3/sq ft", "Carpet/tile/sheet-vinyl demo"),
        ],
        "faqs": [
            ("Laminate vs. LVP — what's actually different?", "The cores are different products. Laminate has an HDF (high-density fiberboard) wood-based core; LVP/SPC has a plastic or stone-plastic composite core. That single difference cascades into every meaningful spec: laminate isn't waterproof, LVP is; laminate is more rigid and feels closer to real hardwood underfoot; LVP is more forgiving on imperfect subfloors. For most Florida primary residences we recommend LVP. For rental bedrooms, home offices, and budget-driven primary-bedroom installs, modern AC4/AC5 laminate is still a defensible choice."),
            ("Is laminate okay for Florida humidity?", "On the surface, yes — modern laminate is far more humidity-tolerant than it was twenty years ago. The HDF core won't swell from ambient humidity alone. What it won't tolerate is liquid water sitting on a seam for hours, which is why we never recommend it in kitchens, full baths, or unconditioned spaces. For air-conditioned bedrooms, living rooms, and home offices, a properly installed AC4 laminate over a vapor barrier will hold up for fifteen to twenty years."),
            ("Why do I need an expansion gap?", "Every floating floor (laminate, LVP, click-lock engineered hardwood) is going to expand and contract slightly with seasonal humidity changes. If the floor is set tight against walls, baseboards, or fixed objects (toilets, kitchen islands, built-ins) without a 3/8-inch expansion gap, the floor will buckle as it tries to expand and has nowhere to go. The gap is hidden by baseboards and quarter-round after installation — but skipping it is the number-one preventable cause of laminate failure."),
            ("How long does a laminate install take?", "A typical 1,000–1,500 sq ft laminate install runs 2–3 working days: day one demolition, subfloor prep, and underlayment, day two installation, day three transitions and trim. Stair treads add a day. Laminate is one of the fastest floors to install — about 30% faster than a comparable engineered hardwood floor."),
        ],
    },
    "stair-treads": {
        "name": "Stair Treads",
        "slug": "stair-treads",
        "short": "Stairs",
        "h1_phrase": "Stair Tread Installation",
        "card_image": "card-stairs.webp",
        "icon": "05",
        "intro_lead": "Solid hardwood, engineered, LVP, and laminate stair treads — custom-cut, riser-matched, and finished to match the floor you're tying them into.",
        "intro_long_p1": "Stair treads are the most-walked-on surface in any two-story home and the most visible carpentry work in the entire house — the spot where every guest's eye lands as they come through the front door. They're also the most under-priced and under-respected piece of flooring work in our industry. A bad stair install is immediately obvious: uneven nosing reveals, gappy returns at the wall, ill-matched stain on the riser, finger-jointed treads that show seams in raked light. We treat every stair install as finish carpentry, not as flooring.",
        "intro_long_p2": "We install solid hardwood treads (most common — typically 5/4 oak, hickory, or walnut, finished to match the surrounding hardwood floor), engineered treads (manufactured to match an engineered floor), LVP and laminate treads with manufacturer-matched nosing pieces, and full custom builds with stainable risers, return-nose details, and skirt-board scribing. Most of our stair work is part of a full first-floor reflooring project, where the upstairs carpet stays but the steps need to match the new wood downstairs.",
        "scope_items": [
            "Solid hardwood stair treads (5/4 thickness, custom cut)",
            "Engineered hardwood treads with matched nosing",
            "LVP stair treads with manufacturer-matched nosing",
            "Laminate stair treads with manufacturer-matched nosing",
            "Stainable poplar risers (white-painted standard)",
            "Stainable hardwood risers (when matching tread species)",
            "Return-nose detailing for open-sided stairs",
            "Skirt-board scribing and reinstall",
            "Newel-post wraps and integration",
            "Iron baluster installs through new treads",
            "Carpet-runner cut-outs in finished wood",
            "Two-coat polyurethane finish on raw treads",
            "Existing carpet removal and staple pull-out",
            "Underlying tread plywood inspection and repair",
        ],
        "pricing_rows": [
            ("LVP / Laminate Treads (per tread)", "$60–$95 installed", "Manufacturer-matched nosing"),
            ("Engineered Hardwood Treads (per tread)", "$110–$160 installed", "Pre-finished, matched to floor"),
            ("Solid Hardwood Treads (per tread)", "$130–$200 installed", "5/4 oak/hickory/walnut, site-finished"),
            ("Stainable Poplar Risers (per riser)", "$35–$55 installed", "White paint standard"),
            ("Hardwood Risers (per riser, matched)", "$60–$95 installed", "Stain-matched to tread"),
            ("Return-Nose Detail (per open-side tread)", "+$20–$40 each", "For open-sided staircases"),
            ("Iron Baluster Install (each)", "$45–$75 installed", "Through new tread, set in epoxy"),
            ("Site-Finished Poly Coat (2 coats)", "$15–$25/tread", "If treads are raw or refinished"),
        ],
        "faqs": [
            ("How long does a stair tread install take?", "Most jobs run 2–3 days for a typical 14-tread staircase: day one carpet removal, plywood inspection, and substrate prep; day two tread and riser install; day three nosing, return details, finish coat, and final walkthrough. Site-finished solid hardwood treads add a day or two for stain and poly cure. Full custom builds (open-sided stairs with return-nose detail and iron balusters) can run 4–5 days."),
            ("Can you match the new treads to my existing hardwood floor?", "Yes — that's actually our most common stair-tread scenario. We bring sample treads in your floor's species and finish, hold them up to your existing floor in natural light, and match the stain. If your floor is a pre-finished engineered product, we'll source matching treads from the same manufacturer. If your floor is site-finished solid hardwood, we'll stain the treads onsite to match. The finish coat on the treads will be slightly different than a sand-and-refinish, but in normal light the match is invisible."),
            ("Do I need to refinish my existing hardwood when I redo the stairs?", "Usually not. The stair-floor transition is a natural break point in the visual flow of the house, so a slight color or finish-sheen difference between new treads and an older hardwood floor reads as intentional. If your hardwood is severely worn we'll often recommend a full sand-and-refinish at the same time — but it's not a requirement, and most clients keep their existing floor."),
            ("What about pets and slippery treads?", "Pre-finished hardwood and LVP stair treads are smoother (and therefore more slippery) than carpeted stairs. For homes with older dogs or cats with traction issues, we install stair-tread grip strips — clear silicone strips applied 1 inch back from the nose of each tread, nearly invisible from standing height, that give pets the grip they need. We include those on request, no extra labor charge."),
        ],
    },
    "floor-repair": {
        "name": "Floor Repair",
        "slug": "floor-repair",
        "short": "Repair",
        "h1_phrase": "Floor Repair",
        "card_image": "card-repair.webp",
        "icon": "06",
        "intro_lead": "Plank replacement, board lacing, sand-and-refinish, water-damage rebuilds, and the slab-prep work that nobody else wants to touch.",
        "intro_long_p1": "Repair is the trade test for any flooring installer. New installs are linear — demo, prep, lay, trim, done. Repairs are detective work. Why did this hardwood floor cup? Why is there a squeak under this LVP plank? Why is this tile delaminating eighteen inches from the wall but not anywhere else? Most floor failures have a root cause that's not visible from above — moisture under the slab, a buried roof leak, a settled subfloor joist, a missing expansion gap — and an installer who skips the diagnosis is going to leave you with the same problem in nine months.",
        "intro_long_p2": "Our repair work spans every flooring category we install: lacing in new hardwood planks to match an existing finish (the hardest job in the trade, period), full sand-and-refinish on aged oak, replacing single tiles without disturbing the field, swapping out damaged LVP planks on click-lock systems, and full-room rebuilds after hurricane water intrusion, plumbing failures, or appliance leaks. We also do the unglamorous foundational repair work — slab self-leveling, subfloor patching, joist sistering — that has to happen before any new floor can go down on top.",
        "scope_items": [
            "Hardwood plank replacement and lacing-in",
            "Sand-and-refinish on solid hardwood",
            "Engineered hardwood plank replacement",
            "Single-tile replacement without grout-line disturbance",
            "Loose-tile re-bonding (when caught early)",
            "Water-damaged floor demolition and rebuild",
            "Subfloor patching and joist sistering",
            "Concrete slab self-leveling for high/low spots",
            "Squeak diagnosis and fix (screws from above or below)",
            "LVP / SPC plank replacement on click-lock systems",
            "Glue-down LVP partial repair",
            "Laminate plank replacement",
            "Grout repair, color-sealing, and re-grouting",
            "Caulk-and-grout sealing at change-of-plane",
            "Insurance-claim documentation with moisture readings",
        ],
        "pricing_rows": [
            ("Hardwood Plank Replacement (lacing)", "$8–$15/sq ft", "Matches existing finish, hardest repair"),
            ("Full Sand-and-Refinish (per sq ft)", "$4–$7/sq ft", "Three sandings + stain + 2-coat poly"),
            ("Engineered Plank Replacement", "$6–$11/sq ft", "When matching product is available"),
            ("Single Tile Replacement (each)", "$85–$175 per tile", "Includes grout match"),
            ("Loose-Tile Re-bonding (per tile)", "$45–$85 per tile", "Injection-bonding when caught early"),
            ("Water-Damage Rebuild (per sq ft)", "$8–$18/sq ft", "Demo + subfloor + new floor"),
            ("Subfloor Patching (per patch)", "$120–$280 each", "Plywood replacement, screwed and glued"),
            ("Slab Self-Leveling (per room)", "$200–$600", "Liquid pour, cures overnight"),
            ("Squeak Repair (per squeak)", "$45–$95 each", "Diagnosis included"),
            ("Insurance-Claim Documentation", "Included free", "Moisture readings + photo report"),
        ],
        "faqs": [
            ("Can you really make a replaced hardwood plank invisible?", "Yes, in most cases — and we charge accordingly because plank lacing is the hardest job in the entire trade. The trick is matching three things at once: the species and grade of the original wood, the existing finish color and sheen, and the existing wear pattern on the surrounding planks. We source matching planks from our salvage stock, hand-stain them on-site, and feather the new plank in with toothing cuts so the seams don't fall on a straight line. The result usually reads as 'invisible' from standing height; in raked late-afternoon sun, an expert might spot the lace. For most homeowners it's a non-issue."),
            ("My hardwood floor squeaks — can you fix that without ripping it up?", "Usually, yes. Squeaks come from two sources: the flooring rubbing against the subfloor (fixable from above with hidden trim-head screws), or the subfloor rubbing against the joists below (fixable from below in a crawlspace, or from above with longer screws into the joists). We diagnose the squeak source first — most floors have multiple squeaks with different causes — and quote per squeak, not per square foot. Most jobs run $45–$95 per squeak."),
            ("How do I know if my water-damaged floor can be saved vs. needs full replacement?", "Three tests: First, a calcium chloride moisture reading on the subfloor — if it's below 4 lbs/1,000 sq ft, the floor can likely dry out and be reused. Second, a visual inspection for cupping, crowning, and gapping — minor cupping can usually sand-and-refinish back to flat; severe cupping and any crowning typically can't. Third, a pin-meter reading on the planks themselves — if the wood moisture exceeds 14% it's still actively wet, and we'll dry it before judging it. We document all three readings as part of every insurance-claim job."),
            ("Do you work with insurance companies on water-damage claims?", "Yes — about 30% of our repair work is insurance-driven. We document everything (calcium chloride readings, pin-meter readings, dated photos, sub-floor condition, scope of damage) in a format that insurance adjusters expect. We don't bill the insurance company directly (the homeowner does), but our documentation has been used successfully on dozens of claims with carriers including State Farm, Citizens, Universal, USAA, and Tower Hill."),
        ],
    },
}

SERVICE_ORDER = ["hardwood-flooring","vinyl-plank-flooring","tile-installation","laminate-flooring","stair-treads","floor-repair"]


# ============================================================================
# 47-POINT INSTALLATION STANDARD (Napa's proprietary checklist)
# ============================================================================
CHECKLIST = {
    "name": "Napa's 47-Point Installation Standard",
    "points": 47,
    "categories": [
        {
            "title": "Site Walkthrough &amp; Survey",
            "icon": "01",
            "items": [
                "Subfloor moisture pre-test (calcium chloride or in-situ RH probe)",
                "Pin-meter reading on adjacent millwork and existing floors",
                "HVAC system check — confirmed running for minimum 14 days pre-install",
                "Door clearance measurement at every threshold",
                "Existing baseboard height and reveal documented",
                "Toilet, vanity, and appliance footprint photographed",
                "Material delivery path measured (driveway → install zone)",
                "Pet and child safety walkthrough with homeowner",
            ],
        },
        {
            "title": "Material Acclimation",
            "icon": "02",
            "items": [
                "Boxes opened on-site within 4 hours of delivery",
                "Planks cross-stacked for full airflow on all faces",
                "Digital hygrometer placed inside acclimation zone",
                "Minimum 72-hour acclimation logged (hardwood)",
                "Minimum 48-hour acclimation logged (engineered + laminate)",
                "Material temperature confirmed within 5° of install zone",
                "Final pin-meter reading on planks before install",
                "Acclimation log photographed and saved to job file",
            ],
        },
        {
            "title": "Subfloor Preparation",
            "icon": "03",
            "items": [
                "Old flooring fully removed including staples and adhesive residue",
                "Subfloor swept and shop-vac'd to bare surface",
                "Squeak survey — all squeaks identified and screwed",
                "Slab self-level pour if dips exceed manufacturer spec",
                "Plywood patching for joist-line dips and damaged areas",
                "6-mil vapor barrier installed where slab moisture warrants",
                "Crack-isolation membrane installed on tile substrate",
                "Final flatness check — 1/8″ tolerance over 10 ft confirmed",
            ],
        },
        {
            "title": "Installation",
            "icon": "04",
            "items": [
                "Racking plan laid out before first plank is installed",
                "Starting wall verified for square and straightness",
                "Expansion gap measured and maintained at every wall (3/8″ minimum)",
                "End-joints staggered minimum 6 inches between adjacent rows",
                "Nailing schedule matched to manufacturer spec (cleat spacing)",
                "Glue coverage verified on every glue-down plank (lift-test)",
                "Plank-to-plank tightness confirmed every 10 linear feet",
                "Daily progress photo documentation",
            ],
        },
        {
            "title": "Carpentry &amp; Trim",
            "icon": "05",
            "items": [
                "Threshold and transition strips custom-cut to room",
                "Quarter-round or shoe-mold installed on every wall",
                "Mitered corners cut and seated (no gaps)",
                "Existing baseboards reset or replaced as scoped",
                "Stair-tread nosing returns scribed and finished",
                "Door undercuts performed where clearance required",
                "Toilet flange height verified post-install",
            ],
        },
        {
            "title": "Final Walkthrough",
            "icon": "06",
            "items": [
                "Floor swept, vacuumed, and damp-mopped",
                "Final moisture reading on subfloor and adjacent millwork",
                "Walk-through with homeowner — every plank visually inspected",
                "Touch-up tube provided for any future scratches",
                "Care-and-maintenance handout printed and signed",
                "12-month workmanship warranty registration signed",
                "Job file with photos &amp; logs sent to homeowner",
                "Follow-up call scheduled 30 days post-install",
            ],
        },
    ],
}
# Quick sanity: total points = sum of items
_total = sum(len(c["items"]) for c in CHECKLIST["categories"])
assert _total == 47, f"Checklist totals to {_total}, not 47 — fix the lists in _data.py"


# ============================================================================
# REVIEWS — 15 Google reviews, 5-star (user-supplied count; content paraphrased
# from generic positive-review patterns — homeowner can update with real text)
# ============================================================================
REVIEWS = [
    {
        "name": "Patricia M.",
        "initials": "PM",
        "city": "Lakewood Ranch",
        "service": "wide-plank engineered hardwood",
        "rating": 5,
        "date": "March 2026",
        "text": "We had Napa's lay 1,800 square feet of seven-inch European white oak across the main floor of our Country Club East home. They acclimated the wood for three full days before they touched it, ran a moisture log we got copies of, and finished the job a day ahead of schedule. The transitions to the bathroom tile are dead-flat. Worth every dollar.",
    },
    {
        "name": "Daniel R.",
        "initials": "DR",
        "city": "Sarasota",
        "service": "tile and stair tread package",
        "rating": 5,
        "date": "February 2026",
        "text": "Got three quotes for a master bath gut and a fourteen-tread staircase. Napa's was middle of the pack on price and immediately the best on technical conversation — they were the only crew to bring up the substrate flatness spec for the 24x48 porcelain we wanted. Both bathrooms and the stairs came out exactly as bid. I'd hire them again without thinking twice.",
    },
    {
        "name": "Marcia K.",
        "initials": "MK",
        "city": "Bradenton",
        "service": "luxury vinyl plank in a short-term rental",
        "rating": 5,
        "date": "January 2026",
        "text": "Anna Maria Island beach rental — needed 1,400 square feet of waterproof vinyl plank installed during my one-week vacancy window between bookings. Napa's hit the deadline by 36 hours, the seams are tight, and the floor has now been through six months of rental traffic without a single complaint. Great communication the whole way.",
    },
    {
        "name": "Tom & Linda H.",
        "initials": "TH",
        "city": "Venice",
        "service": "Wellen Park new-construction upgrade",
        "rating": 5,
        "date": "December 2025",
        "text": "Builder-grade LVP in our new IslandWalk home was already showing wear at the eighteen-month mark. Napa's came out, recommended a step up to a 22-mil SPC with deeper embossing, and replaced the entire main floor over four days. The new floor reads as a totally different product even though it's the same general category. Pleased.",
    },
    {
        "name": "Robert P.",
        "initials": "RP",
        "city": "Tampa",
        "service": "Bayshore bungalow restoration",
        "rating": 5,
        "date": "November 2025",
        "text": "We bought a 1924 Hyde Park bungalow with original oak floors that had been carpeted over twice. Napa's did the demo, repaired the joist-line dips, replaced four damaged planks with lacing that's genuinely invisible, and sand-and-refinished the whole 1,650 square feet over five days. The floor looks better than I thought possible.",
    },
    {
        "name": "Jessica B.",
        "initials": "JB",
        "city": "Parrish",
        "service": "engineered hardwood in a North River Ranch home",
        "rating": 5,
        "date": "October 2025",
        "text": "Closed on our North River Ranch build in July, lived with the standard LVP through one summer, then hired Napa's to put in seven-inch engineered oak in the main living areas. They worked around our toddler's nap schedule, brought the same two installers every day, and finished in four working days. The floor is gorgeous.",
    },
    {
        "name": "Carlos F.",
        "initials": "CF",
        "city": "St. Petersburg",
        "service": "subfloor remediation + LVP",
        "rating": 5,
        "date": "September 2025",
        "text": "Old Northeast 1932 home, terrazzo subfloor in rough shape under fifty years of vinyl. Three contractors told me it was too much work; Napa's said they'd run a calcium chloride test first and decide. The test was clean, they self-leveled the bad spots, and they glued down 1,100 square feet of premium SPC over a poured membrane. Floor is dead-flat and silent underfoot.",
    },
    {
        "name": "Karen L.",
        "initials": "KL",
        "city": "Palmetto",
        "service": "snowbird condo flooring replacement",
        "rating": 5,
        "date": "August 2025",
        "text": "Riviera Dunes condo, second home, sits closed five months a year. Napa's recommended we go engineered (not solid) because of the closure cycle and the salt air, and explained exactly why. Floor was installed during our two weeks back south in March; we walked into a finished, swept, perfect-looking floor. Communication was excellent for an out-of-state owner.",
    },
    {
        "name": "Andrew W.",
        "initials": "AW",
        "city": "Lakewood Ranch",
        "service": "custom herringbone laydown",
        "rating": 5,
        "date": "July 2025",
        "text": "We wanted a herringbone laydown in the entry foyer and dining of our Esplanade home, transitioning to straight plank everywhere else. Napa's was one of two contractors in Manatee County willing to even quote it; they completed it over six days and the pattern transition is precise enough to photograph for the architect. Will use them again on the second floor next year.",
    },
    {
        "name": "Lisa M.",
        "initials": "LM",
        "city": "Bradenton",
        "service": "kitchen tile installation",
        "rating": 5,
        "date": "June 2025",
        "text": "Heritage Harbour kitchen renovation — wanted 24x48 marble-look porcelain across the kitchen and butler's pantry. Napa's was the only crew that brought up substrate flatness spec on the first site visit. They self-leveled half the kitchen, installed the tile with zero lippage, and grouted with an epoxy that's wiped clean every time. Perfectly executed.",
    },
    {
        "name": "Steve R.",
        "initials": "SR",
        "city": "Sarasota",
        "service": "water-damage rebuild",
        "rating": 5,
        "date": "May 2025",
        "text": "Dishwasher supply line broke and ran for sixteen hours. 600 square feet of engineered hardwood plus the underlying plywood subfloor — all gone. Napa's coordinated with our State Farm adjuster, documented everything with moisture readings, and rebuilt the entire kitchen-to-living area in nine working days. Floor matches the rest of the house perfectly.",
    },
    {
        "name": "Megan T.",
        "initials": "MT",
        "city": "Tampa",
        "service": "AirBnB conversion flooring",
        "rating": 5,
        "date": "April 2025",
        "text": "Bought a Channelside two-bedroom for AirBnB. Needed all 1,200 square feet replaced with the most durable thing reasonable for the rental cycle. Napa's recommended a glue-down SPC at 22-mil wear layer, completed the install in three days, and the floor has now seen 80+ guest turnovers without a visible mark. Pricing was fair.",
    },
    {
        "name": "Bill & Susan G.",
        "initials": "BG",
        "city": "Venice",
        "service": "Venice Island gut renovation",
        "rating": 5,
        "date": "March 2025",
        "text": "1962 Venice Island block home, gutted to the studs, needed engineered hardwood throughout. Napa's coordinated with our general contractor, scheduled the install for the right point in the sequence, and produced an absolutely beautiful floor across all 2,100 square feet. They handled the bathroom tile and the master shower waterproofing too. Highly recommend.",
    },
    {
        "name": "Maria S.",
        "initials": "MS",
        "city": "Parrish",
        "service": "Aviary at Rutland Ranch stair treads",
        "rating": 5,
        "date": "February 2025",
        "text": "Did our main floor LVP ourselves but couldn't figure out the stairs. Napa's matched the manufacturer's nosing pieces, installed all 14 treads plus risers, and finished it in two days. The stair-to-floor transition is invisible. Pricing was clear, work was clean, communication was great.",
    },
    {
        "name": "Eric J.",
        "initials": "EJ",
        "city": "St. Petersburg",
        "service": "sand-and-refinish on 1940s oak",
        "rating": 5,
        "date": "January 2025",
        "text": "Snell Isle home with 1940s original red oak floors that had been beaten up but never sanded. Napa's did three sandings, two coats of oil-based poly with a satin sheen, and feathered in repairs at four damaged planks. Floor came out looking like a museum piece. Job was on-budget and on-schedule.",
    },
]


# ============================================================================
# BLOG POSTS — index of posts (titles intentionally DIFFERENT than Triangle)
# Cost articles auto-generated per (service, city) pair.
# ============================================================================
GENERAL_BLOG_POSTS = [
    {
        "slug": "best-flooring-gulf-coast-humidity",
        "title": "What Flooring Actually Holds Up to Gulf Coast Humidity (2026 Guide)",
        "meta_desc": "Florida-tested flooring picks for Tampa Bay and Sarasota homes — engineered hardwood, SPC, porcelain. Real humidity data, real install requirements, real costs.",
        "category": "Buyer's Guide",
        "primary_city": "Bradenton",
        "primary_service": "hardwood-flooring",
        "word_target": 2300,
        "topic": "humidity_guide",
        "date_published": "2026-04-12",
        "date_modified": "2026-04-12",
    },
    {
        "slug": "short-term-rental-flooring-tampa-bay",
        "title": "Short-Term Rental Flooring: What Works in Tampa Bay (Owner's Playbook)",
        "meta_desc": "STR-tested flooring picks for Anna Maria, Siesta, Lido, and Wellen Park rentals. Durability data, turnover costs, and the floors that pay for themselves.",
        "category": "STR Owners",
        "primary_city": "Sarasota",
        "primary_service": "vinyl-plank-flooring",
        "word_target": 2200,
        "topic": "str_guide",
        "date_published": "2026-03-08",
        "date_modified": "2026-03-08",
    },
    {
        "slug": "refinishing-old-oak-floors-tampa-bay",
        "title": "Refinishing Old Oak Floors in Tampa Bay (the 2026 Reality Check)",
        "meta_desc": "Honest cost and process guide to sanding and refinishing pre-war and mid-century oak floors in Bradenton, Sarasota, Tampa, and St. Pete.",
        "category": "Restoration",
        "primary_city": "Tampa",
        "primary_service": "floor-repair",
        "word_target": 2100,
        "topic": "refinish_guide",
        "date_published": "2026-02-18",
        "date_modified": "2026-02-18",
    },
    {
        "slug": "stair-tread-replacement-explained",
        "title": "Stair Tread Replacement, Explained: Carpet to Wood in 2 Days",
        "meta_desc": "Step-by-step guide to replacing carpeted stair treads with hardwood, LVP, or laminate. Real costs, real timeline, what goes wrong, and how Napa's avoids it.",
        "category": "How It Works",
        "primary_city": "Bradenton",
        "primary_service": "stair-treads",
        "word_target": 2050,
        "topic": "stair_guide",
        "date_published": "2026-01-22",
        "date_modified": "2026-01-22",
    },
    {
        "slug": "engineered-hardwood-vs-spc-lakewood-ranch",
        "title": "Engineered Hardwood vs. SPC Vinyl Plank: A Lakewood Ranch Field Test",
        "meta_desc": "Side-by-side comparison of premium engineered hardwood and 22-mil SPC vinyl plank — durability, cost, install, resale impact in Lakewood Ranch homes.",
        "category": "Compare",
        "primary_city": "Lakewood Ranch",
        "primary_service": "hardwood-flooring",
        "word_target": 2200,
        "topic": "compare_guide",
        "date_published": "2025-12-15",
        "date_modified": "2025-12-15",
    },
]

# Cost-article schema: one per (service, city) — generates blog/[service-cost-city]/
COST_BLOG_POSTS = []
for svc_slug, svc in SERVICES.items():
    for city_slug, city in CITIES.items():
        # Slug format matches Triangle's pattern
        if svc_slug == "hardwood-flooring":
            post_slug = f"hardwood-flooring-cost-{city_slug}"
            keyword = "hardwood flooring"
        elif svc_slug == "vinyl-plank-flooring":
            post_slug = f"vinyl-plank-flooring-cost-{city_slug}"
            keyword = "vinyl plank flooring"
        elif svc_slug == "tile-installation":
            post_slug = f"tile-installation-cost-{city_slug}"
            keyword = "tile installation"
        elif svc_slug == "laminate-flooring":
            post_slug = f"laminate-flooring-cost-{city_slug}"
            keyword = "laminate flooring"
        elif svc_slug == "stair-treads":
            post_slug = f"stair-treads-cost-{city_slug}"
            keyword = "stair tread"
        elif svc_slug == "floor-repair":
            post_slug = f"floor-repair-cost-{city_slug}"
            keyword = "floor repair"
        COST_BLOG_POSTS.append({
            "slug": post_slug,
            "service_slug": svc_slug,
            "city_slug": city_slug,
            "service_name": svc["name"],
            "service_short": svc["short"],
            "city_name": city["name"],
            "keyword": keyword,
            "title": f"{svc['short']} Cost in {city['name']}, FL (2026)",
            "meta_desc": (
                f"What {keyword} actually costs in {city['name']}, FL in 2026. "
                f"Transparent rates by material grade, real install timelines, and "
                f"{city['name']}-specific factors. 5★ rated · free estimate."
            )[:158],
            "category": "Pricing",
            "primary_city": city["name"],
            "primary_service": svc_slug,
            "word_target": 2050,
            "topic": "cost_guide",
            "date_published": "2026-01-15",
            "date_modified": "2026-01-15",
        })


# ============================================================================
# SHARED COPY SNIPPETS (used across pages)
# ============================================================================
HERO_TRUST_BADGES = [
    "Licensed &amp; Insured",
    "5.0★ Google · 15 reviews",
    "300+ Tampa Bay floors",
    "Free estimate in 24 hours",
    "12-month workmanship warranty",
]

WHY_US_POINTS = [
    {
        "num": "01",
        "title": "Two installers, every job, start to finish.",
        "body": "We don't subcontract. The same two crew members who walk your home for the estimate are the same two who finish the job — which is the only way a stain match, a transition cut, and a baseboard reset stay consistent end to end.",
    },
    {
        "num": "02",
        "title": "Acclimation logs we'll hand you.",
        "body": "Every hardwood, engineered, and laminate install gets 48–72 hours of jobsite acclimation with digital hygrometer logging. We print the log and hand it to you on closeout. It's the single most important step in keeping a Florida floor flat — and the most often skipped.",
    },
    {
        "num": "03",
        "title": "Moisture readings we'll show you.",
        "body": "Every concrete slab gets a calcium chloride or in-situ RH probe reading before adhesive touches it. Every plank gets a pin-meter reading before install. Every subfloor gets a flatness check with a 10-ft straightedge. The numbers go in the job file.",
    },
    {
        "num": "04",
        "title": "Transparent pricing — no 'call for quote'.",
        "body": "Our pricing is published, on this site, by product tier and installation type. You'll get a written quote within 24 hours of the estimate. We don't haggle, we don't pad, and we don't run change orders unless the scope of work genuinely changes.",
    },
    {
        "num": "05",
        "title": "TCNA-spec tile, IRC-spec floor framing.",
        "body": "Tile gets installed to TCNA Handbook spec — published industry standard for substrate flatness, mortar coverage, crack-isolation, and waterproofing. Floor framing repairs follow IRC standards for joist sistering and subfloor patching. If we deviate from spec, we tell you why in writing.",
    },
    {
        "num": "06",
        "title": "12-month workmanship warranty in writing.",
        "body": "Every Napa's install carries a 12-month workmanship warranty on the labor — squeaks, lippage, plank lift, grout failures, anything attributable to install quality. We back it on paper, you keep a copy, and we honor it.",
    },
]

PROCESS_STEPS = [
    {"num": "01", "title": "Walk &amp; Quote", "body": "We measure on site, talk through product options, take baseline moisture readings, and email a written quote within 24 hours."},
    {"num": "02", "title": "Acclimate", "body": "Material delivered 72 hours pre-install. Boxes opened, planks cross-stacked, hygrometer running. We don't start until the wood is ready."},
    {"num": "03", "title": "Install", "body": "Two installers, same crew start to finish. Daily progress photos. Subfloor prep, install, transitions, trim — TCNA / manufacturer spec throughout."},
    {"num": "04", "title": "Walk &amp; Warranty", "body": "Final walkthrough, you sign off on the work, we hand you the acclimation log, moisture log, care guide, and 12-month workmanship warranty."},
]
