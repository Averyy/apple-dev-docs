# setNeedsUpdateOfPrefersInterfaceOrientationLocked()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the view controller changed the interface orientation lock preference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func setNeedsUpdateOfPrefersInterfaceOrientationLocked()
```

```objc
- (void) setNeedsUpdateOfPrefersInterfaceOrientationLocked;
```

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
- [var childForInterfaceOrientationLock: UIViewController?](./childforinterfaceorientationlock.md)
  A child view controller to query for the interface orientation lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked())*