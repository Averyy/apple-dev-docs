# CadenceThresholdAlert

**Framework**: WorkoutKit  
**Kind**: struct

An alert for a cadence threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct CadenceThresholdAlert
```

## Topics

### Creating new cadence threshold alerts
- [static func cadence(Double, unit: UnitFrequency) -> Self](cadencethresholdalert/cadence(_:unit:).md)
  Returns a new cadence threshold alert for the target value.
- [init(target: Measurement<UnitFrequency>)](cadencethresholdalert/init(target:).md)
  Create a new cadence threshold alert for the target measurement.
### Accessing the alert data
- [var metric: WorkoutAlertMetric](cadencethresholdalert/metric.md)
  The metric for the alert.
- [var target: Measurement<UnitFrequency>](cadencethresholdalert/target.md)
  The target threshold.
- [var targetQuantity: HKQuantity](cadencethresholdalert/targetquantity.md)
  A HealthKit quantity that represents the target cadence threshold.
### Comparing cadence threshold alerts
- [var hashValue: Int](cadencethresholdalert/hashvalue.md)
  The hashed value of the cadence threshold alert.
- [func hash(into: inout Hasher)](cadencethresholdalert/hash(into:).md)
  Hashes the essential components of the cadence threshold alert by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](cadencethresholdalert/!=(_:_:).md)
  Returns a Boolean value that indicates whether two cadence threshold alerts aren’t equal.
- [static func == (CadenceThresholdAlert, CadenceThresholdAlert) -> Bool](cadencethresholdalert/==(_:_:).md)
  Returns a Boolean value that indicates whether two cadence threshold alerts are equal.
### Default Implementations
- [Equatable Implementations](cadencethresholdalert/equatable-implementations.md)
- [WorkoutAlert Implementations](cadencethresholdalert/workoutalert-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func cadence(ClosedRange<Double>, unit: UnitFrequency) -> Self](workoutalert/cadence(_:unit:)-y8da.md)
  Creates a new alert for a range of cadence values.
- [struct CadenceRangeAlert](cadencerangealert.md)
  An alert for a range of cadence values.
- [static func cadence(Double, unit: UnitFrequency) -> Self](workoutalert/cadence(_:unit:)-3fnpg.md)
  Creates an alert for the specified cadence threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/cadencethresholdalert)*