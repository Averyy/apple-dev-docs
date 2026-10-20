# didDisconnectNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification the system posts when a screen disconnects from the device.

**Availability**:
- iOS 3.2+ - Deprecated in 16.0
- iPadOS 3.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- tvOS - Deprecated in 16.0

> **Deprecated**: Use the [`sceneDidDisconnect(_:)`](../uiscenedelegate/scenediddisconnect%28_%29.md) method on a scene delegate or [`didDisconnectNotification`](../uiscene/diddisconnectnotification.md) to recieve notification of disconnecting scenes from other screens.

## Declaration

```swift
nonisolated
class let didDisconnectNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIScreenDidDisconnectNotification;
```

## Mentions

- [Processing queued notifications](../processing-queued-notifications.md)

#### Discussion

The object of the notification is the [`UIScreen`](../uiscreen.md) object that represented the now-disconnected screen. There’s no `userInfo` dictionary.

## See Also

### Deprecated notifications
- [class let didConnectNotification: NSNotification.Name](./didconnectnotification.md)
  A notification the system posts when a new screen connects to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/diddisconnectnotification)*