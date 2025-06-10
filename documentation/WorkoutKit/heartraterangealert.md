# HeartRateRangeAlert

**Framework**: WorkoutKit  
**Kind**: struct

An alert for a range of heart rates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct HeartRateRangeAlert
```

## Topics

### Creating new heart rate alerts
- [static func heartRate(ClosedRange<Double>, unit: UnitFrequency) -> Self](heartraterangealert/heartrate(_:unit:).md)
  Returns a new heart rate alert for the target range.
- [init(target: ClosedRange<Measurement<UnitFrequency>>)](heartraterangealert/init(target:).md)
  Creates a new heart rate alert for a closed range of measurements.
### Accessing the alert data
- [var metric: WorkoutAlertMetric](heartraterangealert/metric.md)
  The metric for the alert.
- [var target: ClosedRange<Measurement<UnitFrequency>>](heartraterangealert/target.md)
  The target range.
- [var targetQuantityLowerBound: HKQuantity](heartraterangealert/targetquantitylowerbound.md)
  The target’s lower bound.
- [var targetQuantityUpperBound: HKQuantity](heartraterangealert/targetquantityupperbound.md)
  The target’s upper bound.
### Comparing heart rate range alerts
- [var hashValue: Int](heartraterangealert/hashvalue.md)
  The hashed value of the heart rate range alert.
- [func hash(into: inout Hasher)](heartraterangealert/hash(into:).md)
  Hashes the essential components of the heart rate range alert by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](heartraterangealert/!=(_:_:).md)
  Returns a Boolean value that indicates whether two heart rate range alerts aren’t equal.
- [static func == (HeartRateRangeAlert, HeartRateRangeAlert) -> Bool](heartraterangealert/==(_:_:).md)
  Returns a Boolean value that indicates whether two heart rate range alerts are equal.
### Default Implementations
- [Equatable Implementations](heartraterangealert/equatable-implementations.md)
- [WorkoutAlert Implementations](heartraterangealert/workoutalert-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func heartRate(ClosedRange<Double>, unit: UnitFrequency) -> Self](workoutalert/heartrate(_:unit:).md)
  Creates a new heart rate alert for the target range.
- [static func heartRate(zone: Int) -> Self](workoutalert/heartrate(zone:).md)
  Creates a new alert for the specified heart rate zone.
- [struct HeartRateZoneAlert](heartratezonealert.md)
  An alert for a heart rate zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/heartraterangealert)*