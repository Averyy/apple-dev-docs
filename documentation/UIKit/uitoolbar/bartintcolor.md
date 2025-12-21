# barTintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the toolbar background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barTintColor: UIColor? { get set }
```

#### Discussion

This color is made translucent by default unless you set the [`isTranslucent`](uitoolbar/istranslucent.md) property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func backgroundImage(forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uitoolbar/backgroundimage(fortoolbarposition:barmetrics:).md)
  Returns the image to use for the background in a given position and with given metrics.
- [func setBackgroundImage(UIImage?, forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics)](uitoolbar/setbackgroundimage(_:fortoolbarposition:barmetrics:).md)
  Sets the image to use for the background in a given position and with given metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/bartintcolor)*