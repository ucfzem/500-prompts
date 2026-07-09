# Session Backup — 9 July 2026

## Goal
Build, deploy, and maintain the **500 Prompts IA Premium** project (`ucfzem.github.io/500-prompts`) with password-gated access from the works page.

## Key Decisions
- **Password**: `UcfZem@2026` validates server-side via Cloudflare Worker `works-validator.azer-tyu199p.workers.dev`; never in client code.
- **Session**: `/works/` locked section uses `sessionStorage` (resets on browser close).
- **Public section**: `/500-prompts/` is public but only linked from the locked `/works/` section.
- **Flags**: 🇫🇷 FR / 🇬🇧 EN / 🇪🇸 ES / 🇲🇦 AR
- **Arabic font**: Cairo (RTL supported)
- **Heading font**: Outfit (sans-serif, elegant)

## Progress

### v1.0 — Initial Setup
1. Created repo `github.com/ucfzem/500-prompts` with GH Pages at `https://ucfzem.github.io/500-prompts/`
2. Deployed initial version (500 prompts in French)

### v2.0 — Tweak
3. Logo SVG (`pack500pts_card.svg`), QR code (`qr_code.svg`)
4. Moroccan flag 🇲🇦 for Arabic language selector
5. RTL support for Arabic
6. Dark/light theme toggle with `localStorage` persistence
7. Real-time search with category filtering
8. Bug fixes: copy button, navigation, search
9. Removed old `500prompts/` directory from main repo `ucfzem.github.io`
10. Removed 500 Prompts IA link from main landing page
11. Vercel (`ucfzem-works.vercel.app`): works page updated, redirect loop fixed (removed conflicting `trailingSlash`)
12. Cloudflare (`500-prompts-ia.pages.dev`): deployed (currently 404 — project-level issue)

### v3.0 — i18n Multilingual
13. **Arabic** (`ar.json`): 500 prompts translated via Google Translate API (deep-translator)
14. **English** (`en.json`): 500 prompts translated
15. **Spanish** (`es.json`): 500 prompts translated
16. `index.html`: loads translation JSONs via `fetch()` on startup
17. Language switcher (FR/EN/ES/AR) switches both UI text and prompt content
18. Search works in all languages (searches translated text)
19. Falls back to French if translation not loaded

### v3.1 — UI Polish
20. **Font**: heading changed from Playfair Display (serif) to Outfit (sans-serif)
21. **Arabic font**: switched from Noto Sans Arabic → El Messiri → Cairo
22. **Copy button**: moved from bottom-right to top using `inset-inline-end` for proper RTL layout
23. **Prompt number**: moved to `inset-inline-start`
24. **Logo**: replaced inline SVG with new PNG logo (`logo.png`)
25. **Header**: text removed beside logo, height increased to 72px
26. **Scroll fix**: language switch no longer scrolls to top — position is preserved

## URLs
- **Main site**: https://ucfzem.github.io/500-prompts/
- **Cloudflare backup**: https://500-prompts-ia.pages.dev (broken — 404)
- **Works page (locked)**: https://ucfzem-works.vercel.app/works/
- **GitHub repo**: https://github.com/ucfzem/500-prompts
- **Session backup**: https://github.com/ucfzem/500-prompts/blob/main/CONVERSATION.md

## Cloudflare Worker
- Password validator: `works-validator.azer-tyu199p.workers.dev`
- Passwords are validated server-side only
- Password: `UcfZem@2026`

## Repo Structure
```
500-prompts/
├── index.html          (main page — FR prompts embedded, loads EN/ES/AR from JSON)
├── ar.json             (500 prompts in Arabic)
├── en.json             (500 prompts in English)
├── es.json             (500 prompts in Spanish)
├── logo.png            (new PNG logo)
├── pack500pts_card.svg (card SVG)
├── qr_code.svg         (QR code SVG)
├── .nojekyll           (disable Jekyll for GH Pages)
└── CONVERSATION.md     (this file)
```
