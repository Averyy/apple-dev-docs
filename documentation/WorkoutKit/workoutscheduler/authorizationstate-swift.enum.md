# WorkoutScheduler.AuthorizationState

**Framework**: WorkoutKit  
**Kind**: enum  
**Role**: Enumeration

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
- [WorkoutScheduler.AuthorizationState.authorized](./authorizationstate-swift.enum/authorized.md)
  The user authorized your app to schedule workouts.
- [WorkoutScheduler.AuthorizationState.denied](./authorizationstate-swift.enum/denied.md)
  The user denied authorization for scheduling workouts.
- [WorkoutScheduler.AuthorizationState.notDetermined](./authorizationstate-swift.enum/notdetermined.md)
  Your app hasn’t yet requested authorization to schedule workouts.
- [WorkoutScheduler.AuthorizationState.restricted](./authorizationstate-swift.enum/restricted.md)
  The system restricted your app from scheduling workouts.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Accessing the scheduler
- [static let shared: WorkoutScheduler](./shared.md)
  A shared instance of the workout scheduler.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current device supports scheduled workouts.
- [func requestAuthorization() async -> WorkoutScheduler.AuthorizationState](./requestauthorization%28%29.md)
  Requests authorization to schedule workouts.
- [var authorizationState: WorkoutScheduler.AuthorizationState](./authorizationstate-swift.property.md)
  The workout scheduler’s authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/authorizationstate-swift.enum)*