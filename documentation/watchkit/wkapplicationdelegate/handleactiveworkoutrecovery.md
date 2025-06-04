# handleActiveWorkoutRecovery()

**Framework**: WatchKit  
**Kind**: method

Tells the delegate when the app relaunches after crashing during an active workout session.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func handleActiveWorkoutRecovery()
```

#### Discussion

To recover from a crash, call your HealthKit store’s [`recoverActiveWorkoutSession(completion:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/2962889-recoveractiveworkoutsession) method to receive a new workout session. You can then set up your data source and delegate as described in [`Running workout sessions`](https://developer.apple.com/documentation/HealthKit/running-workout-sessions).

## See Also

- [func recoverActiveWorkoutSession(completion: (HKWorkoutSession?, (any Error)?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/2962889-recoveractiveworkoutsession)
  Recovers an active workout session.
- [func handle(HKWorkoutConfiguration)](wkapplicationdelegate/handle(_:)-1pfoc.md)
  Tells the delegate that the user started a workout session on the paired iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleactiveworkoutrecovery())*