# preferredStatusBarStyle

**Framework**: UIKit  
**Kind**: property

The preferred status bar style for the view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredStatusBarStyle: UIStatusBarStyle { get }
```

#### Return Value

A [`UIStatusBarStyle`](uistatusbarstyle.md) key indicating your preferred status bar style for the view controller.

#### Discussion

You can override the preferred status bar style for a view controller by implementing the [`childForStatusBarStyle`](uiviewcontroller/childforstatusbarstyle.md) method.

If the return value from this method changes, call the [`setNeedsStatusBarAppearanceUpdate()`](uiviewcontroller/setneedsstatusbarappearanceupdate().md) method.

## See Also

- [var prefersStatusBarHidden: Bool](uiviewcontroller/prefersstatusbarhidden.md)
  Specifies whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarHidden: UIViewController?](uiviewcontroller/childforstatusbarhidden.md)
  The view controller to use for determining the hidden state of the status bar.
- [var childForStatusBarStyle: UIViewController?](uiviewcontroller/childforstatusbarstyle.md)
  Called when the system needs the view controller to use for determining status bar style.
- [enum UIStatusBarStyle](uistatusbarstyle.md)
  Constants that describe the style of the device’s status bar.
- [var modalPresentationCapturesStatusBarAppearance: Bool](uiviewcontroller/modalpresentationcapturesstatusbarappearance.md)
  Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](uiviewcontroller/preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](uiviewcontroller/setneedsstatusbarappearanceupdate.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle)*