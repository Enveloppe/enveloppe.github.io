---
title: Filepath example 
---

In this file, I add a list of example for the file path settings, edited by your **upload configuration**.

## Folder configuration

### Metadata frontmatter

>[!EXAMPLE] Metadata frontmatter
> - You use `category` in a file with `category: Roleplay/Characters/DND`
> - You set a root folder with `_docs/pages`
> - And you set a default folder on `_docs/draft`
>
>  The final path (in GitHub!) will be: `_docs/pages/Roleplay/Characters/DND`
>
>  But, if you don't set `category`, the path will be `_docs/draft`

### Fixed folder

> [!example] Fixed folder
> - If you set `source` as the default folder, any file will be sent to `your_repo/source`, regardless of its frontmatter key or relative path.
> - If you leave it blank, it will be sent directly to `your_repo`.

### Obsidian Path

> [!example] For a file in `20. Compendium/DND/Monster`
>
> - If you set `source`: the final path will be `source/20. Compendium/DND/Monster`
> - If you leave the default folder blank, the final path will be `20. Compendium/DND/Monster`

> [!example] Removing a subpath
> You can use the folder path modification to designate a subfolder as the "vault" for syncing the repository.
> You need to set the `subpath` in entry and leave empty for the replacement. Don't forget to set the editing on `folder path`!
> - You could plug in `vault/sub` as the path removed.
> - The sync will flow `vault/sub` as `repo`.
> - A file in `vault/sub/folderA` will be synced in `repo/folderA`

## Changing the filename

> [!example] Using a frontmatter key `title`:
> - `title: My title`
> - `filename`: `28-03-2020-1845.md`
> - Final filename: `My title.md`

### Links & folder notes

> [!example] frontmatter example with a file named `folder2`:
>
> - Using a category value: `folder1/folder2`
> - With root value named `docs` ⇒ `docs/folder1/folder2/index.md`
> - Without root: `folder1/folder2/index.md`
> - Without category value, with default folder named `drafts`: `draft/folder2.md` (the name won't be converted!)

> [!example] Example with Obsidian Path & a file named `folder2`:
> With a path like: `folder1/folder2` the new path will be:
> - If you use a default folder named `docs`: `docs/folder1/folder2/index.md`
> - Without: `folder1/folder2/index.md`

### Internal links

> [!example]
> - Cited file: `docs/XX/YY/my_file.md`
> - File to convert: `docs/XX/ZZ/new_file.md`
> - Path created: `../YY/my_file.md`