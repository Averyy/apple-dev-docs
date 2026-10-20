# markComplete(_:at:)

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Instance Method

Marks the workout as complete.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
final func markComplete(_ workout: WorkoutPlan, at: DateComponents) async
```

## See Also

### Managing scheduled workouts
- [var scheduledWorkouts: [ScheduledWorkoutPlan]](./scheduledworkouts.md)
  An array of all the workouts scheduled by your app.
- [static let maxAllowedScheduledWorkoutCount: Int](./maxallowedscheduledworkoutcount.md)
  The maximum number of workouts your app can schedule.
- [func remove(WorkoutPlan, at: DateComponents) async](./remove%28_,at%29.md)
  Removes the scheduled workout.
- [func removeAllWorkouts() async](./removeallworkouts%28%29.md)
  Removes all scheduled workouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/markcomplete(_:at:))*