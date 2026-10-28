# setNeedsStatusBarAppearanceUpdate()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Indicates to the system that the view controller status bar attributes have changed.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func setNeedsStatusBarAppearanceUpdate()
```

```objc
- (void) setNeedsStatusBarAppearanceUpdate;
```

## Discussion

Call this method if the view controller’s status bar attributes, such as hidden/unhidden status or style, change. If you call this method within an animation block, the changes are animated along with the rest of the animation block.

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
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](./preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsstatusbarappearanceupdate())*