# prefersStatusBarHidden

**Framework**: UIKit  
**Kind**: property

Specifies whether the view controller prefers the status bar to be hidden or shown.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var prefersStatusBarHidden: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the status bar should be hidden or [`false`](https://developer.apple.com/documentation/Swift/false) if it should be shown.

#### Discussion

If you change the return value for this method, call the [`setNeedsStatusBarAppearanceUpdate()`](uiviewcontroller/setneedsstatusbarappearanceupdate().md) method. To specify that a child view controller should control preferred status bar hidden/unhidden state, implement the [`childForStatusBarHidden`](uiviewcontroller/childforstatusbarhidden.md) method.

By default, this method returns [`false`](https://developer.apple.com/documentation/Swift/false) with one exception. For apps linked against iOS 8 or later, this method returns [`true`](https://developer.apple.com/documentation/Swift/true) if the view controller is in a vertically compact environment.

## See Also

- [var childForStatusBarHidden: UIViewController?](uiviewcontroller/childforstatusbarhidden.md)
  The view controller to use for determining the hidden state of the status bar.
- [var childForStatusBarStyle: UIViewController?](uiviewcontroller/childforstatusbarstyle.md)
  Called when the system needs the view controller to use for determining status bar style.
- [var preferredStatusBarStyle: UIStatusBarStyle](uiviewcontroller/preferredstatusbarstyle.md)
  The preferred status bar style for the view controller.
- [enum UIStatusBarStyle](uistatusbarstyle.md)
  Constants that describe the style of the device’s status bar.
- [var modalPresentationCapturesStatusBarAppearance: Bool](uiviewcontroller/modalpresentationcapturesstatusbarappearance.md)
  Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](uiviewcontroller/preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](uiviewcontroller/setneedsstatusbarappearanceupdate.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/prefersstatusbarhidden)*