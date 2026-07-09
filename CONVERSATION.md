# Session Backup — 9 July 2026

## Goal
Build, deploy, and maintain the **500 Prompts IA Premium** project (`ucfzem.github.io/500-prompts`) with password-gated access from the works page.

## Key Decisions
- **Password**: `UcfZem@2026` validates server-side via Cloudflare Worker `works-validator.azer-tyu199p.workers.dev`; never in client code.
- **Session**: `/works/` locked section uses `sessionStorage` (resets on browser close).
- **Public section**: `/500-prompts/` is public but only linked from the locked `/works/` section.
- **Moroccan flag** 🇲🇦 for Arabic; flags 🇫🇷🇬🇧🇪🇸🇲🇦 for FR/EN/ES/AR.
- **Arabic RTL** supported with Noto Sans Arabic font.

## Progress

### Done
1. Created repo `github.com/ucfzem/500-prompts` with GH Pages at `https://ucfzem.github.io/500-prompts/`
2. v2.0 — logo SVG, QR code, Moroccan flag, RTL Arabic, dark/light theme, real-time search, bug fixes
3. Works page link in locked section points to the new repo URL
4. Removed old `500prompts/` directory from main repo `ucfzem.github.io`
5. Removed 500 Prompts IA link from main landing page
6. Vercel (`ucfzem-works.vercel.app`): works page updated, redirect loop fixed
7. Cloudflare (`500-prompts-ia.pages.dev`): deployed (currently 404 — project-level issue)
8. **v3.0 — i18n**:
   - `ar.json`: 500 prompts translated to Arabic via Google Translate API
   - `en.json`: 500 prompts translated to English
   - `es.json`: 500 prompts translated to Spanish
   - `index.html`: loads translation JSONs via `fetch()` on startup
   - Language switcher (FR/EN/ES/AR) switches both UI and prompt text
   - Search works in all languages
   - Falls back to French if translation not loaded

### URLs
- **Main site**: https://ucfzem.github.io/500-prompts/
- **Cloudflare backup**: https://500-prompts-ia.pages.dev (broken — 404)
- **Works page**: https://ucfzem-works.vercel.app/works/
- **GitHub repo**: https://github.com/ucfzem/500-prompts

### Cloudflare Worker
- Password validator: `works-validator.azer-tyu199p.workers.dev`
- Passwords are validated server-side only

## Next Steps
- Fix Cloudflare Pages deployment (currently returning 404)
- Arabic prompt translation refinement (automatic translations may need manual review)
