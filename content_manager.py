import os
import json
import re
from typing import Dict, List, Optional

from config import TEMPLATES_DIR, TOPICS_PATH, SLIDES_PATH

PLACEHOLDER_PATTERN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def list_templates() -> List[str]:
    if not os.path.isdir(TEMPLATES_DIR):
        return []

    return [
        os.path.splitext(name)[0]
        for name in sorted(os.listdir(TEMPLATES_DIR))
        if name.endswith(".txt")
    ]


def load_template(name: str) -> str:
    path = os.path.join(TEMPLATES_DIR, f"{name}.txt")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Template '{name}' not found.")

    with open(path, "r", encoding="utf-8") as template_file:
        return template_file.read()


def _load_topics() -> Dict[str, Dict[str, str]]:
    if not os.path.isfile(TOPICS_PATH):
        return {}

    try:
        with open(TOPICS_PATH, "r", encoding="utf-8") as file_handle:
            return json.load(file_handle)
    except Exception:
        return {}


def populate_placeholders(template_text: str, replacements: Optional[Dict[str, str]] = None) -> str:
    replacements = replacements or {}

    def replace(match):
        key = match.group(1)
        return replacements.get(key, match.group(0))

    return PLACEHOLDER_PATTERN.sub(replace, template_text)


def create_content_from_template(template_name: str, topic: Optional[str] = None) -> str:
    template_text = load_template(template_name)
    topics = _load_topics()

    if topic:
        default_values = {
            "TOPIC": topic,
            "YEAR": str(os.getenv("YEAR", "2026")),
            "BRAND_NAME": topics.get(topic, {}).get("theme", "LearnWithNura"),
            "CTA": f"Learn more about {topic}!",
        }
        if topic in topics:
            topic_data = topics[topic]
            if "theme" in topic_data:
                default_values["BRAND_NAME"] = topic_data["theme"]
            if "image" in topic_data:
                default_values.setdefault("IMAGE", topic_data["image"])
            if "default_template" in topic_data:
                default_values.setdefault("TEMPLATE", topic_data["default_template"])
    else:
        default_values = {
            "TOPIC": "",
            "YEAR": str(os.getenv("YEAR", "2026")),
            "BRAND_NAME": "LearnWithNura",
            "CTA": "Learn more soon.",
        }

    return populate_placeholders(template_text, default_values)


def save_to_slides(content: str) -> None:
    with open(SLIDES_PATH, "w", encoding="utf-8") as output_file:
        output_file.write(content)


def validate_generated_content(content: str) -> bool:
    if not content or not content.strip():
        return False

    blocks = [block for block in content.split("\n\n") if block.strip()]
    if not blocks:
        return False

    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            return False
        if lines[0].startswith("[") and lines[0].endswith("]") and len(lines) == 1:
            return False
        if not lines[0]:
            return False

    return True
