# WorkoutScheduler.AuthorizationState

**Framework**: Workoutkit  
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
### Working with the raw value
- [init?(rawValue: Int)](workoutscheduler/authorizationstate-swift.enum/init(rawvalue:).md)
  Creates a new authorization status from the provided value.
- [WorkoutScheduler.AuthorizationState.RawValue](workoutscheduler/authorizationstate-swift.enum/rawvalue-swift.typealias.md)
  The data type for the authorization status’s raw value.
### Comparing authorization statuses
- [static func != (Self, Self) -> Bool](workoutscheduler/authorizationstate-swift.enum/!=(_:_:).md)
  Returns a Boolean value that indicates whether two authorization statuses aren’t equal.
- [var hashValue: Int](workoutscheduler/authorizationstate-swift.enum/hashvalue.md)
  The hashed value of the authorization status.
- [func hash(into: inout Hasher)](workoutscheduler/authorizationstate-swift.enum/hash(into:).md)
  Hashes the essential components of the authorization status by feeding them into the given hash function.
- [var rawValue: Int](workoutscheduler/authorizationstate-swift.enum/rawvalue-swift.property.md)
  The authorization status’s raw value.
### Default Implementations
- [Equatable Implementations](workoutscheduler/authorizationstate-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](workoutscheduler/authorizationstate-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
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