# UIStatusBarStyle

**Framework**: UIKit  
**Kind**: enum

Constants that describe the style of the device’s status bar.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum UIStatusBarStyle
```

## Topics

### Constants
- [UIStatusBarStyle.default](uistatusbarstyle/default.md)
  A style that automatically selects an appearance for the status bar and updates it dynamically to maintain contrast with the content below it.
- [UIStatusBarStyle.lightContent](uistatusbarstyle/lightcontent.md)
  A light status bar, intended for use on dark backgrounds.
- [UIStatusBarStyle.darkContent](uistatusbarstyle/darkcontent.md)
  A dark status bar, intended for use on light backgrounds.
### Initializers
- [init?(rawValue: Int)](uistatusbarstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var prefersStatusBarHidden: Bool](uiviewcontroller/prefersstatusbarhidden.md)
  Specifies whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarHidden: UIViewController?](uiviewcontroller/childforstatusbarhidden.md)
  The view controller to use for determining the hidden state of the status bar.
- [var childForStatusBarStyle: UIViewController?](uiviewcontroller/childforstatusbarstyle.md)
  Called when the system needs the view controller to use for determining status bar style.
- [var preferredStatusBarStyle: UIStatusBarStyle](uiviewcontroller/preferredstatusbarstyle.md)
  The preferred status bar style for the view controller.
- [var modalPresentationCapturesStatusBarAppearance: Bool](uiviewcontroller/modalpresentationcapturesstatusbarappearance.md)
  Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](uiviewcontroller/preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](uiviewcontroller/setneedsstatusbarappearanceupdate.md)
  Indicates to the system that the view controller status bar attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistatusbarstyle)*