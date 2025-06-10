# shared

**Framework**: WorkoutKit  
**Kind**: property

A shared instance of the workout scheduler.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static let shared: WorkoutScheduler
```

## See Also

- [static var isSupported: Bool](workoutscheduler/issupported.md)
  A Boolean value that indicates whether the current device supports scheduled workouts.
- [func requestAuthorization() async -> WorkoutScheduler.AuthorizationState](workoutscheduler/requestauthorization.md)
  Requests authorization to schedule workouts.
- [var authorizationState: WorkoutScheduler.AuthorizationState](workoutscheduler/authorizationstate-swift.property.md)
  The workout scheduler’s authorization status.
- [WorkoutScheduler.AuthorizationState](workoutscheduler/authorizationstate-swift.enum.md)
  The workout scheduler’s authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/shared)*