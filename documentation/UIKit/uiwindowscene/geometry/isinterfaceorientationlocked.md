# isInterfaceOrientationLocked

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var isInterfaceOrientationLocked: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isInterfaceOrientationLocked) BOOL interfaceOrientationLocked;
```

## See Also

### Accessing scene geometry
- [var systemFrame: CGRect](./systemframe.md)
  The current frame of the scene, in system coordinates.
- [var coordinateSpace: any UICoordinateSpace](./coordinatespace.md)
  The coordinate space of the scene
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  The current interface orientation for the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometry/isinterfaceorientationlocked)*