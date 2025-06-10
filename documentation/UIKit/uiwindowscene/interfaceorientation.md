# interfaceOrientation

**Framework**: UIKit  
**Kind**: property

The orientation to use when displaying content in your windows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var interfaceOrientation: UIInterfaceOrientation { get }
```

#### Discussion

The interface orientation normally corresponds to the device orientation, but it might also be different. For example, the interface orientation does not always match the device orientation when the user enables rotation lock for the device.

## See Also

- [var coordinateSpace: any UICoordinateSpace](uiwindowscene/coordinatespace.md)
  The coordinate space occupied by the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/interfaceorientation)*