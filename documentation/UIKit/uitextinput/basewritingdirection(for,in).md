# baseWritingDirection(for:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the base writing direction for a position in the text going in a certain direction.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func baseWritingDirection(for position: UITextPosition, in direction: UITextStorageDirection) -> NSWritingDirection
```

```objc
- (NSWritingDirection) baseWritingDirectionForPosition:(UITextPosition *) position inDirection:(UITextStorageDirection) direction;
```

## Return Value

A constant that represents a writing direction (for example, left-to-right or right-to-left).

## Discussion

The base writing direction is set previously when the text input system sends a [`setBaseWritingDirection(_:for:)`](./setbasewritingdirection%28_,for%29.md) message to the conforming document object.

## Parameters

- `position`: An object that identifies a location in a document.
- `direction`: A constant that indicates a direction of storage (forward or backward).

## See Also

### Determining layout and writing direction
- [func position(within: UITextRange, farthestIn: UITextLayoutDirection) -> UITextPosition?](./position%28within,farthestin%29.md)
  Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [func characterRange(byExtending: UITextPosition, in: UITextLayoutDirection) -> UITextRange?](./characterrange%28byextending,in%29.md)
  Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](./setbasewritingdirection%28_,for%29.md)
  Sets the base writing direction for a specified range of text in a document.
- [typealias UITextWritingDirection](../uitextwritingdirection.md)
  The writing direction of the text for the language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/basewritingdirection(for:in:))*