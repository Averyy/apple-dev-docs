# azimuthAngle(in:)

**Framework**: UIKit  
**Kind**: method

Returns the azimuth angle (in radians) of the stylus.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func azimuthAngle(in view: UIView?) -> CGFloat
```

#### Return Value

The azimuth angle of the stylus, in radians.

#### Discussion

In the plane of the screen, the azimuth angle is the direction in which the stylus is pointing. With the tip of the stylus touching the screen, the value of this property is `0` radians when the cap end of the stylus (that is, the end opposite of the tip) points along the positive x axis of the device’s screen. The azimuth angle increases as the user swings the cap end of the stylus in a clockwise direction around the tip.

> **Note**:  It is more expensive to get the azimuth angle (as opposed to the azimuth unit vector), but it can also be more convenient

 It is more expensive to get the azimuth angle (as opposed to the azimuth unit vector), but it can also be more convenient

## Parameters

- `view`: The view that contains the stylus’s touch. Pass   to get the azimuth angle that is relative to the touch’s window.

## See Also

- [var tapCount: Int](uitouch/tapcount.md)
  The number of times the finger was tapped for this given touch.
- [var timestamp: TimeInterval](uitouch/timestamp.md)
  The time when the touch occurred or when it was last mutated.
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
- [func azimuthUnitVector(in: UIView?) -> CGVector](uitouch/azimuthunitvector(in:).md)
  Returns a unit vector that points in the direction of the azimuth of the stylus.
- [var rollAngle: CGFloat](uitouch/rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/azimuthangle(in:))*