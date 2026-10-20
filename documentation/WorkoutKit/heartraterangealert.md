# HeartRateRangeAlert

**Framework**: WorkoutKit  
**Kind**: struct  
**Role**: Structure

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
- [init(target: ClosedRange<Measurement<UnitFrequency>>)](./heartraterangealert/init%28target%29.md)
  Creates a new heart rate alert for a closed range of measurements.
### Accessing the alert data
- [var target: ClosedRange<Measurement<UnitFrequency>>](./heartraterangealert/target.md)
  The target range.
- [var targetQuantityLowerBound: HKQuantity](./heartraterangealert/targetquantitylowerbound.md)
  The target’s lower bound.
- [var targetQuantityUpperBound: HKQuantity](./heartraterangealert/targetquantityupperbound.md)
  The target’s upper bound.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [WorkoutAlert](./workoutalert.md)

## See Also

### Creating heart rate alerts
- [static func heartRate(ClosedRange<Double>, unit: UnitFrequency) -> Self](./workoutalert/heartrate%28_,unit%29.md)
  Creates a new heart rate alert for the target range.
- [static func heartRate(zone: Int) -> Self](./workoutalert/heartrate%28zone%29.md)
  Creates a new alert for the specified heart rate zone.
- [struct HeartRateZoneAlert](./heartratezonealert.md)
  An alert for a heart rate zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/heartraterangealert)*