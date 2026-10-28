# systemFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current frame of the scene, in system coordinates.

**Availability**:
- Mac Catalyst 16.0+

## Declaration

```swift
var systemFrame: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect systemFrame;
```

## Discussion

This property represents the current frame of the scene in the system coordinate space, where an origin of `(0, 0)` corresponds to the top-left corner of the main display.

## See Also

### Accessing scene geometry
- [var coordinateSpace: any UICoordinateSpace](./coordinatespace.md)
  The coordinate space of the scene
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  The current interface orientation for the scene.
- [var isInterfaceOrientationLocked: Bool](./isinterfaceorientationlocked.md)
  If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/systemframe)*