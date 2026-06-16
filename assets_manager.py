import os

from config import ASSETS_DIR


def ensure_output_directory(output_dir):
    """Ensure the output directory exists."""
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        raise RuntimeError(f"Unable to create output directory: {error}") from error


def validate_asset_path(asset_path):
    """Return a valid asset path or None if asset missing."""
    if not asset_path:
        return None
    if os.path.exists(asset_path):
        return asset_path
    return None


def find_asset(filename):
    """Resolve an asset filename inside the assets directory."""
    if not filename:
        return None

    candidate = os.path.join(ASSETS_DIR, filename)
    return candidate if os.path.exists(candidate) else None
