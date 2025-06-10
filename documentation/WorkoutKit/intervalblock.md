# IntervalBlock

**Framework**: WorkoutKit  
**Kind**: struct

Blocks of work and recovery steps that repeat in a custom workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
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
### Hashing interval blocks
- [var hashValue: Int](intervalblock/hashvalue.md)
  The hashed value of the interval block.
- [func hash(into: inout Hasher)](intervalblock/hash(into:).md)
  Hashes the essential components of the interval block by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](intervalblock/!=(_:_:).md)
  Returns a Boolean value that indicates whether two interval blocks aren’t equal.
- [static func == (IntervalBlock, IntervalBlock) -> Bool](intervalblock/==(_:_:).md)
  Returns a Boolean value that indicates whether two interval blocks are equal.
### Default Implementations
- [Equatable Implementations](intervalblock/equatable-implementations.md)

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