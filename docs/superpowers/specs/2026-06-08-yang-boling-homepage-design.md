# Yang Boling Personal Research Homepage Design

Date: 2026-06-08

## Goal

Build a modern, minimalist, bilingual personal research homepage for Yang Boling. The site should present an early-stage but highly promising AI/neuroscience researcher working toward future intelligent systems.

The final output must be a static website that can be uploaded through Cloudflare Pages static file upload. The page must not include an in-page static-file upload feature.

## Source Requirements

The Word prompt asks for:

- A globally styled personal research website for "Yang Boling".
- A blend of AI researcher, computational neuroscience, independent lab, future technology, and elegant academic portfolio.
- Avoidance of corporate templates, flashy startup aesthetics, excessive animations, childish gradients, and clutter.
- Clean white/dark adaptive theme, calm typography, whitespace, subtle glassmorphism, soft shadows, smooth transitions, modern sans-serif typography, responsive design.
- Main sections: Hero, About, Research Interests, Projects, Publications / Notes, Contact, Footer.
- Static, fast, SEO-friendly, mobile-friendly, dark mode, Cloudflare Pages and GitHub Pages compatible.
- Preferred stack in the prompt: HTML/CSS/JS or Next.js. This project will use plain HTML/CSS/JS because the user needs a direct static upload target for Cloudflare Pages.

User clarifications:

- The "Upload your static files" phrasing refers to Cloudflare Pages deployment, not a feature to place on the homepage.
- The visual direction is "B. Future Lab".
- The final framing system is "A. Modular Lab Bento".
- The design should use the provided `ui-ux-pro-max` skill to optimize layout, typography, interaction states, and accessibility.
- The site should use large-company-style framed content sections, extracting structure from Apple, Vercel, and Anthropic rather than copying their branding.

## Selected Direction

The homepage will use a "Future Lab Bento" direction:

- Dark-first hero with light/dark adaptive support.
- Subtle neural-network / world-model visualization in the first viewport.
- Framed content blocks with thin borders and restrained glass surfaces.
- Modular bento grid for About, Research Interests, Projects, Notes, and Contact.
- Academic credibility through clear hierarchy, restrained copy, and research-oriented content.

The design extracts these structural patterns:

- Apple-style confident, isolated hero and feature panels.
- Vercel-style precise bordered grids and developer-tool discipline.
- Anthropic-style readable research/news lists with calm information density.

## Design System

The design system follows the `ui-ux-pro-max` guidance for Bento Box Grid, Modern Dark, dark mode, accessibility, and responsive static HTML.

### Layout

- Page max width: centered content container with generous gutters.
- Grid: bento layout with 4 columns on desktop, 2 columns on tablet, 1 column on mobile.
- Cards: varied spans for hierarchy, but all content must fit without clipping.
- Sections: full-width page bands or unframed layouts; cards are used only for discrete repeated or modular content.
- Navigation: sticky/floating top navigation with bordered glass surface.
- First viewport: hero must show Yang Boling prominently and reveal the next section on common desktop and mobile viewports.

### Visual Style

- Dark mode primary, light mode fully supported.
- Background: near-black dark surfaces with desaturated blue/teal accents; light mode uses off-white and white surfaces.
- Borders: thin, visible, low-contrast borders to define each content module.
- Glassmorphism: subtle translucent surfaces only; avoid heavy blur that hurts readability.
- Shadows: soft and restrained.
- Corners: 16-24px radius for cards and panels.
- Motion: hover/press transitions around 150-300ms; no excessive continuous decorative animation.
- Reduced motion: disable or simplify neural animation and hover movement when `prefers-reduced-motion: reduce`.

### Typography

- Headings: academic but modern, using Crimson Pro if loaded successfully.
- Body: Atkinson Hyperlegible if loaded successfully.
- Chinese fallback: system Chinese fonts such as Noto Sans SC, Microsoft YaHei, PingFang SC, and system sans-serif.
- Letter spacing: 0 for normal text and headings.
- Body text: minimum 16px on mobile with 1.5-1.75 line height.
- Long text measure: keep paragraphs readable, not full-width across large screens.

### Color Tokens

Use semantic CSS variables rather than ad hoc colors in components.

- Dark background: `#08090d` / `#0c0d12`.
- Dark elevated surface: translucent white around 4-8% opacity.
- Dark foreground: `#fafafa`.
- Dark muted foreground: rgba white around 64-76%.
- Accent blue: `#2563eb`.
- Accent teal: `#2dd4bf`.
- Light background: `#fafafa` or `#f5f5f7`.
- Light foreground: `#09090b`.
- Border dark: rgba white around 10-14%.
- Border light: rgba dark around 8-12%.

All text/background pairs must meet WCAG AA contrast.

## Content Structure

### Header

Include:

- Brand/name: Yang Boling.
- Anchor links: Research, Projects, Notes, Contact.
- Language toggle: EN / 中文.
- Theme toggle: automatic system preference by default, manual toggle available.

Header behavior:

- Keyboard focus states must be visible.
- On mobile, navigation may collapse into a compact set of controls while preserving the language and theme toggles.
- All controls must have accessible labels.

### Hero

Content in English:

- Title: "Yang Boling"
- Subtitle: "Exploring AI, brains, and world models."
- Introduction: "Undergraduate student at Huazhong University of Science and Technology. Incoming PhD student at the Institute of Biophysics, Chinese Academy of Sciences."
- Buttons: View Research, Projects, Contact.

Chinese equivalent:

- Title: "杨博凌"
- Subtitle: "探索 AI、大脑与世界模型。"
- Introduction: "华中科技大学本科生。即将进入中国科学院生物物理研究所攻读博士学位。"
- Buttons: 查看研究, 项目, 联系方式.

Visual:

- Framed hero panel and separate framed neural/world-model visualization panel.
- Visualization is built in CSS/SVG/canvas without external runtime dependencies.
- The visualization must remain subtle and non-distracting.

### About

Short biography emphasizing:

- AI agents.
- Computational neuroscience.
- Brain-inspired intelligence.
- World models.
- Brain-computer interfaces.
- Autonomous systems.

Tone:

- Curious, ambitious, research-oriented.
- Avoid inflated claims.
- Make the early-stage status feel focused and credible.

### Research Interests

Use a bounded module containing six compact interest cards:

- AI Agents.
- World Models.
- Computational Neuroscience.
- Brain-Computer Interface.
- Neural Circuits.
- Embodied Intelligence.

Each card includes:

- A consistent inline SVG icon or CSS icon treatment, not emoji.
- Short description.
- Subtle hover state.
- Bilingual text.

### Projects

Display project cards in a framed module:

- Closed-loop Mouse AI Companion System.
- Circadian Stress Research.
- Allen Brain Atlas + AI Prediction.
- Autonomous Behavioral Platform.

Each project card includes:

- A static generated visual/abstract preview treatment, not external stock photography.
- Tags.
- GitHub/demo buttons where URLs can be placeholders if unavailable.
- Concise bilingual description.

If a URL is not known, the button should be visibly disabled or use `href="#"` with accessible disabled semantics and no misleading navigation.

### Publications / Notes

Use a clean list or timeline inside a bordered module. Include categories:

- Papers.
- Blog notes.
- Reading notes.
- Ongoing ideas.

The section should be easy to update manually in HTML.

### Contact

Include:

- Email.
- GitHub.
- Google Scholar.
- X/Twitter as optional.

Unknown URLs should be left as easy-to-edit placeholders in the source and not visually overemphasized.

### Footer

Text:

- English: "Built with curiosity and coffee."
- Chinese: "以好奇心与咖啡构建。"

## Bilingual Behavior

- The default language is English.
- The language toggle switches all visible section copy to Chinese or English.
- The selected language persists in `localStorage`.
- The implementation uses structured data attributes or a simple content dictionary, not duplicated full pages.
- HTML metadata should include English defaults; visible page content can switch client-side.

## Theme Behavior

- The default theme follows `prefers-color-scheme`.
- A manual theme toggle persists the user's choice in `localStorage`.
- Both themes are designed intentionally and must not be simple color inversion.
- The page must avoid horizontal scroll and content overlap in both themes.

## Technical Architecture

Use a no-build static implementation:

- `index.html`
- `styles.css`
- `script.js`
- Optional `assets/` folder for local images or generated static previews.

No build step is required. The folder can be uploaded directly to Cloudflare Pages or served through GitHub Pages. Next.js is intentionally not selected for the first version because it would add project scaffolding and a build/deploy workflow that the current request does not require.

External dependencies:

- Google Fonts may be used with `font-display: swap`.
- Do not use runtime frameworks unless a later implementation plan explicitly changes this.
- Avoid large JavaScript libraries.

JavaScript responsibilities:

- Language toggle.
- Theme toggle.
- Small progressive enhancements such as active nav state or reduced-motion-aware visual behavior.

CSS responsibilities:

- Design tokens.
- Responsive grid.
- Light/dark themes.
- Bordered bento modules.
- Focus states and reduced-motion behavior.

## Accessibility Requirements

- Use semantic HTML: header, nav, main, section, article, footer.
- Keep heading hierarchy sequential.
- Provide skip link to main content.
- All interactive elements must be keyboard reachable.
- Focus rings must be visible.
- Icon-only controls require `aria-label`.
- Normal text contrast must meet at least 4.5:1.
- Touch targets must be at least 44px.
- Do not rely on hover alone.
- Respect `prefers-reduced-motion`.
- Avoid text smaller than 16px for primary body content on mobile.

## Performance Requirements

- Static page should load quickly on Cloudflare Pages.
- Avoid heavy images and external scripts.
- Reserve dimensions for visual modules to prevent layout shift.
- Use CSS/SVG for abstract visuals where practical.
- Lazy-load any non-critical images if images are added.

## SEO Requirements

- Include title and meta description.
- Include viewport meta tag.
- Include canonical-friendly structure without requiring JavaScript for initial main content.
- Use meaningful section headings and link text.
- Include Open Graph and Twitter card metadata with simple defaults.

## Testing / Verification Plan

Before completion, verify:

- Open the static page locally.
- Check desktop and mobile responsive layouts at approximately 375px, 768px, 1024px, and wide desktop.
- Confirm no horizontal scrolling.
- Confirm language toggle updates all major visible copy.
- Confirm theme toggle persists and system preference fallback works.
- Confirm keyboard tab order and focus states.
- Confirm reduced-motion CSS path exists.
- Confirm Lighthouse-style basics manually: title, meta description, semantic headings.

## Out of Scope

- Backend contact form.
- CMS or admin editor.
- File upload inside the homepage.
- Live publication feed.
- Authentication.
- Analytics integration unless requested later.

## Open Implementation Notes

- The first implementation should keep unknown links editable and visible in one source object.
- Project preview images can be CSS/SVG abstract panels if no real screenshots exist.
- If the user later provides real project links, publications, portraits, or lab images, those can replace placeholders without changing the site architecture.
