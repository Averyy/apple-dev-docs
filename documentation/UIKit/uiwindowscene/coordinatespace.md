# coordinateSpace

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The coordinate space occupied by the scene.

**Availability**:
- iOS 13.0+ - Deprecated in 26.0
- iPadOS 13.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 13.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use effectiveGeometry.coordinateSpace instead.

## Declaration

```swift
var coordinateSpace: any UICoordinateSpace { get }
```

```objc
@property (nonatomic, readonly) id<UICoordinateSpace> coordinateSpace;
```

#### Discussion

Use the provided coordinate space to get the bounds of the scene’s bounds rectangle and to convert points and rectangles to and from other coordinate spaces. For example, use [`coordinateSpace`](./coordinatespace.md) to convert a point in the scene to the screen coordinate space.

## See Also

### Deprecated
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  The orientation to use when displaying content in your windows.
- [UIWindowScene.PresentationStyle](./presentationstyle.md)
  The placement of a window scene relative to other scenes in the workspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/coordinatespace)*