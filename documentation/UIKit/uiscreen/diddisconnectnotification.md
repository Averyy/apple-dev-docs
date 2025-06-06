# didDisconnectNotification

**Framework**: UIKit  
**Kind**: property

A notification the system posts when a screen disconnects from the device.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
nonisolated
class let didDisconnectNotification: NSNotification.Name
```

## Mentions

- [Processing queued notifications](processing-queued-notifications.md)

#### Discussion

The object of the notification is the [`UIScreen`](uiscreen.md) object that represented the now-disconnected screen. There’s no `userInfo` dictionary.

## See Also

- [class let didConnectNotification: NSNotification.Name](uiscreen/didconnectnotification.md)
  A notification the system posts when a new screen connects to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/diddisconnectnotification)*