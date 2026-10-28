# isIdle

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the crown is at rest.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var isIdle: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isIdle) BOOL idle;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the user is not rotating the crown and [`false`](../../Swift/false.md) when the user is rotating the crown.

## See Also

### Related Documentation
- [func crownDidBecomeIdle(WKCrownSequencer?)](../wkcrowndelegate/crowndidbecomeidle%28_%29.md)
  Called when the user stops rotating the crown.
### Getting the Current Crown Status
- [var rotationsPerSecond: Double](./rotationspersecond.md)
  The rotational speed of the crown, measured in rotations per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/isidle)*