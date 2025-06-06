# beginningOfDocument

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The text position for the beginning of a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var beginningOfDocument: UITextPosition { get }
```

## See Also

- [func textRange(from: UITextPosition, to: UITextPosition) -> UITextRange?](uitextinput/textrange(from:to:).md)
  Returns the range between two text positions.
- [func position(from: UITextPosition, offset: Int) -> UITextPosition?](uitextinput/position(from:offset:).md)
  Returns the text position at a specified offset from another text position.
- [func position(from: UITextPosition, in: UITextLayoutDirection, offset: Int) -> UITextPosition?](uitextinput/position(from:in:offset:).md)
  Returns the text position at a specified offset in a specified direction from another text position.
- [var endOfDocument: UITextPosition](uitextinput/endofdocument.md)
  The text position for the end of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/beginningofdocument)*