# Adding structure to your documentation pages

**Framework**: Xcode

Make symbols easier to find by arranging them into groups and collections.

#### Overview

By default, when DocC generates documentation for a project, it creates a top-level page that groups the symbols by their kind. For frameworks and packages, DocC includes the public symbols, and for app targets, it includes both the internal and public symbols. You can then provide additional context to explain how your app or framework works and how different symbols relate to each other.

For a more tailored learning experience, use one or more of the following approaches:

- Customize the main landing page for your documentation catalog to introduce your technology and organize its top-level symbols.
- Add symbol-specific extension files that organize nested symbols, such as methods and properties.
- Use collections to group multiple symbols and introduce hierarchy to the navigation of your documentation pages.

For more information about how to use DocC for adding structure to the documentation, see [`Adding Structure to Your Documentation Pages at Swift.org`](https://developer.apple.comhttps://www.swift.org/documentation/docc/adding-structure-to-your-documentation-pages).

##### Customize Your Documentations Landing Page

A  provides an overview of your technology, introduces important terms, and organizes the resources within your  — the files that enrich your source documentation comments. The landing page is an opportunity for you to ease the reader’s learning path, discuss key features of your technology, and offer motivation for the reader to return to when they need it.

![Two side-by-side images of a framework’s top-level page. The image on the left shows the basic empty page that DocC generates by default. The image on the right shows a customized landing page that includes additional content and a color graphic.](https://docs-assets.developer.apple.com/published/a50a02fc4acb28bad8a02a49b9995d77/landing-page%402x.png)

When you add a documentation catalog to your project, Xcode automatically includes an empty landing page. For more information, see [`Documenting apps, frameworks, and packages`](documenting-apps-frameworks-and-packages.md).

If you need to manually add a landing page to your documentation catalog, follow these steps:

1. In Xcode, select your documentation catalog in the Project navigator.
2. Choose File > New > File from Template.
3. Select the Empty template in the Documentation section and click Next.
4. Enter a filename and click Create. Xcode creates a Markdown file that contains only a placeholder for the page title.

![A screenshot of Xcode’s file template chooser with the Empty template in a selected state in the Documentation section.](https://docs-assets.developer.apple.com/published/923c839b16190ba2c307c941acaf21cb/empty-markdown-file%402x.png)

Use a filename that matches the target’s product module name. For example, for the `SlothCreator` framework, the filename is `SlothCreator.md`.

> **Note**: For targets with spaces in the product name, Xcode replaces the spaces with underscores in the product module name. To find the product module name in an Xcode project, select the target in the project editor, click the Build Settings tab, and enter Product Module Name in the search field.

##### Arrange Top Level Symbols Using Topic Groups

By default, DocC arranges the symbols in your project according to their kind. For example, the compiler generates topic groups for classes, structures, protocols, and so forth. You then add information to explain the relationships between those symbols.

To help readers more easily navigate your framework, arrange symbols into groups with meaningful names. Place important symbols higher on the page, and nest supporting symbols inside other symbols. Use group names that are unique, mutually exclusive, and clear. Experiment with different arrangements to find what works best for you.

![Two side-by-side images that show different arrangements of a framework’s top-level symbols. The image on the left shows the basic arrangement that DocC generates by default. The image on the right shows a custom arrangement that includes more descriptive headers and content.](https://docs-assets.developer.apple.com/published/434c99a6e12b1d2313011c2612cefc75/top-level-curation%402x.png)

To override the default organization and manually arrange the top-level symbols in your technology, add a Topics section to your technology’s landing page. Below any content already in the Markdown file, add a double hash (`##`), a space, and the `Topics` keyword.

```markdown
## Topics
```

After the Topics header, create a named section for each group using a triple hash (`###`), and add one or more top-level symbols to each section. Precede each symbol with a dash (`-`) and encapsulate it in a pair of double backticks (``) .

```markdown
## Topics

### Creating sloths

- ``SlothGenerator``
- ``NameGenerator``
- ``Habitat``

### Caring for sloths

- ``Activity``
- ``CareSchedule``
- ``FoodGenerator``
- ``Sloth/Food``
```

DocC uses the double backtick format to create symbol links, and to add the symbol’s type information and summary. For more information, see [`Formatting Your Documentation Content Swift.org`](https://developer.apple.comhttps://www.swift.org/documentation/docc/formatting-your-documentation-content).

When you rebuild your documentation, the documentation viewer reflects these organizational changes in the navigation pane and on the landing page, as the image above shows.

##### Arrange Nested Symbols in Extension Files

Not all symbols appear on the top-level landing page. For example, classes and structures define methods and properties, and in some cases, nested classes or structures introduce additional levels of hierarchy.

As with the top-level landing page, DocC generates default topic groups for nested symbols according to their type. Use extension files to override this default organization and provide a more appropriate structure for your symbols.

![Two side-by-side images that show different arrangements of a symbol’s methods and properties. The image on the left shows the basic arrangement that DocC generates by default. The image on the right shows a custom arrangement that includes more descriptive headers and content.](https://docs-assets.developer.apple.com/published/d6830d5a3171e99c56198bd5508a3281/child-curation%402x.png)

To add an extension file to your documentation catalog for a specific symbol, do the following:

1. In Xcode, select your documentation catalog in the Project navigator.
2. Choose File > New > File from Template.
3. Select the Extension File template in the Documentation section and click Next.
4. Enter the symbol name as the filename and click Create.

![A screenshot of Xcode’s file template chooser with the Extension File template in a selected state in the Documentation section.](https://docs-assets.developer.apple.com/published/0f0de2bc8921361b053edd373c693422/template-chooser%402x.png)

In the extension file, replace the `Symbol` placeholder with the absolute path to the symbol. The absolute path is the target’s product module name followed by the symbol name.

```markdown
# ``SlothCreator/Sloth``
```

The Extension File template includes a `Topics` section with a single named group, ready for you to fill out. Alternatively, if your documentation catalog already contains an extension file for a specific symbol, add a `Topics` section to it by following the steps in the previous section.

As with the landing page, create named sections for each topic group using a triple hash (`###`), and add the necessary symbols to each section using the double backtick (``) syntax.

```markdown
# ``SlothCreator/Sloth``

## Topics

### Creating a sloth

- ``init(name:color:power:)``
- ``SlothGenerator``

### Activities

- ``eat(_:quantity:)``
- ``sleep(in:for:)``

### Schedule

- ``schedule``
```

> 💡 **Tip**: Use a symbol’s full path to include it from elsewhere in the documentation hierarchy.

After you arrange nested symbols in an extension file, choose Product > Build Documentation to compile your changes and review them in Xcode’s documentation viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-structure-to-your-documentation-pages)*