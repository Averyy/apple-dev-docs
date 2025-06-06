# position(from:offset:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the text position at a specified offset from another text position.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func position(from position: UITextPosition, offset: Int) -> UITextPosition?
```

#### Return Value

A custom [`UITextPosition`](uitextposition.md) object that represents the location in a document that is at the specified offset from `position`. Return `nil` if the computed text position is less than 0 or greater than the length of the backing string.

#### Discussion

For an example of an implementation of this method, see [`Using Text Kit to Draw and Manage Text`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/CustomTextProcessing/CustomTextProcessing.html#//apple_ref/doc/uid/TP40009542-CH4) in [`Text Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009542).

## Parameters

- `position`: A custom   object that represents a location in a document.
- `offset`: A character offset from  . It can be a positive or negative value.

## See Also

- [func textRange(from: UITextPosition, to: UITextPosition) -> UITextRange?](uitextinput/textrange(from:to:).md)
  Returns the range between two text positions.
- [func position(from: UITextPosition, in: UITextLayoutDirection, offset: Int) -> UITextPosition?](uitextinput/position(from:in:offset:).md)
  Returns the text position at a specified offset in a specified direction from another text position.
- [var beginningOfDocument: UITextPosition](uitextinput/beginningofdocument.md)
  The text position for the beginning of a document.
- [var endOfDocument: UITextPosition](uitextinput/endofdocument.md)
  The text position for the end of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/position(from:offset:))*