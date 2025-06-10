# setNeedsUpdateOfPrefersInterfaceOrientationLocked()

**Framework**: UIKit  
**Kind**: method

Call whenever the view controller’s preference for interface orientation lock has changed

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
func setNeedsUpdateOfPrefersInterfaceOrientationLocked()
```

## See Also

- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func setNeedsUpdateOfSupportedInterfaceOrientations()](uiviewcontroller/setneedsupdateofsupportedinterfaceorientations.md)
  Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [var prefersInterfaceOrientationLocked: Bool](uiviewcontroller/prefersinterfaceorientationlocked.md)
  Whether this view controller prefers the scene’s interface orientation to be locked when shown. The default is `NO`. Note that this preference may or may not be honored. See `UIWindowScene.Geometry` for the current state of interface orientation lock.
- [var childViewControllerForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childviewcontrollerforinterfaceorientationlock.md)
  Override to return a child view controller or nil. If non-nil, that view controller’s preference for interface orientation lock will be used. If nil, `self` is used. Whenever the return value changes, call `setNeedsUpdateOfPrefersInterfaceOrientationLocked()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked())*