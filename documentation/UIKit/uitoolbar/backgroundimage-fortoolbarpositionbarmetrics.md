# backgroundImage(forToolbarPosition:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Returns the image to use for the background in a given position and with given metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backgroundImage(forToolbarPosition topOrBottom: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?
```

#### Return Value

The image to use for the toolbar background in the position specified by `topOrBottom` and with the metrics specified by `barMetrics`.

#### Discussion

The default value is `nil`. When non-`nil` the image will be used instead of the system image for toolbars in the specified position.

## Parameters

- `topOrBottom`: The location the bar is being drawn in.
- `barMetrics`: The metrics being used to draw the bar.

## See Also

- [var barTintColor: UIColor?](uitoolbar/bartintcolor.md)
  The tint color to apply to the toolbar background.
- [func setBackgroundImage(UIImage?, forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics)](uitoolbar/setbackgroundimage(_:fortoolbarposition:barmetrics:).md)
  Sets the image to use for the background in a given position and with given metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/backgroundimage(fortoolbarposition:barmetrics:))*