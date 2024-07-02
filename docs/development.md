# Development Guide

## Working with Symlinks

Identical copies of some of the content maintained in this repository is published in multiple forum topics. In order to avoid the need to maintain duplicated content in this repository, a single asset is used, with a [symbolic link](https://wikipedia.org/wiki/Symbolic_link) (AKA "symlink") to the asset placed in each of the locations in the category content tree ([example](../content/categories/community/general-discussion/_topics/how-to-get-the-best-out-of-this-forum)).

For certain development operations, it might be necessary to work with the repository's existing symlinks or add new ones.

---

**ⓘ** If your local development work does not involve the project's symlinks, no action is required and you can skip the rest of this section.

---

### Linux or macOS

The Linux and macOS operating systems support symlinks by default so no preparation is required of contributors using these operating systems.

<a name="enable-windows-symlinks"></a>

### Windows

Windows supports symlinks, but by default support for creating symlinks is only available in administrative sessions (e.g., application used to work with the symlinks invoked via "**Run as administrator**").

Windows can be configured to allow creating symlinks even from non-administrative sessions:

https://learn.microsoft.com/windows/apps/get-started/enable-your-device-for-development

#### Git

If a repository is [cloned](https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository) when **Git** does not have the privileges needed to create symlinks, it will create placeholder text files in place of the symlinks. The content of the text file is the path to the symlink's target.

This behavior is controlled by **Git**'s [`core.symlinks` configuration variable](https://git-scm.com/docs/git-config/#Documentation/git-config.txt-coresymlinks). The variable will be set to `false` in the repository's [local configuration](https://git-scm.com/docs/git-config/#Documentation/git-config.txt-GITDIRconfig).

This behavior doesn't pose any problems if your development work won't involve the project's symlinks (the placeholders files for the existing symlinks are not treated as a [repository diff](https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-comparing-branches-in-pull-requests)), but will not be appropriate when you are working with the symlinks since we must commit functional symlinks rather than the placeholder files.

Even when the necessary privileges are present, the fallback behavior will be used when cloning the repository if `core.symlinks` is set to `false` in your [system](https://git-scm.com/docs/git-config/#Documentation/git-config.txt-prefixetcgitconfig) or [global](https://git-scm.com/docs/git-config/#Documentation/git-config.txt-XDGCONFIGHOMEgitconfig) **Git** configuration. You can check the value of the configuration variable by running this command:

```text
git config --get --show-origin --show-scope core.symlinks
```

And if it is set to `false`, you can change the value to `true` with this command:

```text
git config --global core.symlinks true
```

#### Git Bash

Contributors using Windows are recommended to use the excellent open source [**Git Bash**](https://gitforwindows.org/#bash) shell (installed as part of [**Git for Windows**](https://git-scm.com/download/win)).

If you have not [configured Windows](#enable-windows-symlinks) to provide default support for symlinks, an [additional configuration](https://cygwin.com/cygwin-ug-net/using-cygwinenv.html#:~:text=winsymlinks%3Anative%20and-,winsymlinks%3Anativestrict,-is%20this%3A%20If) of the shell is required in addition to using an administrative session. You can configure the current session to support creation of symlinks by running this [`export`](https://www.man7.org/linux/man-pages/man1/export.1p.html) command:

```text
export MSYS=winsymlinks:nativestrict
```

---

**ⓘ** This additional configuration is not required if you are using Windows [**PowerShell**](https://learn.microsoft.com/powershell/scripting/learn/ps101/01-getting-started) instead of **Git Bash**.

---

## Add or Remove a Pinned Topic

"Pinned" topics are always shown at the top of the category's listing.

1. Find the category for the pinned topic under [the `content/categories` folder](../content/categories).
1. Open the `_pins.md` file you find there.
1. Add or remove the URL of the topic to the list.
1. Save the file.
1. Submit a [pull request](contributor-guide/pull-requests.md) for the change.

## Change the Description of a Category

The content of the "**About the \_\_\_\_\_ category**" topics is used as the category description in the category listings. This description helps the users to understand whether the category is the appropriate place for a topic they are creating.

1. Find the category for the pinned topic under [the `content/categories` folder](../content/categories).
1. Open the `_topics` subfolder.
1. Find the subfolder for the category's "**About the \_\_\_\_\_ category**" topic is used as the category description in the category listings.
1. Open the `1.md` file from the subfolder.
1. Make the desired changes to the content of the file.
1. Save the file.
1. Submit a [pull request](contributor-guide/pull-requests.md) for the change.

## Reorder Categories

The forum software is configured to show categories in a specific order in the category listings. Changes to this order can be made by the following procedure:

1. Open the (`content/categories/order.md`)[./content/categories/order.md) file in a text editor.
1. Make the desired changes to the order of the categories listed in the file.
1. Save the file.
1. Submit a [pull request](contributor-guide/pull-requests.md) for the change.

---

**ⓘ** The forum contains some categories that are only accessible to staff members (either due to being archived obsolete content or only of use to staff). Those categories will not be visible on the forum website when not logged into a forum account with staff privileges.

---

## Add or Edit a Discourse Template

["Discourse Templates"](https://meta.discourse.org/t/discourse-templates/229250) provide standardized reusable content for common posts.

Templates are used in posts by clicking the **⚙** icon on the post composer toolbar and then selecting "**Insert template**" from the menu.

---

❗ The Discourse Templates feature is only available for staff members (moderators and administrators).

---

### Add Template

The [existing templates](../content/categories/templates/_topics) will serve as a reference for the addition of new template source content.

1. Open [the `content/categories/templates/_topics` folder](../content/categories/templates/_topics).
1. Create a folder named according to the template title.
1. Create a file named `README.md`.
1. Add the template title as an H1 [heading](https://www.markdownguide.org/basic-syntax/#headings). <br />
   For example:
   ```markdown
   # Some Amazing Template
   ```
   **ⓘ** This will be the title shown in the "**Insert template**" interface on the forum.
1. Save the file.
1. Create a file named `1.md`.
1. Add the template text to the file.
1. Save the file.
1. Submit a [pull request](contributor-guide/pull-requests.md) for the change.

### Edit Template

1. Open [the `content/categories/templates/_topics` folder](../content/categories/templates/_topics).
1. Find the folder of the template you want to edit.
1. If you want to edit the template title, open the `README.md` file and edit the text of the H1 [heading](https://www.markdownguide.org/basic-syntax/#headings). <br />
   For example:
   ```markdown
   # Some Amazing Template
   ```
1. If you want to edit the template text, open the `1.md` file and edit the text.
1. Save the file.
1. Submit a [pull request](contributor-guide/pull-requests.md) for the change.

## Add an Asset Topic

New asset topics can be added to the repository to enable collaborative development and maintenance of its content.

---

❗ In order to allow maintenance to continue in perpetuity, ownership of all posts maintained in this repository must be transferred to the forum's `@system` user.

---

1. Find the category for the topic under [the `content/categories` folder](../content/categories).
1. Open the `_topics` subfolder.
1. Create a folder named according to the topic title.
1. Create a file named `README.md`.
1. Add the topic title as an H1 [heading](https://www.markdownguide.org/basic-syntax/#headings). <br />
   For example:
   ```markdown
   # Some Valuable Topic
   ```
1. If the topic is already published on Arduino Forum, add the URL under a `## Published At` heading.
   For example:

   ```markdown
   ## Published At

   https://forum.arduino.cc/t/some-valuable-topic/1234
   ```

1. Save the file.
1. Create a file named `1.md`.
1. Add the post text to the file.
1. Save the file.
1. Repeat steps (8)-(10) for any additional asset posts in the topic (naming the file according to the post number).
1. Submit a [pull request](contributor-guide/pull-requests.md) for the change.

## Validating Your Work

When you submit a pull request to the repository, automated checks will run to detect any problems or inconsistencies. It is possible to also run these checks locally during the development if you like.

### Prerequisites

The following development tools must be available in your local environment:

- [**Task**](https://taskfile.dev/installation/)
- [**Node.js**](https://nodejs.dev/en/download/)
- [**Python**](https://www.python.org/downloads/)
- [**Poetry**](https://python-poetry.org/docs/#installation)

### Running Checks

Execute the following command from the root of the repository to run all available checks:

```text
task check
```

If you prefer to run specific checks individually, run the `task` command to get a list of available tasks.

### Automatic Corrections

Tools are provided to automatically bring the project into compliance with some of the required checks.

Execute the following command from the root of the repository to run all available corrections:

```text
task fix
```

If you prefer to run specific correction operations individually, run the `task` command to get a list of available tasks.
