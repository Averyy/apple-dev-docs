# prefersStatusBarHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether the view controller prefers the status bar to be hidden or shown.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Has no effect on visionOS

## Declaration

```swift
var prefersStatusBarHidden: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL prefersStatusBarHidden;
```

#### Return Value

[`true`](../../Swift/true.md) if the status bar should be hidden or [`false`](../../Swift/false.md) if it should be shown.

#### Discussion

If you change the return value for this method, call the [`setNeedsStatusBarAppearanceUpdate()`](./setneedsstatusbarappearanceupdate%28%29.md) method. To specify that a child view controller should control preferred status bar hidden/unhidden state, implement the [`childForStatusBarHidden`](./childforstatusbarhidden.md) method.

By default, this method returns [`false`](../../Swift/false.md) with one exception. For apps linked against iOS 8 or later, this method returns [`true`](../../Swift/true.md) if the view controller is in a vertically compact environment.

## See Also

### Managing the status bar
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
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](./preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](./setneedsstatusbarappearanceupdate%28%29.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/prefersstatusbarhidden)*