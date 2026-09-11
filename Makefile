# How To Survive — offline bundle
#
# Everything here uses ONLY the Python standard library. No pip, no network,
# no pandoc, no Node. It must still work in ten years, on a machine that has
# never been online.

PYTHON ?= python3

.PHONY: help offline check links print clean all

help:
	@echo "make offline   build offline/survival-plan.html and .txt"
	@echo "make check     verify the build references nothing external (writes nothing)"
	@echo "make links     verify every internal link and heading anchor resolves"
	@echo "make all       links + offline"
	@echo "make print     how to get a paper copy"
	@echo "make clean     remove generated files"

offline:
	@$(PYTHON) tools/build_offline.py

check:
	@$(PYTHON) tools/build_offline.py --check

links:
	@$(PYTHON) tools/check_links.py

all: links offline

print:
	@echo "To print the whole plan:"
	@echo "  1. make offline"
	@echo "  2. open offline/survival-plan.html in any browser"
	@echo "  3. Print -> A4, double-sided, default margins"
	@echo ""
	@echo "Each chapter starts on a new page; tables and diagrams are kept whole."
	@echo ""
	@echo "If you print only one thing, print worksheets/quick-reference-cards.md"
	@echo "and laminate it. See docs/13-offline-and-paper.md for the print order."

clean:
	@rm -f offline/survival-plan.html offline/survival-plan.txt
	@echo "removed generated files (sources untouched)"
