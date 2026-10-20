# heartRate(zone:)

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Type Method

Creates a new alert for the specified heart rate zone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func heartRate(zone: Int) -> Self
```

Available when `Self` is `HeartRateZoneAlert`.

## Parameters

- `zone`: The target heart rate zone.

## See Also

### Creating heart rate alerts
- [static func heartRate(ClosedRange<Double>, unit: UnitFrequency) -> Self](./heartrate%28_,unit%29.md)
  Creates a new heart rate alert for the target range.
- [struct HeartRateRangeAlert](../heartraterangealert.md)
  An alert for a range of heart rates.
- [struct HeartRateZoneAlert](../heartratezonealert.md)
  An alert for a heart rate zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/heartrate(zone:))*