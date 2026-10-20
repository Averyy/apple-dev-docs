# phase

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The phase of the touch.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var phase: UITouch.Phase { get }
```

```objc
@property (nonatomic, readonly) UITouchPhase phase;
```

#### Discussion

The property value is a constant that indicates whether the touch began, moved, ended, or was canceled. For descriptions of the possible values of this property, see [`UITouch.Phase`](./phase-swift.enum.md).

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
- [var rollAngle: CGFloat](./rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/phase-swift.property)*