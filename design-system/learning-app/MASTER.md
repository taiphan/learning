# Design System — Learning App

**Project:** 52-week Learning App (Banking BA → AI Engineer)  
**Palette:** Anthropic-inspired warm neutrals + quarter accents (see `styles.css` `:root`)

## Typography

| Role | Font | CSS variable |
|------|------|--------------|
| Headings, UI | Poppins | `--font-head` |
| Body | Lora | `--font-body` |

## Colors

| Role | Hex | Token |
|------|-----|-------|
| Text | `#141413` | `--slate` |
| Background | `#faf9f5` | `--cream` |
| Card | `#ffffff` | `--card` |
| Muted text | `#475569` | `--muted` |
| Accent / CTA | `#d97757` | `--clay` |
| Q1 / links | `#6a9bcc` | `--sky` |
| Q2 / success | `#788c5d` | `--olive` |
| Q3 | `#c46686` | `--fig` |

## Layout

- **Full-width views** (Home, Explore, Library, Account): `.view-page` max-width `960px`, centered
- **Learn view** (week detail): sidebar + main via `.layout--sidebar`
- **Page headers**: `.page-hero` (center) or `.page-hero--left` (Explore, Library, Account)
- **Section hub on Home**: `.section-nav` grid — Explore, Library, Account, Learn

## Components

- Buttons: `.btn`, `.btn-primary`, `.btn-ghost`
- Cards: `.card` — white, `--radius`, `--shadow`
- Stats: `.grid-3` + `.stat-card` on Home
- Nav: topbar `.app-nav` + mobile `.mobile-nav` (5 items)

## Do not use

- Kids/playful fonts (Comic Neue, Baloo) — wrong audience for this app
- Dark mode as default
- Layout-shifting hover transforms
