# IntervalBlock

**Framework**: WorkoutKit  
**Kind**: struct

Blocks of work and recovery steps that repeat in a custom workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
struct IntervalBlock
```

## Topics

### Creating an interval block
- [init(steps: [IntervalStep], iterations: Int)](intervalblock/init(steps:iterations:).md)
  Creates a new interval block, in which the workout repeats the provided steps the specified number of times.
### Accessing interval block properties
- [var steps: [IntervalStep]](intervalblock/steps.md)
  A series of work and recovery steps for the interval block.
- [var iterations: Int](intervalblock/iterations.md)
  The number of times the interval block repeats its steps.

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
- [struct IntervalStep](intervalstep.md)
  An interval that represents a work or recovery step in a workout.
- [enum WorkoutGoal](workoutgoal.md)
  A value that specifies the goal for a workout.
- [protocol WorkoutAlert](workoutalert.md)
  An alert that notifies the user of significant events during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/intervalblock)*