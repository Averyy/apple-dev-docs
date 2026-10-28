# position(within:farthestIn:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text position that is at the farthest extent in a specified layout direction within a range of text.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func position(within range: UITextRange, farthestIn direction: UITextLayoutDirection) -> UITextPosition?
```

```objc
- (UITextPosition *) positionWithinRange:(UITextRange *) range farthestInDirection:(UITextLayoutDirection) direction;
```

## Return Value

A text-position object that identifies a location in the visible text.

## Parameters

- `range`: A text-range object that demarcates a range of text in a document.
- `direction`: A constant that indicates a direction of layout (right, left, up, down).

## See Also

### Determining layout and writing direction
- [func characterRange(byExtending: UITextPosition, in: UITextLayoutDirection) -> UITextRange?](./characterrange%28byextending,in%29.md)
  Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [func baseWritingDirection(for: UITextPosition, in: UITextStorageDirection) -> NSWritingDirection](./basewritingdirection%28for,in%29.md)
  Returns the base writing direction for a position in the text going in a certain direction.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](./setbasewritingdirection%28_,for%29.md)
  Sets the base writing direction for a specified range of text in a document.
- [typealias UITextWritingDirection](../uitextwritingdirection.md)
  The writing direction of the text for the language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/position(within:farthestin:))*