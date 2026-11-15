# GR Commerce Suite site — "One order, start to finish" design

Date: 2026-11-15 · Owner pick: direction B (Fable brainstorm) · Status: draft for owner approval

## Intent
The current site reads "casual and basic": every section is the same glass card with text and nothing shows the product. The page's one job is to get Greek shop owners (and the agencies that build their stores) to start the 30-day trial. It should feel professional and show the real plugin, while keeping the liquid-glass look the owner likes.

## Goals
- Explain the plugin by following one example order (#1047) through five real stages: checkout → voucher → delivery → COD money back → «Συμφωνημένο».
- Show a real plugin screen at each stage, built from the plugin's own admin labels (EN and the `el` catalog), with synthetic data marked "Example" / «Παράδειγμα».
- Make the COD "money back" stage the largest section: it is what competitors do not show.
- Professional tone in both languages; no idioms or slang.
- EN (`index.html`) and EL (`el.html`) from one template.

## Non-goals
- No new pages (terms, privacy, refund) until the owner provides them; no links to pages that do not exist.
- No backend, checkout or forms.
- No Klarna (owner 2026-11-15: in the code but switched off, because Klarna's own plugin is free) and no BestPrice feed claims.

## Anti-goals (fails even if it "works")
- Oversized, "in your face" layout like digiqal (headline ≈44px desktop max).
- Invented numbers, testimonials, customer logos or competitor prices we cannot source.
- Generic template tells: label above every section, mono for small labels, middle-dot meta strings, single accented word in the headline, identical cards everywhere.

## Constraints
- Liquid glass kept: frosted panels over faint colour blobs; pills only for the top bar, main button and EN/ΕΛ switch; panel radius 12px.
- Top bar (64px): wordmark only, no logo mark; links visible from 820px; EN/ΕΛ pill with a light/dark pill stacked below it at every width; ☰ below 820px. Theme follows the system until the visitor picks one, then remembers it.
- Fonts must include Greek: Commissioner (one family, headings + body) from Google Fonts.
- Light and dark themes. No horizontal scroll at 375px.
- Owner terms kept exactly: €89/year one site, 30-day free trial, 14-day money-back, support email.

## Approaches considered
- **A. Control desk** — two-column hero with product screens, tabbed showcase. Safe, quick, closest to a standard SaaS page.
- **B. One order, start to finish (picked)** — the page is a journey of one order; each stage is a section with its screen. Most distinctive, tells the COD money story; more to build.
- **C. Switchboard** — hero is the «Ενότητες» screen with switches. Shows breadth but resembles mywooaio and leads with a list.

## Design
Palette: page #F3F6FB, text #0E1626, blue #1F4FD8, glow #BFD2FF, ok #157347, pending #9A5B00 (dark theme derived from the same roles).

Page outline:
1. **Top bar + hero.** Two-line headline, one main button ("Start the 30-day free trial"), secondary link "Follow an order". From 960px the rail sits to the right of the text as a vertical list; below that, one glass rail with five numbered stops for order #1047 (Checkout · Voucher 9900000522 · Delivery BOX NOW · Remittance €89.00 · Reconciled ✓). On phones the rail becomes a vertical list.
2. **Stop 1 Checkout.** Screen: «Τύπος παραστατικού» Receipt/Invoice, ΑΦΜ filled from AADE (neutral status wording, not an invented label), BOX NOW locker choice. Note: Classic and Blocks.
3. **Stop 2 Voucher.** Screen: order list with bulk actions "GRCS: Issue Courier Vouchers (Bulk)" / "GRCS: Print Merged PDF Vouchers". Up to 100 labels per PDF, A4/A6/thermal.
4. **Stop 3 Delivery.** Screen: tracking status timeline, shipped email, courier pickup manifest PDF.
5. **Stop 4–5 Money back → Reconciled (largest).** Screen: «Συμφωνία αντικαταβολών» with the four real totals and the table; buttons "Record COD settlement" / "Accept difference and reconcile". Short explanation of the CSV import.
6. **Selling elsewhere.** Skroutz XML feed panel (last generated, products, excluded offers, "Copy Feed URL"), plus Smart Cart, Analytics, Google/Meta feed.
7. **Modules.** Switch list of the 11 real integrations; Geniki, Speedex, installments "in development". Built-in tools as a mixed-size tile grid (COD blacklist, Customer 360, shipping rates, packing slips + manifest, GDPR tools, courier sandbox).
8. **Release check.** One panel styled like a diagnostics screen: 2,755 automated tests, ~946 tests on real WooCommerce, PHPStan 0 errors, WP 7.1 / WC 11.3, single site + multisite, HPOS.
9. **Price.** €89/year one site, three trial steps, 14-day money-back.
10. **FAQ + footer.** Eight questions (incl. HPOS and large catalogues); non-affiliation notice; support email shown as text.

Comparison: "separate plugins vs one plugin" in prose inside the Modules section; no competitor price figures.

## Decided by the owner
- Direction B; liquid glass kept; EN/ΕΛ switch; links in the top bar; professional Greek.

## Builder's calls (owner may override)
- Trial buttons (top bar, phone menu, hero, price card) go to the Lemon Squeezy checkout https://gr-commerce-suite.lemonsqueezy.com/checkout (owner 2026-11-15); support email stays as text and a footer link.
- Gmail support address kept until a domain address is given (question 2 open).
- No competitor price numbers (question 3 open).
- Drawn screens, not screenshots (question 4 open).
- Build: `src/template.html` + `src/strings.en.json` + `src/strings.el.json`, `python -I src/build.py`; build fails on missing or unused keys.
- Greek mock labels come from `wise-galileo/languages/gr-commerce-suite-el.po`; any label not in the catalog uses neutral wording.
