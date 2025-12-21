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
### Comparing activities
- [var hashValue: Int](swimbikerunworkout/activity/hashvalue.md)
  The hashed value of the activity.
- [func hash(into: inout Hasher)](swimbikerunworkout/activity/hash(into:).md)
  Hashes the essential components of the activity by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](swimbikerunworkout/activity/!=(_:_:).md)
  Returns a Boolean value that indicates whether two activities aren’t equal.
- [static func == (SwimBikeRunWorkout.Activity, SwimBikeRunWorkout.Activity) -> Bool](swimbikerunworkout/activity/==(_:_:).md)
  Returns a Boolean value that indicates whether two activities are equal.
### Default Implementations
- [Equatable Implementations](swimbikerunworkout/activity/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(activities: [SwimBikeRunWorkout.Activity], displayName: String?)](swimbikerunworkout/init(activities:displayname:).md)
  Creates a new multisport workout for the specified activities.
- [static func supportsActivityOrdering([SwimBikeRunWorkout.Activity]) -> Bool](swimbikerunworkout/supportsactivityordering(_:).md)
  Returns a Boolean value that indicates whether the system supports a multisport workout with the specified list of activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout/activity)*