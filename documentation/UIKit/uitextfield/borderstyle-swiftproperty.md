# borderStyle

**Framework**: UIKit  
**Kind**: property

The border style for the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var borderStyle: UITextField.BorderStyle { get set }
```

#### Discussion

The default value for this property is [`UITextField.BorderStyle.none`](uitextfield/borderstyle-swift.enum/none.md). If the value is set to the [`UITextField.BorderStyle.roundedRect`](uitextfield/borderstyle-swift.enum/roundedrect.md) style, the custom background image associated with the text field is ignored.

## See Also

- [var background: UIImage?](uitextfield/background.md)
  The image that represents the background appearance of the text field when it is in an enabled state.
- [var disabledBackground: UIImage?](uitextfield/disabledbackground.md)
  The image that represents the background appearance of the text field when it is in a disabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/borderstyle-swift.property)*