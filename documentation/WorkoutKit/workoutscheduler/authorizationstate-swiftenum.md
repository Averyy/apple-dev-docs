# WorkoutScheduler.AuthorizationState

**Framework**: WorkoutKit  
**Kind**: enum

The workout scheduler’s authorization status.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
enum AuthorizationState
```

## Topics

### Determining the authorization status
- [WorkoutScheduler.AuthorizationState.authorized](workoutscheduler/authorizationstate-swift.enum/authorized.md)
  The user authorized your app to schedule workouts.
- [WorkoutScheduler.AuthorizationState.denied](workoutscheduler/authorizationstate-swift.enum/denied.md)
  The user denied authorization for scheduling workouts.
- [WorkoutScheduler.AuthorizationState.notDetermined](workoutscheduler/authorizationstate-swift.enum/notdetermined.md)
  Your app hasn’t yet requested authorization to schedule workouts.
- [WorkoutScheduler.AuthorizationState.restricted](workoutscheduler/authorizationstate-swift.enum/restricted.md)
  The system restricted your app from scheduling workouts.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [static let shared: WorkoutScheduler](workoutscheduler/shared.md)
  A shared instance of the workout scheduler.
- [static var isSupported: Bool](workoutscheduler/issupported.md)
  A Boolean value that indicates whether the current device supports scheduled workouts.
- [func requestAuthorization() async -> WorkoutScheduler.AuthorizationState](workoutscheduler/requestauthorization.md)
  Requests authorization to schedule workouts.
- [var authorizationState: WorkoutScheduler.AuthorizationState](workoutscheduler/authorizationstate-swift.property.md)
  The workout scheduler’s authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/authorizationstate-swift.enum)*