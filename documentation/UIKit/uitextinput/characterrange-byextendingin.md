# characterRange(byExtending:in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a text range from a specified text position to its farthest extent in a certain direction of layout.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func characterRange(byExtending position: UITextPosition, in direction: UITextLayoutDirection) -> UITextRange?
```

#### Return Value

A text-range object that represents the distance from `position` to the farthest extent in `direction`.

## Parameters

- `position`: A text-position object that identifies a location in a document.
- `direction`: A constant that indicates a direction of layout (right, left, up, down).

## See Also

- [func position(within: UITextRange, farthestIn: UITextLayoutDirection) -> UITextPosition?](uitextinput/position(within:farthestin:).md)
  Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [func baseWritingDirection(for: UITextPosition, in: UITextStorageDirection) -> NSWritingDirection](uitextinput/basewritingdirection(for:in:).md)
  Returns the base writing direction for a position in the text going in a certain direction.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](uitextinput/setbasewritingdirection(_:for:).md)
  Sets the base writing direction for a specified range of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/characterrange(byextending:in:))*