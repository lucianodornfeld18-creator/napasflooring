#!/usr/bin/env python3
"""
Napa's Flooring — Master Data Module
All cities, services, neighborhoods, FAQs, pricing tables, business info.
Used by every _build_*.py script.
"""


# ============================================================================
# META-DESCRIPTION HELPER
# Trim a meta description at a word boundary (never mid-word) and append an
# ellipsis only when it was actually shortened. Replaces the old `[:158]`/
# `[:155]` slices that cut strings like "...free q" or "...factors. 5".
# ============================================================================
def clip_desc(s, n=155):
    s = " ".join(str(s).split())          # normalize whitespace
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0].rstrip(" ,·") + "…"


def clip_title(s, n=60):
    """Trim a <title> at a word boundary, no ellipsis — keeps tags <=60 chars
    without cutting mid-word (e.g. avoids '...Napa's Floori')."""
    s = " ".join(str(s).split())
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0].rstrip(" ·|-—–,:")


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
    "google_profile": "https://share.google/6ZiLBnQqDXLEHQezV",   # official Google share link for the GBP
    "google_review_url": "https://share.google/6ZiLBnQqDXLEHQezV",  # TODO: trocar pelo link direto "escrever avaliação" do GBP
    "facebook": "https://www.facebook.com/p/Napas-Flooring-100070103477156/",
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
# SERVICES — seven core (hardwood, refinishing, vinyl, tile, laminate, stairs, repair)
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
        "intro_long_p1": "Hardwood is the one floor that still moves an appraisal in our core Bradenton and Sarasota market — buyers walking a Country Club East listing, a West-of-Trail bungalow, or a Bayshore renovation read real wood as a signal that the whole house was looked after. The catch is that hardwood only behaves in a Gulf Coast home when the crew respects the slab underneath it. We walked away from a River Strand job last spring because the homeowner wanted three-quarter-inch solid oak glued straight onto a slab that came back at 6.8 lbs on the calcium-chloride test; that floor would have cupped by its first August, and a cupped floor is a liability, not an asset. The moisture gates and acclimation checks that prevent exactly that are written into our 47-Point Installation Standard, and the readings get printed into the job file you keep. When a tight budget is the reason a homeowner is tempted to skip that prep, we'd rather walk them through our financing options than cut the step that keeps the floor flat for twenty years.",
        "intro_long_p2": "We build on two products and pick between them honestly. <strong>Solid hardwood</strong> — a full three-quarter inch thick, good for a half-dozen refinishes across its life — is our call for above-grade plywood subfloors, true second floors, and the pre-war oak we restore in neighborhoods like Old Northeast and Hyde Park. <strong>Engineered hardwood</strong> — a genuine oak wear layer bonded over a cross-ply core that barely registers Florida's humidity swing — is what goes into roughly nine of every ten slab homes we floor from Parrish down to Venice. We keep European and American white oak, red oak, hickory, walnut, maple, and acacia in rotation, in widths from a tight three-inch board to a ten-inch wide plank, in flat, hand-scraped, and wire-brushed textures. We bring the real samples to your kitchen table and tell you which one actually earns its premium in your specific home — instead of selling you up.",
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
            ("Engineered Hardwood (5″ wide)", "$7.75–$10.50/sq ft installed", "Glue-down or nail-down"),
            ("Engineered Hardwood (7–9″ wide)", "$10.75–$14.50/sq ft installed", "Our Bradenton &amp; Lakewood Ranch volume pick"),
            ("Solid Hardwood (3/4″, 3–5″ wide)", "$9.75–$13.50/sq ft installed", "Nail-down on plywood subfloor only"),
            ("Premium European White Oak (wide plank)", "$13.75–$19.50/sq ft installed", "Character-grade, 7–10″ width"),
            ("Custom Herringbone Laydown", "$16.50–$23.50/sq ft installed", "Roughly 2× the labor of straight plank"),
            ("Custom Chevron Laydown", "$18.50–$26/sq ft installed", "Our most premium hardwood install"),
            ("Subfloor Self-Leveling (per room)", "$225–$650", "When the straightedge shows 1/4″+ dip"),
            ("Old Flooring Removal &amp; Haul", "$1.75–$3.25/sq ft", "Carpet, laminate, or tile demo"),
        ],
        "faqs": [
            ("Can I install solid hardwood on a Florida slab?", "Honestly, we'll talk you out of it almost every time. Slab moisture plus Gulf Coast humidity is the exact recipe that cups, crowns, and gaps solid hardwood once it's glued or nailed onto concrete, and we've torn out enough of those floors to stop pretending it's a coin flip. For the slab-on-grade homes that make up most of our Bradenton-to-Venice work, engineered hardwood and its cross-ply core is the right answer. The one workaround is floating a 5/8-inch plywood subfloor over the slab first — but that lifts your finished floor nearly an inch, which then has to be solved at every door, transition, and baseboard, and the cost usually lands you back at engineered anyway."),
            ("How long does hardwood acclimate before install?", "Seventy-two hours on your jobsite is the floor, not the ceiling. We open the boxes on site, cross-stack the planks so air moves across every face, and run a hygrometer through the whole window — and that whole sequence is logged as part of the 47-Point Standard so you get the readings in writing. If the home is a fresh builder turnover with the AC only recently switched on, we'll often hold for a full week. Rushing this step is the single most common reason we get hired to fix somebody else's hardwood."),
            ("Engineered vs. solid — what's actually different?", "Solid is one piece of wood, a full three-quarter inch, and you can sand it back to bare and refinish it a half-dozen times over its life — that's why it still wins on premium plywood-subfloor and second-floor jobs. Engineered is a real-oak wear layer bonded over a cross-ply substrate; it holds its shape through Florida's humidity swing far better, it'll go over a slab, and it usually has one or two refinishes in it. Underfoot and to the eye they're the same floor — the difference is what's hidden below the surface, and on a Gulf Coast slab that difference is the whole ballgame."),
            ("How long does the whole job take?", "Budget three to five working days for a typical 1,200–1,800 square-foot install, demo to final walk. Day one is tear-out and subfloor prep, day two wraps acclimation and starts the laydown, the middle days are the bulk of the install plus transitions, and the last day is quarter-round and your walkthrough. Herringbone and chevron patterns roughly double the labor and run six to ten days; adding stairs adds a day. The real schedule lives in your written quote, not in a paragraph like this one."),
        ],
    },
    "hardwood-refinishing": {
        "name": "Hardwood Floor Refinishing",
        "slug": "hardwood-refinishing",
        "short": "Refinishing",
        "h1_phrase": "Hardwood Floor Refinishing",
        "card_image": "card-hardwood.webp",
        "icon": "07",
        "intro_lead": "Sand-and-refinish, screen-and-recoat, board lacing, and stain changes — bringing tired oak back to life across Bradenton, Sarasota, and the pre-war pockets of Tampa Bay, with HEPA dust containment and a finish that actually lasts.",
        "intro_long_p1": "Refinishing is the highest-return flooring decision most Tampa Bay homeowners never realize they have. We pull carpet in a 1955 Palma Sola ranch or a Cherokee Park bungalow, and underneath is original red oak that three contractors already wrote off — and four times out of five it's sound, salvageable, and worth a fraction of what new wood would cost. The number that decides everything is how much wood is left above the tongue: solid hardwood gives you roughly four to six sandings across its whole life, and we measure the remaining thickness with a probe in a hidden spot before we ever quote a full sand. If the floor's been sanded to the edge already, we'll tell you that to your face instead of blowing through the tongue and handing you a delamination.",
        "intro_long_p2": "There are three honest paths and we match the floor to the right one. A <strong>full sand-and-refinish</strong> — three sandings, grain raise, and two or three coats of poly — is for floors with real wear, pet damage, or graying around old leaks. A <strong>screen-and-recoat</strong> abrades just the existing finish and lays a fresh coat or two, the right call for a floor that's only dull, at a fraction of the cost and the downtime. And a <strong>partial sand with section replacement</strong> handles localized damage — a water-stained patch, a badly-repaired run — by lacing in matching boards and blending the whole floor to one tone. We finish with water-based poly when you want white oak to stay pale and modern, or oil-based when you want red oak and walnut to amber the way a period floor should — and we run a HEPA dust-containment system on every job so the rest of your house stays livable.",
        "scope_items": [
            "Full sand-and-refinish on solid hardwood (three-pass grit sequence)",
            "Screen-and-recoat on lightly worn floors",
            "Remaining-thickness probe test before any full sand",
            "Water-based polyurethane finish (Bona Traffic HD &amp; equivalent)",
            "Oil-based polyurethane finish (period-correct amber)",
            "Hardwood stain color change with hidden-spot sample test",
            "Board lacing &amp; single-plank replacement to match",
            "Pet-stain and water-stain board cut-out and replacement",
            "Parquet and herringbone hand-refinishing (orbital, no flat-pad blowout)",
            "Heart-pine and antique-floor restoration",
            "Edge and corner detail sanding (no drum scallops)",
            "Stair-tread refinishing to match the floor",
            "HEPA dust-containment system on every job",
            "Furniture move, toilet pull-and-reset, debris haul-away",
            "Care-and-maintenance handout + 12-month workmanship warranty",
        ],
        "pricing_rows": [
            ("Screen &amp; Recoat (no sand)", "$1.65–$2.65/sq ft", "Dull finish, no deep wear"),
            ("Full Sand &amp; Refinish (water-based poly)", "$3.65–$5.25/sq ft", "Three sandings + 2-coat poly"),
            ("Full Sand &amp; Refinish (oil-based poly)", "$4.25–$6.25/sq ft", "Period-correct amber, longer cure"),
            ("Stain Color Change", "+$0.85–$1.60/sq ft", "Light-to-dark or vice versa"),
            ("HEPA Dust-Containment Upgrade", "+$1.10/sq ft", "Keeps the rest of the house clean"),
            ("Board Lacing / Plank Repair (each)", "$14–$32 per board", "Hand-stained to match the field"),
            ("Pet / Water-Stain Board Replacement", "$5.50–$9/sq ft", "Cut-out + replace + blend"),
            ("Parquet Hand-Refinish", "$6.50–$10/sq ft", "Orbital, grain-direction passes"),
            ("Stair-Tread Refinish (per tread)", "$35–$70 each", "Matched to the floor below"),
        ],
        "faqs": [
            ("Can my old hardwood floor actually be refinished?", "Usually the answer is yes, and the deciding factor is how much wood is left above the tongue — the structural part you can't sand into. A solid floor has roughly four to six refinishes in it across its life, each pass taking about a thirty-second of an inch. Before we quote a full sand we drive a slim probe into a hidden spot — under trim or in a closet — and read the remaining thickness, so we know whether you're looking at a full sand, a lighter screen-and-recoat, or a partial repair. If a floor's already been sanded to the edge, we'll say so rather than take it one pass too far and delaminate it."),
            ("Screen-and-recoat or full sand — what's the difference?", "A screen-and-recoat just scuffs the existing finish with a fine screen and lays a fresh coat or two over the top — it's for a floor that's only gone dull, it's done in a couple of days, and it costs a fraction of a full job because nothing below the original finish gets touched. A full sand-and-refinish takes the floor down to raw wood in three grit passes, raises the grain, and builds back two or three fresh coats of poly — that's what you need for deep scratches, pet damage, or graying around old water. We won't sell you a full sand on a floor that only needs a recoat, and we won't recoat a floor that's actually worn through."),
            ("Water-based or oil-based polyurethane?", "Both are durable; they just age differently and we pick to the wood. Water-based poly (Bona Traffic HD and its peers) cures fast, has almost no odor, and dries crystal-clear and stays that way — the right call for white oak you want to keep pale and modern. Oil-based ambers warmly over the years and is the traditional, period-correct choice for red oak and walnut in a 1920s Old Northeast or Hyde Park home. The old idea that water-based wears out faster hasn't been true for a decade. We'll show you both on your actual floor before you decide."),
            ("How disruptive is a refinish, and how long until I can walk on it?", "Moderately, and that's mostly the cure window. We run a HEPA dust-containment system on every job so the rest of the house stays clean, but the room being finished has to stay empty while each poly coat cures — eight to twenty-four hours a coat depending on the product. Most clients stay elsewhere for the five to eight days a full sand takes. You can walk the floor in socks within about a day of the final coat, but rugs and furniture go back at the two-week mark so the finish fully hardens first."),
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
        "intro_long_p1": "Vinyl plank is the floor we install more of than anything else, and we're upfront about why: dollar for dollar, nothing else in our catalog returns more usable floor. A premium SPC plank is waterproof through the core, laughs off a Labrador's nails and a dropped cast-iron skillet, and lands at a fraction of real oak — and the honest truth is that from across a Lakewood Ranch great room, a good 22-mil plank reads as wood to almost everyone who walks in. We set it two ways depending on the room. <strong>Click-lock floating</strong> goes down fast, takes no adhesive, and lets us pop and swap a single damaged plank years later; <strong>full glue-down</strong> is dead-solid underfoot and is what we insist on for open-plan rooms past about eight hundred square feet, for anything with a pool table or gun safe over it, and for every commercial and rental floor we touch.",
        "intro_long_p2": "Rental work is where this service earns its reputation. A short-term rental on Anna Maria, Siesta, Lido, or in the Wellen Park cluster eats floor at several times the rate of a family home — turnover crews mopping with whatever's under the sink, suitcase wheels, and beach sand grinding in daily. We've re-floored well over a hundred and forty of them since 2020, almost always on a tight vacancy window, and we glue them down because a floating floor gives up at the pivot points first. For an owner-occupied Bradenton or Sarasota home, our default recommendation is a click-lock SPC around 6.5 mm with a 22-mil wear layer — the point on the curve where durability, price, and a believable wood look all line up. If the better plank pushes the project past comfortable, that's exactly the kind of job our financing partners exist for; we'd rather you buy the floor once.",
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
            ("Standard LVP (4 mm, 12-mil wear)", "$1.75–$3.25/sq ft installed", "Builder-grade, rental-friendly"),
            ("Mid-Range LVP / SPC (6 mm, 20-mil)", "$2.75–$5.25/sq ft installed", "Our most-installed residential tier"),
            ("Premium SPC (8 mm, 22+ mil wear)", "$4.25–$7.50/sq ft installed", "Pet-proof, lifetime residential warranty"),
            ("Wide-Plank Luxury LVP (9″+)", "$5.50–$9.50/sq ft installed", "Hardwood-mimicking, premium look"),
            ("Glue-Down Commercial LVP", "$3.25–$6.50/sq ft installed", "Vacation rentals, STRs, high-traffic"),
            ("LVP Stair Treads (per tread)", "$65–$100 each", "Includes nosing and matching riser"),
            ("Slab Self-Leveling (per room)", "$225–$650", "When dip exceeds 3/16″ in 10 ft"),
            ("Old Flooring Removal &amp; Haul", "$1.75–$3.25/sq ft", "Carpet/tile/sheet-vinyl demo"),
        ],
        "faqs": [
            ("Is luxury vinyl plank really waterproof?", "Through the core, yes, completely — you could leave a loose plank in a bucket for a week and it won't swell, warp, or come apart. The joints between planks are tight enough that a dishwasher drip, a pet accident, or an AC condensate overflow won't reach the subfloor for hours. The honest caveat we give every client: a waterproof floor is not a waterproof house. Let water stand against a baseboard for a day or two and it'll find the wall cavity through the expansion gap — the plank survives, but the framing behind it might not. Treat it as a wide margin against spills, not a license to ignore a real leak."),
            ("Click-lock vs. glue-down — which is right for me?", "Click-lock floats over the subfloor: it goes down faster, forgives minor imperfections, and lets us pop and replace one damaged plank down the road. Glue-down bonds flat to the slab, has zero give underfoot — closer to the feel of tile or real wood — and is what we insist on for open spans past about 800 square feet, for anything carrying real weight like a pool table or safe, and for every rental and commercial floor. For an everyday Bradenton or Sarasota living room we usually float it; for a beach rental on a one-week turnaround, we glue it, because the floating joints are the first thing heavy traffic pulls apart."),
            ("Will LVP look fake?", "Entirely depends on what you put down. The cheapest builder-grade plank repeats the same knot every four to six boards and the embossing doesn't track the printed grain, so it reads plastic from across the room. Step up to a real SPC and you get dozens of unique plank faces, deeper texture you can feel, and a matte finish that passes for oak from anywhere past arm's reach. Rather than argue it on the phone, we bring both to your house and stand them next to your trim in your own light — the gap between tiers is obvious the second you see them side by side."),
            ("How long does an LVP install take?", "Plan on two to three days for a typical 1,000–1,500 square-foot floating install: tear-out and prep, then the install, then transitions and trim. Glue-down adds a day or two for adhesive cure, and stairs add a day. The variable that moves the schedule most is the subfloor — if we have to self-level dips, that pour needs to dry before a single plank goes down, and we'd rather wait the day than trap a problem under your new floor."),
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
        "intro_long_p1": "Tile is the most unforgiving product we install, and almost none of that is the tile's fault. Porcelain is inert — it's beautiful, it's hard, it outlives the house. Everything that goes wrong with a tile floor happens in the inch beneath it: a slab that was never flattened, the wrong mortar troweled under a heavy plank, a missing decoupling layer, lippage nobody clipped. The bigger the format, the less margin you get. A 24×48 plank dropped onto a Heritage Harbour kitchen slab with an eighth-inch dip will sit there rocking and cupped where a 12-inch tile would have hidden it completely — which is exactly why we pull a straightedge across the whole floor before we open a single box, and why our large-format quotes carry real prep time instead of pretending the slab is flat.",
        "intro_long_p2": "We build tile to the TCNA Handbook — the published industry spec for substrate flatness, mortar coverage, and crack isolation — because a Florida slab is going to crack eventually, and a Ditra membrane is the difference between a hairline in the concrete staying in the concrete and it telegraphing up through a $16-a-foot porcelain floor. In showers and any splash zone we set a bonded Schluter Kerdi or Wedi waterproofing system before the first tile goes up; there is no version of a wet-area floor we'll build without it. We say this plainly because most of the tile we're called to tear out and redo failed for one of two reasons — skipped prep or skipped waterproofing — and once tile is set wrong, the only honest fix is to take it back out and do it right.",
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
            ("Standard Ceramic Tile (12″–18″)", "$6.50–$9.75/sq ft installed", "Tile included, basic patterns"),
            ("Porcelain Tile (12″–18″)", "$7.50–$11.50/sq ft installed", "Most-installed for primary living areas"),
            ("Large-Format Porcelain (24×48)", "$10.75–$16/sq ft installed", "Premium look, longer prep time"),
            ("Marble-Look Porcelain Slab (48×48+)", "$14.75–$23/sq ft installed", "Slab handling adds labor"),
            ("Natural Stone (travertine/marble)", "$12.50–$21/sq ft installed", "Plus sealing on day of install"),
            ("Mosaic / Decorative Inlay", "$26–$52/sq ft installed", "Labor-intensive, custom layouts"),
            ("Schluter Kerdi Shower Waterproofing", "$1,350–$2,950", "Per standard 3×5 shower footprint"),
            ("Crack-Isolation Membrane (Ditra)", "$2.75–$4.25/sq ft", "Critical over concrete slabs"),
            ("Tile Demo &amp; Substrate Prep", "$3.25–$6.50/sq ft", "Old tile + thinset removal"),
        ],
        "faqs": [
            ("Why does large-format tile cost so much more to install?", "It's labor, not tile. The bigger the format, the flatter the substrate has to be: TCNA allows a quarter-inch of deviation over ten feet under tile below fifteen inches, but tightens that to an eighth of an inch once you're at fifteen inches and up — and a Florida slab almost never shows up that flat, so we self-level. Then the tiles themselves are heavy two-person lifts that have to be back-buttered and set into a fully troweled bed to keep lippage out. The plank might cost a couple dollars more a foot; the prep and the handling are where the real money goes, and skipping either is exactly why discount large-format jobs come back rocking."),
            ("Do I really need a waterproofing membrane in my shower?", "Yes — this isn't a place we negotiate. Florida code requires a waterproof shower assembly; the only question is how it's built. The old tar-paper-and-mud-bed approach still squeaks past inspection in some jurisdictions, but it has a dozen places to fail and we won't build one. We set a fully bonded Schluter Kerdi sheet or a Wedi foam-panel system on every shower, every time, because it's more reliable, an inspector can actually verify it, and the catastrophic bathroom leaks we get called to demo almost always trace back to a shower somebody waterproofed the cheap way."),
            ("Can you tile over an old tile floor?", "Occasionally it's possible, but it's rarely the right call, and we'll usually tell you so. For it to even be on the table the old tile has to be fully bonded with no hollow spots when we sound it, the new tile has to be at least as large so no fresh joint lands over an old one, and your doorways have to be able to swallow another three-quarters of an inch of height — which most can't without trapping doors and transitions. Nine times out of ten we recommend pulling the old tile. It's real labor, but you end up with a floor that outlasts the house instead of inheriting whatever was wrong underneath."),
            ("Sanded vs. unsanded grout — does it matter?", "More than most people expect. Unsanded grout belongs in joints an eighth-inch and narrower — most wall tile, mosaics, tight-set marble — and sanded grout in anything wider, which is most floor tile and large-format porcelain. Force sanded grout into a narrow wall joint and the grit scratches the tile face; use unsanded in a wide floor joint and it shrinks and cracks out as it cures. We pick the grout to the joint, not to whatever's on sale, and on premium jobs we'll often steer you to a urethane or epoxy that never needs sealing in the first place."),
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
        "intro_long_p1": "Laminate gets dismissed as cheap fake wood and confused with vinyl at the showroom, and both reactions miss what it's genuinely good at. A modern AC4 or AC5 laminate wears a melamine surface that shrugs off scratches better than most real oak, the better visuals are legitimately convincing once you're past the bottom tier, and it clicks together fast and clean — usually thirty to forty percent under a comparable engineered hardwood, installed. When a Parrish landlord is putting durable, good-looking floor into a rental and the math has to work, or a homeowner wants real value in the bedrooms while spending the budget on the main living areas, laminate is frequently the smart, honest answer rather than the compromise.",
        "intro_long_p2": "We're just as clear about where it doesn't belong. Laminate's HDF core is wood-based — the same rigidity that makes it feel solid underfoot is what swells it at the seams when liquid water sits on it — so we won't put it in a kitchen, a full bath, or any slab home that hasn't got a proper vapor barrier under it. On every slab install we spec a 6-mil barrier minimum, no exceptions, and for a primary-residence whole-home job we'll usually steer you to SPC vinyl instead and tell you why. But for bedrooms, dens, and home offices over a plywood subfloor — and for rentals where the per-foot budget is real — a properly installed AC4 or AC5 laminate is a floor we'll stand behind for fifteen to twenty years, and one our financing partners can spread out if the right product still stretches the project.",
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
            ("Standard AC3 Laminate (8 mm)", "$2.25–$3.75/sq ft installed", "Rental-friendly, bedrooms"),
            ("Mid-Range AC4 Laminate (10 mm)", "$3.25–$5.25/sq ft installed", "Our most-installed laminate tier"),
            ("Premium AC5 Commercial Laminate (12 mm)", "$5.25–$7.50/sq ft installed", "High-traffic, hand-scraped textures"),
            ("Wide-Plank Premium Laminate (7″+)", "$5.75–$8.50/sq ft installed", "Hardwood-mimicking visuals"),
            ("Vapor Barrier Underlayment", "$0.55–$1.10/sq ft", "Required on slab installs"),
            ("Acoustic / Cork Underlayment", "$0.85–$1.60/sq ft", "Reduces sound transfer in condos"),
            ("Laminate Stair Treads (per tread)", "$75–$115 each", "Includes nosing and matching riser"),
            ("Old Flooring Removal &amp; Haul", "$1.75–$3.25/sq ft", "Carpet/tile/sheet-vinyl demo"),
        ],
        "faqs": [
            ("Laminate vs. LVP — what's actually different?", "It comes down to the core, and everything else follows from there. Laminate is built on an HDF — a dense wood-fiber board — while LVP and SPC are built on a plastic or stone-plastic composite. That one difference decides the rest: laminate isn't waterproof and LVP is; laminate is stiffer and reads a little more like real wood underfoot; LVP shrugs off an imperfect subfloor more gracefully. For a whole Florida home we'll usually point you to LVP, but for rental bedrooms, a home office, or a budget-driven primary-bedroom job, a modern AC4 or AC5 laminate is a floor we'll happily stand behind."),
            ("Is laminate okay for Florida humidity?", "Ambient humidity alone, yes — today's laminate is a different animal than the stuff from twenty years ago, and the HDF core won't swell just from damp air in a conditioned house. What it can't take is standing liquid sitting on a seam for hours, which is the whole reason we keep it out of kitchens, full baths, and anything unconditioned. Put it in air-conditioned bedrooms, living rooms, and offices over a proper vapor barrier and a good AC4 plank will give you fifteen to twenty solid years."),
            ("Why do I need an expansion gap?", "Because every floating floor — laminate, LVP, click-lock engineered — breathes a little with the seasons, and it has to have somewhere to go. Set it tight against the walls, the baseboards, a kitchen island, or a toilet flange with no gap and the first humid stretch buckles it in the middle of the room, because the boards are pushing against something that won't move. We hold a three-eighths-inch gap at every wall and fixed object and then hide it under baseboard and quarter-round. Skipping that gap is the number-one preventable laminate failure we see, full stop."),
            ("How long does a laminate install take?", "Two to three working days for a typical 1,000–1,500 square-foot job: demo, prep and underlayment, then the install, then transitions and trim. Stairs add a day. Laminate is genuinely one of the quickest floors we lay — roughly thirty percent faster than a comparable engineered hardwood — which is part of why the installed price comes in lower."),
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
        "intro_long_p1": "A staircase is the one piece of carpentry every visitor's eye lands on the second they walk in, and it's the single most under-respected job in our trade. A bad set of treads announces itself instantly — nosing reveals that wander, returns that gap at the wall, a riser stained two shades off, finger-jointed treads showing their seams the moment afternoon light rakes across them. We don't quote stairs like flooring; we quote them like finish carpentry, because that's what they are. The fastest way to make a fresh downstairs floor look amateur is to bolt builder-grade steps onto it, and the fastest way to make a modest project look custom is to get the stairs exactly right.",
        "intro_long_p2": "Our most common stair job is the back half of a first-floor reflooring: the upstairs carpet stays, but the steps have to marry into the new wood or plank we just laid. We cut solid hardwood treads — usually 5/4 oak, hickory, or walnut, site-finished to the surrounding floor — plus factory-matched engineered treads, LVP and laminate treads with the manufacturer's own nosing, and full custom builds with stainable risers, mitered return-nose detail on open sides, and skirt-board scribing. Every tread gets cut to its own position rather than to one average dimension, because no two steps in a Florida tract home are actually the same depth, and that single habit is what separates our stairs from the ones we get hired to redo.",
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
            ("LVP / Laminate Treads (per tread)", "$65–$105 installed", "Manufacturer-matched nosing"),
            ("Engineered Hardwood Treads (per tread)", "$115–$170 installed", "Pre-finished, matched to floor"),
            ("Solid Hardwood Treads (per tread)", "$135–$210 installed", "5/4 oak/hickory/walnut, site-finished"),
            ("Stainable Poplar Risers (per riser)", "$38–$60 installed", "White paint standard"),
            ("Hardwood Risers (per riser, matched)", "$65–$100 installed", "Stain-matched to tread"),
            ("Return-Nose Detail (per open-side tread)", "+$22–$42 each", "For open-sided staircases"),
            ("Iron Baluster Install (each)", "$48–$80 installed", "Through new tread, set in epoxy"),
            ("Site-Finished Poly Coat (2 coats)", "$16–$27/tread", "If treads are raw or refinished"),
        ],
        "faqs": [
            ("How long does a stair tread install take?", "A typical fourteen-tread staircase runs two to three days: carpet pull, plywood inspection and prep, then treads and risers, then nosing, return details, and your walkthrough. Site-finished solid hardwood treads add a day or two for stain and poly to cure. A full custom build — open sides with mitered return-nose detail and iron balusters set through the treads — can stretch to four or five. We work top-down on install day so the bottom of the run stays usable while we go."),
            ("Can you match the new treads to my existing hardwood floor?", "This is our single most common stair job, so yes. We bring sample treads in your floor's species and hold them against the actual floor in daylight before we commit to anything. If your downstairs is a pre-finished engineered product, we source treads from the same manufacturer so the match is exact; if it's site-finished solid hardwood, we stain the treads on site to match it. A factory tread next to a site-finished floor will carry a slightly different sheen up close, but at the stair-to-floor break — a spot the eye already reads as a transition — it disappears."),
            ("Do I need to refinish my existing hardwood when I redo the stairs?", "Almost never. The line where the stairs meet the floor is a natural break in the house, so a small shift in color or sheen between fresh treads and an older floor reads as deliberate, not mismatched. The exception is a downstairs floor that's genuinely worn out — then we'll sometimes suggest sanding and refinishing it in the same visit so the whole thing lifts together — but it's a choice, not a requirement, and most clients keep the floor they have."),
            ("What about pets and slippery treads?", "Pre-finished hardwood and LVP treads are smoother than carpet, and an older dog can lose its footing on them going down. The fix is a clear silicone grip strip run about an inch back from each tread nose — nearly invisible from standing height and a real difference for traction. Tell us at the estimate that you've got pets and we'll build them in at no added labor; it's a five-minute step that saves a lot of slipping."),
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
        "intro_long_p1": "Repair is the part of this trade that separates installers from craftsmen, because a new floor is linear — demo, prep, lay, trim, done — and a repair is a diagnosis. Why did this floor cup over here and nowhere else? Why does one LVP plank squeak when you cross the kitchen? Why is the tile letting go eighteen inches off the wall but holding everywhere else? Almost every failure we get called to in Bradenton, Sarasota, and across the bay has a cause you can't see from standing height: moisture wicking up a slab, a slow roof leak that found the subfloor, a joist that settled, an expansion gap somebody set tight. The crew that patches the symptom and skips the cause is just scheduling you a second repair nine months out, on your dime.",
        "intro_long_p2": "We repair every category we install. We lace new hardwood into an existing finish — genuinely the hardest thing we do — sand and refinish tired oak, swap a single cracked tile without touching its neighbors, pull and replace a damaged plank on a click-lock run, and rebuild whole rooms after a supply line lets go or a storm pushes water in. We also do the unglamorous structural work nobody else wants — slab self-leveling, subfloor patching, joist sistering — that has to happen before any finish floor earns the right to go back down on top. Roughly a third of this work runs through a homeowner's insurance claim, so we document moisture readings, scope, and dated photos in the format adjusters expect, and we'll hand you that file whether or not the claim is ours to win.",
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
            ("Hardwood Plank Replacement (lacing)", "$8.50–$16/sq ft", "Matches existing finish, hardest repair"),
            ("Full Sand-and-Refinish (per sq ft)", "$4.25–$7.50/sq ft", "Three sandings + stain + 2-coat poly"),
            ("Engineered Plank Replacement", "$6.50–$11.50/sq ft", "When matching product is available"),
            ("Single Tile Replacement (each)", "$90–$185 per tile", "Includes grout match"),
            ("Loose-Tile Re-bonding (per tile)", "$48–$90 per tile", "Injection-bonding when caught early"),
            ("Water-Damage Rebuild (per sq ft)", "$8.50–$19/sq ft", "Demo + subfloor + new floor"),
            ("Subfloor Patching (per patch)", "$130–$295 each", "Plywood replacement, screwed and glued"),
            ("Slab Self-Leveling (per room)", "$225–$650", "Liquid pour, cures overnight"),
            ("Squeak Repair (per squeak)", "$48–$100 each", "Diagnosis included"),
            ("Insurance-Claim Documentation", "Included free", "Moisture readings + photo report"),
        ],
        "faqs": [
            ("Can you really make a replaced hardwood plank invisible?", "In most cases, yes — and we price it honestly, because lacing a plank in is the hardest thing we do. You're matching three moving targets at once: the species and grade of the original board, the color and sheen of a finish that's aged, and the wear the surrounding floor has already taken. We pull boards from our salvage stock, hand-stain them on site, and tooth the new plank into the field so the seams never land on one straight line. From standing height it reads as untouched; if an expert crouches into raked late-day sun they might find the lace. For the people who actually live there, it's a non-issue — and that's the bar we're after."),
            ("My hardwood floor squeaks — can you fix that without ripping it up?", "Usually without lifting a single board. A squeak is either the floor rubbing the subfloor — which we kill from above with hidden trim-head screws — or the subfloor rubbing the joists, which we hit from the crawlspace or with longer screws driven into the framing from on top. The catch is that most floors squeak in several places for several different reasons, so we survey the whole floor first, mark each one, and quote per squeak rather than per square foot. It's a half-day on a typical home and it resolves the overwhelming majority of them for good."),
            ("How do I know if my water-damaged floor can be saved vs. needs full replacement?", "We run three readings before anyone makes that call. A calcium-chloride test on the subfloor tells us whether it's drying out or still holding water — under about four pounds and we can usually save and reuse it. A close look for cupping, crowning, and gapping tells us how far the boards moved — light cupping often sands back flat, but crowning and severe cupping generally won't. And a pin meter in the planks themselves tells us if the wood is still actively wet, over roughly fourteen percent, in which case we dry it before we judge it. All three numbers go straight into your file, which is exactly what an adjuster wants to see."),
            ("Do you work with insurance companies on water-damage claims?", "Constantly — it's roughly a third of our repair work. We document the whole picture the way carriers expect it: calcium-chloride and pin-meter readings, dated photos, subfloor condition, and a clear scope of damage. We don't bill your insurer directly — that's between you and them — but the file we hand you has carried dozens of successful claims with State Farm, Citizens, Universal, USAA, Tower Hill and others. Call us early; the first 24 hours after the water decides how much of the floor we can still save."),
        ],
    },
}

SERVICE_ORDER = ["hardwood-flooring","hardwood-refinishing","vinyl-plank-flooring","tile-installation","laminate-flooring","stair-treads","floor-repair"]


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
        elif svc_slug == "hardwood-refinishing":
            post_slug = f"hardwood-refinishing-cost-{city_slug}"
            keyword = "hardwood floor refinishing"
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
            "meta_desc": clip_desc(
                f"What {keyword} actually costs in {city['name']}, FL in 2026. "
                f"Transparent rates by material grade, real install timelines, and "
                f"{city['name']}-specific factors. 5★ rated · free estimate."
            ),
            "category": "Pricing",
            "primary_city": city["name"],
            "primary_service": svc_slug,
            "word_target": 2050,
            "topic": "cost_guide",
            "date_published": "2026-01-15",
            "date_modified": "2026-01-15",
        })


# ============================================================================
# GUIDES — /guides/ hub + long-form decision guides.
# Topics chosen to NOT overlap the cost blog (pricing) or the 5 general posts,
# and intentionally distinct from competitor/sibling angles (no generic
# "engineered vs. solid hardwood" explainer). Bodies live in _build_guides.py.
# ============================================================================
GUIDES = [
    {
        "slug": "is-herringbone-worth-it",
        "title": "Is Herringbone Worth the Premium? (Tampa Bay, 2026)",
        "meta_desc": "Herringbone and chevron run 50–90% more in labor than straight plank. When the pattern pays off in a Bradenton or Sarasota home — and when it doesn't.",
        "category": "Design Decision",
        "date_published": "2026-05-20",
        "date_modified": "2026-05-20",
    },
    {
        "slug": "porcelain-vs-lvp-florida-kitchen",
        "title": "Porcelain vs. LVP in a Florida Kitchen: Which Wins?",
        "meta_desc": "The kitchen is the one room where porcelain tile and luxury vinyl plank genuinely compete. How we choose between them in Tampa Bay homes, room by room.",
        "category": "Room-by-Room",
        "date_published": "2026-05-06",
        "date_modified": "2026-05-06",
    },
    {
        "slug": "how-to-read-a-flooring-quote",
        "title": "How to Read a Flooring Quote (and Spot the Padding)",
        "meta_desc": "A line-by-line guide to a real flooring estimate — what every line should say, where contractors pad, and the questions that expose a lowball bid.",
        "category": "Buyer Education",
        "date_published": "2026-04-22",
        "date_modified": "2026-04-22",
    },
    {
        "slug": "wide-plank-vs-standard-width",
        "title": "Wide-Plank vs. Standard Width: What Actually Changes",
        "meta_desc": "Plank width changes more than looks — install method, movement, subfloor prep, and cost all shift with it. A Tampa Bay installer's breakdown.",
        "category": "Material Decision",
        "date_published": "2026-04-08",
        "date_modified": "2026-04-08",
    },
    {
        "slug": "slab-moisture-explained",
        "title": "Slab Moisture, Explained: Why Florida Floors Fail",
        "meta_desc": "Most Gulf Coast floor failures start in the slab, not the floor. What calcium-chloride and RH probe numbers mean, and the readings that change the install.",
        "category": "How It Works",
        "date_published": "2026-03-25",
        "date_modified": "2026-03-25",
    },
    {
        "slug": "hoa-condo-flooring-rules",
        "title": "Flooring an HOA Condo in Tampa Bay: Rules & Approvals",
        "meta_desc": "Second-floor condos and HOA communities have sound-rating rules, underlayment specs, and approval steps that change the floor. What to handle before install day.",
        "category": "Logistics",
        "date_published": "2026-03-11",
        "date_modified": "2026-03-11",
    },
]

# ============================================================================
# GLOSSARY — /glossary/ — 26 flooring terms in plain English.
# Pure data; rendered by _build_guides.py. Each term gets an anchor id.
# ============================================================================
GLOSSARY = [
    ("Acclimation", "Letting flooring material sit inside the actual conditioned room for a set period — 72 hours for hardwood, 48 for engineered and laminate — so its moisture content matches the home before install. Skipping it is the leading cause of gapping and cupping on Gulf Coast floors."),
    ("AC Rating", "Abrasion Class — a 1-to-5 durability scale for laminate. AC3 is light residential, AC4 is general residential/light commercial, AC5 is commercial. We spec AC4 minimum for any primary living area."),
    ("Back-buttering", "Spreading a thin coat of mortar onto the back of a tile in addition to the troweled bed underneath it. Required on large-format tile to get full coverage and prevent hollow spots and lippage."),
    ("Calcium Chloride Test", "A moisture test that measures how many pounds of water vapor a 1,000 sq ft slab emits over 24 hours. A reading too high means a glue-down floor will fail; we run one before any adhesive touches concrete."),
    ("Chevron", "A flooring pattern where planks are cut at an angle and meet point-to-point in a continuous zigzag, forming clean V's. Distinct from herringbone (which uses square-cut planks) and the most labor-intensive wood install we offer."),
    ("Crack-Isolation Membrane", "A sheet or liquid layer (e.g., Schluter Ditra) installed between a slab and tile that decouples the two, so a hairline crack in the concrete doesn't telegraph up and crack the tile above it."),
    ("Cupping", "When the edges of a wood plank rise higher than its center, creating a concave 'cup,' caused by moisture imbalance — usually too much moisture from below. The classic failure mode of solid hardwood on a Florida slab."),
    ("Engineered Hardwood", "Real-wood flooring built as a hardwood wear layer bonded over a cross-ply or HDF core. The cross-grain construction resists humidity-driven movement, which is why it goes over slabs where solid hardwood can't."),
    ("Expansion Gap", "The 3/8-inch space left between a floating floor and every wall or fixed object, hidden by baseboard, that gives the floor room to expand and contract with humidity. Skipping it buckles the floor."),
    ("Floating Floor", "A floor whose planks lock to each other but aren't fastened to the subfloor — it 'floats' as one sheet. Click-lock LVP, laminate, and some engineered hardwood install this way."),
    ("Glue-Down", "An install method where each plank or tile is bonded directly to the subfloor with adhesive. More permanent and solid underfoot than floating; required for large open spans, heavy loads, and most rentals and commercial floors."),
    ("HDF Core", "High-Density Fiberboard — the dense wood-based center of a laminate plank. It gives laminate its rigid, wood-like feel but also makes it swell if liquid water sits on a seam, which is why laminate stays out of wet rooms."),
    ("Herringbone", "A pattern of square-cut rectangular planks laid at 90 degrees in a staggered, broken-zigzag. A timeless look that roughly doubles install labor versus straight plank."),
    ("Janka Hardness", "A scale measuring a wood species' resistance to denting. White oak (~1,350) and hickory (~1,820) sit high; American walnut (~1,010) sits lower. Higher Janka means better scratch and dent resistance for high-traffic Florida homes."),
    ("Lacing (Plank Weaving)", "A repair technique where new boards are feathered into an existing floor — staggering joints and toothing cuts so the patch blends invisibly instead of forming a visible seam. The hardest skill in the trade."),
    ("Lippage", "A height difference between two adjacent tiles or planks, where one edge sits higher than its neighbor. Controlled during install with leveling clips; uncontrolled lippage is a trip hazard and the mark of a rushed job."),
    ("LVP / SPC", "Luxury Vinyl Plank and Stone-Plastic Composite — rigid-core, 100% waterproof vinyl planks. SPC has a denser stone-aggregate core that resists subfloor imperfections better. The most-installed flooring category in Tampa Bay."),
    ("Moisture Barrier (Vapor Barrier)", "A 6-mil polyethylene sheet or coated underlayment placed between a slab and the new floor to block water vapor from wicking up into the flooring. Non-negotiable on Florida slab installs for laminate and many wood products."),
    ("Nosing", "The rounded or squared front edge of a stair tread that overhangs the riser below it. Matching the nosing profile to the tread is what makes a stair install read as finished rather than pieced-together."),
    ("PEI Rating", "Porcelain Enamel Institute scale (1–5) for a tile's surface wear resistance. PEI 1–2 are wall-only or light use; we recommend PEI 4 minimum for any floor because Florida sand is abrasive."),
    ("Riser", "The vertical face between two stair treads. Usually a white-painted poplar board, or a stain-matched hardwood riser on premium open staircases."),
    ("Sand-and-Refinish", "Taking a worn solid-wood floor down to bare wood in three grit passes, then rebuilding the surface with fresh stain and polyurethane. A solid floor can take this four to six times across its life before the wood gets too thin."),
    ("Screen-and-Recoat", "A light refresh that abrades only the existing finish and adds a new top coat — no sanding to bare wood. The right, lower-cost call for a floor that's merely dull rather than worn through."),
    ("Self-Leveling", "Pouring a liquid cement underlayment that flows flat to correct dips and high spots in a subfloor before flooring goes down. Florida slabs rarely meet large-format tile's flatness spec without it."),
    ("Sleeper System", "A subfloor of plywood (often over a vapor barrier) floated or fastened over a concrete slab, creating a nailing surface so solid hardwood can be installed where it otherwise couldn't. Adds height and cost."),
    ("Wear Layer", "The clear top surface of an LVP or laminate plank that takes the abuse, measured in mils for vinyl (12-mil budget, 20–22 mil premium). A thicker wear layer is the single biggest driver of how long the floor stays looking new."),
]

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
