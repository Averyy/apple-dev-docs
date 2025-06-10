# setNeedsUpdateOfSupportedInterfaceOrientations()

**Framework**: UIKit  
**Kind**: method

Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNeedsUpdateOfSupportedInterfaceOrientations()
```

#### Discussion

By default, this method animates any changes to orientation. To perform a nonanimated update, call this method from [`performWithoutAnimation(_:)`](uiview/performwithoutanimation(_:).md).

## See Also

- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [var prefersInterfaceOrientationLocked: Bool](uiviewcontroller/prefersinterfaceorientationlocked.md)
  Whether this view controller prefers the scene’s interface orientation to be locked when shown. The default is `NO`. Note that this preference may or may not be honored. See `UIWindowScene.Geometry` for the current state of interface orientation lock.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked.md)
  Call whenever the view controller’s preference for interface orientation lock has changed
- [var childViewControllerForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childviewcontrollerforinterfaceorientationlock.md)
  Override to return a child view controller or nil. If non-nil, that view controller’s preference for interface orientation lock will be used. If nil, `self` is used. Whenever the return value changes, call `setNeedsUpdateOfPrefersInterfaceOrientationLocked()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofsupportedinterfaceorientations())*