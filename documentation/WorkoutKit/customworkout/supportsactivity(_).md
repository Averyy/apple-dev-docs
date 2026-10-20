# supportsActivity(_:)

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the system supports the specified workout activity .

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func supportsActivity(_ activity: HKWorkoutActivityType) -> Bool
```

## Parameters

- `activity`: The activity to check.

## See Also

### Creating custom workouts
- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, displayName: String?, warmup: WorkoutStep?, blocks: [IntervalBlock], cooldown: WorkoutStep?)](./init%28activity,location,displayname,warmup,blocks,cooldown%29.md)
  Create a new custom workout.
- [static func supportsAlert(any WorkoutAlert, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](./supportsalert%28_,activity,location%29.md)
  Returns a Boolean value that indicates whether the system supports the specified alert for the given activity type and location.
- [static func supportsGoal(WorkoutGoal, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](./supportsgoal%28_,activity,location%29.md)
  Returns a Boolean value that indicates whether the system supports the specified goal for the given activity type and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/customworkout/supportsactivity(_:))*