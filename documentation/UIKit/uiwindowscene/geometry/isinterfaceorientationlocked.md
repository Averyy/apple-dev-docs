# isInterfaceOrientationLocked

**Framework**: UIKit  
**Kind**: property

If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var isInterfaceOrientationLocked: Bool { get }
```

## See Also

- [var systemFrame: CGRect](uiwindowscene/geometry/systemframe.md)
  The current frame of the scene, in system coordinates.
- [var coordinateSpace: any UICoordinateSpace](uiwindowscene/geometry/coordinatespace.md)
  The coordinate space of the scene
- [var interfaceOrientation: UIInterfaceOrientation](uiwindowscene/geometry/interfaceorientation.md)
  The current interface orientation for the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/isinterfaceorientationlocked)*