# power(_:unit:)

**Framework**: WorkoutKit  
**Kind**: method

Creates a new power alert for the target range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func power(_ range: ClosedRange<Double>, unit: UnitPower) -> Self
```

## Parameters

- `range`: A closed range of power values.
- `unit`: The power units used by the range values.

## See Also

- [struct PowerRangeAlert](powerrangealert.md)
  An alert for a range of power values.
- [static func power(Double, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-289mz.md)
  Creates an alert for the specified power threshold.
- [struct PowerThresholdAlert](powerthresholdalert.md)
  An alert for a power threshold.
- [static func power(zone: Int) -> Self](workoutalert/power(zone:).md)
  Creates a new alert for the specified power zone.
- [struct PowerZoneAlert](powerzonealert.md)
  An alert for a power zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/power(_:unit:)-57ekz)*