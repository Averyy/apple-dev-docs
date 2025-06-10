# maxAllowedScheduledWorkoutCount

**Framework**: WorkoutKit  
**Kind**: property

The maximum number of workouts your app can schedule.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static let maxAllowedScheduledWorkoutCount: Int
```

## See Also

- [var scheduledWorkouts: [ScheduledWorkoutPlan]](workoutscheduler/scheduledworkouts.md)
  An array of all the workouts scheduled by your app.
- [func markComplete(WorkoutPlan, at: DateComponents) async](workoutscheduler/markcomplete(_:at:).md)
  Marks the workout as complete.
- [func remove(WorkoutPlan, at: DateComponents) async](workoutscheduler/remove(_:at:).md)
  Removes the scheduled workout.
- [func removeAllWorkouts() async](workoutscheduler/removeallworkouts.md)
  Removes all scheduled workouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/maxallowedscheduledworkoutcount)*