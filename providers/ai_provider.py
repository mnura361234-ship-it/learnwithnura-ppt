from .base_provider import BaseContentProvider


class AIProvider(BaseContentProvider):
    """Placeholder for future LLM integration.

    This provider is intentionally disabled until API integration is added.
    It does not make network calls or require external dependencies.
    """

    name = "ai"

    def generate(self, topic: str, template_name: str = None, **kwargs) -> str:
        raise NotImplementedError(
            "AIProvider is a stub. Add API integration before using this provider."
        )
