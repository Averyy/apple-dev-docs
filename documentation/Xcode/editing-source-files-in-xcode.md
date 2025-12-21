# Editing source files in Xcode

**Framework**: Xcode

Use features of the source editor to help you write, navigate, document, and understand code more quickly.

#### Overview

As you write code, you can save time by using code completion and code snippets that Xcode provides for you. Also take advantage of the jump bar and minimap features to navigate quickly around your project files. Then add comments to your code so that you can view them in Quick Help, and generate documentation later.

To get started, select a source file in the Project navigator and Xcode opens it in the source editor on the right.

To configure the project window with multiple editors and assistants, see [`Configuring the Xcode project window`](configuring-the-xcode-project-window.md). To use coding intelligence to generate code, playgrounds, previews, and documentation, see [`Writing code with intelligence in Xcode`](writing-code-with-intelligence-in-xcode.md).

##### Enter Code Using Code Completion

As you type code in the source editor, use code completion to assist with variable and function names. When you use code completion for a method or function with parameters, Xcode provides a placeholder for each parameter that you need to add.

![An Xcode screenshot showing the Project navigator on the left and the source editor on the right with the word Button partially entered and a menu showing the first code completion suggestion selected.](https://docs-assets.developer.apple.com/published/4dc03154ae06c89dcfd7fc80e35e1b77/editing-source-code-completion%402x.png)

To navigate between placeholders, press Tab and Shift-Tab (or choose Navigate > Jump to Next Placeholder and Navigate > Jump to Previous Placeholder, respectively).

In Swift files, predictive code completion offers code suggestions at your insertion point. When you type, or press Enter to go to a new line, Xcode predicts code for that location. For example, if you type `Image` into the source editor, Xcode predicts the rest of the code to finish the statement. When the code-completion text appears at the insertion point, press Tab to add the predictive code-completion suggestion, or press Return to accept the regular code completion.

You can customize or disable code completion by choosing Xcode > Settings > Editing > Completion.

##### Add and Create Reusable Code Snippets

For common code structures, Xcode provides preexisting code snippets you can insert into your code, or you can create your own.

To insert a snippet in your code:

1. Choose View > Show Library.
2. In the library, use the search field at the top and the buttons on the toolbar to filter the snippets.
3. Select a snippet and drag it to the desired location in the source editor.
4. In the source editor, press the Tab and Shift-Tab keys to navigate between placeholders in the snippet.

![An Xcode screenshot of the library with Swift Test entered in the search field at the top, Swift Testing: Suite Struct with Traits selected in the sidebar, and the code snippet with placeholders on the right.](https://docs-assets.developer.apple.com/published/f9e861e73763b97a1e9dffeedb12b980/editing-source-add-code-snippet%402x.png)

To create your own code snippet:

1. Select some code in the source editor for the snippet and Control-click, or Control-click anywhere in the source editor, then choose Create Code Snippet from the contextual menu.
2. In the library that opens, enter a name and summary for your snippet in the form on the right.
3. Edit the code in the snippet below and mark placeholders with `<#placeholder name#>`.
4. Select the language and platform, enter any text to use for code completion, and select the scope.
5. Click Done.

![An Xcode screenshot of the library with a new code snippet selected in the sidebar and a form on the right for entering the snippet’s name, summary, and code.](https://docs-assets.developer.apple.com/published/6160e5ac9bfaad653f3ca7da8f2a8861/editing-source-create-code-snippet%402x.png)

To delete a code snippet that you create, select it in the library sidebar and click Delete.

##### Annotate Your Code for Visibility

The jump bar and the minimap each provide a quick visual way to navigate your code in the source editor. To show the minimap that appears on the right of the source editor, choose Minimap from the Adjust Editor Options menu on the right of the editor toolbar.

Then annotate your code with `MARK`, `TODO`, and `FIXME` comments to enhance the power of these tools when organizing your code.

![An Xcode screenshot of the project window with the Project navigator on the left and the source editor on the right with the jump bar menu and minimap on the right showing the MARK, TODO, and FIXME comments.](https://docs-assets.developer.apple.com/published/abe75fc1944da9a87d2fdffd1c16544c/editing-source-annotate-code%402x.png)

Add a `MARK` comment to add a heading to a section of code. Include a dash in the comment to instruct Xcode to show a divider line before the section in the jump bar and minimap.

```swift
// MARK: Views

/// A view with a toggle button that shows or hides earned badges in a vertical layout.
struct BadgesView: View {
```

Add a `TODO` comment to indicate where you want to do future work. The jump bar highlights the `TODO` comment with an icon for easy identification.

```swift
// TODO: Support new types of badges.
func body(content: Content) -> some View {
```

Add a `FIXME` comment to note where you need to make a fix in your code. The jump bar highlights the `FIXME` comment with a different icon.

```swift
// FIXME: Add hover text over the image.
Image(systemName: badge.symbolName)
```

In addition to the organizational benefits, consistent use of `MARK`, `TODO`, and `FIXME` comments improves your ability to search for common sections, future updates, and needed fixes.

For Objective-C, use the `#pragma mark`, `#pragma fixme`, and `#pragma todo` macros instead.

##### Add Quick Help Comments to Your Code

You can use Quick Help to learn about existing APIs and document your own symbols for yourself or other developers. To view Quick Help, Control-click a symbol and choose Show Quick Help from the contextual menu.

To add Quick Help to symbols in your code, Command-click a symbol declaration without documentation comments and choose Add Documentation. Xcode adds lines of comments, preceded with three slashes (`///`), that have placeholders for a description, parameters, throws, and a return value, depending on the symbol declaration. Update the placeholders using Markup syntax to complete the comments and enable Quick Help for the symbol.

![An Xcode screenshot of the project window with the Project navigator on the left and the source editor on the right with the documentation comments appearing above a function with the first placeholder text selected.](https://docs-assets.developer.apple.com/published/d5b5f1594aca1f293a5a07c82a69ca4d/editing-source-add-documentation%402x.png)

Then, to review your documentation in Quick Help, Control-click the symbol and choose Show Quick Help. Xcode formats and displays the information in your documentation comments.

For more information on writing and distributing documentation of your code, see [`Writing documentation`](writing-documentation.md).

## See Also

- [Running code snippets using the playground macro](running-code-snippets-using-the-playground-macro.md)
  Add playgrounds to your code that run and display results in the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/editing-source-files-in-xcode)*