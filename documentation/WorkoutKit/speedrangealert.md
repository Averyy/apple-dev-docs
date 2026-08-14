# SpeedRangeAlert

**Framework**: WorkoutKit  
**Kind**: struct

An alert for a range of speed values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct SpeedRangeAlert
```

## Topics

### Creating speed range alerts
- [init(target: ClosedRange<Measurement<UnitSpeed>>, metric: WorkoutAlertMetric)](speedrangealert/init(target:metric:).md)
  Creates a new speed alert for the provided range of values.
### Accessing alert data
- [var target: ClosedRange<Measurement<UnitSpeed>>](speedrangealert/target.md)
  The target range of speed measurements.
- [var targetQuantityLowerBound: HKQuantity](speedrangealert/targetquantitylowerbound.md)
  The target range’s lower bounds.
- [var targetQuantityUpperBound: HKQuantity](speedrangealert/targetquantityupperbound.md)
  The target range’s upper bounds.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func speed(ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](workoutalert/speed(_:unit:metric:)-1o2j.md)
  Creates a new speed alert for the provided range.
- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](workoutalert/speed(_:unit:metric:)-4zald.md)
  Creates a new speed threshold alert.
- [struct SpeedThresholdAlert](speedthresholdalert.md)
  An alert for a speed threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedrangealert)*