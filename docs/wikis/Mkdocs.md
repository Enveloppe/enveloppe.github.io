---
title: Mkdocs
---

## [Enveloppe](https://enveloppe.github.io/)

> [!warning] Mkdocs is now deprecated, no support and help will be provided.

### Quick installation tutorial

1. Click on [use this template](https://github.com/enveloppe/mkdocs-publisher-template/generate)
1. Use the name of your choice
1. Set and edit the `mkdocs.yml` in the root of the repository. You can set up this by following the [tutorial here](https://enveloppe.github.io/template/configuration/#mkdocs-configuration)

### Plugin configuration

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

#### Support

- [x] Wiki links (`[[Links]]`)
- [x] File transclusion/embed, both wiki links and markdown links
- [x] Obsidian callout and custom callouts
- [x] Folder notes and their citations
- [x] Custom attributes
- [x] Sharing state and custom folder hierarchies
- [x] Mobile and desktop compatibility
- [x] File mini preview on hover
- [x] Graph view 🎉 (using [obsidiantools](https://github.com/mfarragher/obsidiantools))
