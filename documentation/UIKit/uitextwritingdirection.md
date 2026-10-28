# UITextWritingDirection

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The writing direction of the text for the language.

**Availability**:
- iOS 3.2+ - Deprecated in 13.0 (renamed: NSWritingDirection)
- iPadOS 3.2+ - Deprecated in 13.0 (renamed: NSWritingDirection)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSWritingDirection)
- tvOS 9.0+ - Deprecated in 13.0 (renamed: NSWritingDirection)

> **Deprecated**: Use [`NSWritingDirection`](./nswritingdirection.md) instead.

## Declaration

```swift
typealias UITextWritingDirection = NSWritingDirection
```

```c
typedef NSWritingDirection UITextWritingDirection;
```

## Discussion

Constants of this type are returned from the [`baseWritingDirection(for:in:)`](./uitextinput/basewritingdirection%28for,in%29.md) method and are used as arguments of the [`setBaseWritingDirection(_:for:)`](./uitextinput/setbasewritingdirection%28_,for%29.md) method.

## Topics

### Constants
- [UITextWritingDirectionNatural](./uitextwritingdirectionnatural.md)
  The natural writing direction as defined by the Bidi algorithm.
- [UITextWritingDirectionLeftToRight](./uitextwritingdirectionlefttoright.md)
  Writing that goes from left to right.
- [UITextWritingDirectionRightToLeft](./uitextwritingdirectionrighttoleft.md)
  Writing that goes from right to left.

## See Also

### Determining layout and writing direction
- [func position(within: UITextRange, farthestIn: UITextLayoutDirection) -> UITextPosition?](./uitextinput/position%28within,farthestin%29.md)
  Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [func characterRange(byExtending: UITextPosition, in: UITextLayoutDirection) -> UITextRange?](./uitextinput/characterrange%28byextending,in%29.md)
  Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [func baseWritingDirection(for: UITextPosition, in: UITextStorageDirection) -> NSWritingDirection](./uitextinput/basewritingdirection%28for,in%29.md)
  Returns the base writing direction for a position in the text going in a certain direction.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](./uitextinput/setbasewritingdirection%28_,for%29.md)
  Sets the base writing direction for a specified range of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextwritingdirection)*