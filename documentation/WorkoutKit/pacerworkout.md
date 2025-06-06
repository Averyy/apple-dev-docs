# PacerWorkout

**Framework**: Workoutkit  
**Kind**: struct

A workout in which a person covers a specific distance in a given time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct PacerWorkout
```

## Topics

### Creating a new pacer workout
- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, distance: Measurement<UnitLength>, time: Measurement<UnitDuration>)](pacerworkout/init(activity:location:distance:time:).md)
  Creates a new pacer workout for the specified distance and time.
- [static func supportsActivity(HKWorkoutActivityType) -> Bool](pacerworkout/supportsactivity(_:).md)
  Returns a Boolean value that indicates whether the system supports pacer workouts for the given workout activity type.
### Accessing workout data
- [var activity: HKWorkoutActivityType](pacerworkout/activity.md)
  The workout activity type.
- [var location: HKWorkoutSessionLocationType](pacerworkout/location.md)
  The workout location.
- [var distance: Measurement<UnitLength>](pacerworkout/distance.md)
  A length measurement representing the distance goal.
- [var time: Measurement<UnitDuration>](pacerworkout/time.md)
  A time measurement representing the time goal.
### Comparing workouts
- [var hashValue: Int](pacerworkout/hashvalue.md)
  The hashed value of the workout.
- [func hash(into: inout Hasher)](pacerworkout/hash(into:).md)
  Hashes the essential components of the workout by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](pacerworkout/!=(_:_:).md)
  Returns a Boolean value that indicates whether two workouts aren’t equal.
- [static func == (PacerWorkout, PacerWorkout) -> Bool](pacerworkout/==(_:_:).md)
  Returns a Boolean value that indicates whether two workouts are equal.
### Default Implementations
- [Equatable Implementations](pacerworkout/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SingleGoalWorkout](singlegoalworkout.md)
  A workout with a single goal.
- [struct SwimBikeRunWorkout](swimbikerunworkout.md)
  A workout for multisport activities that include running, biking, and swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/pacerworkout)*