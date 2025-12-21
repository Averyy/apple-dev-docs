# init(activity:location:displayName:warmup:blocks:cooldown:)

**Framework**: WorkoutKit  
**Kind**: init

Create a new custom workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType = .unknown, displayName: String? = nil, warmup: WorkoutStep? = nil, blocks: [IntervalBlock] = [], cooldown: WorkoutStep? = nil)
```

## Parameters

- `activity`: The type of activity performed during the workout.
- `location`: The workout session location for the workout.
- `displayName`: The name that the system uses when displaying the workout.
- `warmup`: The warmup step (if any).
- `blocks`: A block of repeating work and recovery steps.
- `cooldown`: The cooldown step (if any).

## See Also

- [static func supportsActivity(HKWorkoutActivityType) -> Bool](customworkout/supportsactivity(_:).md)
  Returns a Boolean value that indicates whether the system supports the specified workout activity .
- [static func supportsAlert(WorkoutAlert, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](customworkout/supportsalert(_:activity:location:).md)
  Returns a Boolean value that indicates whether the system supports the specified alert for the given activity type and location.
- [static func supportsGoal(WorkoutGoal, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](customworkout/supportsgoal(_:activity:location:).md)
  Returns a Boolean value that indicates whether the system supports the specified goal for the given activity type and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/customworkout/init(activity:location:displayname:warmup:blocks:cooldown:))*