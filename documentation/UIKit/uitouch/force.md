# force

**Framework**: UIKit  
**Kind**: property

The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var force: CGFloat { get }
```

#### Discussion

This property is available on devices that support 3D Touch or Apple Pencil. To check at runtime if a device supports 3D Touch, read the value of the [`forceTouchCapability`](uitraitcollection/forcetouchcapability.md) property on the trait collection for any object in your app with a trait environment.

The force reported by Apple Pencil is measured along the axis of the pencil. If you want a force perpendicular to the device, you need to calculate this value using the [`altitudeAngle`](uitouch/altitudeangle.md) value.

The force reported by Apple Pencil is estimated at first, and may not always be updated. To determine if an update is expected, consult [`estimatedPropertiesExpectingUpdates`](uitouch/estimatedpropertiesexpectingupdates.md) and look for a [`force`](uitouch/properties/force.md) flag. In this scenario, [`estimationUpdateIndex`](uitouch/estimationupdateindex.md) contains a non-nil value, which you can correlate with the original touch when the update occurs. When there are no expected force updates, the entire touch sequence usually won’t have updates, so it may be appropriate to apply a custom, tool-specific force curve to the touch sequence.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/force)*