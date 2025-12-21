# init(target:)

**Framework**: WorkoutKit  
**Kind**: init

Creates a cadence alert for a closed range of measurements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(target: ClosedRange<Measurement<UnitFrequency>>)
```

## Parameters

- `target`: A closed range that uses frequency units.

## See Also

- [static func cadence(ClosedRange<Double>, unit: UnitFrequency) -> Self](cadencerangealert/cadence(_:unit:).md)
  Creates a new cadence alert for the target range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/cadencerangealert/init(target:))*