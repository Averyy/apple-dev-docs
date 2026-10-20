# heartRate(_:unit:)

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Type Method

Creates a new heart rate alert for the target range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func heartRate(_ range: ClosedRange<Double>, unit: UnitFrequency = WorkoutAlertMetric.countPerMinute) -> Self
```

Available when `Self` is `HeartRateRangeAlert`.

## Parameters

- `range`: A closed range of heart rate values.
- `unit`: The frequency units used by the range values.

## See Also

### Creating heart rate alerts
- [struct HeartRateRangeAlert](../heartraterangealert.md)
  An alert for a range of heart rates.
- [static func heartRate(zone: Int) -> Self](./heartrate%28zone%29.md)
  Creates a new alert for the specified heart rate zone.
- [struct HeartRateZoneAlert](../heartratezonealert.md)
  An alert for a heart rate zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/heartrate(_:unit:))*