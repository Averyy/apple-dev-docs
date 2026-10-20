# requestAuthorization()

**Framework**: WorkoutKit  
**Kind**: method  
**Role**: Instance Method

Requests authorization to schedule workouts.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
final func requestAuthorization() async -> WorkoutScheduler.AuthorizationState
```

## See Also

### Accessing the scheduler
- [static let shared: WorkoutScheduler](./shared.md)
  A shared instance of the workout scheduler.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current device supports scheduled workouts.
- [var authorizationState: WorkoutScheduler.AuthorizationState](./authorizationstate-swift.property.md)
  The workout scheduler’s authorization status.
- [WorkoutScheduler.AuthorizationState](./authorizationstate-swift.enum.md)
  The workout scheduler’s authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutscheduler/requestauthorization())*