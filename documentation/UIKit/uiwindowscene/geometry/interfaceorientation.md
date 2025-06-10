# interfaceOrientation

**Framework**: UIKit  
**Kind**: property

The current interface orientation for the scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var interfaceOrientation: UIInterfaceOrientation { get }
```

## See Also

- [var systemFrame: CGRect](uiwindowscene/geometry/systemframe.md)
  The current frame of the scene, in system coordinates.
- [var coordinateSpace: any UICoordinateSpace](uiwindowscene/geometry/coordinatespace.md)
  The coordinate space of the scene
- [var isInterfaceOrientationLocked: Bool](uiwindowscene/geometry/isinterfaceorientationlocked.md)
  If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/interfaceorientation)*