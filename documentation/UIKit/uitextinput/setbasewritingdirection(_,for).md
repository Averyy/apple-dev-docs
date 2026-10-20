# setBaseWritingDirection(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
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
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, for range: UITextRange)
```

```objc
- (void) setBaseWritingDirection:(NSWritingDirection) writingDirection forRange:(UITextRange *) range;
```

## Parameters

- `writingDirection`: A constant that represents a writing direction (for example, left-to-right or right-to-left)
- `range`: An object that represents a range of text in a document.

## See Also

### Determining layout and writing direction
- [func position(within: UITextRange, farthestIn: UITextLayoutDirection) -> UITextPosition?](./position%28within,farthestin%29.md)
  Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [func characterRange(byExtending: UITextPosition, in: UITextLayoutDirection) -> UITextRange?](./characterrange%28byextending,in%29.md)
  Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [func baseWritingDirection(for: UITextPosition, in: UITextStorageDirection) -> NSWritingDirection](./basewritingdirection%28for,in%29.md)
  Returns the base writing direction for a position in the text going in a certain direction.
- [typealias UITextWritingDirection](../uitextwritingdirection.md)
  The writing direction of the text for the language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/setbasewritingdirection(_:for:))*