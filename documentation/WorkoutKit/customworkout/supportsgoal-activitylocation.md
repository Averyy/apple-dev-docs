# supportsGoal(_:activity:location:)

**Framework**: WorkoutKit  
**Kind**: method

Returns a Boolean value that indicates whether the system supports the specified goal for the given activity type and location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func supportsGoal(_ goal: WorkoutGoal, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType = .unknown) -> Bool
```

## Parameters

- `goal`: The goal to check.
- `activity`: The workout activity.
- `location`: The workout location.

## See Also

- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, displayName: String?, warmup: WorkoutStep?, blocks: [IntervalBlock], cooldown: WorkoutStep?)](customworkout/init(activity:location:displayname:warmup:blocks:cooldown:).md)
  Create a new custom workout.
- [static func supportsActivity(HKWorkoutActivityType) -> Bool](customworkout/supportsactivity(_:).md)
  Returns a Boolean value that indicates whether the system supports the specified workout activity .
- [static func supportsAlert(WorkoutAlert, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](customworkout/supportsalert(_:activity:location:).md)
  Returns a Boolean value that indicates whether the system supports the specified alert for the given activity type and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/customworkout/supportsgoal(_:activity:location:))*