# SpeedThresholdAlert

**Framework**: Workoutkit  
**Kind**: struct

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
- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](speedthresholdalert/speed(_:unit:metric:).md)
  Returns a new speed threshold alert.
- [init(target: Measurement<UnitSpeed>, metric: WorkoutAlertMetric)](speedthresholdalert/init(target:metric:).md)
  Creates a new speed threshold alert.
### Accessing alert data
- [var target: Measurement<UnitSpeed>](speedthresholdalert/target.md)
  A speed measurement that represents the target threshold.
- [var targetQuantity: HKQuantity](speedthresholdalert/targetquantity.md)
  A HealthKit quantity that represents the target speed threshold.
- [var metric: WorkoutAlertMetric](speedthresholdalert/metric.md)
  The metric used to measure the speed.
### Comparing alerts
- [var hashValue: Int](speedthresholdalert/hashvalue.md)
  The hashed value of the speed threshold alert.
- [func hash(into: inout Hasher)](speedthresholdalert/hash(into:).md)
  Hashes the essential components of the speed threshold alert by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](speedthresholdalert/!=(_:_:).md)
  Returns a Boolean value that indicates whether two speed threshold alerts aren’t equal.
- [static func == (SpeedThresholdAlert, SpeedThresholdAlert) -> Bool](speedthresholdalert/==(_:_:).md)
  Returns a Boolean value that indicates whether two speed threshold alerts are equal.
### Default Implementations
- [Equatable Implementations](speedthresholdalert/equatable-implementations.md)
- [WorkoutAlert Implementations](speedthresholdalert/workoutalert-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func speed(ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](workoutalert/speed(_:unit:metric:)-1o2j.md)
  Creates a new speed alert for the provided range.
- [struct SpeedRangeAlert](speedrangealert.md)
  An alert for a range of speed values.
- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](workoutalert/speed(_:unit:metric:)-4zald.md)
  Creates a new speed threshold alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedthresholdalert)*