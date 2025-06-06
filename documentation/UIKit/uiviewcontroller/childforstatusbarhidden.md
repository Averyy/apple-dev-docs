# childForStatusBarHidden

**Framework**: UIKit  
**Kind**: property

The view controller to use for determining the hidden state of the status bar.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var childForStatusBarHidden: UIViewController? { get }
```

#### Discussion

If your container view controller derives the hidden state of the status bar from one of its child view controllers, implement this property to specify which child view controller you want to control the hidden/unhidden state. If you return `nil` or don’t override this property, the status bar hidden/unhidden state for `self` is used.

Call [`setNeedsStatusBarAppearanceUpdate()`](uiviewcontroller/setneedsstatusbarappearanceupdate().md) if the child view controller for determining the hidden state of the status bar changes.

## See Also

- [var prefersStatusBarHidden: Bool](uiviewcontroller/prefersstatusbarhidden.md)
  Specifies whether the view controller prefers the status bar to be hidden or shown.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforstatusbarhidden)*