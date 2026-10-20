# HeartRateZoneAlert

**Framework**: WorkoutKit  
**Kind**: struct  
**Role**: Structure

An alert for a heart rate zone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct HeartRateZoneAlert
```

## Topics

### Creating new heart rate zone alerts
- [init(zone: Int)](./heartratezonealert/init%28zone%29.md)
  Creates a new alert for the target heart rate zone.
### Accessing the alert data
- [var zone: Int](./heartratezonealert/zone.md)
  The target heart rate zone.

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
- [struct HeartRateRangeAlert](./heartraterangealert.md)
  An alert for a range of heart rates.
- [static func heartRate(zone: Int) -> Self](./workoutalert/heartrate%28zone%29.md)
  Creates a new alert for the specified heart rate zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/heartratezonealert)*