# ScheduledWorkoutPlan

**Framework**: WorkoutKit  
**Kind**: struct  
**Role**: Structure

A wrapper around a workout plan that your app can use to schedule the workout plan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct ScheduledWorkoutPlan
```

## Topics

### Creating scheduled workout plans
- [init(WorkoutPlan, date: DateComponents)](./scheduledworkoutplan/init%28_,date%29.md)
  Creates a new scheduled workout plan.
### Accessing plan data
- [var plan: WorkoutPlan](./scheduledworkoutplan/plan.md)
  The target workout plan to schedule.
- [var date: DateComponents](./scheduledworkoutplan/date.md)
  Date components that determine when the workout should begin.
- [var complete: Bool](./scheduledworkoutplan/complete.md)
  A Boolean value that indicates whether the workout is complete.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Workout plans and schedules
- [struct WorkoutPlan](./workoutplan.md)
  A wrapper around a workout object that your app can use to open the object in Workout or schedule it for later.
- [class WorkoutScheduler](./workoutscheduler.md)
  An object for scheduling and managing workouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/scheduledworkoutplan)*