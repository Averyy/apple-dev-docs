# SwimBikeRunWorkout

**Framework**: WorkoutKit  
**Kind**: struct

A workout for multisport activities that include running, biking, and swimming.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct SwimBikeRunWorkout
```

## Topics

### Creating new multisport workouts.
- [init(activities: [SwimBikeRunWorkout.Activity], displayName: String?)](swimbikerunworkout/init(activities:displayname:).md)
  Creates a new multisport workout for the specified activities.
- [SwimBikeRunWorkout.Activity](swimbikerunworkout/activity.md)
  An activity in a multisport workout.
- [static func supportsActivityOrdering([SwimBikeRunWorkout.Activity]) -> Bool](swimbikerunworkout/supportsactivityordering(_:).md)
  Returns a Boolean value that indicates whether the system supports a multisport workout with the specified list of activities.
### Accessing workout data
- [var activities: [SwimBikeRunWorkout.Activity]](swimbikerunworkout/activities.md)
  An ordered list of activities for the multisport workout.
- [var displayName: String?](swimbikerunworkout/displayname.md)
  The name that the system uses when displaying the workout.
### Comparing workouts
- [var hashValue: Int](swimbikerunworkout/hashvalue.md)
  The hashed value of the workout.
- [func hash(into: inout Hasher)](swimbikerunworkout/hash(into:).md)
  Hashes the essential components of the workout by feeding them into the given hash function.
- [static func == (SwimBikeRunWorkout, SwimBikeRunWorkout) -> Bool](swimbikerunworkout/==(_:_:).md)
  Returns a Boolean value that indicates whether two workouts aren’t equal.
- [static func != (Self, Self) -> Bool](swimbikerunworkout/!=(_:_:).md)
  Returns a Boolean value that indicates whether two workouts are equal.
### Default Implementations
- [Equatable Implementations](swimbikerunworkout/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SingleGoalWorkout](singlegoalworkout.md)
  A workout with a single goal.
- [struct PacerWorkout](pacerworkout.md)
  A workout in which a person covers a specific distance in a given time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout)*