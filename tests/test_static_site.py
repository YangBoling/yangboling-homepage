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
            "Institute of Biophysics",
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
        self.assertRegex(self.styles, r"min-height:\s*44px")
        self.assertIn("--accent-teal", self.styles)
        self.assertIn("--border", self.styles)

    def test_no_in_page_file_upload_feature(self):
        self.assertNotIn('type="file"', self.index)
        self.assertNotIn("<input type='file'", self.index)
        self.assertNotIn("upload", self.index.lower())


if __name__ == "__main__":
    unittest.main()
