# PowerThresholdAlert

**Framework**: WorkoutKit  
**Kind**: struct  
**Role**: Structure

An alert for a power threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct PowerThresholdAlert
```

## Topics

### Creating power threshold alerts
- [init(target: Measurement<UnitPower>)](./powerthresholdalert/init%28target%29.md)
  Returns a new power threshold alert for the target measurement.
### Accessing alert data
- [var target: Measurement<UnitPower>](./powerthresholdalert/target.md)
  The target measurement using power units.
- [var targetQuantity: HKQuantity](./powerthresholdalert/targetquantity.md)
  A HealthKit quantity that represents the target power threshold.
### Initializers
- [init(target: Measurement<UnitPower>, metric: WorkoutAlertMetric)](./powerthresholdalert/init%28target,metric%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [WorkoutAlert](./workoutalert.md)

## See Also

### Creating power alerts
- [static func power(ClosedRange<Double>, unit: UnitPower) -> Self](./workoutalert/power%28_,unit%29-57ekz.md)
  Creates a new power alert for the target range.
- [struct PowerRangeAlert](./powerrangealert.md)
  An alert for a range of power values.
- [static func power(Double, unit: UnitPower) -> Self](./workoutalert/power%28_,unit%29-289mz.md)
  Creates an alert for the specified power threshold.
- [static func power(zone: Int) -> Self](./workoutalert/power%28zone%29.md)
  Creates a new alert for the specified power zone.
- [struct PowerZoneAlert](./powerzonealert.md)
  An alert for a power zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/powerthresholdalert)*