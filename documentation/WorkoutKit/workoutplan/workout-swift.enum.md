# WorkoutPlan.Workout

**Framework**: WorkoutKit  
**Kind**: enum  
**Role**: Enumeration

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
- [WorkoutPlan.Workout.custom(_:)](./workout-swift.enum/custom%28_%29.md)
  A custom workout.
- [WorkoutPlan.Workout.goal(_:)](./workout-swift.enum/goal%28_%29.md)
  A single goal workout
- [WorkoutPlan.Workout.pacer(_:)](./workout-swift.enum/pacer%28_%29.md)
  A pacer workout.
- [case swimBikeRun(SwimBikeRunWorkout)](./workout-swift.enum/swimbikerun%28_%29.md)
  A multisport workout.
### Accessing workout data
- [var activity: HKWorkoutActivityType](./workout-swift.enum/activity.md)
  The workout activity type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a workout plan
- [init(WorkoutPlan.Workout, id: UUID)](./init%28_,id%29.md)
  Creates a new workout plan from the provided workout and ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutplan/workout-swift.enum)*