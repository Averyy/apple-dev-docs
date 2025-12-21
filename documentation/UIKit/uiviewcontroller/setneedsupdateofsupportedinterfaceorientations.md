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
  A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked.md)
  Indicates that the view controller changed the interface orientation lock preference.
- [var childForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childforinterfaceorientationlock.md)
  A child view controller to query for the interface orientation lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofsupportedinterfaceorientations())*