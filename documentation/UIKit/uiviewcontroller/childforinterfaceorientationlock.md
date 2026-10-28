# childForInterfaceOrientationLock

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A child view controller to query for the interface orientation lock preference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var childForInterfaceOrientationLock: UIViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIViewController * childViewControllerForInterfaceOrientationLock;
```

## Discussion

Override to return a child view controller or `nil`. If you return a view controller, the system uses that view controller’s preference for interface orientation lock. If you return `nil`, the system uses `self` to get the preference for interface orientation lock. Call [`setNeedsUpdateOfPrefersInterfaceOrientationLocked()`](./setneedsupdateofprefersinterfaceorientationlocked%28%29.md) if the child view controller that the system needs to query for the interface orientation lock preference changes.

## See Also

### Configuring the view rotation settings
- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](./supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](./preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func setNeedsUpdateOfSupportedInterfaceOrientations()](./setneedsupdateofsupportedinterfaceorientations%28%29.md)
  Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [var prefersInterfaceOrientationLocked: Bool](./prefersinterfaceorientationlocked.md)
  A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](./setneedsupdateofprefersinterfaceorientationlocked%28%29.md)
  Indicates that the view controller changed the interface orientation lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforinterfaceorientationlock)*