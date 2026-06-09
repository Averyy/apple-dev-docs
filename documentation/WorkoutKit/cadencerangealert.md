# CadenceRangeAlert

**Framework**: WorkoutKit  
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
- [init(target: ClosedRange<Measurement<UnitFrequency>>)](cadencerangealert/init(target:).md)
  Creates a cadence alert for a closed range of measurements.
### Accessing the alert data
- [var target: ClosedRange<Measurement<UnitFrequency>>](cadencerangealert/target.md)
  The target range.
- [var targetQuantityLowerBound: HKQuantity](cadencerangealert/targetquantitylowerbound.md)
  The target’s lower bound.
- [var targetQuantityUpperBound: HKQuantity](cadencerangealert/targetquantityupperbound.md)
  The target’s upper bound.

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
- [static func cadence(Double, unit: UnitFrequency) -> Self](workoutalert/cadence(_:unit:)-3fnpg.md)
  Creates an alert for the specified cadence threshold.
- [struct CadenceThresholdAlert](cadencethresholdalert.md)
  An alert for a cadence threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/cadencerangealert)*