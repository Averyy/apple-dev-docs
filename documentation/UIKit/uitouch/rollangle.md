# rollAngle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A value that represents the current barrel-roll angle of Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 1.2+

## Declaration

```swift
var rollAngle: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat rollAngle;
```

## Discussion

For models of Apple Pencil that don’t support barrel-roll angle data, the value of this property is `0`.

## See Also

### Getting touch attributes
- [var tapCount: Int](./tapcount.md)
  The number of times the finger was tapped for this given touch.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when the touch occurred or when it was last mutated.
- [var type: UITouch.TouchType](./type.md)
  The type of the touch.
- [UITouch.TouchType](./touchtype.md)
  The type of touch received.
- [var phase: UITouch.Phase](./phase-swift.property.md)
  The phase of the touch.
- [UITouch.Phase](./phase-swift.enum.md)
  The phase of a touch event.
- [var force: CGFloat](./force.md)
  The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [var maximumPossibleForce: CGFloat](./maximumpossibleforce.md)
  The maximum possible force for a touch.
- [var altitudeAngle: CGFloat](./altitudeangle.md)
  The altitude (in radians) of the stylus.
- [func azimuthAngle(in: UIView?) -> CGFloat](./azimuthangle%28in%29.md)
  Returns the azimuth angle (in radians) of the stylus.
- [func azimuthUnitVector(in: UIView?) -> CGVector](./azimuthunitvector%28in%29.md)
  Returns a unit vector that points in the direction of the azimuth of the stylus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/rollangle)*