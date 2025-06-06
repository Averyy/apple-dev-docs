# PowerZoneAlert

**Framework**: Workoutkit  
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
- [static func power(zone: Int) -> Self](powerzonealert/power(zone:).md)
  Returns a new power zone alert.
- [init(zone: Int)](powerzonealert/init(zone:).md)
  Creates a new power zone alert.
### Accessing alert data
- [var metric: WorkoutAlertMetric](powerzonealert/metric.md)
  The metric for the alert.
- [var zone: Int](powerzonealert/zone.md)
  The target power zone.
### Comparing alerts
- [var hashValue: Int](powerzonealert/hashvalue.md)
  The hashed value of the power zone alert.
- [func hash(into: inout Hasher)](powerzonealert/hash(into:).md)
  Hashes the essential components of the power zone alert by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](powerzonealert/!=(_:_:).md)
  Returns a Boolean value that indicates whether two power zone alerts aren’t equal.
- [static func == (PowerZoneAlert, PowerZoneAlert) -> Bool](powerzonealert/==(_:_:).md)
  Returns a Boolean value that indicates whether two power zone alerts are equal.
### Default Implementations
- [Equatable Implementations](powerzonealert/equatable-implementations.md)
- [WorkoutAlert Implementations](powerzonealert/workoutalert-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
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