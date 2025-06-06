# traitCollection

**Framework**: UIKit  
**Kind**: property

The traits that describe the current environment of the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var traitCollection: UITraitCollection { get }
```

#### Discussion

Use this property to get additional information about the current scene, such as the size class and scale factor. For more information about the available traits, see [`UITraitCollection`](uitraitcollection.md).

## See Also

- [var coordinateSpace: any UICoordinateSpace](uiwindowscene/coordinatespace.md)
  The coordinate space occupied by the scene.
- [var interfaceOrientation: UIInterfaceOrientation](uiwindowscene/interfaceorientation.md)
  The orientation to use when displaying content in your windows.
- [var sizeRestrictions: UISceneSizeRestrictions?](uiwindowscene/sizerestrictions.md)
  The minimum and maximum size of the app’s windows.
- [class UISceneSizeRestrictions](uiscenesizerestrictions.md)
  An object that specifies the minimum and maximum sizes for resizable windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/traitcollection)*