# CadenceRangeAlert

**Framework**: Workoutkit  
**Kind**: struct

An alert for a range of cadence values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct CadenceRangeAlert
```

## Topics

### Creating new cadence range alerts
- [static func cadence(ClosedRange<Double>, unit: UnitFrequency) -> Self](cadencerangealert/cadence(_:unit:).md)
  Creates a new cadence alert for the target range.
- [init(target: ClosedRange<Measurement<UnitFrequency>>)](cadencerangealert/init(target:).md)
  Creates a cadence alert for a closed range of measurements.
### Accessing the alert data
- [var metric: WorkoutAlertMetric](cadencerangealert/metric.md)
  The metric for the alert.
- [var target: ClosedRange<Measurement<UnitFrequency>>](cadencerangealert/target.md)
  The target range.
- [var targetQuantityLowerBound: HKQuantity](cadencerangealert/targetquantitylowerbound.md)
  The target’s lower bound.
- [var targetQuantityUpperBound: HKQuantity](cadencerangealert/targetquantityupperbound.md)
  The target’s upper bound.
### Comparing alerts
- [var hashValue: Int](cadencerangealert/hashvalue.md)
  The hashed value of the cadence range alert.
- [func hash(into: inout Hasher)](cadencerangealert/hash(into:).md)
  Hashes the essential components of the cadence range alert by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](cadencerangealert/!=(_:_:).md)
  Returns a Boolean value that indicates whether two cadence range alerts aren’t equal.
- [static func == (CadenceRangeAlert, CadenceRangeAlert) -> Bool](cadencerangealert/==(_:_:).md)
  Returns a Boolean value that indicates whether two cadence range alerts are equal.
### Default Implementations
- [Equatable Implementations](cadencerangealert/equatable-implementations.md)
- [WorkoutAlert Implementations](cadencerangealert/workoutalert-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func cadence(ClosedRange<Double>, unit: UnitFrequency) -> Self](workoutalert/cadence(_:unit:)-y8da.md)
  Creates a new alert for a range of cadence values.
- [static func cadence(Double, unit: UnitFrequency) -> Self](workoutalert/cadence(_:unit:)-3fnpg.md)
  Creates an alert for the specified cadence threshold.
- [struct CadenceThresholdAlert](cadencethresholdalert.md)
  An alert for a cadence threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/cadencerangealert)*