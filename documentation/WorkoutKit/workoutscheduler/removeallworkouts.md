# removeAllWorkouts()

**Framework**: WorkoutKit  
**Kind**: method

Removes all scheduled workouts.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final func removeAllWorkouts() async
```

## See Also

- [var scheduledWorkouts: [ScheduledWorkoutPlan]](workoutscheduler/scheduledworkouts.md)
  An array of all the workouts scheduled by your app.
- [static let maxAllowedScheduledWorkoutCount: Int](workoutscheduler/maxallowedscheduledworkoutcount.md)
  The maximum number of workouts your app can schedule.
- [func markComplete(WorkoutPlan, at: DateComponents) async](workoutscheduler/markcomplete(_:at:).md)
  Marks the workout as complete.
- [func remove(WorkoutPlan, at: DateComponents) async](workoutscheduler/remove(_:at:).md)
  Removes the scheduled workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/removeallworkouts())*