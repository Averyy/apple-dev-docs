# UITextWritingDirection

**Framework**: UIKit  
**Kind**: typealias

The writing direction of the text for the language.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
typealias UITextWritingDirection = NSWritingDirection
```

#### Discussion

Constants of this type are returned from the [`baseWritingDirection(for:in:)`](uitextinput/basewritingdirection(for:in:).md) method and are used as arguments of the [`setBaseWritingDirection(_:for:)`](uitextinput/setbasewritingdirection(_:for:).md) method.

## See Also

- [func position(within: UITextRange, farthestIn: UITextLayoutDirection) -> UITextPosition?](uitextinput/position(within:farthestin:).md)
  Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [func characterRange(byExtending: UITextPosition, in: UITextLayoutDirection) -> UITextRange?](uitextinput/characterrange(byextending:in:).md)
  Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [func baseWritingDirection(for: UITextPosition, in: UITextStorageDirection) -> NSWritingDirection](uitextinput/basewritingdirection(for:in:).md)
  Returns the base writing direction for a position in the text going in a certain direction.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](uitextinput/setbasewritingdirection(_:for:).md)
  Sets the base writing direction for a specified range of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextwritingdirection)*