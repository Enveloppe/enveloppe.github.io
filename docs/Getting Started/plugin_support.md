---
title: Supported, unsupported and other useful plugins
order: 5
---

## Supported plugins

### [Dataview](https://github.com/blacksmithgu/obsidian-dataview)

Dataview is supported and transformed into Markdown by the plugin. However there are some problems with Dataview I can't fix. Moreover, I can't update the API properly (see [obsidian-dataview/issue#2080](https://github.com/blacksmithgu/obsidian-dataview/issues/2080)).

Not only that, Dataview seems to be in maintenant mode and will be replaced by [Datacore](https://github.com/blacksmithgu/datacore/). Therefore, I will not fix the problems with Dataview until Datacore or a proper way to update Dataview is released.

Some known bugs:

- `0` will be transformed into empty string
- `dv.paragraph` with collapside callout in it.

### [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin)

`.excalidraw` files will be exported natively into `svg` file, you don't need to export the file manually.

## Unsupported plugin (for now)
### [Metabind](https://github.com/mProjectsCode/obsidian-meta-bind-plugin)

For the moment, Metabind doesn't allow to export to Markdown. You can [make an FR on the official repository](https://github.com/mProjectsCode/obsidian-meta-bind-plugin) to allow it.

## Other useful plugins

- [Metacopy](https://github.com/mara-li/obsidian-metacopy)
- [Commander](https://github.com/phibr0/obsidian-commander)
- [Folder Note](https://github.com/LostPaul/obsidian-folder-notes)

> [!warning] Some of the information presented here may not be up to date.

### Metacopy

Using [metacopy](https://github.com/mara-li/obsidian-metacopy), you can quickly copy a link to a shared page. To create a link, you need to configure:

1.  `category` in `key`
2.  Add your `set_url` in `base link`
3.  Add `category` in `key link`

You can also remove metacopy from the file menu using a key, so you can activate metacopy only for `share: true`. Metacopy support also folder note.

The final configuration of metacopy will be:
![](./img/metacopy3.png)
![](./img/metacopy2.png)

In the end, a menu will appear on files with `share: true` and a configured `category`. This menu is on the left-click and the file menu. You can quickly copy a link from there, like a Google or Notion sharing link!
