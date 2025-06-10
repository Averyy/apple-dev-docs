# speed(_:unit:metric:)

**Framework**: WorkoutKit  
**Kind**: method

Returns a new speed alert for the provided range of values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static func speed(_ range: ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric = .current) -> Self
```

## Parameters

- `range`: A closed range of speed values.
- `unit`: The speed units used for the values.
- `metric`: The metric used to measure the speed.

## See Also

- [init(target: ClosedRange<Measurement<UnitSpeed>>, metric: WorkoutAlertMetric)](speedrangealert/init(target:metric:).md)
  Creates a new speed alert for the provided range of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/speedrangealert/speed(_:unit:metric:))*