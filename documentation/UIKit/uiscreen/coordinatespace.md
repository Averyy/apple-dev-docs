# coordinateSpace

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current coordinate space of the screen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
var coordinateSpace: any UICoordinateSpace { get }
```

```objc
@property (readonly) id<UICoordinateSpace> coordinateSpace;
```

#### Discussion

The screen’s current coordinate space always reflects any interface orientations applied to the device. Therefore, the bounds of this coordinate space match the [`bounds`](./bounds.md) property of the screen itself.

## See Also

### Getting the coordinate space
- [var fixedCoordinateSpace: any UICoordinateSpace](./fixedcoordinatespace.md)
  The fixed coordinate space of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/coordinatespace)*