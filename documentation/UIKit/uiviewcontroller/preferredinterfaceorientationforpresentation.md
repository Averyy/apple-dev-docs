# preferredInterfaceOrientationForPresentation

**Framework**: UIKit  
**Kind**: property

The interface orientation to use when presenting the view controller.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }
```

#### Return Value

The interface orientation with which to present the view controller.

#### Discussion

The system calls this method when presenting the view controller full screen. When your view controller supports two or more orientations but the content appears best in one of those orientations, override this method and return the preferred orientation.

If your view controller implements this method, your view controller’s view is shown in the preferred orientation (although it can later be rotated to another supported rotation). If you do not implement this method, the system presents the view controller using the current orientation of the status bar.

## See Also

- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [func setNeedsUpdateOfSupportedInterfaceOrientations()](uiviewcontroller/setneedsupdateofsupportedinterfaceorientations.md)
  Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [var prefersInterfaceOrientationLocked: Bool](uiviewcontroller/prefersinterfaceorientationlocked.md)
  Whether this view controller prefers the scene’s interface orientation to be locked when shown. The default is `NO`. Note that this preference may or may not be honored. See `UIWindowScene.Geometry` for the current state of interface orientation lock.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked.md)
  Call whenever the view controller’s preference for interface orientation lock has changed
- [var childViewControllerForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childviewcontrollerforinterfaceorientationlock.md)
  Override to return a child view controller or nil. If non-nil, that view controller’s preference for interface orientation lock will be used. If nil, `self` is used. Whenever the return value changes, call `setNeedsUpdateOfPrefersInterfaceOrientationLocked()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredinterfaceorientationforpresentation)*