# cadence(_:unit:)

**Framework**: WorkoutKit  
**Kind**: method

Creates a new cadence alert for the target range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static func cadence(_ range: ClosedRange<Double>, unit: UnitFrequency = WorkoutAlertMetric.countPerMinute) -> Self
```

## Parameters

- `range`: A closed range representing the cadence’s value.
- `unit`: The frequency units for the specified range.

## See Also

- [init(target: ClosedRange<Measurement<UnitFrequency>>)](cadencerangealert/init(target:).md)
  Creates a cadence alert for a closed range of measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/cadencerangealert/cadence(_:unit:))*