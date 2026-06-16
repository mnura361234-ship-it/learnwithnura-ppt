from .base_provider import BaseContentProvider
from content_manager import create_content_from_template


class TemplateProvider(BaseContentProvider):
    name = "template"

    def generate(self, topic: str, template_name: str = None, **kwargs) -> str:
        if not template_name:
            raise ValueError("template_name is required for TemplateProvider")

        return create_content_from_template(template_name, topic)
