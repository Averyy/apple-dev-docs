# background

**Framework**: UIKit  
**Kind**: property

The image that represents the background appearance of the text field when it is in an enabled state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var background: UIImage? { get set }
```

#### Discussion

When set, the image referred to by this property replaces the standard appearance controlled by the [`borderStyle`](uitextfield/borderstyle-swift.property.md) property. Background images are drawn in the border rectangle portion of the text field. Images you use for the text field’s background should be able to stretch to fit.

This property is set to `nil` by default.

## See Also

- [var borderStyle: UITextField.BorderStyle](uitextfield/borderstyle-swift.property.md)
  The border style for the text field.
- [var disabledBackground: UIImage?](uitextfield/disabledbackground.md)
  The image that represents the background appearance of the text field when it is in a disabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/background)*