# supportsActivity(_:)

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the system supports the provided workout activity.

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

- `activity`: The target workout activity type.

## See Also

### Creating single goal workouts
- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, swimmingLocation: HKWorkoutSwimmingLocationType, goal: WorkoutGoal)](./init%28activity,location,swimminglocation,goal%29.md)
  Creates a new workout with a single goal.
- [static func supportsGoal(WorkoutGoal, activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType) -> Bool](./supportsgoal%28_,activity,location%29.md)
  Returns a Boolean value that determines whether the system supports the provided goal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/singlegoalworkout/supportsactivity(_:))*