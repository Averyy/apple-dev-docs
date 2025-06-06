# Source Editor Release Notes for Xcode 10

**Framework**: Xcode Release Notes

Update your programming workflow to use new features, and test your workflow against changes.

#### Overview

Read these notes when you’re editing source code in Xcode 10.

Xcode 10 has increased support for code folding, including:

1. A new code folding ribbon showing all of the multi-line foldable blocks of code in the editor
2. A new style for folded code in the editor that allows you to edit lines with folded code
3. Support for folding any block of code enclosed in curly braces
4. Support for folding blocks of code from the folding ribbon, from structured selection, or from the Editor > Code Folding > Fold menu item

To turn on the code folding ribbon, open preferences under Text Editing > Editing and select “Code folding ribbon”. (33518606, 34203382, 35391767, 35932817, 36554006)

##### New Features

- Selected text ranges in the source editor can now be split into multiple selected text ranges by line using the Editor > Structure > Split Selection By Lines menu item. (39300660)
- You can add selections for the next and previous find results using the “Find and Select Next” and “Find and Select Previous” menu commands. Additionally, you can quickly add selections for the next and previous occurrences of the current selected text using the “Select Next Occurrence” and “Select Previous Occurrence” menu commands. (39283721)
- The source editor will now automatically detect and use the predominant line ending style in a file. (35343242)
- The source editor now supports configurable overscroll at the end of the file. The overscroll amount can be configured in Preferences > Text Editing > Editor Overscroll. (9075043)
- Moved some menu items into a new Editor > Selection submenu. Added new “Select Column Up” and “Select Column Down” items to allow creating columnar selections with the keyboard. (39321297)
- Xcode now supports syntax highlighting for Swift pound directives. (40887538)
- All instances of the current symbol can be selected in the editor with the Editor > Structure > Select All Symbols command. (35064345)
- Custom code snippets can now be added to the library via the Editor > Create Code Snippet menu item. (37946810)
- Updated default source editor themes for light and dark, with improved colors optimized for contrast, and taking advantage of bold and italic font traits. (40036785)
- Xcode no longer allows creating discontiguous selections using the command modifier key. To create discontiguous selections, hold Control-Shift during the selection. (42564654)
- Find results in the source editor can now be selected using the Find > Select All Find Matches menu item. The results to select can be constrained to those in the current selection using the menu item Find > Select Find Matches in Selection. (35064581, 39283557)
- The Xcode Source Editor now supports multi-cursor editing allowing you to quickly edit multiple ranges of code at once. You can place additional cursors with the mouse via ⌃+⇧+Click or with column select (⌥+Click+Drag), or with the keyboard using ⌃+⇧+Up to column select up or ⌃+⇧+Down to column select down. (12564506)

##### Resolved Issues

- Highlighting of a matching brace can now be disabled with the following user default: `defaults write com.apple.dt.Xcode DVTTextShowMatchingBrace -bool NO` (33876309)
- Fixed issue that could cause Xcode to crash when working with some Windows-formatted Markdown files. (35725637)
- Improved the performance of many editing operations, including Undo and Redo. (30874294)
- Resolved an issue where the scroll position may change slightly when switching files. (39100209)
- Fixed an issue that caused tabs before a closing brace to still be shown when folding code. (40041202)
- Fixed an issue where using the `noexcept` keyword in C++ source files would cause functions to not show up in the Jump Bar. (13266374)
- Removed duplication in the Superclasses submenu of the jump bar’s Related Items menu. (32954204)
- Fixed an issue where comments in XML files that contained `MARK:` or `TODO:` would cause syntax coloring of the rest of the file to fail. (12051726)
- Resolved an issue where breakpoints may appear at the incorrect line in folded code. (37288192)
- Enhanced reliability of Jump to Definition, which now shows results more reliably in situations with syntax errors or other errors in the code. (34905255)
- Live issues will now be cleared when renaming a file. This resolves an issue where live issues may remain after a file has been renamed and edited. (36186038)
- Fixed crash of image literal quick editor. (38281672)
- Resolved a crash that could occur when editing markup files. (36566474)
- Fixed an issue that caused Xcode to crash after deleting code. (40817677)
- The source editor now provides more accurate code completion when typing initializers in Swift. (38265505)
- Improved the scrolling estimation for large files. (39344677)
- Fixed an issue that caused semantic highlighting to disappear in files that are open in multiple tabs. (39675025)
- Resolved an issue where the scroll position may jump when scrolling through a file with very long lines. (40252210)
- Fixed problems where the  and  commands didn’t work correctly. (38477237)
- Fixed a problem where the  preference was not respected. (34195824)
- Fixed a problem where double-clicking UI Test recording tokens deleted the text instead of confirming the selection. It now properly replaces the token with the selected item. (33573785)
- Fixed a problem where code completion would fail for Swift source files included in multiple targets. (40909436)
- Fixed an issue where breakpoints could not be added or modified by command clicking when Xcode was in the background. (37835585)
- Fixed an issue that caused the source editor to skip a line when pressing up arrow on a wrapped line. (41504239)
- Fixed a problem with code completion using code snippets starting with `@` character, such as `@autoreleasepool`. (31768452)
- Improved formatting for JSON files in the source editor. (31758362)

## See Also

- [Build System Release Notes for Xcode 10](build-system-release-notes-for-xcode-10.md)
  Update your apps to use new features, and test your apps against changes.
- [Interface Builder Release Notes for Xcode 10](interface-builder-release-notes-for-xcode-10.md)
  Update your apps to use new features, and test your apps against changes.
- [Swift 4.2 Release Notes for Xcode 10](swift-4_2-release-notes-for-xcode-10.md)
  Update your code to use new language features and test your apps against changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/source-editor-release-notes-for-xcode-10)*