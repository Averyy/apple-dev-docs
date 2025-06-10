# XCSourceTextBuffer

**Framework**: XcodeKit  
**Kind**: class

A buffer you use to access and modify the text contents and text selections in a source editor.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class XCSourceTextBuffer
```

#### Overview

Mutations to the buffer are tracked and committed when a command completes successfully and has not been canceled by the user.

## Topics

### Accessing Source Text
- [var completeBuffer: String](xcsourcetextbuffer/completebuffer.md)
  The complete buffer’s string representation.
- [var contentUTI: String](xcsourcetextbuffer/contentuti.md)
  The Uniform Type Identifier (UTI) of the content in the buffer.
### Editing Source Text
- [var lines: NSMutableArray](xcsourcetextbuffer/lines.md)
  The lines of text in the buffer, including line endings.
- [var selections: NSMutableArray](xcsourcetextbuffer/selections.md)
  The text selections in the buffer.
### Configuring Source Editor Indentation
- [var indentationWidth: Int](xcsourcetextbuffer/indentationwidth.md)
  The number of space characters used for indentation of the text in the buffer.
- [var usesTabsForIndentation: Bool](xcsourcetextbuffer/usestabsforindentation.md)
  A Boolean value that indicates whether tabs are used for indentation.
- [var tabWidth: Int](xcsourcetextbuffer/tabwidth.md)
  The number of space characters represented by a tab character in the buffer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct XCSourceTextPosition](xcsourcetextposition.md)
  A zero-based position in a source editor, defined by a line number and column number.
- [class XCSourceTextRange](xcsourcetextrange.md)
  A half-open range of text in a buffer you use to select text or specify the insertion point for new text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourcetextbuffer)*