# disabledBackground

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image that represents the background appearance of the text field when it is in a disabled state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var disabledBackground: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * disabledBackground;
```

#### Discussion

Background images are drawn in the border rectangle portion of the text field. Images you use for the text field’s background should be able to stretch to fit. This property is ignored if the [`background`](./background.md) property is not also set.

This property is set to `nil` by default.

## See Also

### Setting the view’s background appearance
- [var borderStyle: UITextField.BorderStyle](./borderstyle-swift.property.md)
  The border style for the text field.
- [var background: UIImage?](./background.md)
  The image that represents the background appearance of the text field when it is in an enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/disabledbackground)*