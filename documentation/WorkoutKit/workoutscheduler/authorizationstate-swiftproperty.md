# authorizationState

**Framework**: WorkoutKit  
**Kind**: property

The workout scheduler’s authorization status.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final var authorizationState: WorkoutScheduler.AuthorizationState { get async }
```

## See Also

- [static let shared: WorkoutScheduler](workoutscheduler/shared.md)
  A shared instance of the workout scheduler.
- [static var isSupported: Bool](workoutscheduler/issupported.md)
  A Boolean value that indicates whether the current device supports scheduled workouts.
- [func requestAuthorization() async -> WorkoutScheduler.AuthorizationState](workoutscheduler/requestauthorization.md)
  Requests authorization to schedule workouts.
- [WorkoutScheduler.AuthorizationState](workoutscheduler/authorizationstate-swift.enum.md)
  The workout scheduler’s authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/authorizationstate-swift.property)*