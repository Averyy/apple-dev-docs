# SingleGoalWorkout

**Framework**: WorkoutKit  
**Kind**: struct

A workout with a single goal.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct SingleGoalWorkout
```

## Topics

### Creating single goal workouts
- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, swimmingLocation: HKWorkoutSwimmingLocationType, goal: WorkoutGoal)](singlegoalworkout/init(activity:location:swimminglocation:goal:).md)
  Creates a new workout with a single goal.
- [static func supportsActivity(HKWorkoutActivityType) -> Bool](singlegoalworkout/supportsactivity(_:).md)
  Returns a Boolean value that indicates whether the system supports the provided workout activity.
- [static func supportsGoal(WorkoutGoal, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](singlegoalworkout/supportsgoal(_:activity:location:).md)
  Returns a Boolean value that determines whether the system supports the provided goal.
### Accessing workout data
- [var activity: HKWorkoutActivityType](singlegoalworkout/activity.md)
  The workout activity type.
- [var location: HKWorkoutSessionLocationType](singlegoalworkout/location.md)
  The workout location.
- [var swimmingLocation: HKWorkoutSwimmingLocationType](singlegoalworkout/swimminglocation.md)
  For swimming workouts, the workout’s swimming location.
- [var goal: WorkoutGoal](singlegoalworkout/goal.md)
  The goal for the workout.
### Comparing workouts
- [var hashValue: Int](singlegoalworkout/hashvalue.md)
  The hashed value of the workout.
- [func hash(into: inout Hasher)](singlegoalworkout/hash(into:).md)
  Hashes the essential components of the workout by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](singlegoalworkout/!=(_:_:).md)
  Returns a Boolean value that indicates whether two workouts aren’t equal.
- [static func == (SingleGoalWorkout, SingleGoalWorkout) -> Bool](singlegoalworkout/==(_:_:).md)
  Returns a Boolean value that indicates whether two workouts are equal.
### Default Implementations
- [Equatable Implementations](singlegoalworkout/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PacerWorkout](pacerworkout.md)
  A workout in which a person covers a specific distance in a given time.
- [struct SwimBikeRunWorkout](swimbikerunworkout.md)
  A workout for multisport activities that include running, biking, and swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/singlegoalworkout)*