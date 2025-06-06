# childViewControllerForPointerLock

**Framework**: UIKit  
**Kind**: property

A child view controller to query for the pointer lock preference.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var childViewControllerForPointerLock: UIViewController? { get }
```

#### Discussion

Call [`setNeedsUpdateOfPrefersPointerLocked()`](uiviewcontroller/setneedsupdateofpreferspointerlocked().md) if the child view controller that the system needs to query for the pointer lock preference changes.

## See Also

- [var prefersPointerLocked: Bool](uiviewcontroller/preferspointerlocked.md)
  A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.
- [func setNeedsUpdateOfPrefersPointerLocked()](uiviewcontroller/setneedsupdateofpreferspointerlocked.md)
  Indicates that the view controller changed the pointer lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerforpointerlock)*