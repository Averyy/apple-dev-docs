# handleActiveWorkoutRecovery()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate when the app relaunches after crashing during an active workout session.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor optional func handleActiveWorkoutRecovery()
```

## Overview

To recover from a crash, call your HealthKit store’s [`recoverActiveWorkoutSession(completion:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/2962889-recoveractiveworkoutsession) method to receive a new workout session. You can then set up your data source and delegate as described in [`Running workout sessions`](https://developer.apple.com/documentation/HealthKit/running-workout-sessions).

## See Also

- func recoverActiveWorkoutSession(completion: (HKWorkoutSession?, (any Error)?) -> Void) ([Apple Docs](https://developer.apple.com/documentation/healthkit/hkhealthstore/2962889-recoveractiveworkoutsession))
- [func handle(HKWorkoutConfiguration)](handle(_:)-1pfoc.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-1pfoc))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleactiveworkoutrecovery())*