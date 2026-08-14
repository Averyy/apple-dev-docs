# isIdle

**Framework**: WatchKit  
**Kind**: property

A Boolean value indicating whether the crown is at rest.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var isIdle: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the user is not rotating the crown and [`false`](https://developer.apple.com/documentation/swift/false) when the user is rotating the crown.

## See Also

- [func crownDidBecomeIdle(WKCrownSequencer?)](wkcrowndelegate/crowndidbecomeidle(_:).md)
  Called when the user stops rotating the crown.
- [var rotationsPerSecond: Double](wkcrownsequencer/rotationspersecond.md)
  The rotational speed of the crown, measured in rotations per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/isidle)*