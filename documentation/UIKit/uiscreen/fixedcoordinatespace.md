# fixedCoordinateSpace

**Framework**: UIKit  
**Kind**: property

The fixed coordinate space of the screen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var fixedCoordinateSpace: any UICoordinateSpace { get }
```

#### Discussion

The bounds of this coordinate space always reflect the screen dimensions of the device in a portrait-up orientation. You can use this coordinate space in places where you need a fixed frame of reference. For example, if your app saves screen coordinate values to disk, convert those values to the fixed coordinate space before doing so. Saving them in the fixed coordinate space ensures that when your app reads the values later, it can convert them to the current coordinate space correctly.

## See Also

- [var coordinateSpace: any UICoordinateSpace](uiscreen/coordinatespace.md)
  The current coordinate space of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/fixedcoordinatespace)*