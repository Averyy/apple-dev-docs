# heartRate(zone:)

**Framework**: WorkoutKit  
**Kind**: method

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

## Parameters

- `zone`: The target heart rate zone.

## See Also

- [static func heartRate(ClosedRange<Double>, unit: UnitFrequency) -> Self](workoutalert/heartrate(_:unit:).md)
  Creates a new heart rate alert for the target range.
- [struct HeartRateRangeAlert](heartraterangealert.md)
  An alert for a range of heart rates.
- [struct HeartRateZoneAlert](heartratezonealert.md)
  An alert for a heart rate zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/heartrate(zone:))*