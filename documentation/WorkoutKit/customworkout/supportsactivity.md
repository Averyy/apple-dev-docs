# supportsActivity(_:)

**Framework**: WorkoutKit  
**Kind**: method

Returns a Boolean value that indicates whether the system supports the specified workout activity .

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static func supportsActivity(_ activity: HKWorkoutActivityType) -> Bool
```

## Parameters

- `activity`: The activity to check.

## See Also

- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, displayName: String?, warmup: WorkoutStep?, blocks: [IntervalBlock], cooldown: WorkoutStep?)](customworkout/init(activity:location:displayname:warmup:blocks:cooldown:).md)
  Create a new custom workout.
- [static func supportsAlert(any WorkoutAlert, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](customworkout/supportsalert(_:activity:location:).md)
  Returns a Boolean value that indicates whether the system supports the specified alert for the given activity type and location.
- [static func supportsGoal(WorkoutGoal, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](customworkout/supportsgoal(_:activity:location:).md)
  Returns a Boolean value that indicates whether the system supports the specified goal for the given activity type and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/customworkout/supportsactivity(_:))*