# coordinateSpace

**Framework**: UIKit  
**Kind**: property

The coordinate space occupied by the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var coordinateSpace: any UICoordinateSpace { get }
```

#### Discussion

Use the provided coordinate space to get the bounds of the scene’s bounds rectangle and to convert points and rectangles to and from other coordinate spaces. For example, use [`coordinateSpace`](uiwindowscene/coordinatespace.md) to convert a point in the scene to the screen coordinate space.

## See Also

- [var traitCollection: UITraitCollection](uiwindowscene/traitcollection.md)
  The traits that describe the current environment of the scene.
- [var interfaceOrientation: UIInterfaceOrientation](uiwindowscene/interfaceorientation.md)
  The orientation to use when displaying content in your windows.
- [var sizeRestrictions: UISceneSizeRestrictions?](uiwindowscene/sizerestrictions.md)
  The minimum and maximum size of the app’s windows.
- [class UISceneSizeRestrictions](uiscenesizerestrictions.md)
  An object that specifies the minimum and maximum sizes for resizable windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/coordinatespace)*