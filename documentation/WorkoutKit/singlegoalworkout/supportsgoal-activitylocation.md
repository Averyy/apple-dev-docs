# supportsGoal(_:activity:location:)

**Framework**: WorkoutKit  
**Kind**: method

Returns a Boolean value that determines whether the system supports the provided goal.

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

- `goal`: The target goal.
- `activity`: The workout’s activity type.
- `location`: The workout’s location.

## See Also

- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, swimmingLocation: HKWorkoutSwimmingLocationType, goal: WorkoutGoal)](singlegoalworkout/init(activity:location:swimminglocation:goal:).md)
  Creates a new workout with a single goal.
- [static func supportsActivity(HKWorkoutActivityType) -> Bool](singlegoalworkout/supportsactivity(_:).md)
  Returns a Boolean value that indicates whether the system supports the provided workout activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/singlegoalworkout/supportsgoal(_:activity:location:))*