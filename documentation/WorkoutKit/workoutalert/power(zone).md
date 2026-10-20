# power(zone:)

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Type Method

Creates a new alert for the specified power zone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func power(zone: Int) -> Self
```

Available when `Self` is `PowerZoneAlert`.

## Parameters

- `zone`: The target heart rate zone.

## See Also

### Creating power alerts
- [static func power(ClosedRange<Double>, unit: UnitPower) -> Self](./power%28_,unit%29-57ekz.md)
  Creates a new power alert for the target range.
- [struct PowerRangeAlert](../powerrangealert.md)
  An alert for a range of power values.
- [static func power(Double, unit: UnitPower) -> Self](./power%28_,unit%29-289mz.md)
  Creates an alert for the specified power threshold.
- [struct PowerThresholdAlert](../powerthresholdalert.md)
  An alert for a power threshold.
- [struct PowerZoneAlert](../powerzonealert.md)
  An alert for a power zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert/power(zone:))*