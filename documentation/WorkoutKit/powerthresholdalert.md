# PowerThresholdAlert

**Framework**: Workoutkit  
**Kind**: struct

An alert for a power threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct PowerThresholdAlert
```

## Topics

### Creating power threshold alerts
- [static func power(Double, unit: UnitPower) -> Self](powerthresholdalert/power(_:unit:).md)
  Returns a new power threshold alert for the target value.
- [init(target: Measurement<UnitPower>)](powerthresholdalert/init(target:).md)
  Returns a new power threshold alert for the target measurement.
### Accessing alert data
- [var metric: WorkoutAlertMetric](powerthresholdalert/metric.md)
  The metric for the alert.
- [var target: Measurement<UnitPower>](powerthresholdalert/target.md)
  The target measurement using power units.
- [var targetQuantity: HKQuantity](powerthresholdalert/targetquantity.md)
  A HealthKit quantity that represents the target power threshold.
### Comparing alerts
- [var hashValue: Int](powerthresholdalert/hashvalue.md)
  The hashed value of the power threshold alert.
- [func hash(into: inout Hasher)](powerthresholdalert/hash(into:).md)
  Hashes the essential components of the power threshold alert by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](powerthresholdalert/!=(_:_:).md)
  Returns a Boolean value that indicates whether two power threshold alerts aren’t equal.
- [static func == (PowerThresholdAlert, PowerThresholdAlert) -> Bool](powerthresholdalert/==(_:_:).md)
  Returns a Boolean value that indicates whether two power threshold alerts are equal.
### Initializers
- [init(target: Measurement<UnitPower>, metric: WorkoutAlertMetric)](powerthresholdalert/init(target:metric:).md)
### Default Implementations
- [Equatable Implementations](powerthresholdalert/equatable-implementations.md)
- [WorkoutAlert Implementations](powerthresholdalert/workoutalert-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func power(ClosedRange<Double>, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-57ekz.md)
  Creates a new power alert for the target range.
- [struct PowerRangeAlert](powerrangealert.md)
  An alert for a range of power values.
- [static func power(Double, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-289mz.md)
  Creates an alert for the specified power threshold.
- [static func power(zone: Int) -> Self](workoutalert/power(zone:).md)
  Creates a new alert for the specified power zone.
- [struct PowerZoneAlert](powerzonealert.md)
  An alert for a power zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/powerthresholdalert)*