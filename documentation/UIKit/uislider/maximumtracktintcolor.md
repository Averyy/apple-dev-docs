# maximumTrackTintColor

**Framework**: UIKit  
**Kind**: property

The color used to tint the default maximum track images.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var maximumTrackTintColor: UIColor? { get set }
```

#### Discussion

Setting this property resets the maximum track images back to the slider’s default images; any custom images are released by the slider. Setting this property to `nil` resets the tint color to the default and removes any custom maximum track images.

> ❗ **Important**:  This property isn’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md) and [`behavioralStyle`](uislider/behavioralstyle.md) is [`UIBehavioralStyle.mac`](uibehavioralstyle/mac.md) — setting it while in this state throws an exception.

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
- [var currentMaximumTrackImage: UIImage?](uislider/currentmaximumtrackimage.md)
  Contains the maximum track image currently being used to render the slider.
- [func maximumTrackImage(for: UIControl.State) -> UIImage?](uislider/maximumtrackimage(for:).md)
  Returns the maximum track image associated with the specified control state.
- [func setMaximumTrackImage(UIImage?, for: UIControl.State)](uislider/setmaximumtrackimage(_:for:).md)
  Assigns a maximum track image to the specified control states.
- [var thumbTintColor: UIColor?](uislider/thumbtintcolor.md)
  The color used to tint the default thumb images.
- [var currentThumbImage: UIImage?](uislider/currentthumbimage.md)
  The thumb image currently being used to render the slider.
- [func thumbImage(for: UIControl.State) -> UIImage?](uislider/thumbimage(for:).md)
  Returns the thumb image associated with the specified control state.
- [func setThumbImage(UIImage?, for: UIControl.State)](uislider/setthumbimage(_:for:).md)
  Assigns a thumb image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/maximumtracktintcolor)*