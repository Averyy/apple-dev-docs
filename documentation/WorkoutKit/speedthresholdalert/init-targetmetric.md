# init(target:metric:)

**Framework**: Workoutkit  
**Kind**: init

Creates a new speed threshold alert.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(target: Measurement<UnitSpeed>, metric: WorkoutAlertMetric)
```

## Parameters

- `target`: A speed measurement that represents the target threshold.
- `metric`: The metric used to measure the speed.

## See Also

- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](speedthresholdalert/speed(_:unit:metric:).md)
  Returns a new speed threshold alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedthresholdalert/init(target:metric:))*