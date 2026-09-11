#!/usr/bin/env python3
"""Verify every internal link and heading anchor in the repo resolves.

Standard library only. Run with: python3 tools/check_links.py  (or: make links)
Exits non-zero if anything is broken, so it works as a pre-commit gate.
"""
import os
import re
import sys
from urllib.parse import unquote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_offline import heading_slug  # noqa: E402  (same slug rules as the build)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def main():
    anchors, files = {}, []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            files.append(path)
            seen, found = {}, set()
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    m = re.match(r"^#{1,6}\s+(.*)", line)
                    if m:
                        slug = heading_slug(m.group(1))
                        n = seen.get(slug, 0)
                        seen[slug] = n + 1
                        found.add(slug if n == 0 else "%s-%d" % (slug, n))
            anchors[path] = found

    problems, total = [], 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for m in LINK.finditer(text):
            url = m.group(2).strip()
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            total += 1
            path_part, _, frag = url.partition("#")
            target = (os.path.normpath(
                os.path.join(os.path.dirname(path), unquote(path_part)))
                if path_part else path)
            rel = os.path.relpath(path, ROOT)
            if not os.path.exists(target):
                problems.append("%s: missing file   [%s](%s)"
                                % (rel, m.group(1), url))
            elif frag and target.endswith(".md") \
                    and unquote(frag) not in anchors.get(target, set()):
                problems.append("%s: missing anchor [%s](%s)"
                                % (rel, m.group(1), url))

    for p in problems:
        print("  " + p)
    print("checked %d internal links across %d files -> %s"
          % (total, len(files), "ALL OK" if not problems
             else "%d PROBLEM(S)" % len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
