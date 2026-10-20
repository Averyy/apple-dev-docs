# preferredStatusBarUpdateAnimation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies the animation style to use for hiding and showing the status bar for the view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Has no effect on visionOS

## Declaration

```swift
var preferredStatusBarUpdateAnimation: UIStatusBarAnimation { get }
```

```objc
@property (nonatomic, readonly) UIStatusBarAnimation preferredStatusBarUpdateAnimation;
```

#### Return Value

The style of status bar animation to use; one of the constants from the [`UIStatusBarAnimation`](../uistatusbaranimation.md) enum. Default value is [`UIStatusBarAnimation.fade`](../uistatusbaranimation/fade.md).

#### Discussion

This property comes into play only when you actively change the status bar’s show/hide state by changing the return value of the [`prefersStatusBarHidden`](./prefersstatusbarhidden.md) method.

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
- [var modalPresentationCapturesStatusBarAppearance: Bool](./modalpresentationcapturesstatusbarappearance.md)
  Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [func setNeedsStatusBarAppearanceUpdate()](./setneedsstatusbarappearanceupdate%28%29.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarupdateanimation)*