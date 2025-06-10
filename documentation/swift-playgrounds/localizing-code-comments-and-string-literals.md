# Localizing Code Comments and String Literals

**Framework**: Swift Playgrounds

In Swift Playgrounds 3.0 and later, mark up code zones to replace them with code that’s localized for the current user.

#### Overview

If you’re writing a playground book for distribution in multiple locales, you can localize the comments and string literals on each page using a comment syntax that delimits a zone for localization.

##### Add Localization Delimiters

Specify the code you want to make localizable by wrapping it within a delimiter; for example:

```swift
/*
//#-localizable-zone(welcome1)
Welcome!
//#-end-localizable-zone
*/
```

Each delimiter carries a unique  (for example, `welcome1`, `welcome2`, and so forth) that matches an entry in the `LocalizableCode.strings` file you define for each page.

You can also use inline comment delimiters to make string literals localizable; for example:

```swift
let message = "/*#-localizable-zone(welcome2)*/Hello!/*#-end-localizable-zone*/"
```

> ❗ **Important**: Only use localization delimiters to surround code comments and string literals. Doing so helps ensure that you don’t introduce locale-sensitive compilation errors.

##### Create a Localization Strings File

When a user opens a page in your book, the system looks in the appropriate language directory (for example, the page’s `PrivateResources/de.lproj` directory for strings localized in German) for the `LocalizableCode.strings` file. It then matches the delimeters with their corresponding zone ID, and substitutes the text string in the page with the localized text.

Format localization strings files as a list of localization identifiers followed by the localized string. The following example defines localized forms of the content identified by `welcome1` and `welcome2`:

```other
/* Initial greeting. */
"welcome1" = "Willkommen!";

/* Second greeting. */
"welcome2" = "Guten Tag!";
```

Localized versions of comments and strings appear on devices set to the appropriate locale:

```swift
/*
Willkommen!
*/

let message = "Guten Tag!"
```

## See Also

- [Writing Prose for a Playground Page](writing-prose-for-a-playground-page.md)
  Add comment markers in your Swift code to mark text as prose.
- [Specifying Editable Regions in a Playground Page](specifying-editable-regions-in-a-playground-page.md)
  Guide learning by marking code that learners can change or copy forward.
- [Hiding Code from a Playground Page](hiding-code-from-a-playground-page.md)
  Use special Swift comments to hide code from display but continue to run it.
- [Customizing the Completions in the Shortcut Bar](customizing-the-completions-in-the-shortcut-bar.md)
  Guide learners toward a solution by hiding some symbols and showing others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/localizing-code-comments-and-string-literals)*