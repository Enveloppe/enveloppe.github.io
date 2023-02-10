---
title: Upload configuration
---

[You can find some examples of path created by the plugin here](filepath_example.md).

## Folder reception settings

There are three options available for managing folder reception:

- Use a “fixed” folder: All files will be sent to this folder.
- Use a folder created based on a `category` key.
- Use the relative path from Obsidian. You can prepend a folder using the default folder.

In all cases, you will need to configure the **default folder**: The file will be sent here if it doesn't match the other conditions.

> [!note]
> If you use the option for frontmatter, this folder will be the default folder: the file will be sent here if the key doesn't exist.

### Metadata frontmatter

Using the second option will activate two additional options:

- <u>Frontmatter key</u>: The key you want to use in your file.
- <u>Root folder</u>: This option allows you to prepend a path **before** the category key is found (if any key is found!).

### Fixed Folder

When using this option, every file will be sent to the default folder. If the default folder is left blank, the files will be sent to the root of the repository.

### Obsidian Path

This option uses the relative path in your Obsidian vault. The default folder will be prepended before the relative Obsidian path. If left blank, the files will be sent to the root of the repository.

The `path removing` option allows you to remove a specific part of the path created. This can be useful for syncing subfolders. If the removed path is not found, the normal behavior applies.

## Frontmatter title

You can change the filename using a configured frontmatter key, as well as using a regex or a string to change the name.

### Folder note

Some publishing solutions support folder notes, but these notes need to be named `index`. In case you use [Folder Note](https://github.com/aidenlx/alx-folder-note) with [the `same name` strategies](https://github.com/aidenlx/alx-folder-note/wiki/folder-note-pref) you will have a problem, right?
Fortunately, I have a solution for you!

Now, the plugin will convert these files into `index` (or another name) if you activate the settings.

> [!warning] This option doesn't work with fixed folder.

### Workflow

#### GitHub Actions

If your workflow requires activating a GitHub action, set the name of it here. Leave it empty to remove it.

> [!note] The action will be triggered by a `workflow_dispatch` event.

#### Metadata Extractor

It is also possible to send files generated by [metadata extractor](https://github.com/kometenstaub/metadata-extractor) plugins. If you'd like to, just set the folder path where the files must be sent.

> [!warning] Warning:
> 1. This option does not appear if you do not have the plugin installed.
> 2. The function only works on the desktop version (as the plugin `metadata-extractor` is not available on mobile).
> 3. Only the files generated in `.obsidian/plugins` will be sent. The plugin doesn't support sending files from external folders.

#### Auto Clean-Up

You can also set up an “auto-delete” feature when you use the commands to delete files:

- Deleted from your vault
- Which you have stopped sharing ("depublished")

This option will also add a new command to delete files (without sharing the new file) from the remote repository.


> [!warning] Warning[^1]
> You can't use the delete command if you haven't set a default folder (and a root folder if you use the YAML configuration).
> Also, you can lose some files using this command, so be careful!
> Please keep in mind that you can revert commits in case the plugin deletes a file you want to avoid deleting.

> [!warning] Changing the option
> In case you change the folder configuration, the previous files won't be deleted and it may result in errors in this workflow. Be cautious when making changes to the folder configuration, as it can affect the integrity of the files and the overall workflow.

You can set the path of the folder you want to avoid deleting the files. Separate multiple folders with a comma. This will ensure that the files in these specified folders are not deleted even if they are removed from the vault or depublished. It's important to double check the paths to ensure that the right folders are excluded from deletion.

> [!info] Regex
> You can use regex here, but you need to enclose the regex between `/`.
> For example, `/folder1/,/folder2/.*\/subfolder/` will exclude files in the folder1, folder2 and all subfolders under folder2. Be careful when using regex as it can result in unexpected behavior if not written correctly.

Finally, to prevent deleting `index` files created outside of Obsidian, you can use some parameters in your front matter:

- `delete: false`
- `index: true` or by removing the `share` key.

> [!warning] About Per-File Repository:
>
> It's important to keep in mind that when using the per-file repository option, the cleanup commands will only work for the repository set in the settings. However, the auto-cleanup feature will work on the per-file repository during the `Upload single current active note` process.
>
> For attachments, the situation can be a bit tricky as they don't have frontmatter metadata. In these cases, attachments will be deleted in the global repository or in the per-file repository if it's a one file sharing. Be sure to double-check the settings for these files to ensure they are not accidentally deleted.

[^1]: Only file supported by Obsidian will be deleted.