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
  A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked.md)
  Indicates that the view controller changed the interface orientation lock preference.
- [var childForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childforinterfaceorientationlock.md)
  A child view controller to query for the interface orientation lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredinterfaceorientationforpresentation)*