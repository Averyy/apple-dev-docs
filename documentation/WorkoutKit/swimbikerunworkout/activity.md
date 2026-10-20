# SwimBikeRunWorkout.Activity

**Framework**: WorkoutKit  
**Kind**: enum  
**Role**: Enumeration

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
- [case cycling(HKWorkoutSessionLocationType)](./activity/cycling%28_%29.md)
  A cycling workout activity, with the specified location type.
- [case running(HKWorkoutSessionLocationType)](./activity/running%28_%29.md)
  A running workout activity, with the specified location type.
- [case swimming(HKWorkoutSwimmingLocationType)](./activity/swimming%28_%29.md)
  A swimming workout activity, with the specified location type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating new multisport workouts.
- [init(activities: [SwimBikeRunWorkout.Activity], displayName: String?)](./init%28activities,displayname%29.md)
  Creates a new multisport workout for the specified activities.
- [static func supportsActivityOrdering([SwimBikeRunWorkout.Activity]) -> Bool](./supportsactivityordering%28_%29.md)
  Returns a Boolean value that indicates whether the system supports a multisport workout with the specified list of activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout/activity)*