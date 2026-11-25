# Glam by Khushali — Website

Live site: **https://glambykhushali.com**

The website of Glam by Khushali, a studio for luxury makeup, skincare and bridal henna. This README explains how the site is designed and why, and how to update it. It's written for anyone who edits the site, whether a designer, a developer or the owner.

---

## 1. Design goals

| Goal | What it means on the page |
|---|---|
| **Feel premium** | Warm neutral colors, a serif display font, plenty of white space, soft shadows, and few elements per screen. |
| **Make booking easy** | A "Book" button is visible on every page and every screen size. Booking is at most two taps away. |
| **Build trust before price** | Each service page shows what's included, how it works and a gallery before the price summary. |
| **Be clear about prices** | One hourly rate, an estimated total for each service, and payment terms stated plainly. |
| **Design for phones first** | Most visitors arrive from Instagram or WhatsApp on a phone, so every layout starts at 375 px wide. |

---

## 2. Site structure

```
/                         Home: hero, About, service cards, pricing teaser, call to action
├── /services/makeup/     Luxury Makeup Artistry
├── /services/skincare/   Professional Skincare and Facials
├── /services/henna/      Bridal Henna Artistry
├── /pricing/             Services and pricing ($250/hr), booking and payment policy
├── /book/                Book Now: choose "Request a quote" (bridal, events, groups) or "Book online"
│   └── /book/online/     Calendly booking for single appointments
├── /contact/             Call · Text · Email · quote request form
└── /404.html             Branded "page not found"
```

**Navigation**
- **Desktop (900 px and wider):** the logo is centered, with a balanced split navigation. About and Services sit on the left; Pricing, Contact and a filled **Book Now** button sit on the right.
- **Mobile:** a **Menu** button on the left, the logo in the center, and a **Book** button on the right. The menu lists every page, including the three services, so all of them are one tap away.
- **Footer:** About, Services, Pricing and Contact links, a link to each service, and Call / Text / Email buttons.
- The header stays fixed at the top of the screen, with a slightly see-through blurred background, so the main actions are always available.

---

## 3. Key user journeys

1. **"I want to book my bridal look"**: Home → tap a service card → read what's included and the gallery → **Book This Service** → Book Now page → request a quote or book online.
2. **"How much will it cost?"**: Pricing in the header → find the service → see the estimated total and what's included → **Book Your Appointment**.
3. **"I just want to ask a question"**: Contact → Call / Text / Email buttons. On a phone these open the dialer, the messaging app or the mail app.

Every page ends with a dark call-to-action band (Book an Appointment · View Pricing), so no page is a dead end.

---

## 4. Visual design system

### Colors

| Token | Hex | Used for |
|---|---|---|
| `--bg` | `#f7f4f1` | Page background (warm ivory) |
| `--surface` | `#ffffff` | Cards and panels |
| `--ink` | `#262626` | Body text |
| `--ink-soft` | `#5a5552` | Secondary text |
| `--brand` | `#404040` | Headings, primary buttons, call-to-action band |
| `--accent` | `#a98157` | Small labels, links, list bullets (a rose-gold tone that matches the logo) |
| `--accent-soft` | `#efe5da` | Tinted sections and icon circles |
| `--line` | `#e4ddd6` | Borders and dividers |

**Contrast** (checked against the WCAG accessibility guidelines)
- Body text is 13.8:1, secondary text 6.7:1, and buttons 10.4:1. All pass AA.
- The accent color is 3.2:1. That only passes AA for large text, and the site also uses it for small labels and links. See the roadmap.

### Typography
- **Headings:** Playfair Display, an elegant serif that suits the editorial, luxury feel. Sizes scale smoothly with the screen width, from 2.1rem to 3.4rem for page titles.
- **Body:** Roboto, at 17 px with 1.65 line height for easy reading on phones.
- **Small labels** (above headings): uppercase with wide letter spacing, in the accent color.

### Shapes, spacing and motion
- Corner radius 14 px for cards and 999 px (fully rounded) for buttons.
- Content is capped at 1120 px wide. Sections have 72 px of vertical padding, and the side margin is 20 px.
- Cards lift 4 px with a deeper shadow on hover, which signals they can be clicked. All animations last 0.2–0.25 s.

### Components
Header · Hero (photo with dark overlay) · Service card · Checklist · Four-step "How it works" · Gallery grid · Price card · Policy panel · Contact card · Calendly box · Call-to-action band · Footer.
All styles are in `assets/site.css`, and the menu and form behavior is in `assets/site.js`.

---

## 5. Content and UX decisions

- **Photos match their services.** The henna section shows mehndi, skincare shows a facial, and makeup shows an artist at work. The current photos are free stock images from Unsplash, used as placeholders. Replacing them with Khushali's own work is the most valuable next step.
- **The phone number is shown on the Contact page and in the footer,** and also powers the Call and Text buttons.
- **Pricing uses one rate:** $250/hr, with estimated totals worked out from typical appointment lengths. This avoids a confusing menu of packages.
- **Booking:** the Calendly calendar is embedded on the Book Online page (`/book/online/`). Its height is 1120 px on phones so the whole calendar and the time list fit without scrolling inside the frame, and 760 px on desktop.
- **Service pages** follow a set order that answers visitor questions one at a time: experience → what's included → who it's for → how it works → gallery → price → other services.

---

## 6. Accessibility

- Semantic structure: `header`, `nav` with labels, `main`, `footer`, one `h1` per page, and headings in order.
- The mobile menu button reports whether the menu is open (`aria-expanded`), and the current page is marked (`aria-current="page"`).
- All content images have descriptive alt text. Icons are hidden from screen readers.
- Form fields have visible labels and suggest saved details (`autocomplete`), and the focus outline is in the accent color.
- No layout scrolls sideways at any width (checked at 375, 800 and 1280 px).

---

## 7. How to edit the site

The pages are generated from one Python script, so the header, footer and styling stay consistent everywhere.

```bash
python3 tools/build.py      # regenerates all pages from the content in the script
```

| To change… | Edit in `tools/build.py` |
|---|---|
| Service text, what's included, gallery photos | the `SERVICES` list |
| Prices, hours, inclusions | `RATE` and the `PRICING` table |
| Calendly link | `CALENDLY_URL` |
| Email or phone | `EMAIL`, `PHONE_E164`, `PHONE_DISPLAY` |
| Hero or About photo | `HERO`, `ABOUT` (Unsplash photo IDs) |

Styling lives in `assets/site.css`. Change the color tokens in `:root` to re-theme the whole site.

**To publish:** commit and push to `main`. GitHub Pages serves the repository root at glambykhushali.com, with HTTPS enforced. Changes appear within about a minute; GitHub caches pages for up to 10 minutes.

```bash
git add -A
git commit -m "Describe the change"
git push
```

Preview locally before publishing:

```bash
python3 -m http.server 8765
```

Then open http://localhost:8765 in a browser.

---

## 8. Roadmap

- [ ] Replace the stock photos with Khushali's own makeup, skincare and mehndi work (highest impact on trust).
- [ ] Darken the accent color for small text (to about `#8a6640`) so it passes WCAG AA contrast.
- [ ] Rename the Calendly event from "30 Minute Meeting" to something like "Glam Consultation".
- [ ] Add testimonials and an Instagram link or feed.
- [ ] Move the contact form off the old site builder's server before cancelling that plan.
- [ ] Add structured data (LocalBusiness and Service) to improve how the site appears in search results.

---

© 2026 Glam by Khushali. All rights reserved.
