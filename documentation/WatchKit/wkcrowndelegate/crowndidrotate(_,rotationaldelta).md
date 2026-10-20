# crownDidRotate(_:rotationalDelta:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Called when the user rotates the crown.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
optional func crownDidRotate(_ crownSequencer: WKCrownSequencer?, rotationalDelta: Double)
```

```objc
- (void) crownDidRotate:(WKCrownSequencer *) crownSequencer rotationalDelta:(double) rotationalDelta;
```

## Parameters

- `crownSequencer`: The crown sequencer object reporting the change.
- `rotationalDelta`: The amount that the crown has rotated since the last update. A value of `1.0` represents one full rotation. The value’s sign indicates the rotation’s direction, but the sign is adjusted based on the crown’s orientation. Positive values always indicate an upward scrolling gesture, while negative numbers indicate a downward scrolling gesture.

  - If the digital crown is oriented on the right, clockwise rotations generate positive values, while counterclockwise rotations generate negative values.
  - If the digital crown is oriented on the left, the signs are reversed (counterclockwise rotations generate positive values, while clockwise rotations generate negative values).

  The user can change the digital crown’s orientation in the watch’s settings.

## See Also

### Related Documentation
- [var rotationsPerSecond: Double](../wkcrownsequencer/rotationspersecond.md)
  The rotational speed of the crown, measured in rotations per second.
### Receiving Crown Events
- [func crownDidBecomeIdle(WKCrownSequencer?)](./crowndidbecomeidle%28_%29.md)
  Called when the user stops rotating the crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidrotate(_:rotationaldelta:))*