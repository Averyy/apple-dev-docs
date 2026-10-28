# XCSourceTextRange

**Framework**: XcodeKit  
**Kind**: class  
**Role**: Class

A half-open range of text in a buffer you use to select text or specify the insertion point for new text.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class XCSourceTextRange
```

```objc
@interface XCSourceTextRange : NSObject
```

## Overview

Source text ranges are half-open ranges. As a result, source text ranges include the character at the start position but exclude the character at the end position.

A range with equal start and end positions may be used to indicate a point within the buffer, such as an insertion point. The `start` and `end` position may be improperly ordered while you prepare them in your own code, but must be properly ordered before passing an `XCSourceTextRange` instance to other methods.

## Topics

### Creating Source Text Ranges
- [init(start: XCSourceTextPosition, end: XCSourceTextPosition)](./xcsourcetextrange/init%28start,end%29.md)
  Creates a new source text range defined by its starting and ending positions.
### Getting the Bounds of Source Text Ranges
- [var start: XCSourceTextPosition](./xcsourcetextrange/start.md)
  The start position of the range.
- [var end: XCSourceTextPosition](./xcsourcetextrange/end.md)
  The end position of the range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Source Text
- [class XCSourceTextBuffer](./xcsourcetextbuffer.md)
  A buffer you use to access and modify the text contents and text selections in a source editor.
- [struct XCSourceTextPosition](./xcsourcetextposition.md)
  A zero-based position in a source editor, defined by a line number and column number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourcetextrange)*