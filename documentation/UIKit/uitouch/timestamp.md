# timestamp

**Framework**: UIKit  
**Kind**: property

The time when the touch occurred or when it was last mutated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var timestamp: TimeInterval { get }
```

#### Discussion

The value of this property is the time, in seconds since system startup, that the touch originated or was last changed. You can store the value of this property and compare it to the timestamp in subsequent [`UITouch`](uitouch.md) objects to determine the duration of the touch and, if it is being swiped, the speed of movement. For a definition of the time since system startup, see the description of the [`systemUptime`](https://developer.apple.com/documentation/Foundation/ProcessInfo/systemUptime) method of the [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo) class.

## See Also

- [var tapCount: Int](uitouch/tapcount.md)
  The number of times the finger was tapped for this given touch.
- [var type: UITouch.TouchType](uitouch/type.md)
  The type of the touch.
- [UITouch.TouchType](uitouch/touchtype.md)
  The type of touch received.
- [var phase: UITouch.Phase](uitouch/phase-swift.property.md)
  The phase of the touch.
- [UITouch.Phase](uitouch/phase-swift.enum.md)
  The phase of a touch event.
- [var force: CGFloat](uitouch/force.md)
  The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [var maximumPossibleForce: CGFloat](uitouch/maximumpossibleforce.md)
  The maximum possible force for a touch.
- [var altitudeAngle: CGFloat](uitouch/altitudeangle.md)
  The altitude (in radians) of the stylus.
- [func azimuthAngle(in: UIView?) -> CGFloat](uitouch/azimuthangle(in:).md)
  Returns the azimuth angle (in radians) of the stylus.
- [func azimuthUnitVector(in: UIView?) -> CGVector](uitouch/azimuthunitvector(in:).md)
  Returns a unit vector that points in the direction of the azimuth of the stylus.
- [var rollAngle: CGFloat](uitouch/rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/timestamp)*