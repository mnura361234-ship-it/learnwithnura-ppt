import os
import re
from dataclasses import dataclass
from typing import List, Optional

from config import SLIDES_PATH

LAYOUT_TAG_PATTERN = re.compile(r"^\s*\[([a-zA-Z0-9_]+)\]\s*$")
DEBUG_PARSER = False


@dataclass
class SlideContent:
    layout: Optional[str]
    title: str
    body: str


def _read_slide_lines():
    if not os.path.exists(SLIDES_PATH):
        raise FileNotFoundError(f"slides.txt not found at {SLIDES_PATH}")

    with open(SLIDES_PATH, "r", encoding="utf-8") as source:
        return [line.rstrip("\n") for line in source]


def _split_into_blocks(lines: List[str]) -> List[List[str]]:
    blocks: List[List[str]] = []
    current: List[str] = []

    for line in lines:
        if line.strip() == "":
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line)

    if current:
        blocks.append(current)

    return blocks


def _parse_layout_tag(line: str) -> Optional[str]:
    match = LAYOUT_TAG_PATTERN.match(line)
    return match.group(1).lower() if match else None


def _parse_structured_block(block: List[str], index: int) -> Optional[SlideContent]:
    if not block:
        return None

    lines = list(block)
    layout = None

    first_tag = _parse_layout_tag(lines[0])
    if first_tag:
        layout = first_tag
        lines = lines[1:]

    if not lines:
        print(f"WARNING: Slide block {index} has no title or body; skipping.")
        return None

    title = lines[0].strip()
    if not title:
        print(f"WARNING: Slide block {index} has an empty title; skipping.")
        return None

    body = "\n".join(lines[1:]).strip()

    return SlideContent(
        layout=layout,
        title=title,
        body=body
    )


def _parse_explicit_slide_format(lines: List[str]) -> List[SlideContent]:
    """
    Supports:
    ===SLIDE===
    [optional_layout]
    TITLE: ...
    BODY: ...
    BODY: ...
    """

    slides: List[SlideContent] = []

    current_layout = None
    current_title = ""
    current_body: List[str] = []

    def flush():
        nonlocal current_layout, current_title, current_body

        if current_title.strip():
            slides.append(
                SlideContent(
                    layout=current_layout,
                    title=current_title.strip(),
                    body="\n".join(current_body).strip()
                )
            )

        current_layout = None
        current_title = ""
        current_body = []

    for raw_line in lines:
        line = raw_line.strip()

        if not line:
            continue

        if line == "===SLIDE===":
            flush()
            continue

        layout = _parse_layout_tag(line)
        if layout:
            current_layout = layout
            continue

        if line.upper().startswith("TITLE:"):
            current_title = line[6:].strip()
            continue

        if line.upper().startswith("BODY:"):
            current_body.append(line[5:].strip())
            continue

        # Any additional lines after BODY are treated as body continuation.
        if current_title:
            current_body.append(line)

    flush()
    return slides


def _parse_legacy_blocks(blocks: List[List[str]]) -> List[SlideContent]:
    slides: List[SlideContent] = []

    if len(blocks) == 1:
        lines = [line.strip() for line in blocks[0] if line.strip()]

        if len(lines) <= 2:
            title = lines[0] if lines else ""
            body = lines[1] if len(lines) > 1 else ""
            slides.append(
                SlideContent(layout=None, title=title, body=body)
            )
            return slides

        if len(lines) % 2 == 1:
            title = lines[0]
            body = "\n".join(lines[1:]).strip()
            slides.append(
                SlideContent(layout=None, title=title, body=body)
            )
            return slides

        for i in range(0, len(lines), 2):
            title = lines[i]
            body = lines[i + 1] if i + 1 < len(lines) else ""
            slides.append(
                SlideContent(layout=None, title=title, body=body)
            )

        return slides

    for block in blocks:
        lines = [line.strip() for line in block if line.strip()]
        if not lines:
            continue

        title = lines[0]
        body = "\n".join(lines[1:]).strip()

        slides.append(
            SlideContent(layout=None, title=title, body=body)
        )

    return slides


def load_slides():
    raw_lines = _read_slide_lines()

    if not raw_lines:
        raise ValueError("slides.txt is empty.")

    # New explicit format:
    # ===SLIDE===
    # TITLE:
    # BODY:
    if any(line.strip() == "===SLIDE===" for line in raw_lines):
        slides = _parse_explicit_slide_format(raw_lines)
    else:
        blocks = _split_into_blocks(raw_lines)

        if not blocks:
            raise ValueError(
                "slides.txt is empty or contains only blank lines."
            )

        has_layout_tags = any(
            _parse_layout_tag(block[0])
            for block in blocks
            if block
        )

        if has_layout_tags:
            slides: List[SlideContent] = []

            for index, block in enumerate(blocks, start=1):
                slide = _parse_structured_block(block, index)
                if slide:
                    slides.append(slide)
        else:
            slides = _parse_legacy_blocks(blocks)

    if not slides:
        raise ValueError(
            "No valid slides could be loaded from slides.txt."
        )

    if DEBUG_PARSER:
        print("-" * 50)
        for idx, slide in enumerate(slides, start=1):
            print(f"Parsed Slide #{idx}")
            print(f"Layout : {slide.layout or 'automatic'}")
            print(f"Title  : {slide.title}")
            print("Body   :")
            print(slide.body or "<empty>")
            print("-" * 50)

    return slides