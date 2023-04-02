# Development Guide

## Add or Remove a Pinned Topic

"Pinned" topics are always shown at the top of the category's listing.

1. Find the category for the pinned topic under [the `content/categories` folder](../content/categories).
1. Open the `_pins.md` file you find there.
1. Add or remove the URL of the topic to the list.
1. Save the file.
1. Submit a [pull request](contributor-guide/pull-requests.md) for the change.

## Change the Description of a Topic

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
