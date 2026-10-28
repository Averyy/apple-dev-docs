# setMinimumTrackImage(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Assigns a minimum track image to the specified control states.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setMinimumTrackImage(_ image: UIImage?, for state: UIControl.State)
```

```objc
- (void) setMinimumTrackImage:(UIImage *) image forState:(UIControlState) state;
```

## Discussion

Because the movement of the slider’s thumb changes the width of the area occupied by the minimum track image, the image width changes accordingly. To accommodate this requirement, specify track images as stretchable images that can grow or shrink to fill the available space. For information about how to create stretchable images, see [`UIImage`](../uiimage.md).

When you specify a custom minimum track image, the slider ignores the custom minimum track tint color, if any.

Sliders respond to user interaction with dynamic effects and appearance. If you use images to customize the appearance of the track, then the slider doesn’t apply the dynamic effects or alter the appearance.

> ❗ **Important**:  This method isn’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](../uiuserinterfaceidiom/mac.md) and [`behavioralStyle`](./behavioralstyle.md) is [`UIBehavioralStyle.mac`](../uibehavioralstyle/mac.md) — calling it while in this state throws an exception.

## Parameters

- `image`: The minimum track image to associate with the specified states.
- `state`: The control state with which to associate the image.

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
- [var maximumTrackTintColor: UIColor?](./maximumtracktintcolor.md)
  The color used to tint the default maximum track images.
- [var currentMaximumTrackImage: UIImage?](./currentmaximumtrackimage.md)
  Contains the maximum track image currently being used to render the slider.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/setminimumtrackimage(_:for:))*