# handle(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user started a workout session on the paired iPhone.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
optional func handle(_ workoutConfiguration: HKWorkoutConfiguration)
```

```objc
- (void) handleWorkoutConfiguration:(HKWorkoutConfiguration *) workoutConfiguration;
```

#### Discussion

When your iPhone app starts a workout session using the HealthKit store’s `startWatchAppWithWorkoutConfiguration:completion:` method, the system launches or wakes the corresponding Watch app in the background and calls this method. Use this method to configure an [`HKWorkoutSession`](../../HealthKit/hkworkoutsession.md) object in your Watch app, and then call [`start(_:)`](../../HealthKit/hkhealthstore/start%28_%29.md) to start the session.

## Parameters

- `workoutConfiguration`: The workout configuration data. You can use this information to start a workout session on the user’s Apple Watch.

## See Also

### Handling a workout session
- [func handleActiveWorkoutRecovery()](./handleactiveworkoutrecovery%28%29.md)
  Tells the delegate when the app relaunches after crashing during an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-1pfoc)*