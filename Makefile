THEMES_DIR := $(HOME)/.config/zed/themes

.PHONY: install uninstall generate list

install:
	@mkdir -p $(THEMES_DIR)
	@cp themes/*.json $(THEMES_DIR)/
	@echo "Installed $$(ls themes/*.json | wc -l | tr -d ' ') theme files to $(THEMES_DIR)"
	@echo "Open Zed and press Cmd+K Cmd+T, then search for 'Palette Masters'"

uninstall:
	@rm -f $(THEMES_DIR)/palette-masters-*.json
	@echo "Removed all Palette Masters themes from $(THEMES_DIR)"

generate:
	@python3 generate.py
	@echo "Themes regenerated in $(THEMES_DIR)"

list:
	@python3 -c "\
	import json, glob, os; \
	files = sorted(glob.glob('themes/*.json')); \
	[print(t['name']) for f in files for t in json.load(open(f))['themes']]"
