# init(activities:displayName:)

**Framework**: WorkoutKit  
**Kind**: init

Creates a new multisport workout for the specified activities.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(activities: [SwimBikeRunWorkout.Activity], displayName: String? = nil)
```

## Parameters

- `activities`: An ordered list of workout activity types included in the workout.
- `displayName`: The name that the system uses when displaying the workout.

## See Also

- [SwimBikeRunWorkout.Activity](swimbikerunworkout/activity.md)
  An activity in a multisport workout.
- [static func supportsActivityOrdering([SwimBikeRunWorkout.Activity]) -> Bool](swimbikerunworkout/supportsactivityordering(_:).md)
  Returns a Boolean value that indicates whether the system supports a multisport workout with the specified list of activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout/init(activities:displayname:))*