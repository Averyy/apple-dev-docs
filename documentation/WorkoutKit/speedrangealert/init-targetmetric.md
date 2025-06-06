# init(target:metric:)

**Framework**: Workoutkit  
**Kind**: init

Creates a new speed alert for the provided range of values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(target: ClosedRange<Measurement<UnitSpeed>>, metric: WorkoutAlertMetric)
```

## Parameters

- `target`: A range of speed measurements.
- `metric`: The metric used to measure the speed.

## See Also

- [static func speed(ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](speedrangealert/speed(_:unit:metric:).md)
  Returns a new speed alert for the provided range of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedrangealert/init(target:metric:))*