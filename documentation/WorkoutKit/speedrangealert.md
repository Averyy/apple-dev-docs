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
- [static func speed(ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](speedrangealert/speed(_:unit:metric:).md)
  Returns a new speed alert for the provided range of values.
- [init(target: ClosedRange<Measurement<UnitSpeed>>, metric: WorkoutAlertMetric)](speedrangealert/init(target:metric:).md)
  Creates a new speed alert for the provided range of values.
### Accessing alert data
- [var target: ClosedRange<Measurement<UnitSpeed>>](speedrangealert/target.md)
  The target range of speed measurements.
- [var targetQuantityLowerBound: HKQuantity](speedrangealert/targetquantitylowerbound.md)
  The target range’s lower bounds.
- [var targetQuantityUpperBound: HKQuantity](speedrangealert/targetquantityupperbound.md)
  The target range’s upper bounds.
- [var metric: WorkoutAlertMetric](speedrangealert/metric.md)
  The metric used to measure the speed.
### Comparing alerts
- [var hashValue: Int](speedrangealert/hashvalue.md)
  The hashed value of the speed range alert.
- [func hash(into: inout Hasher)](speedrangealert/hash(into:).md)
  Hashes the essential components of the speed range alert by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](speedrangealert/!=(_:_:).md)
  Returns a Boolean value that indicates whether two speed range alerts aren’t equal.
- [static func == (SpeedRangeAlert, SpeedRangeAlert) -> Bool](speedrangealert/==(_:_:).md)
  Returns a Boolean value that indicates whether two speed range alerts are equal.
### Default Implementations
- [Equatable Implementations](speedrangealert/equatable-implementations.md)
- [WorkoutAlert Implementations](speedrangealert/workoutalert-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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