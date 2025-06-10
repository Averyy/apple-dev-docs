# Fixing issues in your code as you type

**Framework**: Xcode

Minimize typing-related errors using code completion, and let Xcode fix common mistakes for you.

#### Overview

Xcode includes a number of features that help reduce typical coding mistakes, such as when you misspell a symbol name or forget to add a closing delimiter. By leveraging these features, you can focus more time on adding value to your app and less time fixing easily avoidable issues. With your explicit consent, Xcode can help you locate the correct symbol, fix common errors, and automatically match braces, parentheses, and brackets, by directly changing your code.

##### Avoid Syntax Errors By Using Code Completion

When you begin typing the name of a symbol in the source editor, Xcode displays a list of suggestions for completing the name. You can dismiss this list by pressing Escape or clicking elsewhere in the source editor. If the possible completions share a common string, Xcode highlights that string. If there isn’t a common string, Xcode highlights the matching parts of the string instead.

Use the Up Arrow and Down Arrow keys to navigate through the list of possible completions. Alternatively, you can click an item in the list to select it. A selected item displays its description below the list.

![A screenshot of the source editor’s code completion list. One of the symbols is in a selected state and the list displays its description below.](https://docs-assets.developer.apple.com/published/527798ef5628bb2fcb01db1d153e34ca/auto-complete%402x.png)

To insert a suggested completion into your source code, select the item and press Return. You can double-click an item to achieve the same. If you don’t see the desired completion, or the list is too long, continue typing to refine the list of suggestions.

If the inserted symbol contains parameters or arguments, Xcode adds a placeholder for each one. Use the Tab key to cycle through the placeholders, and Shift-Tab to cycle through them in reverse order. Alternatively, you can choose Navigate > Jump to Next Placeholder or Navigate > Jump to Previous Placeholder.

To prevent Xcode from suggesting completions as you type, follow these steps:

1. Choose Xcode > Settings or press Command-Comma.
2. Select Text Editing > Editing.
3. Deselect the “Suggest completions while typing” preference.

Even if you disable automatic suggestions, you can invoke code completion at any time when in the source editor by pressing Control-Space or Escape. The “Use Escape key to show completion suggestions” preference manages the behavior of the Escape key in this context.

##### Match Braces Parentheses and Brackets Automatically

Xcode helps you identify and balance opening and closing delimiters — braces, parentheses, and brackets — within your code. You can take advantage of this functionality by doing one or more of the following:

- Type an opening delimiter and press Return or any character to automatically insert a closing delimiter.
- Type a closing delimiter, or move the insertion point immediately after an existing closing delimiter, to briefly highlight the opening delimiter in the source editor.
- Conversely, move the insertion point immediately after an opening delimiter to temporarily highlight the closing delimiter.
- Move the insertion point between two delimiters and choose Editor > Selection > Balance Delimiters to select those delimiters and the code in between. Alternatively, double-click one of the delimiters to achieve the same.
- Select code in the source editor and type an opening delimiter to automatically enclose the selection in a pair of matching delimiters.

To prevent Xcode from automatically inserting delimiters, follow these steps:

1. Choose Xcode > Settings or press Command-Comma.
2. Select Text Editing > Editing.
3. Deselect the “Automatically insert closing braces” and “Enclose selection in matching delimiters” preferences. If you write code in Objective-C, deselect “Automatically balance brackets in Objective-C method calls” in addition to the other two preferences.

##### Make a Fix It Correction

 is an Xcode feature that offers suggested fixes for syntax errors as you write code. The source editor highlights any issues with a red underline and presents an issue summary and icon. Clicking the icon displays more information about the problem and, in many cases, presents a Fix-It that’ll repair the issue for you.

![A screenshot of an Xcode Fix-It correction, which displays a message about the error that generates it and a possible solution along with a Fix button.](https://docs-assets.developer.apple.com/published/8541ca8e64350ce333fa3e7f0d0e8065/fix-it-correction%402x.png)

> ❗ **Important**: To use Fix-It, you must build your target with either the LLVM or Swift compiler. Fix-It is compatible with Swift, C, Objective-C, and Objective-C++.

To apply a suggested Fix-It correction:

1. Enter code into the source editor, which marks any issues with a red underline and displays a summary of the problem to the right.
2. When a summary appears, click the icon to display a more comprehensive description of the issue, along with any suggested corrections.
3. Click the Fix button to select a correction, and Xcode makes the necessary updates to your source code.

If your source code contains multiple issues, navigate between them by choosing Navigate > Jump to Next Issue or Navigate > Jump to Previous Issue. To dismiss the Fix-It dialog, press the Escape key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/fixing-issues-in-your-code-as-you-type)*