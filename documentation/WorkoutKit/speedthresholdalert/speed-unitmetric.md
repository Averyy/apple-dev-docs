# speed(_:unit:metric:)

**Framework**: Workoutkit  
**Kind**: method

Returns a new speed threshold alert.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static func speed(_ value: Double, unit: UnitSpeed, metric: WorkoutAlertMetric = .current) -> Self
```

## Parameters

- `value`: The value of the target threshold.
- `unit`: The speed units used by the value.
- `metric`: The metric used to measure the speed.

## See Also

- [init(target: Measurement<UnitSpeed>, metric: WorkoutAlertMetric)](speedthresholdalert/init(target:metric:).md)
  Creates a new speed threshold alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedthresholdalert/speed(_:unit:metric:))*