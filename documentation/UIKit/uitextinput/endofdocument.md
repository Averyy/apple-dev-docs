# endOfDocument

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The text position for the end of a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var endOfDocument: UITextPosition { get }
```

```objc
@property (nonatomic, readonly) UITextPosition * endOfDocument;
```

## See Also

### Computing text ranges and text positions
- [func textRange(from: UITextPosition, to: UITextPosition) -> UITextRange?](./textrange%28from,to%29.md)
  Returns the range between two text positions.
- [func position(from: UITextPosition, offset: Int) -> UITextPosition?](./position%28from,offset%29.md)
  Returns the text position at a specified offset from another text position.
- [func position(from: UITextPosition, in: UITextLayoutDirection, offset: Int) -> UITextPosition?](./position%28from,in,offset%29.md)
  Returns the text position at a specified offset in a specified direction from another text position.
- [var beginningOfDocument: UITextPosition](./beginningofdocument.md)
  The text position for the beginning of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/endofdocument)*