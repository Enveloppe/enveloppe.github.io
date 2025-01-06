---
title: Developing
order: 7
---

## Plugin development

You can help me develop the plugin using `pnpm`!

1. First, clone the project on your computer with `git clone git@github.com:enveloppe/obsidian-enveloppe.git`
2. `cd obsidian-enveloppe`
3. `pnpm install`
4. Create an `.env` file with the following content:
```env
VAULT=PATH/TO/YOUR/MAIN/VAULT
```
4. `pnpm run dev`
4. Enjoy!

Some notes:

- I use [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/) to generate the commit message, so please respect the format! 
- Don't forget to document your functions!

## Translation or paraphrasing

The plugin uses [i18n](https://www.i18next.com/) to manage translation and UX writing.

To add a new language or rephrase current wording:

- Clone [locales](https://github.com/enveloppe/locales), the dedicated repository for language
- Create the file of the langage you want to translate (for example `es.json` for Spanish) and use the english file (`en.json`) as a base.
- Translate the file, while keeping the `{{variable}}` (you can't translate them)
- Create a pull request on the repository with the new file

>[!info] Test locally 
> You can test locally your translation if you want, but you need to clone the main repository with submodule, have `node` and `pnpm`, run `pnpm i` and run `pnpm run build`, without forget to add the file `main.js` in your `.obsidian/plugin/obsidian-mkdocs-publisher`. Don't forget to reload Obsidian after the copy!

> [!note] Advice
> If you use VSCode or jetbrain editor, you can look at [i18n Ally](https://i18nally.org) to get some useful tool for your translation!

It is also possible to use [Weblate](https://hosted.weblate.org/projects/enveloppe/locales) to translate the plugin!