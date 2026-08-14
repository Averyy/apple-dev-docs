# WorkoutPlan.Workout

**Framework**: WorkoutKit  
**Kind**: enum

The workout for the workout plan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
enum Workout
```

## Topics

### Setting the workout
- [WorkoutPlan.Workout.custom(_:)](workoutplan/workout-swift.enum/custom(_:).md)
  A custom workout.
- [WorkoutPlan.Workout.goal(_:)](workoutplan/workout-swift.enum/goal(_:).md)
  A single goal workout
- [WorkoutPlan.Workout.pacer(_:)](workoutplan/workout-swift.enum/pacer(_:).md)
  A pacer workout.
- [case swimBikeRun(SwimBikeRunWorkout)](workoutplan/workout-swift.enum/swimbikerun(_:).md)
  A multisport workout.
### Accessing workout data
- [var activity: HKWorkoutActivityType](workoutplan/workout-swift.enum/activity.md)
  The workout activity type.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(WorkoutPlan.Workout, id: UUID)](workoutplan/init(_:id:).md)
  Creates a new workout plan from the provided workout and ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutplan/workout-swift.enum)*