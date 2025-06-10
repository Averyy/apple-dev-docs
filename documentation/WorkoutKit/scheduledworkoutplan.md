# ScheduledWorkoutPlan

**Framework**: WorkoutKit  
**Kind**: struct

A wrapper around a workout plan that your app can use to schedule the workout plan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct ScheduledWorkoutPlan
```

## Topics

### Creating scheduled workout plans
- [init(WorkoutPlan, date: DateComponents)](scheduledworkoutplan/init(_:date:).md)
  Creates a new scheduled workout plan.
### Accessing plan data
- [var plan: WorkoutPlan](scheduledworkoutplan/plan.md)
  The target workout plan to schedule.
- [var date: DateComponents](scheduledworkoutplan/date.md)
  Date components that determine when the workout should begin.
- [var complete: Bool](scheduledworkoutplan/complete.md)
  A Boolean value that indicates whether the workout is complete.
### Comparing plans
- [var hashValue: Int](scheduledworkoutplan/hashvalue.md)
  The hashed value of the scheduled plan.
- [func hash(into: inout Hasher)](scheduledworkoutplan/hash(into:).md)
  Hashes the essential components of the scheduled plan by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](scheduledworkoutplan/!=(_:_:).md)
  Returns a Boolean value that indicates whether two scheduled plans aren’t equal.
- [static func == (ScheduledWorkoutPlan, ScheduledWorkoutPlan) -> Bool](scheduledworkoutplan/==(_:_:).md)
  Returns a Boolean value that indicates whether two scheduled plans are equal.
### Default Implementations
- [Equatable Implementations](scheduledworkoutplan/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WorkoutPlan](workoutplan.md)
  A wrapper around a workout object that your app can use to open the object in Workout or schedule it for later.
- [class WorkoutScheduler](workoutscheduler.md)
  An object for scheduling and managing workouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/scheduledworkoutplan)*