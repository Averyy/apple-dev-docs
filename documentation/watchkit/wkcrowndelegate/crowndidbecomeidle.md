# crownDidBecomeIdle(_:)

**Framework**: Watchkit  
**Kind**: method

Called when the user stops rotating the crown.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
optional func crownDidBecomeIdle(_ crownSequencer: WKCrownSequencer?)
```

#### Discussion

The crown sequencer calls this method when the crown finally comes to rest. The sequencer calls this method only after one or more calls to the [`crownDidRotate(_:rotationalDelta:)`](wkcrowndelegate/crowndidrotate(_:rotationaldelta:).md) method.

## Parameters

- `crownSequencer`: The crown sequencer object reporting the change.

## See Also

- [var isIdle: Bool](wkcrownsequencer/isidle.md)
  A Boolean value indicating whether the crown is at rest.
- [func crownDidRotate(WKCrownSequencer?, rotationalDelta: Double)](wkcrowndelegate/crowndidrotate(_:rotationaldelta:).md)
  Called when the user rotates the crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidbecomeidle(_:))*