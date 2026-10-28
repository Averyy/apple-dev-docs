# childViewControllerForPointerLock

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A child view controller to query for the pointer lock preference.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var childViewControllerForPointerLock: UIViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIViewController * childViewControllerForPointerLock;
```

## Discussion

Call [`setNeedsUpdateOfPrefersPointerLocked()`](./setneedsupdateofpreferspointerlocked%28%29.md) if the child view controller that the system needs to query for the pointer lock preference changes.

## See Also

### Managing pointer lock state
- [var prefersPointerLocked: Bool](./preferspointerlocked.md)
  A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.
- [func setNeedsUpdateOfPrefersPointerLocked()](./setneedsupdateofpreferspointerlocked%28%29.md)
  Indicates that the view controller changed the pointer lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerforpointerlock)*