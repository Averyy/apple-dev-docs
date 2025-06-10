# WorkoutGoal

**Framework**: WorkoutKit  
**Kind**: enum

A value that specifies the goal for a workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
enum WorkoutGoal
```

## Topics

### Determining workout goals
- [WorkoutGoal.open](workoutgoal/open.md)
  An open workout with no set goal.
- [case distance(Double, UnitLength)](workoutgoal/distance(_:_:).md)
  A goal based on distance traveled during the workout.
- [case energy(Double, UnitEnergy)](workoutgoal/energy(_:_:).md)
  A goal based on the amount of energy burned during the workout.
- [case time(Double, UnitDuration)](workoutgoal/time(_:_:).md)
  A goal based on the amount of time that has elapsed during the workout.
### Comparing workout goals
- [var hashValue: Int](workoutgoal/hashvalue.md)
  The hashed value of the workout goal.
- [func hash(into: inout Hasher)](workoutgoal/hash(into:).md)
  Hashes the essential components of the workout goal by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](workoutgoal/!=(_:_:).md)
  Returns a Boolean value that indicates whether two workout goals aren’t equal.
- [static func == (WorkoutGoal, WorkoutGoal) -> Bool](workoutgoal/==(_:_:).md)
  Returns a Boolean value that indicates whether two workout goals are equal.
### Enumeration Cases
- [case poolSwimDistanceWithTime(Measurement<UnitLength>, Measurement<UnitDuration>)](workoutgoal/poolswimdistancewithtime(_:_:).md)
### Default Implementations
- [Equatable Implementations](workoutgoal/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CustomWorkout](customworkout.md)
  A workout that includes a repeating series of work and recovery steps.
- [struct WorkoutStep](workoutstep.md)
  A step in a workout.
- [struct IntervalBlock](intervalblock.md)
  Blocks of work and recovery steps that repeat in a custom workout.
- [struct IntervalStep](intervalstep.md)
  An interval that represents a work or recovery step in a workout.
- [protocol WorkoutAlert](workoutalert.md)
  An alert that notifies the user of significant events during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutgoal)*