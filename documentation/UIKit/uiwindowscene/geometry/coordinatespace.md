# coordinateSpace

**Framework**: UIKit  
**Kind**: property

The coordinate space of the scene

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var coordinateSpace: any UICoordinateSpace { get }
```

## See Also

- [var systemFrame: CGRect](uiwindowscene/geometry/systemframe.md)
  The current frame of the scene, in system coordinates.
- [var interfaceOrientation: UIInterfaceOrientation](uiwindowscene/geometry/interfaceorientation.md)
  The current interface orientation for the scene.
- [var isInterfaceOrientationLocked: Bool](uiwindowscene/geometry/isinterfaceorientationlocked.md)
  If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/coordinatespace)*