# setBaseWritingDirection(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Sets the base writing direction for a specified range of text in a document.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, for range: UITextRange)
```

## Parameters

- `writingDirection`: A constant that represents a writing direction (for example, left-to-right or right-to-left)
- `range`: An object that represents a range of text in a document.

## See Also

- [func position(within: UITextRange, farthestIn: UITextLayoutDirection) -> UITextPosition?](uitextinput/position(within:farthestin:).md)
  Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [func characterRange(byExtending: UITextPosition, in: UITextLayoutDirection) -> UITextRange?](uitextinput/characterrange(byextending:in:).md)
  Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [func baseWritingDirection(for: UITextPosition, in: UITextStorageDirection) -> NSWritingDirection](uitextinput/basewritingdirection(for:in:).md)
  Returns the base writing direction for a position in the text going in a certain direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/setbasewritingdirection(_:for:))*