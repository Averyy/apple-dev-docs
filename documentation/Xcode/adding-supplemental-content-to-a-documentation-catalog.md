# Adding supplemental content to a documentation catalog

**Framework**: Xcode

Include articles and extension files to extend your source documentation comments or provide supporting conceptual content.

#### Overview

The process of crafting great documentation is an art. Your content is unique; you know which elements, beyond source documentation comments, provide the most value to your readers. For information about adding supplemental content to a documentation catalog with DocC, see [`Adding Supplemental Content to a Documentation Catalog Swift.Org`](https://developer.apple.comhttps://www.swift.org/documentation/docc/adding-supplemental-content-to-a-documentation-catalog).

##### Add Articles to Explain Concepts or Describe Tasks

If your documentation catalog includes an article file with the name `GettingStarted.md`, Xcode displays this article in the documentation viewer with a document icon.

![A screenshot of the Xcode documentation viewer that shows the Getting started with sloths article in a selected state in the Project navigator on the left. The pane on the right displays the article page with a document icon. ](https://docs-assets.developer.apple.com/published/109d7b40f073542e0f9b6202a798c46a/adding-supplemental-content-to-a-documentation-catalog-1%402x.png)

The structure of an article is similar to symbol files or a top-level landing page, with the exception that the first level 1 header is regular content instead of a symbol reference. For example, the Getting Started with Sloths article contains the following title, single-sentence abstract or summary, and Overview section:

```markdown
# Getting started with sloths

Create a sloth and assign personality traits and abilities.

## Overview

Sloths are complex creatures that require careful creation and a suitable
habitat.
...
```

After the Overview section, additional sections and subsections use a double hash (##) for a level 2 header, and a triple hash (###) for a level 3 header. Follow the hashes with a space, and then the title for that section or subsection.

To add an article to your documentation catalog in Xcode, do the following:

1. Select your documentation catalog in the Project navigator.
2. Choose File > New > File from Template.
3. Select the Article File template in the Documentation section and click Next.
4. Enter a filename and click Create. Xcode creates a new article file with a default name.
5. Modify the first line of the file to specify its title.
6. Replace the summary and placeholders in the file with appropriate content.

![A screenshot that shows the Xcode file template chooser with the Article File template in a selected state.](https://docs-assets.developer.apple.com/published/6f5277c5bdf3c4dcb28fcd1baf63d041/adding-supplemental-content-to-a-documentation-catalog-2%402x.png)

##### Add Extension Files to Append to or Override Source Documentation Comments

DocC supports supplementing or completely replacing source documentation comments with content in extension files. To add an extension file to your documentation catalog, do the following:

1. In Xcode, select your documentation catalog in the Project navigator.
2. Choose File > New > File from Template.
3. Select the Extension File template in the Documentation section and click Next.
4. Enter the symbol name as the filename and click Create.
5. Modify the first line of the file to identify the symbol that the file relates to.

In the extension file, replace the `Symbol` placeholder with the absolute path to the symbol. The absolute path is the target’s product module name followed by the symbol name.

![A screenshot that shows the Xcode file template chooser with the Extension File template in a selected state.](https://docs-assets.developer.apple.com/published/67a08fbc893ce8a92ff05e6c6896ab4a/adding-supplemental-content-to-a-documentation-catalog-3%402x.png)

## See Also

- [Writing symbol documentation in your source files](writing-symbol-documentation-in-your-source-files.md)
  Add reference documentation to your symbols that explains how to use them.
- [SlothCreator: Building DocC documentation in Xcode](slothcreator-building-docc-documentation-in-xcode.md)
  Build DocC documentation for a Swift package that contains a DocC Catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-supplemental-content-to-a-documentation-catalog)*