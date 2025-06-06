# modalPresentationCapturesStatusBarAppearance

**Framework**: UIKit  
**Kind**: property

Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var modalPresentationCapturesStatusBarAppearance: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

When you present a view controller by calling the [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method, status bar appearance control is transferred from the presenting to the presented view controller only if the presented controller’s [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) value is [`UIModalPresentationStyle.fullScreen`](uimodalpresentationstyle/fullscreen.md). By setting this property to [`true`](https://developer.apple.com/documentation/swift/true), you specify the presented view controller controls status bar appearance, even though presented non-fullscreen.

The system ignores this property’s value for a view controller presented fullscreen.

## See Also

- [var prefersStatusBarHidden: Bool](uiviewcontroller/prefersstatusbarhidden.md)
  Specifies whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarHidden: UIViewController?](uiviewcontroller/childforstatusbarhidden.md)
  The view controller to use for determining the hidden state of the status bar.
- [var childForStatusBarStyle: UIViewController?](uiviewcontroller/childforstatusbarstyle.md)
  Called when the system needs the view controller to use for determining status bar style.
- [var preferredStatusBarStyle: UIStatusBarStyle](uiviewcontroller/preferredstatusbarstyle.md)
  The preferred status bar style for the view controller.
- [enum UIStatusBarStyle](uistatusbarstyle.md)
  Constants that describe the style of the device’s status bar.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](uiviewcontroller/preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](uiviewcontroller/setneedsstatusbarappearanceupdate.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/modalpresentationcapturesstatusbarappearance)*