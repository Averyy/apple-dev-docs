# cadence(_:unit:)

**Framework**: WorkoutKit  
**Kind**: method

Creates an alert for the specified cadence threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static func cadence(_ value: Double, unit: UnitFrequency = WorkoutAlertMetric.countPerMinute) -> Self
```

## Parameters

- `value`: The target cadence threshold for the alert.
- `unit`: The frequency units used for the threshold.

## See Also

- [static func cadence(ClosedRange<Double>, unit: UnitFrequency) -> Self](workoutalert/cadence(_:unit:)-y8da.md)
  Creates a new alert for a range of cadence values.
- [struct CadenceRangeAlert](cadencerangealert.md)
  An alert for a range of cadence values.
- [struct CadenceThresholdAlert](cadencethresholdalert.md)
  An alert for a cadence threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/cadence(_:unit:)-3fnpg)*