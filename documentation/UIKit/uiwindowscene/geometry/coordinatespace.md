# coordinateSpace

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) id<UICoordinateSpace> coordinateSpace;
```

## See Also

### Accessing scene geometry
- [var systemFrame: CGRect](./systemframe.md)
  The current frame of the scene, in system coordinates.
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  The current interface orientation for the scene.
- [var isInterfaceOrientationLocked: Bool](./isinterfaceorientationlocked.md)
  If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/coordinatespace)*