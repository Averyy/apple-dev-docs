# rotationsPerSecond

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The rotational speed of the crown, measured in rotations per second.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var rotationsPerSecond: Double { get }
```

```objc
@property (nonatomic, readonly) double rotationsPerSecond;
```

#### Discussion

This property contains the last reported rotational speed of the crown in rotations per second.  The rotational speed is an absolute value. It is always positive, regardless of the rotation’s direction.

## See Also

### Related Documentation
- [func crownDidRotate(WKCrownSequencer?, rotationalDelta: Double)](../wkcrowndelegate/crowndidrotate%28_,rotationaldelta%29.md)
  Called when the user rotates the crown.
### Getting the Current Crown Status
- [var isIdle: Bool](./isidle.md)
  A Boolean value indicating whether the crown is at rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/rotationspersecond)*