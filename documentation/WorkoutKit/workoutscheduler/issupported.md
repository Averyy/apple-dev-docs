# isSupported

**Framework**: WorkoutKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the current device supports scheduled workouts.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
static var isSupported: Bool { get }
```

## See Also

### Accessing the scheduler
- [static let shared: WorkoutScheduler](./shared.md)
  A shared instance of the workout scheduler.
- [func requestAuthorization() async -> WorkoutScheduler.AuthorizationState](./requestauthorization%28%29.md)
  Requests authorization to schedule workouts.
- [var authorizationState: WorkoutScheduler.AuthorizationState](./authorizationstate-swift.property.md)
  The workout scheduler’s authorization status.
- [WorkoutScheduler.AuthorizationState](./authorizationstate-swift.enum.md)
  The workout scheduler’s authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/issupported)*