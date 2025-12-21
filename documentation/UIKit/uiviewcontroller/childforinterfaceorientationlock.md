# childForInterfaceOrientationLock

**Framework**: UIKit  
**Kind**: property

A child view controller to query for the interface orientation lock preference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
var childForInterfaceOrientationLock: UIViewController? { get }
```

#### Discussion

Override to return a child view controller or `nil`. If you return a view controller, the system uses that view controller’s preference for interface orientation lock. If you return `nil`, the system uses `self` to get the preference for interface orientation lock. Call [`setNeedsUpdateOfPrefersInterfaceOrientationLocked()`](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked().md) if the child view controller that the system needs to query for the interface orientation lock preference changes.

## See Also

- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func setNeedsUpdateOfSupportedInterfaceOrientations()](uiviewcontroller/setneedsupdateofsupportedinterfaceorientations.md)
  Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [var prefersInterfaceOrientationLocked: Bool](uiviewcontroller/prefersinterfaceorientationlocked.md)
  A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked.md)
  Indicates that the view controller changed the interface orientation lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforinterfaceorientationlock)*