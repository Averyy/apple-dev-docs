# XcodeKit

**Framework**: Xcodekit  
**Kind**: module

Create extensions to add commands to the Xcode source editor.

**Availability**:
- macOS 10.12+

#### Overview

Using the XcodeKit framework, you can customize Xcode with source editor extensions to add functionality and specialized behavior to the source editor. Source editor extensions provide a group of editor commands alongside the built-in commands in the Editor menu in Xcode.  Source editor extensions can read and modify the contents of a source file, as well as read and modify the current text selection within the editor. Include source editor extensions in developer apps distributed on the Mac App Store.

## Topics

### Essentials
- [Creating a Source Editor Extension](creating-a-source-editor-extension.md)
  Add and configure a source editor extension in your Xcode project.
- [Testing Your Source Editor Extension](testing-your-source-editor-extension.md)
  Launch a special instance of Xcode to test your source editor extension.
- [protocol XCSourceEditorExtension](xcsourceeditorextension.md)
  The protocol you implement to create Xcode source editor extensions.
### Editor Commands
- [protocol XCSourceEditorCommand](xcsourceeditorcommand.md)
  The protocol you implement to handle command invocations in a source editor extension.
- [class XCSourceEditorCommandInvocation](xcsourceeditorcommandinvocation.md)
  An object that identifies the command issued to your extension and provides the contents of the active source editor.
### Source Text
- [class XCSourceTextBuffer](xcsourcetextbuffer.md)
  A buffer you use to access and modify the text contents and text selections in a source editor.
- [struct XCSourceTextPosition](xcsourcetextposition.md)
  A zero-based position in a source editor, defined by a line number and column number.
- [class XCSourceTextRange](xcsourcetextrange.md)
  A half-open range of text in a buffer you use to select text or specify the insertion point for new text.
### XcodeKit Constants
- [XcodeKit Version Constants](xcodekit-version-constants.md)
  Determine the version of XcodeKit available in an instance of Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/XcodeKit)*