# crownDidRotate(_:rotationalDelta:)

**Framework**: WatchKit  
**Kind**: method

Called when the user rotates the crown.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
optional func crownDidRotate(_ crownSequencer: WKCrownSequencer?, rotationalDelta: Double)
```

## Parameters

- `crownSequencer`: The crown sequencer object reporting the change.
- `rotationalDelta`: The user can change the digital crown’s orientation in the watch’s settings.

## See Also

- [var rotationsPerSecond: Double](rotationspersecond.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/rotationspersecond))
  The rotational speed of the crown, measured in rotations per second.
- [func crownDidBecomeIdle(WKCrownSequencer?)](crowndidbecomeidle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidbecomeidle(_:)))
  Called when the user stops rotating the crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidrotate(_:rotationaldelta:))*