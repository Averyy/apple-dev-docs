# setNeedsUpdateOfPrefersInterfaceOrientationLocked()

**Framework**: UIKit  
**Kind**: method

Indicates that the view controller changed the interface orientation lock preference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

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
  A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [var childForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childforinterfaceorientationlock.md)
  A child view controller to query for the interface orientation lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked())*