from config import DEFAULT_IMAGE, IMAGE_MAP
from assets_manager import find_asset


def select_topic_image(topic):
    """Select a topic image using exact and whole-word matching."""
    if not topic:
        return find_asset(DEFAULT_IMAGE), DEFAULT_IMAGE

    normalized = topic.lower().strip()
    selected = None

    if normalized in IMAGE_MAP:
        selected = IMAGE_MAP[normalized]

    if selected is None:
        words = normalized.replace("-", " ").split()
        for keyword, filename in IMAGE_MAP.items():
            keyword_words = keyword.split()
            if len(keyword_words) == 1 and keyword in words:
                selected = filename
                break
            if keyword == normalized:
                selected = filename
                break

    if selected is None:
        selected = DEFAULT_IMAGE

    image_path = find_asset(selected)
    if image_path:
        return image_path, selected

    fallback = find_asset(DEFAULT_IMAGE)
    return fallback, DEFAULT_IMAGE
