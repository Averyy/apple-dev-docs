# SwimBikeRunWorkout.Activity

**Framework**: WorkoutKit  
**Kind**: enum

An activity in a multisport workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
enum Activity
```

## Topics

### Setting valid activities
- [case cycling(HKWorkoutSessionLocationType)](swimbikerunworkout/activity/cycling(_:).md)
  A cycling workout activity, with the specified location type.
- [case running(HKWorkoutSessionLocationType)](swimbikerunworkout/activity/running(_:).md)
  A running workout activity, with the specified location type.
- [case swimming(HKWorkoutSwimmingLocationType)](swimbikerunworkout/activity/swimming(_:).md)
  A swimming workout activity, with the specified location type.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(activities: [SwimBikeRunWorkout.Activity], displayName: String?)](swimbikerunworkout/init(activities:displayname:).md)
  Creates a new multisport workout for the specified activities.
- [static func supportsActivityOrdering([SwimBikeRunWorkout.Activity]) -> Bool](swimbikerunworkout/supportsactivityordering(_:).md)
  Returns a Boolean value that indicates whether the system supports a multisport workout with the specified list of activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout/activity)*