"""Rebuild the standalone air alias from the use-air package."""

from pathlib import Path


root = Path(__file__).resolve().parents[1]
source = root / "use-air"
alias = root / "air"
skill = (source / "SKILL.md").read_text()
_, metadata, instructions = skill.split("---\n", 2)
assert metadata.startswith("name: use-air\n")
(alias / "SKILL.md").write_text(
    "---\nname: air\ndescription: Short name for use-air. "
    "Use when the user invokes $air or /air with an optional mode.\n---\n"
    + instructions
)
ui = (source / "agents/openai.yaml").read_text()
(alias / "agents/openai.yaml").write_text(
    ui.replace('display_name: "use-air"', 'display_name: "air"')
    .replace("$use-air", "$air")
)
