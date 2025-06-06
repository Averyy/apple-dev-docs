# textRange(from:to:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the range between two text positions.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func textRange(from fromPosition: UITextPosition, to toPosition: UITextPosition) -> UITextRange?
```

#### Return Value

An object that represents the range between `fromPosition` and `toPosition`.

## Parameters

- `fromPosition`: An object that represents a location in a document.
- `toPosition`: An object that represents another location in a document.

## See Also

- [func position(from: UITextPosition, offset: Int) -> UITextPosition?](uitextinput/position(from:offset:).md)
  Returns the text position at a specified offset from another text position.
- [func position(from: UITextPosition, in: UITextLayoutDirection, offset: Int) -> UITextPosition?](uitextinput/position(from:in:offset:).md)
  Returns the text position at a specified offset in a specified direction from another text position.
- [var beginningOfDocument: UITextPosition](uitextinput/beginningofdocument.md)
  The text position for the beginning of a document.
- [var endOfDocument: UITextPosition](uitextinput/endofdocument.md)
  The text position for the end of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/textrange(from:to:))*