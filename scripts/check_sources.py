from pathlib import Path
import re
import sys

root = Path("docs/blog/posts")
bad = False

for path in sorted(root.glob("*.md")):
    source = path.read_text(encoding="utf-8")

    if re.search(r"\\(?:\(|\)|\[|\])", source):
        print(f"BAD_DELIMITER: {path}")
        bad = True

    if any(value in source for value in ("<br", "Missing argument", "\ufffd")):
        print(f"BAD_TEXT: {path}")
        bad = True

    if source.replace("$$", "").count("$") % 2:
        print(f"ODD_DOLLARS: {path}")
        bad = True

    if sum(line.startswith("> 发布于") for line in source.splitlines()) != 1:
        print(f"DATE_COUNT: {path}")
        bad = True

    for line_number, line in enumerate(source.splitlines(), 1):
        if re.match(r"^\s*(?:date|title)\b", line, re.I):
            print(f"RAW_METADATA: {path}:{line_number}")
            bad = True

print("SOURCE_CHECK", "FAIL" if bad else "PASS")
sys.exit(1 if bad else 0)

