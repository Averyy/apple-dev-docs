# selections

**Framework**: XcodeKit  
**Kind**: property  
**Role**: Instance Property

The text selections in the buffer.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var selections: NSMutableArray { get }
```

```objc
@property (strong, readonly) NSMutableArray<XCSourceTextRange *> * selections;
```

## Discussion

An empty range represents an insertion point. Modifying the lines of text in the buffer automatically updates the selections to match.

## See Also

### Editing Source Text
- [var lines: NSMutableArray](./lines.md)
  The lines of text in the buffer, including line endings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourcetextbuffer/selections)*