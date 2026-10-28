# barTintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tint color to apply to the toolbar background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var barTintColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * barTintColor;
```

## Discussion

This color is made translucent by default unless you set the [`isTranslucent`](./istranslucent.md) property to [`false`](../../Swift/false.md).

## See Also

### Changing the background
- [func backgroundImage(forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28fortoolbarposition,barmetrics%29.md)
  Returns the image to use for the background in a given position and with given metrics.
- [func setBackgroundImage(UIImage?, forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,fortoolbarposition,barmetrics%29.md)
  Sets the image to use for the background in a given position and with given metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/bartintcolor)*