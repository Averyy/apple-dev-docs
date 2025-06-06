# cadence(_:unit:)

**Framework**: Workoutkit  
**Kind**: method

Returns a new cadence threshold alert for the target value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static func cadence(_ value: Double, unit: UnitFrequency = WorkoutAlertMetric.countPerMinute) -> Self
```

## Parameters

- `value`: The threshold’s value.
- `unit`: The frequency units used by the threshold’s value.

## See Also

- [init(target: Measurement<UnitFrequency>)](cadencethresholdalert/init(target:).md)
  Create a new cadence threshold alert for the target measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/cadencethresholdalert/cadence(_:unit:))*