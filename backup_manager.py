import glob
import os
from datetime import datetime
from typing import List, Optional

from config import BACKUP_DIR, SLIDES_PATH


def _ensure_backup_dir() -> None:
    os.makedirs(BACKUP_DIR, exist_ok=True)


def _current_backup_name() -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"slides_{timestamp}.txt"


def list_backups() -> List[str]:
    _ensure_backup_dir()
    pattern = os.path.join(BACKUP_DIR, "slides_*.txt")
    backups = sorted(glob.glob(pattern), reverse=True)
    return backups


def create_backup() -> Optional[str]:
    if not os.path.isfile(SLIDES_PATH):
        return None

    _ensure_backup_dir()
    backup_name = _current_backup_name()
    backup_path = os.path.join(BACKUP_DIR, backup_name)

    with open(SLIDES_PATH, "r", encoding="utf-8") as source:
        content = source.read()

    with open(backup_path, "w", encoding="utf-8") as destination:
        destination.write(content)

    return backup_path


def restore_backup(backup_file: str) -> bool:
    if not os.path.isfile(backup_file):
        return False

    with open(backup_file, "r", encoding="utf-8") as source:
        content = source.read()

    with open(SLIDES_PATH, "w", encoding="utf-8") as destination:
        destination.write(content)

    return True
