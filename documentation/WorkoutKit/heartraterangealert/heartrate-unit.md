# heartRate(_:unit:)

**Framework**: WorkoutKit  
**Kind**: method

Returns a new heart rate alert for the target range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static func heartRate(_ range: ClosedRange<Double>, unit: UnitFrequency = WorkoutAlertMetric.countPerMinute) -> Self
```

## Parameters

- `range`: A closed range of heart rate values.
- `unit`: The frequency units used by the range values.

## See Also

- [init(target: ClosedRange<Measurement<UnitFrequency>>)](heartraterangealert/init(target:).md)
  Creates a new heart rate alert for a closed range of measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/heartraterangealert/heartrate(_:unit:))*