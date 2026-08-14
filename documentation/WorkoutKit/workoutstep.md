# WorkoutStep

**Framework**: WorkoutKit  
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
- [init(goal: WorkoutGoal, alert: (any WorkoutAlert)?)](workoutstep/init(goal:alert:).md)
  Creates a new workout step with the provided goal and alerts.
### Accessing step data
- [var alert: (any WorkoutAlert)?](workoutstep/alert.md)
  Alerts used during the step.
- [var goal: WorkoutGoal](workoutstep/goal.md)
  A goal that determines when the step ends.
### Initializers
- [init(goal: WorkoutGoal, alert: (any WorkoutAlert)?, displayName: String?)](workoutstep/init(goal:alert:displayname:).md)
### Instance Properties
- [var displayName: String?](workoutstep/displayname.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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