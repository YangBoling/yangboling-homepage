# Yang Boling Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the approved static bilingual Future Lab Bento homepage for Yang Boling.

**Architecture:** Use a no-build static site with semantic HTML, tokenized CSS, and small vanilla JavaScript enhancements. The initial HTML contains English content for SEO and no-JS readability; JavaScript switches visible text to Chinese and persists language/theme preferences.

**Tech Stack:** HTML, CSS, vanilla JavaScript, Python `unittest` for static regression checks.

---

## File Structure

- Create `tests/test_static_site.py`: static regression tests for required files, semantic sections, i18n hooks, theme hooks, accessibility basics, and deployment constraints.
- Create `index.html`: semantic homepage content, bilingual text keys, header/nav, hero, bento modules, project cards, notes list, contact links, SEO metadata.
- Create `styles.css`: UI/UX Pro Max design tokens, dark/light themes, bordered bento grid, responsive rules, focus states, reduced-motion handling.
- Create `script.js`: content dictionary, language toggle, theme toggle, localStorage persistence, system theme fallback, no-framework behavior.

The project is not a Git repository, so commit steps are not executable in this workspace.

---

### Task 1: Static Regression Tests

**Files:**
- Create: `tests/test_static_site.py`
- Test: `tests/test_static_site.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_static_site.py` with tests that fail until the static homepage files exist:

```python
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
STYLES = ROOT / "styles.css"
SCRIPT = ROOT / "script.js"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.attrs = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self.tags.append(tag)
        self.attrs.append((tag, attr_dict))

    def handle_data(self, data):
        stripped = data.strip()
        if stripped:
            self.text.append(stripped)


def read(path):
    return path.read_text(encoding="utf-8")


class StaticSiteTests(unittest.TestCase):
    def setUp(self):
        self.index = read(INDEX)
        self.styles = read(STYLES)
        self.script = read(SCRIPT)
        self.parser = SiteParser()
        self.parser.feed(self.index)

    def test_required_static_files_exist(self):
        self.assertTrue(INDEX.exists())
        self.assertTrue(STYLES.exists())
        self.assertTrue(SCRIPT.exists())

    def test_semantic_sections_and_seo_exist(self):
        for tag in ["header", "nav", "main", "section", "article", "footer"]:
            self.assertIn(tag, self.parser.tags)
        self.assertIn('<meta name="description"', self.index)
        self.assertIn('property="og:title"', self.index)
        self.assertIn('name="twitter:card"', self.index)
        self.assertIn('name="viewport"', self.index)

    def test_required_homepage_content_exists(self):
        required = [
            "Yang Boling",
            "Exploring AI, brains, and world models.",
            "Huazhong University of Science and Technology",
            "expected to graduate in 2026",
            "AI Agents",
            "World Models",
            "Computational Neuroscience",
            "Brain-Computer Interface",
            "Closed-loop Mouse AI Companion System",
            "Built with curiosity and coffee.",
        ]
        for text in required:
            self.assertIn(text, self.index)

    def test_bilingual_and_theme_hooks_exist(self):
        self.assertIn("data-i18n", self.index)
        self.assertIn("data-lang-toggle", self.index)
        self.assertIn("data-theme-toggle", self.index)
        self.assertIn("const translations", self.script)
        self.assertIn("localStorage", self.script)
        self.assertIn("prefers-color-scheme", self.script)

    def test_uiux_accessibility_and_responsive_css_exist(self):
        self.assertIn(":focus-visible", self.styles)
        self.assertIn("@media (prefers-reduced-motion: reduce)", self.styles)
        self.assertIn("@media (max-width: 760px)", self.styles)
        self.assertIn("grid-template-columns: repeat(4", self.styles)
        self.assertRegex(self.styles, r"min-height:\\s*44px")
        self.assertIn("--accent-teal", self.styles)
        self.assertIn("--border", self.styles)

    def test_no_in_page_file_upload_feature(self):
        self.assertNotIn('type="file"', self.index)
        self.assertNotIn("<input type='file'", self.index)
        self.assertNotIn("upload", self.index.lower())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: FAIL because `index.html`, `styles.css`, and `script.js` do not exist yet.

---

### Task 2: Static Homepage Markup

**Files:**
- Create: `index.html`
- Test: `tests/test_static_site.py`

- [ ] **Step 1: Create semantic HTML**

Create `index.html` with:

- SEO metadata and linked `styles.css` / `script.js`.
- Skip link.
- Header/nav with Research, Projects, Notes, Contact anchors.
- Language and theme buttons with `data-lang-toggle` and `data-theme-toggle`.
- Hero section with Yang Boling, English default content, and neural visualization markup.
- Bento modules for About, Research Interests, Projects, Notes, Contact.
- Footer.
- `data-i18n` attributes for all text that must switch language.

- [ ] **Step 2: Run tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: still FAIL because CSS and JS are not implemented.

---

### Task 3: UI/UX Pro Max CSS System

**Files:**
- Create: `styles.css`
- Test: `tests/test_static_site.py`

- [ ] **Step 1: Create tokenized CSS**

Create `styles.css` with:

- Semantic color variables for dark and light themes.
- 4-column desktop bento grid, 2-column tablet grid, 1-column mobile grid.
- Thin bordered glass modules.
- 16-24px rounded panels.
- 44px minimum interaction targets.
- Visible `:focus-visible` rings.
- `@media (prefers-reduced-motion: reduce)` handling.
- No negative letter spacing and no viewport-scaled font-size rules.

- [ ] **Step 2: Run tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: still FAIL because JS behavior is not implemented.

---

### Task 4: Bilingual And Theme JavaScript

**Files:**
- Create: `script.js`
- Test: `tests/test_static_site.py`

- [ ] **Step 1: Create vanilla JavaScript**

Create `script.js` with:

- `const translations = { en: {...}, zh: {...} }`.
- Language toggle that updates every `[data-i18n]` element.
- Theme toggle that sets `data-theme`.
- `localStorage` persistence for language and theme.
- System theme fallback through `window.matchMedia("(prefers-color-scheme: dark)")`.
- Defensive checks so the page does not error if an optional element is missing.

- [ ] **Step 2: Run tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: PASS.

---

### Task 5: Manual Static Verification

**Files:**
- Verify: `index.html`
- Verify: `styles.css`
- Verify: `script.js`

- [ ] **Step 1: Serve locally**

Run:

```bash
python3 -m http.server 8000
```

Expected: local server starts and serves the static site.

- [ ] **Step 2: Inspect the page**

Open `http://localhost:8000` and verify:

- The hero shows Yang Boling prominently.
- The next bento section is visible without needing a long scroll.
- Language toggle switches English and Chinese.
- Theme toggle switches light and dark.
- No in-page upload control exists.
- No obvious overlap on desktop or mobile widths.

- [ ] **Step 3: Stop server**

Stop the local server after inspection.

---

### Task 6: Final Verification

**Files:**
- Verify: all created files.

- [ ] **Step 1: Run static tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: PASS.

- [ ] **Step 2: Check generated file list**

Run:

```bash
find . -maxdepth 2 -type f | sort
```

Expected: includes `index.html`, `styles.css`, `script.js`, design spec, implementation plan, Word prompt, and tests.

- [ ] **Step 3: Git commit**

Skipped in this workspace because `/home/ybl/mysite` is not a Git repository.
