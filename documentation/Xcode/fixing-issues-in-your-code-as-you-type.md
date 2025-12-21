# Fixing issues in your code as you type

**Framework**: Xcode

Minimize typing-related errors using code completion, and let Xcode fix common mistakes for you.

#### Overview

Xcode includes a number of features that help reduce typical coding mistakes, such as when you misspell a symbol name or forget to add a closing delimiter. By leveraging these features, you can focus more time on adding value to your app and less time fixing easily avoidable issues. With your explicit consent, Xcode can help you locate the correct symbol, fix common errors, and automatically match braces, parentheses, and brackets, by directly changing your code.

##### Avoid Syntax Errors By Using Code Completion

When you begin typing the name of a symbol in the source editor, Xcode displays a list of suggestions for completing the name. You can dismiss this list by pressing Escape or clicking elsewhere in the source editor. If the possible completions share a common string, Xcode highlights that string. If there isn’t a common string, Xcode highlights the matching parts of the string instead.

Press the Up Arrow and Down Arrow keys to navigate through the list of possible completions. Alternatively, you can click an item in the list to select it. Xcode displays a description of the selected item below the list.

![An Xcode screenshot of the Project navigator on the left and the source editor on the right showing the completion list with a symbol selected and a description of it below.](https://docs-assets.developer.apple.com/published/1ea9b42ad35ff3923b3b954b42f05416/auto-complete%402x.png)

For initializers with multiple signatures, click the disclosure triangle on the right to see the variations below.

To insert a suggested completion into your source code, select the item and double-click it or press Return. If you don’t see the desired completion, or the list is too long, continue typing to refine the list of suggestions.

If you insert a method or function with parameters, Xcode provides a placeholder for each parameter that you need to add. To navigate between placeholders, press Tab and Shift-Tab (or Navigate > Jump to Next Placeholder and Navigate > Jump to Previous Placeholder).

To prevent Xcode from suggesting completions as you type:

1. Choose Xcode > Settings (or Command-Comma).
2. Select Editing in the sidebar and then select Completion on the right.
3. From the “Display code completions while typing” pop-up menu, choose Never.

Alternatively, invoke code completion as needed by choosing On Demand and pressing Control-Space or Escape while typing. You can change the shortcut for code completion in Xcode > Settings > Shortcuts.

##### Match Braces Parentheses and Brackets Automatically

Xcode helps you identify and balance opening and closing delimiters — braces, parentheses, and brackets — within your code. You can take advantage of this functionality by doing one or more of the following:

- Type an opening delimiter and press Return or any character to automatically insert a closing delimiter.
- Type a closing delimiter, or move the insertion point immediately after an existing closing delimiter, to briefly highlight the opening delimiter in the source editor.
- Conversely, move the insertion point immediately after an opening delimiter to temporarily highlight the closing delimiter.
- Move the insertion point between two delimiters and choose Editor > Selection > Balance Delimiters to select those delimiters and the code in between. Alternatively, double-click one of the delimiters.
- Select code in the source editor and type an opening delimiter to automatically enclose the selection in a pair of matching delimiters.

To prevent Xcode from automatically inserting delimiters:

1. Choose Xcode > Settings, then select Editing in the sidebar.
2. Toggle the “Automatically insert closing braces” and “Enclose selection in matching delimiters” settings off.

##### Apply Fixes to Your Code

As you enter code in the source editor, Xcode checks the syntax and offers fixes when you pause typing.

Xcode highlights issues with a red underline and presents an issue summary and icon. Clicking the icon displays more information about the issue and, in many cases, provides a fix that you can apply.

![An Xcode screenshot showing the Issues navigator on the left and the source editor on the right with more information about three issues.](https://docs-assets.developer.apple.com/published/08b7176c0b276a59f08d4836e5f83173/fix-it-correction%402x.png)

To apply a fix for an issue:

1. Click the icon on the right of the issue summary.
2. In the popover, click the Apply button on the right of the fix that you want to make.

If the popover contains multiple issues, navigate between them using the Up Arrow and Down Arrow keys (or Navigate > Jump to Next Issue and Navigate > Jump to Previous Issue). To dismiss the popover, press the Escape key or click anywhere else.

You can configure the appearance and behavior of issues that appear in the source editor in Xcode > Settings > General under Issues. For example, to turn off fix suggestions, toggle the “Show live issues” setting off.

If you set up coding intelligence, you can click the Generate button that appears at the bottom of the popover to fix the issues. See [`Writing code with intelligence in Xcode`](writing-code-with-intelligence-in-xcode.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/fixing-issues-in-your-code-as-you-type)*