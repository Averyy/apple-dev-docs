# XCSourceTextPosition

**Framework**: XcodeKit  
**Kind**: struct

A zero-based position in a source editor, defined by a line number and column number.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct XCSourceTextPosition
```

## Topics

### Creating Source Text Positions
- [init()](xcsourcetextposition/init.md)
  Creates a new source text position at the beginning of the source text.
- [init(line: Int, column: Int)](xcsourcetextposition/init(line:column:).md)
  Creates a source text position at the specified line and column.
### Inspecting Source Text Positions
- [var column: Int](xcsourcetextposition/column.md)
  The horizontal component of a source text position.
- [var line: Int](xcsourcetextposition/line.md)
  The vertical component of a source text position.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class XCSourceTextBuffer](xcsourcetextbuffer.md)
  A buffer you use to access and modify the text contents and text selections in a source editor.
- [class XCSourceTextRange](xcsourcetextrange.md)
  A half-open range of text in a buffer you use to select text or specify the insertion point for new text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourcetextposition)*