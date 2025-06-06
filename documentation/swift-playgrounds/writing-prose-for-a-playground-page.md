# Writing Prose for a Playground Page

**Framework**: Swift Playgrounds

Add comment markers in your Swift code to mark text as prose.

#### Overview

Playground pages almost always need prose to introduce the concepts you’re teaching on the page. You use a special kind of Swift comment to mark single lines or blocks of text as prose. When a playground page’s `main.swift` file is displayed in Swift Playgrounds, comments marked as prose are displayed using a proportional font.

##### Add Single Line Prose

To add short sections of prose to a page, write a single-line Swift comment that starts with a colon (`//:`).

```swift
//: This line contains a short sentence.
```

Comments without the colon are treated as normal Swift comments and are displayed in a monospace font. Text that’s outside of any sort of comment is treated as Swift code and runs when you tap Run My Code.

You can use markup in prose to add semantic treatments like emphasis and code voice. For information on supported markup, see [`Markup Formatting Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html#//apple_ref/doc/uid/TP40016497).

##### Add Multiline Prose

Use multiline Swift comments for longer passages. You indicate that a multiline comment is prose by adding a colon immediately after the comment’s starting delimiter (`/*:`).

```swift
/*:
    Roses are `UIColor.red`,
    Violets are 🔵,
    Swift Playgrounds are rad,
    and so are you!
*/
```

You don’t need to use a special delimiter to close the comment; use the regular comment closing syntax (`*/`) to finish a multiline prose block.

##### Reference Localized Prose

Localize the content on a page by using the special comment syntax: `//:#localized(key: ``)`. The  key must correspond to an entry in the playground page’s `Prose.strings` file for each localization folder in the PrivateResources folder.

In the following example, the `ExplanationOfLoops` key refers to localized prose in a page’s `Prose.strings` file, in the en.lproj folder under PrivateResources.

```swift
//:#localized(key: "ExplanationOfLoops")
```

Strings files (localization files with names ending in `.strings`) contain multiple key-value pairs, where the key is a phrase you use to identify a block of localized prose, and the value is the localized prose.

The example below shows an English localization of `ExplanationOfLoops`.

```swift
/* An intro to loops. */
"ExplanationOfLoops"="Use loops to repeat an action multiple times until a condition is met.";
```

The rendered playground page shows the text “Use loops to repeat an action multiple times until a condition is met.” If you provide multiple localizations of your playground book, the text displayed is matched to the locale chosen on the learner’s iPad.

Strings files are a common format used for several kinds of localization and internationalization tasks. For more information about formatting strings files, see [`String Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6) and [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

## See Also

- [Specifying Editable Regions in a Playground Page](specifying-editable-regions-in-a-playground-page.md)
  Guide learning by marking code that learners can change or copy forward.
- [Hiding Code from a Playground Page](hiding-code-from-a-playground-page.md)
  Use special Swift comments to hide code from display but continue to run it.
- [Customizing the Completions in the Shortcut Bar](customizing-the-completions-in-the-shortcut-bar.md)
  Guide learners toward a solution by hiding some symbols and showing others.
- [Localizing Code Comments and String Literals](localizing-code-comments-and-string-literals.md)
  In Swift Playgrounds 3.0 and later, mark up code zones to replace them with code that’s localized for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/writing-prose-for-a-playground-page)*