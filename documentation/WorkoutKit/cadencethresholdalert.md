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
- [init(target: Measurement<UnitFrequency>)](cadencethresholdalert/init(target:).md)
  Create a new cadence threshold alert for the target measurement.
### Accessing the alert data
- [var target: Measurement<UnitFrequency>](cadencethresholdalert/target.md)
  The target threshold.
- [var targetQuantity: HKQuantity](cadencethresholdalert/targetquantity.md)
  A HealthKit quantity that represents the target cadence threshold.

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