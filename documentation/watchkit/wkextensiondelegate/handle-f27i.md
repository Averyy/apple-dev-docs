# handle(_:)

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that the user started a workout session on the paired iPhone.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor
optional func handle(_ workoutConfiguration: HKWorkoutConfiguration)
```

#### Discussion

When your iPhone app starts a workout session using the HealthKit store’s `startWatchAppWithWorkoutConfiguration:completion:` method, the system launches or wakes the corresponding Watch app in the background and calls this method. Use this method to configure an [`HKWorkoutSession`](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession) object in your Watch app, and then call [`start(_:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/1627946-start) to start the session.

## Parameters

- `workoutConfiguration`: The workout configuration data. You can use this information to start a workout session on the user’s Apple Watch.

## See Also

- [func handleActiveWorkoutRecovery()](wkextensiondelegate/handleactiveworkoutrecovery.md)
  Tells the delegate when the app relaunches after crashing during an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-f27i)*