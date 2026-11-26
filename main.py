#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun bounty entry.

Writes one deadpan weather forecast for the invented city of Qorvath to
/output/entry.txt: at two in the afternoon it rains small keys, which is
exactly the sort of thing the forecast desk reports without blinking — keys,
not rain, and nobody in Qorvath finds that strange anymore.
"""

import os

ENTRY = "In Qorvath, expect light rain of small keys at 14:00, clearing by dusk; residents are advised to check their pockets and carry one umbrella, just in case."


def validate(text: str) -> str:
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    return text


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
