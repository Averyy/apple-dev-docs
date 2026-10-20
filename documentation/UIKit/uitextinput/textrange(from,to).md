# textRange(from:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the range between two text positions.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func textRange(from fromPosition: UITextPosition, to toPosition: UITextPosition) -> UITextRange?
```

```objc
- (UITextRange *) textRangeFromPosition:(UITextPosition *) fromPosition toPosition:(UITextPosition *) toPosition;
```

#### Return Value

An object that represents the range between `fromPosition` and `toPosition`.

## Parameters

- `fromPosition`: An object that represents a location in a document.
- `toPosition`: An object that represents another location in a document.

## See Also

### Computing text ranges and text positions
- [func position(from: UITextPosition, offset: Int) -> UITextPosition?](./position%28from,offset%29.md)
  Returns the text position at a specified offset from another text position.
- [func position(from: UITextPosition, in: UITextLayoutDirection, offset: Int) -> UITextPosition?](./position%28from,in,offset%29.md)
  Returns the text position at a specified offset in a specified direction from another text position.
- [var beginningOfDocument: UITextPosition](./beginningofdocument.md)
  The text position for the beginning of a document.
- [var endOfDocument: UITextPosition](./endofdocument.md)
  The text position for the end of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/textrange(from:to:))*