# SpeedThresholdAlert

**Framework**: WorkoutKit  
**Kind**: struct  
**Role**: Structure

An alert for a speed threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct SpeedThresholdAlert
```

## Topics

### Creating speed threshold alerts
- [init(target: Measurement<UnitSpeed>, metric: WorkoutAlertMetric)](./speedthresholdalert/init%28target,metric%29.md)
  Creates a new speed threshold alert.
### Accessing alert data
- [var target: Measurement<UnitSpeed>](./speedthresholdalert/target.md)
  A speed measurement that represents the target threshold.
- [var targetQuantity: HKQuantity](./speedthresholdalert/targetquantity.md)
  A HealthKit quantity that represents the target speed threshold.

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
- [struct SpeedRangeAlert](./speedrangealert.md)
  An alert for a range of speed values.
- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](./workoutalert/speed%28_,unit,metric%29-4zald.md)
  Creates a new speed threshold alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedthresholdalert)*