# cadence(_:unit:)

**Framework**: Workoutkit  
**Kind**: method

Creates a new alert for a range of cadence values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func cadence(_ range: ClosedRange<Double>, unit: UnitFrequency = WorkoutAlertMetric.countPerMinute) -> Self
```

## Parameters

- `range`: A closed range representing the cadence’s value.
- `unit`: The frequency units for the specified range.

## See Also

- [struct CadenceRangeAlert](cadencerangealert.md)
  An alert for a range of cadence values.
- [static func cadence(Double, unit: UnitFrequency) -> Self](workoutalert/cadence(_:unit:)-3fnpg.md)
  Creates an alert for the specified cadence threshold.
- [struct CadenceThresholdAlert](cadencethresholdalert.md)
  An alert for a cadence threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/cadence(_:unit:)-y8da)*