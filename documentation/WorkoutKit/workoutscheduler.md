# WorkoutScheduler

**Framework**: Workoutkit  
**Kind**: class

An object for scheduling and managing workouts.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
final class WorkoutScheduler
```

## Topics

### Accessing the scheduler
- [static let shared: WorkoutScheduler](workoutscheduler/shared.md)
  A shared instance of the workout scheduler.
- [static var isSupported: Bool](workoutscheduler/issupported.md)
  A Boolean value that indicates whether the current device supports scheduled workouts.
- [func requestAuthorization() async -> WorkoutScheduler.AuthorizationState](workoutscheduler/requestauthorization.md)
  Requests authorization to schedule workouts.
- [var authorizationState: WorkoutScheduler.AuthorizationState](workoutscheduler/authorizationstate-swift.property.md)
  The workout scheduler’s authorization status.
- [WorkoutScheduler.AuthorizationState](workoutscheduler/authorizationstate-swift.enum.md)
  The workout scheduler’s authorization status.
### Scheduling workouts
- [func schedule(WorkoutPlan, at: DateComponents) async](workoutscheduler/schedule(_:at:).md)
  Schedules the provided workout at the specified date.
### Managing scheduled workouts
- [var scheduledWorkouts: [ScheduledWorkoutPlan]](workoutscheduler/scheduledworkouts.md)
  An array of all the workouts scheduled by your app.
- [static let maxAllowedScheduledWorkoutCount: Int](workoutscheduler/maxallowedscheduledworkoutcount.md)
  The maximum number of workouts your app can schedule.
- [func markComplete(WorkoutPlan, at: DateComponents) async](workoutscheduler/markcomplete(_:at:).md)
  Marks the workout as complete.
- [func remove(WorkoutPlan, at: DateComponents) async](workoutscheduler/remove(_:at:).md)
  Removes the scheduled workout.
- [func removeAllWorkouts() async](workoutscheduler/removeallworkouts.md)
  Removes all scheduled workouts.

## See Also

- [struct WorkoutPlan](workoutplan.md)
  A wrapper around a workout object that your app can use to open the object in Workout or schedule it for later.
- [struct ScheduledWorkoutPlan](scheduledworkoutplan.md)
  A wrapper around a workout plan that your app can use to schedule the workout plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler)*