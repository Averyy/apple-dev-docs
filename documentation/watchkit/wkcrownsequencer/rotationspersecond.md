# rotationsPerSecond

**Framework**: WatchKit  
**Kind**: property

The rotational speed of the crown, measured in rotations per second.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var rotationsPerSecond: Double { get }
```

#### Discussion

This property contains the last reported rotational speed of the crown in rotations per second.  The rotational speed is an absolute value. It is always positive, regardless of the rotation’s direction.

## See Also

- [func crownDidRotate(WKCrownSequencer?, rotationalDelta: Double)](crowndidrotate(_:rotationaldelta:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidrotate(_:rotationaldelta:)))
  Called when the user rotates the crown.
- [var isIdle: Bool](isidle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/isidle))
  A Boolean value indicating whether the crown is at rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/rotationspersecond)*