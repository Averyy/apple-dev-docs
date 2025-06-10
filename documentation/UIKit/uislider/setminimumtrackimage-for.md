# setMinimumTrackImage(_:for:)

**Framework**: UIKit  
**Kind**: method

Assigns a minimum track image to the specified control states.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setMinimumTrackImage(_ image: UIImage?, for state: UIControl.State)
```

#### Discussion

Because the movement of the slider’s thumb changes the width of the area occupied by the minimum track image, the image width changes accordingly. To accommodate this requirement, specify track images as stretchable images that can grow or shrink to fill the available space. For information about how to create stretchable images, see [`UIImage`](uiimage.md).

When you specify a custom minimum track image, the slider ignores the custom minimum track tint color, if any.

Sliders respond to user interaction with dynamic effects and appearance. If you use images to customize the appearance of the track, then the slider doesn’t apply the dynamic effects or alter the appearance.

> ❗ **Important**:  This method isn’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md) and [`behavioralStyle`](uislider/behavioralstyle.md) is [`UIBehavioralStyle.mac`](uibehavioralstyle/mac.md) — calling it while in this state throws an exception.

## Parameters

- `image`: The minimum track image to associate with the specified states.
- `state`: The control state with which to associate the image.

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
- [var currentThumbImage: UIImage?](uislider/currentthumbimage.md)
  The thumb image currently being used to render the slider.
- [func thumbImage(for: UIControl.State) -> UIImage?](uislider/thumbimage(for:).md)
  Returns the thumb image associated with the specified control state.
- [func setThumbImage(UIImage?, for: UIControl.State)](uislider/setthumbimage(_:for:).md)
  Assigns a thumb image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/setminimumtrackimage(_:for:))*