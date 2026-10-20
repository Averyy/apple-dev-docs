# interfaceOrientation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The orientation to use when displaying content in your windows.

**Availability**:
- iOS 13.0+ - Deprecated in 26.0
- iPadOS 13.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use effectiveGeometry.interfaceOrientation instead.

## Declaration

```swift
var interfaceOrientation: UIInterfaceOrientation { get }
```

```objc
@property (nonatomic, readonly) UIInterfaceOrientation interfaceOrientation;
```

#### Discussion

The interface orientation normally corresponds to the device orientation, but it might also be different. For example, the interface orientation does not always match the device orientation when the user enables rotation lock for the device.

## See Also

### Deprecated
- [var coordinateSpace: any UICoordinateSpace](./coordinatespace.md)
  The coordinate space occupied by the scene.
- [UIWindowScene.PresentationStyle](./presentationstyle.md)
  The placement of a window scene relative to other scenes in the workspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/interfaceorientation)*