"""Read and validate the Pac-Man configuration."""

import json
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "highscore_filename": "highscores.json",
    "lives": 3,
    "pacgum": 42,
    "points_per_pacgum": 10,
    "points_per_super_pacgum": 50,
    "points_per_ghost": 200,
    "seed": 42,
    "level_max_time": 90,
}

# Allowed range for each integer parameter.
LIMITS = {
    "lives": (1, 10),
    "pacgum": (0, 10000),
    "points_per_pacgum": (0, 10000),
    "points_per_super_pacgum": (0, 10000),
    "points_per_ghost": (0, 10000),
    "seed": (0, 2147483647),
    "level_max_time": (10, 3600),
    "width": (7, 99),
    "height": (7, 99),
}


def validate_int(
    value: Any,
    name: str,
    default: int,
) -> int:
    """Validate an integer and clamp it to safe limits."""
    minimum, maximum = LIMITS[name]

    if type(value) is not int:
        print(f"Warning: invalid {name}, using {default}")
        return default

    if value < minimum:
        print(f"Warning: {name} too small, using {minimum}")
        return minimum

    if value > maximum:
        print(f"Warning: {name} too large, using {maximum}")
        return maximum

    return value


def validate_levels(value: Any) -> list[dict[str, int]]:
    """Validate level dimensions and provide at least 10 levels."""
    if not isinstance(value, list):
        print("Warning: invalid levels, using defaults")
        value = []

    levels: list[dict[str, int]] = []

    for index, level in enumerate(value):
        if not isinstance(level, dict):
            print(f"Warning: invalid level {index + 1}")
            level = {}

        width = validate_int(
            level.get("width", 15), "width", 15
        )
        height = validate_int(
            level.get("height", 15), "height", 15
        )

        levels.append({"width": width, "height": height})

    while len(levels) < 10:
        levels.append({"width": 15, "height": 15})

    return levels


def load_config(filename: str) -> dict[str, Any]:
    """Read a JSON configuration and validate its values."""
    try:
        with Path(filename).open("r", encoding="utf-8") as file:
            lines = file.readlines()

    except OSError as error:
        raise ValueError(
            f"Cannot read configuration file: {error}"
        ) from error

    # Remove full-line comments.
    content = "".join(
        line for line in lines
        if not line.lstrip().startswith("#")
    )

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        print("Warning: invalid JSON, using default configuration")
        data = {}

    if not isinstance(data, dict):
        print("Warning: config must be an object, using defaults")
        data = {}

    config = DEFAULT_CONFIG.copy()

    # Validate numeric parameters.
    for key in LIMITS:
        if key in ("width", "height"):
            continue

        if key in data:
            config[key] = validate_int(
                data[key], key, DEFAULT_CONFIG[key]
            )

    # Validate highscore filename.
    filename_value = data.get("highscore_filename")
    if filename_value is not None:
        if (
            isinstance(filename_value, str)
            and filename_value.strip()
            and not Path(filename_value).is_absolute()
            and ".." not in Path(filename_value).parts
        ):
            config["highscore_filename"] = filename_value
        else:
            print("Warning: invalid highscore filename")

    # Validate level definitions.
    config["levels"] = validate_levels(data.get("levels", []))

    return config
