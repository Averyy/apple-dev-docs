# maxAllowedScheduledWorkoutCount

**Framework**: WorkoutKit  
**Kind**: property  
**Role**: Type Property

The maximum number of workouts your app can schedule.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static let maxAllowedScheduledWorkoutCount: Int
```

## See Also

### Managing scheduled workouts
- [var scheduledWorkouts: [ScheduledWorkoutPlan]](./scheduledworkouts.md)
  An array of all the workouts scheduled by your app.
- [func markComplete(WorkoutPlan, at: DateComponents) async](./markcomplete%28_,at%29.md)
  Marks the workout as complete.
- [func remove(WorkoutPlan, at: DateComponents) async](./remove%28_,at%29.md)
  Removes the scheduled workout.
- [func removeAllWorkouts() async](./removeallworkouts%28%29.md)
  Removes all scheduled workouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/maxallowedscheduledworkoutcount)*