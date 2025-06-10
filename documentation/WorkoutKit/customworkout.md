# CustomWorkout

**Framework**: WorkoutKit  
**Kind**: struct

A workout that includes a repeating series of work and recovery steps.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct CustomWorkout
```

## Topics

### Creating custom workouts
- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, displayName: String?, warmup: WorkoutStep?, blocks: [IntervalBlock], cooldown: WorkoutStep?)](customworkout/init(activity:location:displayname:warmup:blocks:cooldown:).md)
  Create a new custom workout.
- [static func supportsActivity(HKWorkoutActivityType) -> Bool](customworkout/supportsactivity(_:).md)
  Returns a Boolean value that indicates whether the system supports the specified workout activity .
- [static func supportsAlert(any WorkoutAlert, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](customworkout/supportsalert(_:activity:location:).md)
  Returns a Boolean value that indicates whether the system supports the specified alert for the given activity type and location.
- [static func supportsGoal(WorkoutGoal, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](customworkout/supportsgoal(_:activity:location:).md)
  Returns a Boolean value that indicates whether the system supports the specified goal for the given activity type and location.
### Accessing workout data
- [var displayName: String?](customworkout/displayname.md)
  The name that the system uses when displaying the workout.
- [var activity: HKWorkoutActivityType](customworkout/activity.md)
  The type of activity performed during the workout.
- [var location: HKWorkoutSessionLocationType](customworkout/location.md)
  The workout session location for the workout.
- [var warmup: WorkoutStep?](customworkout/warmup.md)
  The warmup step (if any).
- [var blocks: [IntervalBlock]](customworkout/blocks.md)
  A block of repeating work and recovery steps.
- [var cooldown: WorkoutStep?](customworkout/cooldown.md)
  The cooldown step (if any).
### Comparing workouts
- [var hashValue: Int](customworkout/hashvalue.md)
  The hashed value of the custom workout.
- [func hash(into: inout Hasher)](customworkout/hash(into:).md)
  Hashes the essential components of the custom workout by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](customworkout/!=(_:_:).md)
  Returns a Boolean value that indicates whether two custom workouts aren’t equal.
- [static func == (CustomWorkout, CustomWorkout) -> Bool](customworkout/==(_:_:).md)
  Returns a Boolean value that indicates whether two custom workouts are equal.
### Default Implementations
- [Equatable Implementations](customworkout/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WorkoutStep](workoutstep.md)
  A step in a workout.
- [struct IntervalBlock](intervalblock.md)
  Blocks of work and recovery steps that repeat in a custom workout.
- [struct IntervalStep](intervalstep.md)
  An interval that represents a work or recovery step in a workout.
- [enum WorkoutGoal](workoutgoal.md)
  A value that specifies the goal for a workout.
- [protocol WorkoutAlert](workoutalert.md)
  An alert that notifies the user of significant events during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/customworkout)*