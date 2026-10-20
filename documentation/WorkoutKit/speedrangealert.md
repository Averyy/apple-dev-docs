# SpeedRangeAlert

**Framework**: WorkoutKit  
**Kind**: struct  
**Role**: Structure

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
- [init(target: ClosedRange<Measurement<UnitSpeed>>, metric: WorkoutAlertMetric)](./speedrangealert/init%28target,metric%29.md)
  Creates a new speed alert for the provided range of values.
### Accessing alert data
- [var target: ClosedRange<Measurement<UnitSpeed>>](./speedrangealert/target.md)
  The target range of speed measurements.
- [var targetQuantityLowerBound: HKQuantity](./speedrangealert/targetquantitylowerbound.md)
  The target range’s lower bounds.
- [var targetQuantityUpperBound: HKQuantity](./speedrangealert/targetquantityupperbound.md)
  The target range’s upper bounds.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [WorkoutAlert](./workoutalert.md)

## See Also

### Creating speed alerts
- [static func speed(ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](./workoutalert/speed%28_,unit,metric%29-1o2j.md)
  Creates a new speed alert for the provided range.
- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](./workoutalert/speed%28_,unit,metric%29-4zald.md)
  Creates a new speed threshold alert.
- [struct SpeedThresholdAlert](./speedthresholdalert.md)
  An alert for a speed threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedrangealert)*