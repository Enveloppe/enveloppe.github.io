---
title: Mkdocs
---

## Local
### Requirements
- [Python 3.13](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/)

### Local installation
To install and locally test the Mkdocs plugin, you need to follow these steps:
```
pip install uv
uv venv
uv sync
uv run mkdocs serve
```

## Quick installation tutorial

1. Click on [use this template](https://github.com/enveloppe/mkdocs/generate)
1. Use the name of your choice
1. Set and edit the `mkdocs.yml` in the root of the repository. It is possible to use a github action: "generate.yml", that will automatically update the mkdocs.yml.

## Plugin configuration

🆕** Enveloppe 6.1.0** : You can load the settings from the preset using the button "Preset" and selecting `mkdocs` in the selector!

The majority of the settings are optional and help you to manage your repository.

The mandatory settings are :

1. In [[Upload|Upload configuration]] :
   - <u>Folder behavior: </u> YAML frontmatter or Obsidian Path
   - <u>Root folder: </u> `docs`
   - <u>Folder note:</u> `index.md`
   - <u>Excluded files</u> : (_Only if you use the auto-clean up function_) : `docs/assets/js, docs/assets/meta, docs/assets/css, tags.md, graph.md`
1. [[Content|Content's conversion]] :
   - <u>Internal Links : </u> Toggle on
1. Embed files :
   - <u>Transfer attachments:</u>✅
   - <u>Default attachment folder:</u> `docs/assets/img`
     The images must be in the `docs/` folder, but you can change the `assets/img` part as you want.

### Support

- [x] Wiki links (`[[Links]]`)
- [x] File transclusion/embed, both wiki links and markdown links
- [x] Obsidian callout and custom callouts
- [x] Folder notes and their citations
- [x] Custom attributes
- [x] Sharing state and custom folder hierarchies
- [x] Mobile and desktop compatibility
- [x] File mini preview on hover
