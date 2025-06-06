# currentThumbImage

**Framework**: UIKit  
**Kind**: property

The thumb image currently being used to render the slider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var currentThumbImage: UIImage? { get }
```

#### Discussion

Sliders can have different thumb images for different control states. The active control state determines which thumb image is stored in this property. To get the thumb image for a different control state, use the [`thumbImage(for:)`](uislider/thumbimage(for:).md) method.

If no custom thumb images have been set using the [`setThumbImage(_:for:)`](uislider/setthumbimage(_:for:).md) method, this property is `nil`. In that situation, the slider uses the default thumb image for drawing.

## See Also

- [var minimumValueImage: UIImage?](uislider/minimumvalueimage.md)
  The image that represents the slider’s minimum value.
- [var maximumValueImage: UIImage?](uislider/maximumvalueimage.md)
  The image representing the slider’s maximum value.
- [var minimumTrackTintColor: UIColor?](uislider/minimumtracktintcolor.md)
  The color used to tint the default minimum track images.
- [var currentMinimumTrackImage: UIImage?](uislider/currentminimumtrackimage.md)
  The minimum track image currently being used to render the slider.
- [func minimumTrackImage(for: UIControl.State) -> UIImage?](uislider/minimumtrackimage(for:).md)
  Returns the minimum track image associated with the specified control state.
- [func setMinimumTrackImage(UIImage?, for: UIControl.State)](uislider/setminimumtrackimage(_:for:).md)
  Assigns a minimum track image to the specified control states.
- [var maximumTrackTintColor: UIColor?](uislider/maximumtracktintcolor.md)
  The color used to tint the default maximum track images.
- [var currentMaximumTrackImage: UIImage?](uislider/currentmaximumtrackimage.md)
  Contains the maximum track image currently being used to render the slider.
- [func maximumTrackImage(for: UIControl.State) -> UIImage?](uislider/maximumtrackimage(for:).md)
  Returns the maximum track image associated with the specified control state.
- [func setMaximumTrackImage(UIImage?, for: UIControl.State)](uislider/setmaximumtrackimage(_:for:).md)
  Assigns a maximum track image to the specified control states.
- [var thumbTintColor: UIColor?](uislider/thumbtintcolor.md)
  The color used to tint the default thumb images.
- [func thumbImage(for: UIControl.State) -> UIImage?](uislider/thumbimage(for:).md)
  Returns the thumb image associated with the specified control state.
- [func setThumbImage(UIImage?, for: UIControl.State)](uislider/setthumbimage(_:for:).md)
  Assigns a thumb image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/currentthumbimage)*