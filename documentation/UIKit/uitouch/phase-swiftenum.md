# UITouch.Phase

**Framework**: UIKit  
**Kind**: enum

The phase of a touch event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Phase
```

#### Overview

The phase of a `UITouch` instance changes as the system receives updates during the course of an event. Access this value through the [`phase`](uitouch/phase-swift.property.md) property.

## Topics

### Constants
- [UITouch.Phase.began](uitouch/phase-swift.enum/began.md)
  A touch for a given event has pressed down on the screen.
- [UITouch.Phase.moved](uitouch/phase-swift.enum/moved.md)
  A touch for a given event has moved over the screen.
- [UITouch.Phase.stationary](uitouch/phase-swift.enum/stationary.md)
  A touch for a given event is pressed down on the screen, but hasn’t moved since the previous event.
- [UITouch.Phase.ended](uitouch/phase-swift.enum/ended.md)
  A touch for a given event has lifted from the screen.
- [UITouch.Phase.cancelled](uitouch/phase-swift.enum/cancelled.md)
  The system canceled tracking for a touch, for example, when the user moves the device against their face.
- [UITouch.Phase.regionEntered](uitouch/phase-swift.enum/regionentered.md)
  A touch for a given event has entered a window on the screen.
- [UITouch.Phase.regionMoved](uitouch/phase-swift.enum/regionmoved.md)
  A touch for the given event is within a window on the screen, but has not yet pressed down.
- [UITouch.Phase.regionExited](uitouch/phase-swift.enum/regionexited.md)
  A touch for a given event has left a window on the screen.
### Initializers
- [init?(rawValue: Int)](uitouch/phase-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/phase-swift.enum)*