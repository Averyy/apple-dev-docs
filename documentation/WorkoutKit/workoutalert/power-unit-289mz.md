# power(_:unit:)

**Framework**: WorkoutKit  
**Kind**: method

Creates an alert for the specified power threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static func power(_ value: Double, unit: UnitPower) -> Self
```

## Parameters

- `value`: The target power threshold for the alert.
- `unit`: The power units used for the threshold.

## See Also

- [static func power(ClosedRange<Double>, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-57ekz.md)
  Creates a new power alert for the target range.
- [struct PowerRangeAlert](powerrangealert.md)
  An alert for a range of power values.
- [struct PowerThresholdAlert](powerthresholdalert.md)
  An alert for a power threshold.
- [static func power(zone: Int) -> Self](workoutalert/power(zone:).md)
  Creates a new alert for the specified power zone.
- [struct PowerZoneAlert](powerzonealert.md)
  An alert for a power zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/power(_:unit:)-289mz)*