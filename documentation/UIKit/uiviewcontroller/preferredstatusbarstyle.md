# preferredStatusBarStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred status bar style for the view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Has no effect on visionOS

## Declaration

```swift
var preferredStatusBarStyle: UIStatusBarStyle { get }
```

```objc
@property (nonatomic, readonly) UIStatusBarStyle preferredStatusBarStyle;
```

#### Return Value

A [`UIStatusBarStyle`](../uistatusbarstyle.md) key indicating your preferred status bar style for the view controller.

#### Discussion

You can override the preferred status bar style for a view controller by implementing the [`childForStatusBarStyle`](./childforstatusbarstyle.md) method.

If the return value from this method changes, call the [`setNeedsStatusBarAppearanceUpdate()`](./setneedsstatusbarappearanceupdate%28%29.md) method.

## See Also

### Managing the status bar
- [var prefersStatusBarHidden: Bool](./prefersstatusbarhidden.md)
  Specifies whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarHidden: UIViewController?](./childforstatusbarhidden.md)
  The view controller to use for determining the hidden state of the status bar.
- [var childForStatusBarStyle: UIViewController?](./childforstatusbarstyle.md)
  Called when the system needs the view controller to use for determining status bar style.
- [enum UIStatusBarStyle](../uistatusbarstyle.md)
  Constants that describe the style of the device’s status bar.
- [var modalPresentationCapturesStatusBarAppearance: Bool](./modalpresentationcapturesstatusbarappearance.md)
  Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](./preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](./setneedsstatusbarappearanceupdate%28%29.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle)*