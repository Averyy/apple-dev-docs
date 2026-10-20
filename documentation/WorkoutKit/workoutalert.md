# WorkoutAlert

**Framework**: WorkoutKit  
**Kind**: protocol  
**Role**: Protocol

An alert that notifies the user of significant events during a workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
protocol WorkoutAlert : Hashable, Sendable
```

## Topics

### Determining support
- [func supports(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](./workoutalert/supports%28activity,location%29.md)
  Returns a Boolean value that indicates whether the alert supports the provided activity and location.
### Setting the alert metric
- [var metric: WorkoutAlertMetric](./workoutalert/metric.md)
  The metric used to measure performance for the alert.
- [enum WorkoutAlertMetric](./workoutalertmetric.md)
  A value that specifies the type of metric used to measure performance.
### Creating cadence alerts
- [static func cadence(ClosedRange<Double>, unit: UnitFrequency) -> Self](./workoutalert/cadence%28_,unit%29-y8da.md)
  Creates a new alert for a range of cadence values.
- [struct CadenceRangeAlert](./cadencerangealert.md)
  An alert for a range of cadence values.
- [static func cadence(Double, unit: UnitFrequency) -> Self](./workoutalert/cadence%28_,unit%29-3fnpg.md)
  Creates an alert for the specified cadence threshold.
- [struct CadenceThresholdAlert](./cadencethresholdalert.md)
  An alert for a cadence threshold.
### Creating heart rate alerts
- [static func heartRate(ClosedRange<Double>, unit: UnitFrequency) -> Self](./workoutalert/heartrate%28_,unit%29.md)
  Creates a new heart rate alert for the target range.
- [struct HeartRateRangeAlert](./heartraterangealert.md)
  An alert for a range of heart rates.
- [static func heartRate(zone: Int) -> Self](./workoutalert/heartrate%28zone%29.md)
  Creates a new alert for the specified heart rate zone.
- [struct HeartRateZoneAlert](./heartratezonealert.md)
  An alert for a heart rate zone.
### Creating power alerts
- [static func power(ClosedRange<Double>, unit: UnitPower) -> Self](./workoutalert/power%28_,unit%29-57ekz.md)
  Creates a new power alert for the target range.
- [struct PowerRangeAlert](./powerrangealert.md)
  An alert for a range of power values.
- [static func power(Double, unit: UnitPower) -> Self](./workoutalert/power%28_,unit%29-289mz.md)
  Creates an alert for the specified power threshold.
- [struct PowerThresholdAlert](./powerthresholdalert.md)
  An alert for a power threshold.
- [static func power(zone: Int) -> Self](./workoutalert/power%28zone%29.md)
  Creates a new alert for the specified power zone.
- [struct PowerZoneAlert](./powerzonealert.md)
  An alert for a power zone.
### Creating speed alerts
- [static func speed(ClosedRange<Double>, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](./workoutalert/speed%28_,unit,metric%29-1o2j.md)
  Creates a new speed alert for the provided range.
- [struct SpeedRangeAlert](./speedrangealert.md)
  An alert for a range of speed values.
- [static func speed(Double, unit: UnitSpeed, metric: WorkoutAlertMetric) -> Self](./workoutalert/speed%28_,unit,metric%29-4zald.md)
  Creates a new speed threshold alert.
- [struct SpeedThresholdAlert](./speedthresholdalert.md)
  An alert for a speed threshold.
### Type Methods
- [static func power(Double, unit: UnitPower, metric: WorkoutAlertMetric) -> Self](./workoutalert/power%28_,unit,metric%29-2847m.md)
- [static func power(ClosedRange<Double>, unit: UnitPower, metric: WorkoutAlertMetric) -> Self](./workoutalert/power%28_,unit,metric%29-5c94p.md)

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [CadenceRangeAlert](./cadencerangealert.md)
- [CadenceThresholdAlert](./cadencethresholdalert.md)
- [HeartRateRangeAlert](./heartraterangealert.md)
- [HeartRateZoneAlert](./heartratezonealert.md)
- [PowerRangeAlert](./powerrangealert.md)
- [PowerThresholdAlert](./powerthresholdalert.md)
- [PowerZoneAlert](./powerzonealert.md)
- [SpeedRangeAlert](./speedrangealert.md)
- [SpeedThresholdAlert](./speedthresholdalert.md)

## See Also

### Custom interval workouts
- [struct CustomWorkout](./customworkout.md)
  A workout that includes a repeating series of work and recovery steps.
- [struct WorkoutStep](./workoutstep.md)
  A step in a workout.
- [struct IntervalBlock](./intervalblock.md)
  Blocks of work and recovery steps that repeat in a custom workout.
- [struct IntervalStep](./intervalstep.md)
  An interval that represents a work or recovery step in a workout.
- [enum WorkoutGoal](./workoutgoal.md)
  A value that specifies the goal for a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalert)*