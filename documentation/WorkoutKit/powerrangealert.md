# PowerRangeAlert

**Framework**: WorkoutKit  
**Kind**: struct

An alert for a range of power values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct PowerRangeAlert
```

## Topics

### Creating new power range alerts
- [init(target: ClosedRange<Measurement<UnitPower>>)](powerrangealert/init(target:).md)
  Creates a new power alert for the target range.
### Accessing the alert value
- [var target: ClosedRange<Measurement<UnitPower>>](powerrangealert/target.md)
  The target range.
- [var targetQuantityLowerBound: HKQuantity](powerrangealert/targetquantitylowerbound.md)
  The target’s lower bound.
- [var targetQuantityUpperBound: HKQuantity](powerrangealert/targetquantityupperbound.md)
  The target’s upper bound.
### Initializers
- [init(target: ClosedRange<Measurement<UnitPower>>, metric: WorkoutAlertMetric)](powerrangealert/init(target:metric:).md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func power(ClosedRange<Double>, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-57ekz.md)
  Creates a new power alert for the target range.
- [static func power(Double, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-289mz.md)
  Creates an alert for the specified power threshold.
- [struct PowerThresholdAlert](powerthresholdalert.md)
  An alert for a power threshold.
- [static func power(zone: Int) -> Self](workoutalert/power(zone:).md)
  Creates a new alert for the specified power zone.
- [struct PowerZoneAlert](powerzonealert.md)
  An alert for a power zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/powerrangealert)*