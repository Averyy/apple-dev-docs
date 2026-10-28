# modalPresentationCapturesStatusBarAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var modalPresentationCapturesStatusBarAppearance: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL modalPresentationCapturesStatusBarAppearance;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md).

When you present a view controller by calling the [`present(_:animated:completion:)`](./present%28_,animated,completion%29.md) method, status bar appearance control is transferred from the presenting to the presented view controller only if the presented controller’s [`modalPresentationStyle`](./modalpresentationstyle.md) value is [`UIModalPresentationStyle.fullScreen`](../uimodalpresentationstyle/fullscreen.md). By setting this property to [`true`](../../Swift/true.md), you specify the presented view controller controls status bar appearance, even though presented non-fullscreen.

The system ignores this property’s value for a view controller presented fullscreen.

## See Also

### Managing the status bar
- [var prefersStatusBarHidden: Bool](./prefersstatusbarhidden.md)
  Specifies whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarHidden: UIViewController?](./childforstatusbarhidden.md)
  The view controller to use for determining the hidden state of the status bar.
- [var childForStatusBarStyle: UIViewController?](./childforstatusbarstyle.md)
  Called when the system needs the view controller to use for determining status bar style.
- [var preferredStatusBarStyle: UIStatusBarStyle](./preferredstatusbarstyle.md)
  The preferred status bar style for the view controller.
- [enum UIStatusBarStyle](../uistatusbarstyle.md)
  Constants that describe the style of the device’s status bar.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](./preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](./setneedsstatusbarappearanceupdate%28%29.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/modalpresentationcapturesstatusbarappearance)*