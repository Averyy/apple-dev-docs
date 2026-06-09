# HeartRateZoneAlert

**Framework**: WorkoutKit  
**Kind**: struct

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
- [init(zone: Int)](heartratezonealert/init(zone:).md)
  Creates a new alert for the target heart rate zone.
### Accessing the alert data
- [var zone: Int](heartratezonealert/zone.md)
  The target heart rate zone.

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
- [struct HeartRateRangeAlert](heartraterangealert.md)
  An alert for a range of heart rates.
- [static func heartRate(zone: Int) -> Self](workoutalert/heartrate(zone:).md)
  Creates a new alert for the specified heart rate zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/heartratezonealert)*