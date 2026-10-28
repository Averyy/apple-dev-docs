# currentMaximumTrackImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Contains the maximum track image currently being used to render the slider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var currentMaximumTrackImage: UIImage? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIImage * currentMaximumTrackImage;
```

## Discussion

Sliders can have different track images for different control states. The active control state determines which maximum track image is stored in this property. To get the maximum track image for a different control state, use the [`maximumTrackImage(for:)`](./maximumtrackimage%28for%29.md) method.

If no custom track images have been set using the [`setMaximumTrackImage(_:for:)`](./setmaximumtrackimage%28_,for%29.md) method, this property contains the value `nil`. In that situation, the slider uses the default maximum track image for drawing.

## See Also

### Changing the slider’s appearance
- [var minimumValueImage: UIImage?](./minimumvalueimage.md)
  The image that represents the slider’s minimum value.
- [var maximumValueImage: UIImage?](./maximumvalueimage.md)
  The image representing the slider’s maximum value.
- [var minimumTrackTintColor: UIColor?](./minimumtracktintcolor.md)
  The color used to tint the default minimum track images.
- [var currentMinimumTrackImage: UIImage?](./currentminimumtrackimage.md)
  The minimum track image currently being used to render the slider.
- [func minimumTrackImage(for: UIControl.State) -> UIImage?](./minimumtrackimage%28for%29.md)
  Returns the minimum track image associated with the specified control state.
- [func setMinimumTrackImage(UIImage?, for: UIControl.State)](./setminimumtrackimage%28_,for%29.md)
  Assigns a minimum track image to the specified control states.
- [var maximumTrackTintColor: UIColor?](./maximumtracktintcolor.md)
  The color used to tint the default maximum track images.
- [func maximumTrackImage(for: UIControl.State) -> UIImage?](./maximumtrackimage%28for%29.md)
  Returns the maximum track image associated with the specified control state.
- [func setMaximumTrackImage(UIImage?, for: UIControl.State)](./setmaximumtrackimage%28_,for%29.md)
  Assigns a maximum track image to the specified control states.
- [var thumbTintColor: UIColor?](./thumbtintcolor.md)
  The color used to tint the default thumb images.
- [var currentThumbImage: UIImage?](./currentthumbimage.md)
  The thumb image currently being used to render the slider.
- [func thumbImage(for: UIControl.State) -> UIImage?](./thumbimage%28for%29.md)
  Returns the thumb image associated with the specified control state.
- [func setThumbImage(UIImage?, for: UIControl.State)](./setthumbimage%28_,for%29.md)
  Assigns a thumb image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/currentmaximumtrackimage)*