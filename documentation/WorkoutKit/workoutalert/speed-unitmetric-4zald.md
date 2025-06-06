# speed(_:unit:metric:)

**Framework**: Workoutkit  
**Kind**: method

Creates a new speed threshold alert.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func speed(_ value: Double, unit: UnitSpeed, metric: WorkoutAlertMetric = .current) -> Self
```

## Parameters

- `value`: The threshold value.
- `unit`: The speed units used by the threshold value.
- `metric`: The metric used to measure the speed.

## See Also

- [static func speed(ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](workoutalert/speed(_:unit:metric:)-1o2j.md)
  Creates a new speed alert for the provided range.
- [struct SpeedRangeAlert](speedrangealert.md)
  An alert for a range of speed values.
- [struct SpeedThresholdAlert](speedthresholdalert.md)
  An alert for a speed threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/speed(_:unit:metric:)-4zald)*