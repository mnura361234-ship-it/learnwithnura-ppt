import os

from pptx.util import Inches

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SLIDES_PATH = os.path.join(BASE_DIR, "slides.txt")
CONFIG_PATH = os.path.join(BASE_DIR, "config.py")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
PROVIDERS_DIR = os.path.join(BASE_DIR, "providers")
LAYOUTS_DIR = os.path.join(BASE_DIR, "layouts")
COMPONENTS_DIR = os.path.join(BASE_DIR, "components")
TOPICS_PATH = os.path.join(BASE_DIR, "topics.json")

TOPIC = "web3"
BRAND_NAME = "LearnWithNura"
DEFAULT_PROVIDER = "manual"
DEFAULT_TEMPLATE = "generic_template"
OUTPUT_FILENAME_TEMPLATE = "{topic}_Carousel.pptx"
DEFAULT_CTA = "Learn more soon."
DEFAULT_YEAR = "2026"

OUTPUT_DIRECTORY = OUTPUT_DIR
ASSETS_DIRECTORY = ASSETS_DIR
TEMPLATES_DIRECTORY = TEMPLATES_DIR
BACKUP_DIRECTORY = BACKUP_DIR

IMAGE_MAP = {
    "artificial intelligence": "ai.png",
    "blockchain": "blockchain.png",
    "cryptocurrency": "crypto.png",
    "web 3": "web3.png",
    "web3": "web3.png",
    "crypto": "crypto.png",
    "ai": "ai.png",
}
DEFAULT_IMAGE = "default.png"

SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

LAYOUT_ORDER = [
    "standard",
    "reversed",
    "key_takeaway",
    "comparison",
    "standard",
    "reversed",
]

THEME_FALLBACK = "default"
