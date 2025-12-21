# Finding and refactoring code

**Framework**: Xcode

Search your code for text, patterns, and symbols that you can refactor quickly and easily.

#### Overview

When writing and analyzing code, you frequently need to look up a symbol to learn how to use it and to determine how other code uses it. Use Xcode’s search capabilities to find text and symbols in your code to analyze potential changes, determine current functionality, or debug code.

Rename files or symbols to clarify usage with a more descriptive and meaningful name. Refactor your code when you identify duplicate code or code that you can reuse. Transform existing code into more reusable functions, methods, or variables.

##### Find Files By Name or Included Symbols

Open a file quickly by pressing Shift-Command-O to bring up the Open Quickly dialog. Type in part of a filename or symbol name, and the dialog presents a list of potential matches.

![An Xcode screenshot showing the Open Quickly dialog with a search term and matches. The match results include files and structures.](https://docs-assets.developer.apple.com/published/4b384ad5acffa1467a6d73cbd1fd1c5d/finding-and-refactoring-open-quickly%402x.png)

Select an item from the search results to open it and navigate to the matched file or symbol. If the file is already open in a tab, Xcode switches to that tab; otherwise, Xcode opens the file in a new tab.

When there are a lot of files in your project, type part of the filename into the Filter field at the bottom of the Project navigator. Xcode displays matching group names and filenames with their parent groupings so you can easily see their locations in your project.

![An Xcode screenshot showing the Project navigator with a search term in the filter field, and matching files displayed and highlighted in the list above.](https://docs-assets.developer.apple.com/published/3f5ca9a121883a0c6d6a19e69b4c7218/finding-and-refactoring-project-navigator-filter%402x.png)

##### Find Text or Patterns in Your Source Code

To find text in a file, open the file in the Xcode source editor and choose Find > Find from the menu bar (or press Command-F). Xcode displays the Find bar and its search controls at the top of the file.

![An Xcode screenshot showing the Find bar above the source code editor with a search term entered. The source editor displays several highlighted matches to the search term.](https://docs-assets.developer.apple.com/published/3f81258dc8a8af10eb120c771fbb948b/finding-and-refactoring-find-bar%402x.png)

Enter a search term. Xcode searches the file, highlights matches, and notes how many it finds. Refine your search using the following options:

- Click the Find Options menu on the left to display options to replace text, run recent searches, or clear recent search history.
- Click the Insert Pattern button (+) to include tabs, line breaks, or special characters in your search term.
- Toggle the Case Sensitive button to indicate whether you want Xcode to match the case of your search term.
- Click the Match Style button to customize how Xcode looks for your search term in your source code.
- Navigate between matches using the arrow buttons.
- Close the Find bar by clicking the Done button.

##### Find Symbols in Your Source Code

To find a symbol in your code, Control-click the variable or function name, and choose Find > Find Selected Symbol in Workspace.

![An Xcode screenshot showing the Find navigator with a symbol entered in the search field and matches below.](https://docs-assets.developer.apple.com/published/0c099d9a96ef9a75f69f05765eedeff5/finding-and-refactoring-find-navigator%402x.png)

Xcode displays the declaration of the symbol in the Find navigator, along with any places where your code references the symbol below.

Alternatively, open the Find navigator and choose Symbols from the Find pop-up menu at the top. In the search field below, enter part of a symbol name and press Return.

Refine your Symbols search using the following options:

- Choose Find or Replace.
- Choose what you want to search for: text, symbol references, symbol definitions, text that matches regular expressions, or call hierarchy.
- Select a match style to customize how Xcode looks for your search term.
- Click the magnifying glass icon to view recent searches.
- Customize the scope of your search: in your project, or in any groups/folders inside your project. If you’re using a workspace, you can search across the workspace, or inside a project.
- Select Ignoring Case or Matching Case.

If your search returns a large number of matches, narrow the results by entering another term in the Filter field.

##### Rename Symbols Throughout Your Project

To rename a function, method, class, structure, or enumeration in your project, Control-click either the declaration of the symbol or a use of the symbol, and choose Refactor > Rename. Xcode highlights the symbol, searches your project for its name, and shows everywhere that the symbol appears.

![An Xcode screenshot showing the rename view for the example class named Landmark. The view is highlighting the class name in several places in a few files, and the focus is set on an instance where a person can type in an updated class name.](https://docs-assets.developer.apple.com/published/cfed4d66555e8072fd6fe002890a9b77/finding-and-refactoring-rename-symbol%402x.png)

Type a new name into the highlighted selection and Xcode previews all the changes. Click a proposed renaming instance to toggle whether Xcode renames it. Click Rename to complete the changes, or Cancel to not make the changes.

To rename a local variable or instance variable, Control-click the variable and choose Edit All in Scope. Xcode highlights instances of the variable in scope in the source editor. Type a new name and Xcode updates all instances to the same name. To cancel a name change, choose Edit > Undo.

##### Refactor Code Into Functions

When you have code that repeats in a function or code that you can reuse, refactor it into a function. Select the lines of code you want to refactor, then Control-click and choose Refactor > Extract to Method. Xcode creates a new function, and highlights its name so you can rename it.

![An Xcode screenshot showing the source editor with an extracted function. The call site of the extracted function is highlighted so a person can rename it.](https://docs-assets.developer.apple.com/published/656a4a13d0e38b294c0468de03a81e51/finding-and-refactoring-extract-method%402x.png)

If the lines of code reference parameters, Xcode includes those in the parameter list for the new function. To rename a parameter, Command-click it and choose Edit All in Scope, or Control-click it and choose Refactor > Rename.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/finding-and-refactoring-code)*