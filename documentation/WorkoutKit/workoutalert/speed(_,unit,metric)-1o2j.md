# speed(_:unit:metric:)

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Type Method

Creates a new speed alert for the provided range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func speed(_ range: ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric = .current) -> Self
```

Available when `Self` is `SpeedRangeAlert`.

## Parameters

- `range`: A closed range of speed values.
- `unit`: The speed units used by the range.
- `metric`: The metric used for the speed measurements.

## See Also

### Creating speed alerts
- [struct SpeedRangeAlert](../speedrangealert.md)
  An alert for a range of speed values.
- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](./speed%28_,unit,metric%29-4zald.md)
  Creates a new speed threshold alert.
- [struct SpeedThresholdAlert](../speedthresholdalert.md)
  An alert for a speed threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/speed(_:unit:metric:)-1o2j)*