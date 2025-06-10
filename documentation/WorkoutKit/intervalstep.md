# IntervalStep

**Framework**: WorkoutKit  
**Kind**: struct

An interval that represents a work or recovery step in a workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct IntervalStep
```

## Topics

### Creating interval steps
- [init(IntervalStep.Purpose, goal: WorkoutGoal, alert: (any WorkoutAlert)?)](intervalstep/init(_:goal:alert:).md)
- [init(IntervalStep.Purpose, step: WorkoutStep)](intervalstep/init(_:step:).md)
  Creates a new interval step.
### Accessing step data
- [var purpose: IntervalStep.Purpose](intervalstep/purpose-swift.property.md)
  The purpose of the interval step.
- [var step: WorkoutStep](intervalstep/step.md)
  The workout step to perform.
### Comparing interval steps
- [var hashValue: Int](intervalstep/hashvalue.md)
  The hashed value of the interval step.
- [func hash(into: inout Hasher)](intervalstep/hash(into:).md)
  Hashes the essential components of the interval step by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](intervalstep/!=(_:_:).md)
  Returns a Boolean value that indicates whether two interval steps aren’t equal.
- [static func == (IntervalStep, IntervalStep) -> Bool](intervalstep/==(_:_:).md)
  Returns a Boolean value that indicates whether two interval steps are equal.
### Enumerations
- [IntervalStep.Purpose](intervalstep/purpose-swift.enum.md)
  An interval step’s purpose.
### Default Implementations
- [Equatable Implementations](intervalstep/equatable-implementations.md)

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
- [enum WorkoutGoal](workoutgoal.md)
  A value that specifies the goal for a workout.
- [protocol WorkoutAlert](workoutalert.md)
  An alert that notifies the user of significant events during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/intervalstep)*