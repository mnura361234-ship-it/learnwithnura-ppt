from typing import List, Dict

from content_manager import save_to_slides


class PresentationAdapter:
    """
    Bridges the Education Pipeline and the existing Build System.

    The adapter converts SlideBuilder output (list of dicts) into the
    textual slides format expected by the existing `slides.txt` parser and
    `generate.py` rendering pipeline.
    """

    def prepare(self, slides: List[Dict[str, str]]) -> str:
        """
        Convert SlideBuilder output into a slides.txt string and persist it.

        Returns the slides content string that was written.
        """
        blocks: List[str] = []

        for slide in slides:
            # If layout provided, include as a tag
            layout = slide.get("layout")
            if layout:
                blocks.append(f"[{layout}]")

            title = slide.get("title", "")
            body = slide.get("body", "")

            if title:
                blocks.append(title)

            if body:
                # Ensure body lines are preserved
                blocks.extend(body.splitlines())

            # Separate slides with a blank line
            blocks.append("")

        content = "\n".join(blocks).strip() + "\n"

        # Persist using existing content manager to keep backups and consistency
        save_to_slides(content)

        return content
