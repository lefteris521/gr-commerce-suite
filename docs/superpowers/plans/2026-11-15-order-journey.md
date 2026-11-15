# Order Journey Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the GR Commerce Suite marketing site (EN + EL) as the "one order, start to finish" liquid-glass page.

**Architecture:** One `src/template.html` with `{{key}}` slots, two string tables (`src/strings.en.json`, `src/strings.el.json`), and `src/build.py` that writes `index.html` and `el.html` and fails on missing or unused keys. Static HTML/CSS, a few lines of vanilla JS (mobile menu only).

**Tech Stack:** HTML, CSS, vanilla JS, Python 3 (build), Google Fonts (Commissioner).

**Spec:** `docs/superpowers/specs/2026-11-15-order-journey-design.md`

## Global Constraints

- Liquid glass kept; pills only for top bar, main button and EN/ΕΛ switch; panel radius 12px.
- Headline ≤ 44px on desktop; no oversized hero.
- Palette: page #F3F6FB, text #0E1626, blue #1F4FD8, glow #BFD2FF, ok #157347, pending #9A5B00; dark theme from the same roles.
- Font: Commissioner (Greek subset) for headings and body.
- Top bar: links visible from 720px, EN/ΕΛ at every width, ☰ only below 720px.
- No horizontal scroll at 375px; light and dark themes.
- Owner terms exact: €89/year one site, 30-day free trial, 14-day money-back, support email `lethshiningstar@gmail.com` shown as text.
- No Klarna, no BestPrice feed, no competitor prices, no invented stats or testimonials.
- Avoid template tells: no label above every section, no mono small labels, no middle-dot meta strings, no single accented headline word.
- Greek mock labels from `wise-galileo/languages/gr-commerce-suite-el.po`; neutral wording where the catalog has none.

## Review Focus

- Long Greek strings in the journey rail and screen mocks: must wrap inside their panel, never push the page wider at 375px.
- Mobile menu: opens, closes on link tap, never covers the EN/ΕΛ switch.
- Dark theme: every mock pill and table stays readable (no light-only literal colours).
- Greek glyphs: headings render in Commissioner, not a fallback (check `document.fonts`).
- Build: a key present in one language but not the other fails the build.

---

### Task 1: Template for the order journey

**Files:**
- Modify: `src/template.html` (full rewrite)
- Keep: `src/build.py`

**Interfaces:**
- Produces: the full set of `{{key}}` names Tasks 2–3 must define (build lists them on failure).

- [ ] **Step 1:** Rewrite `src/template.html`: top bar; hero with headline, lead, main button, "Follow an order" link and a five-stop rail (Checkout, Voucher, Delivery, Remittance, Reconciled) for order #1047; stop sections 1–3 alternating text/screen; a larger COD section (stops 4–5) with four totals, table and two buttons; "Selling elsewhere" feed panel; Modules (11 switches + 3 in development, built-in tile grid); release-check panel; price with three trial steps; FAQ (6); footer with non-affiliation notice.
- [ ] **Step 2:** Run `python -I src/build.py`. Expected: fails listing missing keys for `en` and `el` (template parses, keys collected).

### Task 2: English strings

**Files:**
- Modify: `src/strings.en.json` (rewrite to the Task 1 key set)

- [ ] **Step 1:** Write every key in a professional register, English plugin labels for mocks.
- [ ] **Step 2:** Run `python -I src/build.py`. Expected: `wrote index.html`; failure only for `el` missing keys.

### Task 3: Greek strings

**Files:**
- Create: `src/strings.el.json`

- [ ] **Step 1:** Write every key in professional Greek; mock labels from the `.po` catalog; Greek number format (`€4.812,60`).
- [ ] **Step 2:** Run `python -I src/build.py`. Expected: `wrote index.html`, `wrote el.html`, exit 0.
- [ ] **Step 3:** Run a leftover check listing `el.html` text nodes with no Greek letters. Expected: only brand names, numbers, plugin UI names.

### Task 4: Browser check

- [ ] **Step 1:** Serve `nifty-newton` on 127.0.0.1 and open both pages at 1280, 940, 720 and 375px, light and dark.
- [ ] **Step 2:** For each: `document.documentElement.scrollWidth <= innerWidth`; `.nav` has no overflow; mobile menu opens and closes; `document.fonts.check('700 20px Commissioner', 'Αντικαταβολή')` is true on `el.html`.
- [ ] **Step 3:** Fix what fails, rebuild, recheck once. No commit (owner decides).
