"""Write one funny developer excuse to /output/entry.txt.

Entry for make.fun bounty "Make the AI Judge Laugh: Developer Excuses"
(u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).
"""

import os

ENTRY = (
    "Production broke because a cron job I never wrote, on a server I never "
    "touched, deleted the table I definitely backed up \u2014 in my head."
)


def main():
    # Validation guard: the gate requires 1-200 chars, a single line,
    # non-blank UTF-8 text.
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range 1-200"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
