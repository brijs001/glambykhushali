"""Generate the static pages for glambykhushali.com.

Run from the repo root:  python3 tools/build.py
Edit the content below, re-run, commit and push. GitHub Pages serves the output.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent

# --- Settings ---------------------------------------------------------------
SITE = "Glam by Khushali"
DOMAIN = "https://glambykhushali.com"
EMAIL = "contact@glambykhushali.com"
PHONE_E164 = "+17327075613"  # used in call/text links
PHONE_DISPLAY = "(732) 707-5613"  # shown as text on the Contact page and footer
RATE = 250
# Paste the Calendly scheduling link here (e.g. "https://calendly.com/<name>/consultation").
# While empty, the Contact page shows call/text/email booking instead of the calendar.
CALENDLY_URL = "https://calendly.com/khushalisoni90/30min"
CONTACT_ENDPOINT = ("https://builder-api.corporatetools.com/public/websites/"
                    "9048f01f-244c-4d34-af2e-d03e6a4a56a2/contact")


def img(photo_id, w=1200):
    return f"https://images.unsplash.com/photo-{photo_id}?auto=format&fit=crop&w={w}&q=80"


# Stock photos (Unsplash) — replace with Khushali's own work when available.
HERO = "1684868268327-7e5590bcfbd6"      # bride in red and gold
ABOUT = "1636023730877-233b9237d4ec"     # artist doing a client's makeup

ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    "text": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
}

# --- Services ---------------------------------------------------------------
SERVICES = [
    {
        "slug": "makeup",
        "name": "Luxury Makeup Artistry",
        "short": "Luxury Makeup",
        "card_img": "1773688189414-7637b9b138e1",
        "card_alt": "Makeup artist applying blush to a client",
        "summary": "Personalized luxury makeup for weddings, parties, and special occasions, from timeless bridal looks to occasion-ready glam that enhances your natural features.",
        "intro": [
            "Every look begins with you: your features, your skin, your outfit and the feeling you want to carry through the day. Khushali designs makeup that photographs beautifully, lasts from the first look to the last dance, and still looks like the best version of you.",
            "From soft, luminous bridal glam to bold reception looks, each application uses professional, long-wear products chosen for your skin type and tone.",
        ],
        "includes": [
            "One-on-one consultation on your look, outfit, jewelry and theme",
            "Skin prep with hydrating, skin-type-matched primers",
            "Long-wear, HD-finish makeup built to photograph flawlessly",
            "Premium lashes, customized to your eye shape",
            "Dupatta, veil and jewelry setting for bridal looks",
            "Touch-up guidance so your look stays fresh all day",
        ],
        "ideal": "Brides, bridal parties, engagements, sangeet and reception, galas, photoshoots and milestone celebrations.",
        "gallery": [
            ("1610173827043-9db50e0d8ef9", "Bride in red with gold jewelry and finished bridal makeup"),
            ("1600685890506-593fdf55949b", "Traditional bridal look with ornate gold jewelry"),
            ("1487412947147-5cebf100ffc2", "Close-up of lipstick being applied"),
        ],
    },
    {
        "slug": "skincare",
        "name": "Professional Skincare and Facials",
        "short": "Skincare & Facials",
        "card_img": "1570172619644-dfd03ed5d881",
        "card_alt": "Client receiving a facial treatment",
        "summary": "Professional skincare treatments and facials tailored to your skin type, designed to refresh, rejuvenate, and prepare your complexion for your special day.",
        "intro": [
            "Beautiful makeup starts with healthy skin. Each facial is tailored after a skin analysis, so your treatment targets exactly what your complexion needs: hydration, clarity, brightness or calm.",
            "For brides, a planned skin-prep series in the weeks before the wedding gives you a smooth, radiant canvas on the day itself.",
        ],
        "includes": [
            "Skin analysis and treatment plan for your skin type",
            "Deep double cleanse and gentle exfoliation",
            "Extractions where needed",
            "Targeted mask: hydrating, brightening or soothing",
            "Relaxing face, neck and shoulder massage",
            "Personalized home-care advice to maintain your glow",
        ],
        "ideal": "Brides preparing for the big day, pre-event glow, and anyone who wants refreshed, healthy-looking skin.",
        "gallery": [
            ("1552693673-1bf958298935", "Client relaxing during a professional facial"),
            ("1616394584738-fc6e612e71b9", "Facial mask treatment"),
            ("1761718209835-c8586b7dcac0", "Brush applying a facial treatment cream"),
        ],
    },
    {
        "slug": "henna",
        "name": "Bridal Henna Artistry",
        "short": "Bridal Henna",
        "card_img": "1525135850648-b42365991054",
        "card_alt": "Close-up of intricate mehndi on a hand",
        "summary": "Beautiful, intricate henna designs for weddings and celebrations, crafted to complement your bridal look and add a touch of tradition and elegance.",
        "intro": [
            "Bridal mehndi is one of the most personal parts of your wedding. Khushali creates intricate, hand-drawn designs that reflect your style, from traditional paisleys and florals to modern, minimal patterns, with the details that make them yours.",
            "Fresh, hand-mixed henna paste and careful aftercare guidance help you achieve a deep, rich stain for your celebrations.",
        ],
        "includes": [
            "Design consultation to match your outfit, theme and traditions",
            "Fresh, hand-mixed henna paste",
            "Intricate, custom bridal designs for hands, arms and feet",
            "Personal touches such as hidden initials or your partner's name",
            "Sealant and aftercare instructions for a deep, lasting stain",
        ],
        "ideal": "Brides, mehndi nights, bridal parties and guests, Karva Chauth, Eid, Diwali, Teej and other celebrations.",
        "gallery": [
            ("1771992230380-bc023f41771e", "Hand with intricate bridal henna and a ring"),
            ("1732118400647-a81e3b37be87", "Hands decorated with detailed henna"),
            ("1674884060571-96a46a9a7a72", "Hand with fine floral henna design"),
        ],
    },
]

# --- Pricing (all at the standard hourly rate) -----------------------------
PRICING = {
    "makeup": [
        ("Bridal Makeup — Wedding Day", 3, None,
         ["Pre-wedding consultation", "Skin prep and long-wear HD-finish makeup",
          "Premium lashes", "Dupatta, veil and jewelry setting", "Lip color to keep for touch-ups"]),
        ("Bridal Makeup Trial", 2, None,
         ["Look planning with your outfit, jewelry and theme", "Full trial application",
          "Adjustments until it feels perfect", "Reference photos of your final look"]),
        ("Pre-Wedding Event Glam", 2, None,
         ["For engagement, sangeet, mehndi or reception", "Skin prep and full glam",
          "Lashes included", "Jewelry and dupatta setting"]),
        ("Occasion Glam", 1.5, None,
         ["Parties, galas, photoshoots and milestones", "Skin prep and full makeup",
          "Lashes included", "Soft glam to bold evening looks"]),
        ("Bridal Party & Family Makeup", 1, "per person",
         ["Polished, coordinated looks for your group", "Skin prep and full makeup",
          "Lashes included", "Scheduled around the bride's timeline"]),
    ],
    "skincare": [
        ("Signature Glow Facial", 1, None,
         ["Skin analysis", "Double cleanse and exfoliation", "Extractions where needed",
          "Targeted mask and massage", "Home-care advice"]),
        ("Bridal Skin Prep Series", 4.5, "3 sessions × 1.5 hrs",
         ["Three facials spaced over the 8–12 weeks before your wedding",
          "Treatment plan adjusted at every session", "Timed so skin is at its best on the day",
          "Home-care routine between sessions"]),
        ("Facial + Event Makeup", 2.5, None,
         ["Hydrating prep facial", "Full occasion makeup on freshly prepped skin",
          "Lashes included", "Ideal on the day of your event"]),
    ],
    "henna": [
        ("Bridal Mehndi — Hands & Feet", (5, 6), None,
         ["Design consultation", "Intricate custom designs to the elbows",
          "Matching feet designs", "Hidden initials or name", "Sealant and aftercare guide"]),
        ("Bridal Mehndi — Hands Only", (3, 4), None,
         ["Design consultation", "Detailed bridal designs on both hands and arms",
          "Hidden initials or name", "Sealant and aftercare guide"]),
        ("Festive & Engagement Mehndi", 1, "per person",
         ["Both hands, elegant medium-detail designs", "For engagements, Karva Chauth, Eid, Diwali and Teej",
          "Aftercare guide"]),
        ("Guest Henna at Your Event", 2, "minimum, per hour after",
         ["Quick, elegant designs for your guests", "Typically 6–10 guests per hour",
          "Ideal for mehndi nights and celebrations"]),
    ],
}


def money(x):
    return f"${x:,.0f}"


def hours_text(h):
    if isinstance(h, tuple):
        return f"{fmt_h(h[0])}–{fmt_h(h[1])} hrs"
    return f"{fmt_h(h)} hr" + ("" if h == 1 else "s")


def fmt_h(h):
    return f"{h:g}"


def estimate(h):
    if isinstance(h, tuple):
        return f"{money(h[0] * RATE)}–{money(h[1] * RATE)}"
    return money(h * RATE)


# --- Layout -----------------------------------------------------------------
def header(current):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    sub = "".join(f'<a href="/services/{x["slug"]}/">{x["short"]}</a>' for x in SERVICES)
    mobile_sub = "".join(f'<a class="sub" href="/services/{x["slug"]}/">{x["short"]}</a>' for x in SERVICES)
    return f"""<header class="brand-bar">
  <a class="book-mobile" href="/contact/#book">Book</a>
  <a class="logo" href="/" aria-label="{SITE} home"><img src="/assets/logo.svg" alt="{SITE}" width="470" height="266"></a>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menu">{ICON['menu']}</button>
</header>
<nav class="main-nav" aria-label="Primary">
  {a('/', 'Home', 'home')}
  {a('/#about', 'About', 'about')}
  <div class="has-sub">{a('/#services', 'Services', 'services')}<span class="caret" aria-hidden="true"></span>
    <div class="submenu">{sub}</div>
  </div>
  {a('/pricing/', 'Pricing', 'pricing')}
  {a('/contact/', 'Contact', 'contact')}
  <a class="nav-book" href="/contact/#book">Book Now</a>
</nav>
<div class="menu-overlay"></div>
<nav id="mobile-menu" class="mobile-menu" aria-label="Mobile">
  <button class="menu-close" type="button" aria-label="Close menu">&times;</button>
  <a href="/">Home</a>
  <a href="/#about">About</a>
  <a href="/#services">Services</a>
  {mobile_sub}
  <a href="/pricing/">Pricing</a>
  <a href="/contact/">Contact</a>
  <a class="nav-book" href="/contact/#book">Book Now</a>
</nav>"""


def footer():
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <h3>{SITE}</h3>
      <p class="note">Luxury makeup, professional skincare and bridal henna artistry for weddings and special occasions.</p>
      <p class="note"><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <div class="footer-actions">
        <a class="btn btn--ghost" href="tel:{PHONE_E164}">{ICON['phone']}Call</a>
        <a class="btn btn--ghost" href="sms:{PHONE_E164}">{ICON['text']}Text</a>
        <a class="btn btn--ghost" href="mailto:{EMAIL}">{ICON['mail']}Email</a>
      </div>
    </div>
    <div>
      <h3>Explore</h3>
      <ul class="footer-links">
        <li><a href="/#about">About</a></li>
        <li><a href="/#services">Services</a></li>
        <li><a href="/pricing/">Pricing</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div>
      <h3>Services</h3>
      <ul class="footer-links">
        {''.join(f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)}
      </ul>
    </div>
  </div>
  <p class="copyright">© 2026 {SITE}. All rights reserved.</p>
</footer>"""


def page(path, title, description, current, body, extra_head=""):
    full_title = f"{title} | {SITE}" if title != SITE else f"{SITE} | Luxury Makeup, Skincare and Henna Artistry"
    canonical = DOMAIN + "/" + path.replace("index.html", "")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:image" content="{img(HERO, 1200)}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Roboto:wght@300;400;500&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{extra_head}</head>
<body>
{header(current)}
<main>
{body}
</main>
{footer()}
<script src="/assets/site.js" defer></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", path)


def cta_band(title="Ready to book your glam?", text="Call, text or email, or pick a time online."):
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="actions">
      <a class="btn btn--light" href="/contact/#book">Book an Appointment</a>
      <a class="btn btn--ghost" style="color:#fff;border-color:#fff" href="/pricing/">View Pricing</a>
    </div>
  </div>
</section>"""


# --- Pages ------------------------------------------------------------------
def build_home():
    cards = "".join(f"""
      <a class="card" href="/services/{s['slug']}/">
        <img src="{img(s['card_img'], 800)}" alt="{s['card_alt']}" loading="lazy" width="800" height="600">
        <div class="card-body">
          <h3>{s['name']}</h3>
          <p>{s['summary']}</p>
          <span class="card-link">View service &amp; details →</span>
        </div>
      </a>""" for s in SERVICES)
    body = f"""<section class="hero" style="background-image:url('{img(HERO, 1800)}')">
  <div class="wrap">
    <p class="eyebrow" style="color:#f1dcc4">Luxury Makeup · Skincare · Henna</p>
    <h1>{SITE}</h1>
    <p>Your Expert Beauty &amp; Makeup Artist</p>
    <div class="actions">
      <a class="btn btn--light" href="/contact/#book">Book an Appointment</a>
      <a class="btn btn--ghost" style="color:#fff;border-color:#fff" href="#services">Explore Our Services</a>
    </div>
  </div>
</section>

<section id="about" class="section">
  <div class="wrap split">
    <img src="{img(ABOUT, 1000)}" alt="Khushali applying makeup to a client" loading="lazy" width="1000" height="750">
    <div>
      <p class="eyebrow">About</p>
      <h2>About {SITE}</h2>
      <p>{SITE} is a beauty studio dedicated to personalized luxury makeup, professional skincare, and beautiful henna artistry. Every service is tailored to enhance your natural features, so you leave feeling confident, radiant, and completely yourself.</p>
      <p>From timeless bridal looks to occasion-ready glam, each appointment begins with understanding your style, skin, and vision. Whether you are preparing for your wedding day or a special event, {SITE} brings careful attention, artistry, and a polished finish to every detail.</p>
      <a class="btn btn--ghost" href="/contact/">Get in Touch</a>
    </div>
  </div>
</section>

<section id="services" class="section section--tint">
  <div class="wrap center">
    <p class="eyebrow">Services</p>
    <h2>Our Services</h2>
    <p class="lead">Tap a service to see what's included, how it works and examples of the work.</p>
    <div class="cards" style="text-align:left">{cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap center">
    <p class="eyebrow">Simple, transparent pricing</p>
    <h2>One standard rate: {money(RATE)} per hour</h2>
    <a class="btn" href="/pricing/">See Services &amp; Pricing</a>
  </div>
</section>

{cta_band()}"""
    page("index.html", SITE,
         "Glam by Khushali offers personalized luxury makeup, professional skincare and facials, and henna artistry for weddings and special events. Book your bridal or occasion-ready glam today.",
         "home", body)


def build_service(s):
    includes = "".join(f"<li>{i}</li>" for i in s["includes"])
    gallery = "".join(f'<img src="{img(pid, 700)}" alt="{alt}" loading="lazy" width="700" height="700">'
                      for pid, alt in [(s["card_img"], s["card_alt"])] + s["gallery"])
    rows = PRICING[s["slug"]]
    price_lines = "".join(
        f"<li><strong>{n}</strong> — {hours_text(h)}{(' ' + q) if q else ''}, est. {estimate(h)}</li>"
        for n, h, q, _ in rows)
    others = "".join(f'<a class="btn btn--ghost" href="/services/{o["slug"]}/">{o["short"]}</a> '
                     for o in SERVICES if o is not s)
    body = f"""<section class="hero page-hero" style="background-image:url('{img(s['card_img'], 1800)}')">
  <div class="wrap">
    <p class="eyebrow" style="color:#f1dcc4">Services</p>
    <h1>{s['name']}</h1>
    <p>{s['summary']}</p>
    <div class="actions"><a class="btn btn--light" href="/contact/#book">Book This Service</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <h2>The experience</h2>
      {''.join(f'<p>{p}</p>' for p in s['intro'])}
      <p><strong>Perfect for:</strong> {s['ideal']}</p>
    </div>
    <div>
      <h2>What's included</h2>
      <ul class="checklist">{includes}</ul>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <h2 class="center">How it works</h2>
    <div class="steps">
      <div class="step"><h3>Book</h3><p>Pick a time online, or call, text or email to check your date.</p></div>
      <div class="step"><h3>Consult</h3><p>We plan your look around your skin, style, outfit and occasion.</p></div>
      <div class="step"><h3>Glow</h3><p>Relax and enjoy your service.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="center">Gallery</h2>
    <div class="gallery">{gallery}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <h2>Pricing at a glance</h2>
    <p>All services are billed at our standard rate of <strong>{money(RATE)}/hour</strong>.</p>
    <ul class="checklist">{price_lines}</ul>
    <a class="btn" href="/pricing/#{s['slug']}">Full pricing details</a>
  </div>
</section>

<section class="section center">
  <div class="wrap">
    <h2>Explore other services</h2>
    <p>{others}</p>
  </div>
</section>

{cta_band()}"""
    page(f"services/{s['slug']}/index.html", s["name"], s["summary"], "services", body)


def build_pricing():
    groups = ""
    for s in SERVICES:
        items = ""
        for name, h, qual, inc in PRICING[s["slug"]]:
            q = f" ({qual})" if qual else ""
            items += f"""
        <div class="price-item">
          <div class="price-head"><h3>{name}</h3><span class="price-est">est. {estimate(h)}</span></div>
          <div class="price-time">Approx. {hours_text(h)}{q} at {money(RATE)}/hr</div>
          <ul class="checklist">{''.join(f'<li>{i}</li>' for i in inc)}</ul>
        </div>"""
        groups += f"""
    <div class="price-group" id="{s['slug']}">
      <h2>{s['name']}</h2>
      <div class="price-list">{items}
      </div>
      <p style="margin-top:18px"><a href="/services/{s['slug']}/">More about {s['short']} →</a></p>
    </div>"""
    body = f"""<section class="section section--tint center">
  <div class="wrap">
    <p class="eyebrow">Pricing</p>
    <h1>Services &amp; Pricing</h1>
    <div class="rate-badge">{money(RATE)} per hour</div>
    <p class="lead">One standard rate for every service. Estimates below show typical appointment times; your exact time is confirmed when you book.</p>
  </div>
</section>

<section class="section" style="padding-top:8px">
  <div class="wrap">{groups}

    <div class="policy" id="policy">
      <h2>Booking &amp; payment</h2>
      <ul class="checklist">
        <li>All services are billed at {money(RATE)} per hour for the time booked.</li>
        <li>Times shown are estimates; group and multi-event bookings are scheduled together with you.</li>
      </ul>
      <a class="btn" href="/contact/#book">Book Your Appointment</a>
    </div>
  </div>
</section>

{cta_band()}"""
    page("pricing/index.html", "Pricing",
         f"Glam by Khushali pricing: one standard rate of {money(RATE)}/hour for luxury makeup, skincare and bridal henna.",
         "pricing", body)


def build_contact():
    if CALENDLY_URL:
        booking = f"""<div class="calendly-box">
        <div class="calendly-inline-widget" data-url="{CALENDLY_URL}?hide_gdpr_banner=1"></div>
      </div>"""
        extra = '<script src="https://assets.calendly.com/assets/external/widget.js" async></script>\n'
    else:
        booking = f"""<div class="calendly-box booking-fallback">
        <p>Online booking is coming soon. To reserve your date now, call, text or email and we'll confirm availability.</p>
        <a class="btn" href="sms:{PHONE_E164}">{ICON['text']}Text to Book</a>
      </div>"""
        extra = ""
    body = f"""<section class="section section--tint center">
  <div class="wrap">
    <p class="eyebrow">Contact &amp; Booking</p>
    <h1>Book Your Glam</h1>
    <p class="lead">Call, text or email to ask a question or check a date, or choose a time online below.</p>
    <div class="contact-options">
      <div class="contact-card">
        <div class="icon">{ICON['phone']}</div>
        <h3>Call</h3>
        <p>Speak with Khushali directly.<br><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></p>
        <a class="btn" href="tel:{PHONE_E164}">Call Now</a>
      </div>
      <div class="contact-card">
        <div class="icon">{ICON['text']}</div>
        <h3>Text</h3>
        <p>Send your date, service and location.<br><a href="sms:{PHONE_E164}">{PHONE_DISPLAY}</a></p>
        <a class="btn" href="sms:{PHONE_E164}">Send a Text</a>
      </div>
      <div class="contact-card">
        <div class="icon">{ICON['mail']}</div>
        <h3>Email</h3>
        <p>{EMAIL}</p>
        <a class="btn" href="mailto:{EMAIL}">Send an Email</a>
      </div>
    </div>
  </div>
</section>

<section id="book" class="section">
  <div class="wrap">
    <div class="center">
      <p class="eyebrow">Online booking</p>
      <h2>Choose a time</h2>
      <p class="lead">Pick a day and time that works for you. <a href="/pricing/">See pricing</a>.</p>
    </div>
    {booking}
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="center">
      <h2>Send a message</h2>
      <p class="lead">Prefer to write? Leave your details and we'll get back to you.</p>
    </div>
    <form id="contact-form-el" class="form" data-endpoint="{CONTACT_ENDPOINT}">
      <div id="contact-fields" class="fields">
        <div><label for="contact-name">Name</label><input id="contact-name" name="name" type="text" autocomplete="name" required></div>
        <div><label for="contact-email">Email</label><input id="contact-email" name="email" type="email" autocomplete="email" required></div>
        <div><label for="contact-message">Message (date, service, location)</label><textarea id="contact-message" name="message" rows="5" required></textarea></div>
        <div><button id="contact-submit" class="btn" type="submit">Send Message</button></div>
      </div>
      <p id="contact-success" class="hidden center">Thank you, your message has been sent.</p>
      <p id="contact-failure" class="hidden center" role="alert">Sorry, your message could not be sent. Please call, text or email instead.</p>
    </form>
  </div>
</section>"""
    page("contact/index.html", "Contact & Booking",
         "Book Glam by Khushali: call, text or email, or choose a time online.",
         "contact", body, extra)


def build_404():
    body = """<section class="section center">
  <div class="wrap">
    <p class="eyebrow">404</p>
    <h1>This page does not exist</h1>
    <p class="lead">The page you were looking for isn't here.</p>
    <a class="btn" href="/">Back to the homepage</a>
  </div>
</section>"""
    page("404.html", "Page not found", "Page not found.", "", body)


if __name__ == "__main__":
    build_home()
    for s in SERVICES:
        build_service(s)
    build_pricing()
    build_contact()
    build_404()
