# force

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var force: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat force;
```

#### Discussion

This property is available on devices that support 3D Touch or Apple Pencil. To check at runtime if a device supports 3D Touch, read the value of the [`forceTouchCapability`](../uitraitcollection/forcetouchcapability.md) property on the trait collection for any object in your app with a trait environment.

The force reported by Apple Pencil is measured along the axis of the pencil. If you want a force perpendicular to the device, you need to calculate this value using the [`altitudeAngle`](./altitudeangle.md) value.

The force reported by Apple Pencil is estimated at first, and may not always be updated. To determine if an update is expected, consult [`estimatedPropertiesExpectingUpdates`](./estimatedpropertiesexpectingupdates.md) and look for a [`force`](./properties/force.md) flag. In this scenario, [`estimationUpdateIndex`](./estimationupdateindex.md) contains a non-nil value, which you can correlate with the original touch when the update occurs. When there are no expected force updates, the entire touch sequence usually won’t have updates, so it may be appropriate to apply a custom, tool-specific force curve to the touch sequence.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/force)*