# supportsActivityOrdering(_:)

**Framework**: WorkoutKit  
**Kind**: method

Returns a Boolean value that indicates whether the system supports a multisport workout with the specified list of activities.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static func supportsActivityOrdering(_ activities: [SwimBikeRunWorkout.Activity]) -> Bool
```

## Parameters

- `activities`: An ordered list of activities for the multisport workout.

## See Also

- [init(activities: [SwimBikeRunWorkout.Activity], displayName: String?)](swimbikerunworkout/init(activities:displayname:).md)
  Creates a new multisport workout for the specified activities.
- [SwimBikeRunWorkout.Activity](swimbikerunworkout/activity.md)
  An activity in a multisport workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout/supportsactivityordering(_:))*