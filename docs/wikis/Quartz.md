---
title: Quartz
---

-> [PRESET](https://github.com/Enveloppe/plugin-presets):

- [YAML based](https://github.com/Enveloppe/plugin-presets/blob/main/presets/quartz-yaml-based.json)
- [Obsidian path based](https://github.com/Enveloppe/plugin-presets/blob/main/presets/quartz-yaml-based.json)

## [Quartz](https://quartz.jzhao.xyz/)

See the official documentation on how to configure Quartz.

For the template, a special template that add a "little" more features is available [here](https://github.com/Enveloppe/Enveloppe-Quartz).

The template includes:

- File and folder icons
- Mobile navigation

> [!tip] You can click on "Sync fork" to get the latest updates from the original repository.

### File & Folder icons configuration

- Use [Iconize Assistant](https://github.com/mara-li/iconize-assistant) to save icon path into the frontmatter of the file.
  > [!note] Iconize icons needs to be accessible by the plugin! I store them into `_assets/PLUGINS/icons`.
- Configure the plugin to send icons file (using override attachment) into `quartz/static/icons` : Replace path of attachment for svg files: `/(_assets\/_PLUGINS\/icons)\/(.*)\/(.*)\.(svg)$/`->`quartz/static/icons/$2/{{name}}`
- Configure the plugin to send file by frontmatter key: `icon_file`
- In the file [quartz.layout.ts], add this:
  ```ts
  const iconsOptions: IconFolderOptions = {
    rootIconFolder: "quartz/static/icons",
    default: {
      file: "file",
    },
  }
  ```
  > [!warning] Don't forget to add the default icon (named `file.svg`) in the `quartz/static/icons` folder.
- Edit `Component.ExlorerBurger()` as follow:
  ```
  Component.ExplorerBurger({
  	//keep your old settings; add only iconSettings
  	iconSettings: iconsOptions,
  }),
  ```
- Edit `Component.ArticleTitle()` as follow: `Component.ArticleTitle(iconsOptions)`

### Mobile navigation

The mobile navigation is instable and rely on a specific layout. Don't change the layout, order, or place of the components.

### Sort order

You can use the frontmatter key `order` to sort the files and folder by number. If not found, the sort order will use the display name.