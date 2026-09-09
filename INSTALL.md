# Install Kopi

Kopi contains eleven instruction-based skills. Installing it adds workflows; it does
not install Python libraries, connect accounts, provide an MCP server, or grant
access to calendars, files, trackers, or conversation history.

The portable root `plugin.json` supports current Agent Plugins hosts (OpenAI and
Cursor). Claude uses `.claude-plugin/`; the Codex compatibility manifest remains
for older OpenAI hosts. All formats share the same `skills/` directory.

## Get this version

Clone or download this repository, then open a terminal in its root. The commands
below use the local checkout, so they also work before a change is published to
GitHub. Building and validation require Python 3.10 or newer; using the installed
skills does not require Python unless the selected workflow tools need it.

```bash
python3 scripts/validate_pack.py .
python3 scripts/package_plugin.py
```

The builder produces:

- `dist/kopi-0.1.2.zip`: a plugin ZIP with manifests at the archive root.
- `dist/kopi-openai-0.1.2/`: a self-contained local OpenAI marketplace.
- `dist/kopi-openai-0.1.2.zip`: the same marketplace for transfer to another machine.

The build includes only release files and is reproducible. Identical rebuilds
are allowed. For changed contents, bump all manifest versions together or pass
`--output /path/to/a/new-output-directory`; existing different files are not overwritten.

## Claude Code

For a quick session, run from this repository root:

```bash
claude --plugin-dir .
```

For a persistent installation, run these commands **inside Claude Code**, replacing
`/absolute/path/to/kopi` with the checkout's absolute path:

```text
/plugin marketplace add /absolute/path/to/kopi
/plugin install kopi@kopi-plugins
/reload-plugins
```

Run `/kopi:kopi-mode` or `/kopi:decide-architecture`. After these changes are pushed
to GitHub, `/plugin marketplace add alcedo/kopi` can be used instead of the local path.
Do not use that remote command to test unpublished local changes.

## Claude chat, Desktop, and Cowork

Build the plugin ZIP above. In Claude, open **Customize → Plugins**, choose the
custom plugin upload option, and select `dist/kopi-0.1.2.zip`. Use `/` or `+` to
find Kopi's skills. For Cowork, first open the Cowork tab, then Customize.
Plugin availability depends on your plan and organization settings. A plugin
can load in chat while file creation, rendering, or connected-source operations
still require a host with those capabilities.

## ChatGPT Work / Codex

Use the generated OpenAI marketplace, not the standalone plugin ZIP, for the
local installation route. In a terminal at this repository root:

```bash
codex plugin marketplace add ./dist/kopi-openai-0.1.2
```

Restart the desktop app, open the **Plugins Directory**, select **Kopi Local**,
and install **Kopi**. Start a new task with the plugin enabled and ask:
“Use Kopi's kopi-mode to prepare an architecture review.”

If transferring the marketplace ZIP, extract it to a persistent folder first
and add that extracted folder as the marketplace root. Keep it in place after
registration. Local-source support varies by app surface and workspace policy;
a browser-only ChatGPT session may not offer this local route. Workspace or
public distribution uses OpenAI's publishing flow and is separate from building
these files. This repository does not claim a public directory listing.

Kopi is skills-only: do not create an MCP connection or supply an API key to
install it. The `.agents/plugins/marketplace.json` inside the generated bundle
points to `./plugins/kopi`, relative to the marketplace root.

## Cursor

Current Cursor supports the portable root manifest. On macOS or Linux, run these
commands from the repository root to link this checkout as a local plugin:

```bash
mkdir -p "$HOME/.cursor/plugins/local"
kopi_target="$HOME/.cursor/plugins/local/kopi"
if [ -e "$kopi_target" ] || [ -L "$kopi_target" ]; then
  echo "Kopi already exists at $kopi_target; inspect it before replacing it."
else
  ln -s "$PWD" "$kopi_target"
fi
```

These commands leave an existing `kopi` entry untouched. Inspect the
existing plugin before choosing to replace it. On Windows, or if symlinks are
unavailable, extract the plugin ZIP's contents into your user profile's
`.cursor/plugins/local/kopi/` directory. `plugin.json` must be directly inside
that directory, beside `skills/`.

Restart Cursor or run **Developer: Reload Window**, open **Customize**, and check
Kopi's skills. Local plugin imports must be allowed by your organization. An
installed marketplace plugin of the same name takes precedence over a local copy.

## Workflow prerequisites

| Workflow | Capabilities supplied by the host or user |
|---|---|
| Research | Fresh web search and primary-source retrieval |
| Presentations | A presentation skill or file-generation tools, a PPTX renderer, and image inspection |
| Spreadsheets | A spreadsheet skill/application or file tools; a calculation engine when formulas need recalculation |
| Meetings | Calendar connector, identities, time zones and appropriate account access for scheduling |
| Portfolio and recall | In-scope records, uploaded evidence, or connected source/history tools |
| Architecture, review and learning | Relevant source material; these can work from supplied text |
| Performance reviews | Person's role, supplied 360 feedback and self-reflection; goals optional; text is sufficient, file output uses available document tools |

OpenAI presentation/spreadsheet skills and Claude `pptx`/`xlsx` skills are examples
of usable adapters, not mandatory plugin dependencies. If a specific skill is
absent, Kopi may use available equivalent tools. It preserves the same evidence
and verification requirements. Missing creation tools block file creation;
missing rendering or recalculation is reported as incomplete verification on a
draft, never a completed check. Kopi does not install dependencies automatically.

## Check the installation

Start a new conversation with Kopi enabled:

1. Confirm that all eleven skills in the README catalog are available.
2. Ask: “Use Kopi to compare a modular monolith and microservices for a small
   internal tool. Use only these facts: three engineers, one database, one deployment.”
   Confirm it uses `decide-architecture` and its decision-record reference.
3. Request a three-slide PPTX from the same facts. Confirm that it uses available
   host tools and returns a real file, or identifies the exact missing capability.
4. Ask it to analyze a supplied spreadsheet. Check the saved file and calculation
   verification, or the explicitly reported missing capability.
5. Ask for a meeting draft with no invitations sent. Confirm no calendar write occurs.
6. Use `write-performance-review` with fictional feedback and self-reflection.
   Confirm it first shows private evidence tables and numbered ideas, waits for
   your observations/selection, and then produces separate employee and manager
   reports with reviewer attribution confined to the manager copy.

Repository tests validate packaging and resource integrity. They do not prove
that a particular account, app version, or connector can execute every workflow.

## Updates and removal

- Claude Code: update the `kopi-plugins` marketplace, update Kopi through `/plugin`,
  then `/reload-plugins`. Use `/plugin` to uninstall.
- Claude upload: upload the rebuilt ZIP through the plugin management interface;
  verify the new version and start a new conversation.
- OpenAI: build a new version, register its new marketplace root (remove the old
  `kopi-local` source first if the host reports a duplicate), then reinstall/update
  Kopi in the directory and start a new task. Uninstall in the directory before
  removing a local marketplace with `codex plugin marketplace remove kopi-local`.
- Cursor: a symlink follows local checkout changes; reload the window. For an
  extracted copy, replace it deliberately with the new release. Remove the local
  `kopi` symlink or folder and reload to uninstall.

## Official installation references

Checked 2026-09-09; host UI and account availability can change.

- [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference)
- [Claude marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude chat and Cowork plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [OpenAI plugin packaging and local marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Cursor local plugins](https://cursor.com/docs/plugins)
