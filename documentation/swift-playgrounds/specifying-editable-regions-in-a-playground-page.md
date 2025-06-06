# Specifying Editable Regions in a Playground Page

**Framework**: Swift Playgrounds

Guide learning by marking code that learners can change or copy forward.

#### Overview

You mark a region of code as editable by surrounding the region with a special comment syntax. You use editable and noneditable regions of code to guide learners to the part of the code they should change while completing the task on a page.

By default, all of the code on a playground page is editable until you add at least one editable region. Marking any region in a playground page as editable locks the rest of the code on the page. For playground pages geared toward beginners, restrict the editable area to a small region to avoid accidental edits that might be difficult to recover from.

##### Mark Inline Editable Areas

You use an inline editable area to let learners edit a small region of code. For example, you might want to progressively disclose how a larger region of code works by first letting a learner experiment with changing a single value or variable to see how it influences the execution of the whole page.

You add an inline editable area by using the special comment expression:

![A diagram showing “/](https://docs-assets.developer.apple.com/published/a28fd46bb1114ace63b637c31e204c6b/specifying-editable-regions-in-a-playground-page-1%402x.png)

The  is text that’s displayed until the learner starts editing and adds their own code. The  is text that represents the default value for the Swift code until the value is edited.

The inline editable area in the example below displays “number of repetitions” until edited, and uses `1` as the initial value for the Swift code.

```swift
var x = 0
for i in 1 ... /*#-editable-code number*/1/*#-end-editable-code*/ {
    x += 5
}
```

When displayed on a playground page, the code from the example above is displayed with the placeholder text in a tappable button that activates editing.

![A screenshot showing the rendered version of the code listing above. ](https://docs-assets.developer.apple.com/published/2c19eb5382306077600467b0df026edf/specifying-editable-regions-in-a-playground-page-2%402x.png)

##### Mark Multiline Editable Areas

You use the same special comment syntax to mark editable areas that span multiple lines.

![None](https://docs-assets.developer.apple.com/published/1fe225e19fb38fb8b5681d1be6b1c6fd/specifying-editable-regions-in-a-playground-page-3%402x.png)

The content you write inside multiline editable areas must be indented to the same level as the surrounding code.

##### Mark Editable Areas with Placeholder Tokens

You can add placeholder tokens to editable areas. Placeholder tokens are rendered as selectable labels and can contain spaces and special characters. You can include the name of any Swift type in a placeholder token to restrict the type of values entered in the editable area.

![Diagram showing placeholder token syntax. The first line shows “<#”, followed by placeholder text, terminated with “#>”. The second like shows “<#T##”, followed by placeholder text, followed by “##”, followed by the type name placeholder, terminated with “#>”. ](https://docs-assets.developer.apple.com/published/d997569d0924f06a8395c824b875150c/specifying-editable-regions-in-a-playground-page-4%402x.png)

Selecting a placeholder on a playground page shows the shortcut bar. Selecting a placeholder with a defined type shows a type-specific popover, if one exists. For example, if a typed placeholder specifies an [`Int`](https://developer.apple.com/documentation/Swift/Int); selecting the placeholder opens the number-entry popover.

The following shows variable declarations with untyped and typed placeholders tokens.

```swift
var untypedLlamaCount = /*#-editable-code*/<#number of llamas#>/*#-end-editable-code*/

var typedLlamaCount = /*#-editable-code*/<#T##number of llamas##Int#>/*#-end-editable-code*/
```

##### Mark Editable Areas As Copyable

You can mark editable areas with an identifier that lets learners reuse code between pages. Mark an editable area as a source area by using the `copy-source(``)` and `end-copy-source` comment syntax. Mark another editable area as a copy destination by using the `copy-destination(``, ``)` comment syntax. Once you’ve marked both the source and destination areas, the code a learner types in the source area becomes available in the destination area if they’ve passed the source page’s assessment.

Copy-source areas depend on information you specify in the playground page’s `Manifest.plist` file’s `CopyCodeSetup` dictionary. Use the following keys and values in the `CopyCodeSet` dictionary to configure a copy-source area:

For more information on configuring a page’s manifest, see [`Specify the Page Name and Metadata`](adding-a-page-to-a-playground-book#Specify-the-Page-Name-and-Metadata.md).

The example below uses a copy-source area named `id1` to arrange the page so that when a learner changes the code in the editable area to a different emoji, such as 🤔, the new emoji replaces the default emoji in copy destinations that reference `id1`.

```swift
// Pick a character
let character: Character = /*#-copy-source(id1)*//*#-editable-code*/"😃"/*#-end-editable-code*//*#-end-copy-source*/

//#-hidden-code
import PlaygroundSupport
PlaygroundPage.current.assessmentStatus = .pass(message: nil)
//#-end-hidden-code
```

The following uses the identifier from the code above to determine which code to copy forward into a copy-destination area.

```swift
let character: Character = /*#-editable-code*//*#-copy-destination("Page1.playgroundpage", id1)*/"😃"/*#-end-copy-destination*//*#-end-editable-code*/
```

## See Also

- [Writing Prose for a Playground Page](writing-prose-for-a-playground-page.md)
  Add comment markers in your Swift code to mark text as prose.
- [Hiding Code from a Playground Page](hiding-code-from-a-playground-page.md)
  Use special Swift comments to hide code from display but continue to run it.
- [Customizing the Completions in the Shortcut Bar](customizing-the-completions-in-the-shortcut-bar.md)
  Guide learners toward a solution by hiding some symbols and showing others.
- [Localizing Code Comments and String Literals](localizing-code-comments-and-string-literals.md)
  In Swift Playgrounds 3.0 and later, mark up code zones to replace them with code that’s localized for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/specifying-editable-regions-in-a-playground-page)*