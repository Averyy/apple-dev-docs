# coordinateSpace

**Framework**: UIKit  
**Kind**: property

The current coordinate space of the screen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var coordinateSpace: any UICoordinateSpace { get }
```

#### Discussion

The screen’s current coordinate space always reflects any interface orientations applied to the device. Therefore, the bounds of this coordinate space match the [`bounds`](uiscreen/bounds.md) property of the screen itself.

## See Also

- [var fixedCoordinateSpace: any UICoordinateSpace](uiscreen/fixedcoordinatespace.md)
  The fixed coordinate space of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/coordinatespace)*