from abc import ABC, abstractmethod


class BaseContentProvider(ABC):
    name = "base"

    @abstractmethod
    def generate(self, topic: str, template_name: str = None, **kwargs) -> str:
        """Return parser-compatible content as a string."""
        raise NotImplementedError
