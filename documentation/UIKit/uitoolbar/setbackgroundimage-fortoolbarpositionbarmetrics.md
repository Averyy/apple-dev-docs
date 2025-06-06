# setBackgroundImage(_:forToolbarPosition:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Sets the image to use for the background in a given position and with given metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackgroundImage(_ backgroundImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage`: The image to use for the toolbar background in the position specified by   and with the metrics specified by  .
- `topOrBottom`: A toolbar position constant.
- `barMetrics`: A bar metrics constant.

## See Also

- [var barTintColor: UIColor?](uitoolbar/bartintcolor.md)
  The tint color to apply to the toolbar background.
- [func backgroundImage(forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uitoolbar/backgroundimage(fortoolbarposition:barmetrics:).md)
  Returns the image to use for the background in a given position and with given metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/setbackgroundimage(_:fortoolbarposition:barmetrics:))*