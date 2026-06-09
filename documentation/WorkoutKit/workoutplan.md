# WorkoutPlan

**Framework**: WorkoutKit  
**Kind**: struct

A wrapper around a workout object that your app can use to open the object in Workout or schedule it for later.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct WorkoutPlan
```

## Topics

### Creating a workout plan
- [init(WorkoutPlan.Workout, id: UUID)](workoutplan/init(_:id:).md)
  Creates a new workout plan from the provided workout and ID.
- [WorkoutPlan.Workout](workoutplan/workout-swift.enum.md)
  The workout for the workout plan.
### Accessing workout plan data
- [var workout: WorkoutPlan.Workout](workoutplan/workout-swift.property.md)
  The workout represented by this plan.
### Opening the workout plan
- [func openInWorkoutApp() async throws](workoutplan/openinworkoutapp.md)
  Opens the workout in Workout on Apple Watch.
### Initializers
- [init(from: Data) throws](workoutplan/init(from:).md)
### Instance Properties
- [var dataRepresentation: Data](workoutplan/datarepresentation.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ScheduledWorkoutPlan](scheduledworkoutplan.md)
  A wrapper around a workout plan that your app can use to schedule the workout plan.
- [class WorkoutScheduler](workoutscheduler.md)
  An object for scheduling and managing workouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutplan)*