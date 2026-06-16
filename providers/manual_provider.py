from .base_provider import BaseContentProvider
from config import SLIDES_PATH


class ManualProvider(BaseContentProvider):
    name = "manual"

    def generate(self, topic: str, template_name: str = None, **kwargs) -> str:
        with open(SLIDES_PATH, "r", encoding="utf-8") as slides_file:
            return slides_file.read()
