# minimumValueImage

**Framework**: UIKit  
**Kind**: property

The image that represents the slider’s minimum value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumValueImage: UIImage? { get set }
```

#### Discussion

The image you specify must fit within the bounding rectangle returned by the [`minimumValueImageRect(forBounds:)`](uislider/minimumvalueimagerect(forbounds:).md) method. If it doesn’t, the slider scales the image to fit. In addition, the slider lengthens or shortens its track as needed to accommodate the image in its bounding rectangle.

Because  is a semantic concept, in a right-to-left user interface, the slider automatically flips the image placement, always placing it at the leading end of the slider’s track.

The default value of this property is `nil`.

> ❗ **Important**:  This property isn’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md) and [`behavioralStyle`](uislider/behavioralstyle.md) is [`UIBehavioralStyle.mac`](uibehavioralstyle/mac.md) — setting it while in this state throws an exception.

## See Also

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
- [var currentThumbImage: UIImage?](uislider/currentthumbimage.md)
  The thumb image currently being used to render the slider.
- [func thumbImage(for: UIControl.State) -> UIImage?](uislider/thumbimage(for:).md)
  Returns the thumb image associated with the specified control state.
- [func setThumbImage(UIImage?, for: UIControl.State)](uislider/setthumbimage(_:for:).md)
  Assigns a thumb image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/minimumvalueimage)*