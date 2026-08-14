# HeartRateRangeAlert

**Framework**: WorkoutKit  
**Kind**: struct

An alert for a range of heart rates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct HeartRateRangeAlert
```

## Topics

### Creating new heart rate alerts
- [init(target: ClosedRange<Measurement<UnitFrequency>>)](heartraterangealert/init(target:).md)
  Creates a new heart rate alert for a closed range of measurements.
### Accessing the alert data
- [var target: ClosedRange<Measurement<UnitFrequency>>](heartraterangealert/target.md)
  The target range.
- [var targetQuantityLowerBound: HKQuantity](heartraterangealert/targetquantitylowerbound.md)
  The target’s lower bound.
- [var targetQuantityUpperBound: HKQuantity](heartraterangealert/targetquantityupperbound.md)
  The target’s upper bound.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
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