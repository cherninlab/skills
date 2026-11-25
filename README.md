# use-air

[![Skills.sh installs](https://skills.sh/b/cherninlab/skills)](https://skills.sh/cherninlab/skills/use-air)

**use-air** (short name **air**) is an Agent Skill that helps AI agents make every addition earn its place—in UI and UX design, websites, writing, documentation, and software work.

It asks your agent to understand the person’s task, decide what belongs, and develop it with care. Before adding a section, sentence, control, visual detail, or feature, the agent asks: **Does this help the person enough to earn its place?**

[Try use-air](https://skills.cherninlab.com/use-air) · [Read the skill](use-air/SKILL.md) · [Download](https://skills.cherninlab.com/use-air.zip)

## Examples

| Example | Off | Lite | Full | Ultra | Ultra ×2 |
| --- | --- | --- | --- | --- | --- |
| [Five AI tools infographic](examples/01-five-ai-tools/README.md) | <a href="examples/01-five-ai-tools/images/off.png"><img src="examples/01-five-ai-tools/images/off.png" width="128" alt="Off: five AI tools infographic"></a> | <a href="examples/01-five-ai-tools/images/lite.png"><img src="examples/01-five-ai-tools/images/lite.png" width="128" alt="Lite: five AI tools infographic"></a> | <a href="examples/01-five-ai-tools/images/full.png"><img src="examples/01-five-ai-tools/images/full.png" width="128" alt="Full: five AI tools infographic"></a> | <a href="examples/01-five-ai-tools/images/ultra.png"><img src="examples/01-five-ai-tools/images/ultra.png" width="128" alt="Ultra: five AI tools infographic"></a> | <a href="examples/01-five-ai-tools/images/ultra-x2.png"><img src="examples/01-five-ai-tools/images/ultra-x2.png" width="128" alt="Ultra ×2: five AI tools infographic"></a> |

> Ultra ×2 gives the Ultra result one more edit pass with the same Ultra instructions.

## Try it

Install with the [skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add cherninlab/skills --skill use-air air
```

This installs both names. For just the primary name, use `--skill use-air`.

Or give an agent with access to your files this setup prompt:

```text
Install the use-air skill from https://skills.cherninlab.com/use-air/SKILL.md in your skills directory, then activate /use-air full for this conversation.
```

Then give it your task. From this repository, for example:

```text
Build a landing page for ./use-air.
```

The `./use-air` folder is the brief.

You can also [download the ZIP](https://skills.cherninlab.com/use-air.zip) and place its `use-air` folder in your agent’s skills directory. In Codex, use `.agents/skills/use-air/` for a project or `~/.agents/skills/use-air/` for personal use. See the [official installation locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

## Choose a mode

| Include in your prompt | What the agent should do |
| --- | --- |
| `/use-air lite` | Remove clear filler, duplication, and speculative additions. Keep optional elements with a plausible, specific benefit. |
| `/use-air full` | Require a clear contribution to usefulness, convenience, understanding, or the intended experience. This is the default. |
| `/use-air ultra` | Reconsider the core experience and look for a stronger central idea. Apply the strongest scrutiny to weak additions, and fully develop what belongs. |
| `/use-air off` | Suspend Air’s constraints and follow the other instructions normally. |

Every mode keeps the same standard of care. The selected mode stays active in the current conversation until you switch. Both names accept the same modes. For example, `/air ultra` also selects Ultra.

Change modes with your next task:

```text
/use-air ultra
Improve this screen.
```

In Codex, mention the installed skill with `$use-air` or `$air` when both are installed; other agents use their own skill selectors or invocation flow. The mode cues above are instructions for the agent within the conversation.

## When Air helps

- **Designing interfaces and websites:** choose content, layout, typography, color, and motion from the user’s needs. Check the rendered result at the sizes people will use.
- **Writing and documentation:** combine repeated ideas, keep useful detail, and choose a structure that helps the reader follow the thought.
- **Planning and building software:** question features and abstractions added from habit, while preserving the capabilities and convenience the task needs.

A landing page can demonstrate the product before explaining it. A label, heading, and paragraph can become one well-written paragraph. A dense working tool can keep its controls and use better grouping, spacing, and feedback to make them easier to use.

Beauty, atmosphere, character, and delight belong when they serve the experience. The result can be expressive, intricate, or visually rich. Air asks the agent to choose these qualities deliberately and verify the finished work.

## Format and compatibility

Air follows the [Agent Skills format](https://agentskills.io/specification). Agents such as Claude Code, Codex, and Cursor load skills through their supported installation flows. Your agent provides the model, tools, and permissions; Air provides the decision process.

The installable package contains:

```text
use-air/
├── SKILL.md
└── agents/
    └── openai.yaml
```

`SKILL.md` contains the metadata and instructions. `agents/openai.yaml` supplies Codex display metadata.

The `air/` package also works on its own for existing installs. After editing `use-air/`, run `python3 scripts/sync_air_alias.py` to refresh it.

## License

Licensed under the [MIT License](LICENSE).

Copyright (c) 2026 Fedor Chernin
