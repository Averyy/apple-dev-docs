# init(target:)

**Framework**: WorkoutKit  
**Kind**: init

Creates a new heart rate alert for a closed range of measurements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(target: ClosedRange<Measurement<UnitFrequency>>)
```

## Parameters

- `target`: A range of values that use frequency units.

## See Also

- [static func heartRate(ClosedRange<Double>, unit: UnitFrequency) -> Self](heartraterangealert/heartrate(_:unit:).md)
  Returns a new heart rate alert for the target range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/heartraterangealert/init(target:))*