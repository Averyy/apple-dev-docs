# WorkoutStep

**Framework**: Workoutkit  
**Kind**: struct

A step in a workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct WorkoutStep
```

## Topics

### Creating new workout steps
- [init(goal: WorkoutGoal, alert: (WorkoutAlert)?)](workoutstep/init(goal:alert:).md)
  Creates a new workout step with the provided goal and alerts.
### Accessing step data
- [var alert: (WorkoutAlert)?](workoutstep/alert.md)
  Alerts used during the step.
- [var goal: WorkoutGoal](workoutstep/goal.md)
  A goal that determines when the step ends.
### Comparing workout steps
- [var hashValue: Int](workoutstep/hashvalue.md)
  The hashed value of the workout step.
- [func hash(into: inout Hasher)](workoutstep/hash(into:).md)
  Hashes the essential components of the workout step by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](workoutstep/!=(_:_:).md)
  Returns a Boolean value that indicates whether two workout steps aren’t equal.
- [static func == (WorkoutStep, WorkoutStep) -> Bool](workoutstep/==(_:_:).md)
  Returns a Boolean value that indicates whether two workout steps are equal.
### Initializers
- [init(goal: WorkoutGoal, alert: (any WorkoutAlert)?, displayName: String?)](workoutstep/init(goal:alert:displayname:).md)
### Instance Properties
- [var displayName: String?](workoutstep/displayname.md)
### Default Implementations
- [Equatable Implementations](workoutstep/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CustomWorkout](customworkout.md)
  A workout that includes a repeating series of work and recovery steps.
- [struct IntervalBlock](intervalblock.md)
  Blocks of work and recovery steps that repeat in a custom workout.
- [struct IntervalStep](intervalstep.md)
  An interval that represents a work or recovery step in a workout.
- [enum WorkoutGoal](workoutgoal.md)
  A value that specifies the goal for a workout.
- [protocol WorkoutAlert](workoutalert.md)
  An alert that notifies the user of significant events during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutstep)*