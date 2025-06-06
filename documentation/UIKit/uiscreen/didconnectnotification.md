# didConnectNotification

**Framework**: UIKit  
**Kind**: property

A notification the system posts when a new screen connects to the device.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
nonisolated
class let didConnectNotification: NSNotification.Name
```

## Mentions

- [Processing queued notifications](processing-queued-notifications.md)

#### Discussion

Connection notifications aren’t sent for screens that are already present when the app launches. The app can instead use the [`screens`](uiscreen/screens.md) method to get the current set of screens at launch time.

The object of the notification is the [`UIScreen`](uiscreen.md) object representing the new screen. There’s no `userInfo` dictionary.

## See Also

- [class let didDisconnectNotification: NSNotification.Name](uiscreen/diddisconnectnotification.md)
  A notification the system posts when a screen disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/didconnectnotification)*