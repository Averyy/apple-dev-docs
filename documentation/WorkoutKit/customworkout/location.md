# location

**Framework**: WorkoutKit  
**Kind**: property  
**Role**: Instance Property

The workout session location for the workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
var location: HKWorkoutSessionLocationType { get set }
```

## See Also

### Accessing workout data
- [var displayName: String?](./displayname.md)
  The name that the system uses when displaying the workout.
- [var activity: HKWorkoutActivityType](./activity.md)
  The type of activity performed during the workout.
- [var warmup: WorkoutStep?](./warmup.md)
  The warmup step (if any).
- [var blocks: [IntervalBlock]](./blocks.md)
  A block of repeating work and recovery steps.
- [var cooldown: WorkoutStep?](./cooldown.md)
  The cooldown step (if any).


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/customworkout/location)*