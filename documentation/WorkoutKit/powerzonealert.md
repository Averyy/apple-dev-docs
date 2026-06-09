# PowerZoneAlert

**Framework**: WorkoutKit  
**Kind**: struct

An alert for a power zone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct PowerZoneAlert
```

## Topics

### Creating power zone alerts
- [init(zone: Int)](powerzonealert/init(zone:).md)
  Creates a new power zone alert.
### Accessing alert data
- [var zone: Int](powerzonealert/zone.md)
  The target power zone.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WorkoutAlert](workoutalert.md)

## See Also

- [static func power(ClosedRange<Double>, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-57ekz.md)
  Creates a new power alert for the target range.
- [struct PowerRangeAlert](powerrangealert.md)
  An alert for a range of power values.
- [static func power(Double, unit: UnitPower) -> Self](workoutalert/power(_:unit:)-289mz.md)
  Creates an alert for the specified power threshold.
- [struct PowerThresholdAlert](powerthresholdalert.md)
  An alert for a power threshold.
- [static func power(zone: Int) -> Self](workoutalert/power(zone:).md)
  Creates a new alert for the specified power zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/powerzonealert)*