"""The Comment Above the Code.

Writes one line -- a comment a developer left above fragile
production code -- to entry.txt in the output directory.
Deterministic: every run produces the same bytes.
No arguments, no input, no network, no other files read.
"""

import os

LINE = "// This endpoint returns 200 even when it fails, because the dashboard only counts 500s."


def main() -> None:
    # Gate guard: the entry must be one line of 1-200 characters.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
