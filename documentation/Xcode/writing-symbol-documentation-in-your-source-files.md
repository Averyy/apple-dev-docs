# Writing symbol documentation in your source files

**Framework**: Xcode

Add reference documentation to your symbols that explains how to use them.

#### Overview

To help the people who use your API have a better understanding of it, follow the steps in the sections below to add documentation comments to the symbols in your project. DocC compiles those comments and generates formatted documentation that you share with your users. For frameworks and packages, add the comments to the public symbols, and for apps, add the comments to both the internal and public symbols.

For a deeper understanding of how to write symbol documentation, please refer to [`Writing Symbol Documentation in Your Source Files Swift.org`](https://developer.apple.comhttps://www.swift.org/documentation/docc/writing-symbol-documentation-in-your-source-files).

##### Add a Basic Description for Each Symbol

The first step toward writing great documentation is to add single-sentence abstracts or summaries, and where necessary, *Discussion* sections, to each of your public symbols.

Use the Code Actions menu in Xcode to generate a template that you fill out. Control-click the symbol in the source editor and choose Add Documentation from the Code Actions menu.

![A screenshot that shows the placeholder Xcode inserts when you select the Add Documentation menu item.](/images/com.apple.Xcode/quick-help-method-placeholder@2x.png)

Replace the Description placeholder with a summary for the symbol.

> 💡 **Tip**: The Add Documentation action recognizes the type of symbol and generates a template that includes placeholders for all the necessary elements, such as parameters and return values.

After you add a summary, Option-click the symbol to review the changes in Xcode’s Quick Help. It displays the text you add directly below the Summary header.

![A screenshot of Xcode’s Quick Help pop-over displaying a method’s summary above its declaration.](/images/com.apple.Xcode/quick-help-method-summary@2x.png)

Any paragraphs you add appear below the Discussion header in Xcode’s Quick Help, and in the symbol reference page that DocC generates.

After adding a Discussion section, invoke Quick Help to view the updated documentation comment. Alternatively, choose Product > Build Documentation to compile your documentation and open it in the documentation viewer.

![A screenshot of a symbol’s compiled reference page in Xcode’s documentation viewer. The page shows a summary and a Discussion section that includes the content from the symbol’s documentation comment.](/images/com.apple.Xcode/doc-viewer-discussion@2x.png)

##### Describe the Parameters of a Method

For methods that take parameters, document those parameters directly below the summary, or the Discussion section, if you include one. Describe each parameter in isolation. Discuss its purpose and, where necessary, the range of acceptable values.

```swift
/// - Parameters:
///   - food: The food for the sloth to eat.
///   - quantity: The quantity of the food for the sloth to eat.
mutating public func eat(_ food: Food, quantity: Int) throws -> Int {
```

```swift
/// - Parameter food: The food for the sloth to eat.
/// - Parameter quantity: The quantity of the food for the sloth to eat.
mutating public func eat(_ food: Food, quantity: Int) throws -> Int {
```

After you add documentation for a method’s parameters, it appears in Xcode’s Quick Help, and in the symbol reference page that DocC generates when you choose Product > Build Documentation.

![A screenshot of a symbol’s compiled reference page in Xcode’s documentation viewer, which includes a Parameters section. The page displays the content from the symbol’s documentation comment.](/images/com.apple.Xcode/doc-viewer-parameters@2x.png)

##### Describe the Return Value of a Method

For methods that return a value, include a *Returns* section in your documentation comment to describe the returned value.

```swift
/// - Returns: The sloth's energy level after eating.
mutating public func eat(_ food: Food, quantity: Int) throws -> Int {
```

You can see your Returns section in the symbol reference page that DocC generates, as well as in Xcode’s Quick Help.

![A screenshot of Xcode’s Quick Help pop-over, which includes a Returns section below all the other content from the documentation comment.](/images/com.apple.Xcode/returns-section@2x.png)

##### Describe the Thrown Errors of a Method

If a method can throw an error, add a *Throws* section to your documentation comment. Explain the circumstances that cause the method to throw an error, and list the types of possible errors.

```swift
/// - Throws: `SlothError.tooMuchFood` if the quantity is more than 100.
mutating public func eat(_ food: Food, quantity: Int) throws -> Int {
```

The Throws section appears in the symbol’s reference page, in the Quick Help pop-over, and in the Quick Help inspector that you can view using Command-Option-3.

![A screenshot of Xcode’s Quick Help inspector that shows how it displays the documentation comment’s information, highlighting the Throws section.](/images/com.apple.Xcode/quick-help-inspector@2x.png)

## See Also

- [Adding supplemental content to a documentation catalog](adding-supplemental-content-to-a-documentation-catalog.md)
  Include articles and extension files to extend your source documentation comments or provide supporting conceptual content.
- [SlothCreator: Building DocC documentation in Xcode](slothcreator-building-docc-documentation-in-xcode.md)
  Build DocC documentation for a Swift package that contains a DocC Catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/writing-symbol-documentation-in-your-source-files)*