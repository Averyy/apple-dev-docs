# handleActiveWorkoutRecovery()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the app relaunches after crashing during an active workout session.

**Availability**:
- watchOS 5.0+ - Deprecated in 9.2

## Declaration

```swift
optional func handleActiveWorkoutRecovery()
```

```objc
- (void) handleActiveWorkoutRecovery;
```

## Discussion

To recover from a crash, call your HealthKit store’s [`recoverActiveWorkoutSession(completion:)`](../../HealthKit/hkhealthstore/recoveractiveworkoutsession%28completion%29.md) method to receive a new workout session. You can then set up your data source and delegate as described in [Running workout sessions](../../HealthKit/running-workout-sessions.md).

## See Also

### Related Documentation
- [func recoverActiveWorkoutSession(completion: (HKWorkoutSession?, (any Error)?) -> Void)](../../HealthKit/hkhealthstore/recoveractiveworkoutsession%28completion%29.md)
  Recovers an active workout session.
### Handling a workout session
- [func handle(HKWorkoutConfiguration)](./handle%28_%29-f27i.md)
  Tells the delegate that the user started a workout session on the paired iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleactiveworkoutrecovery())*