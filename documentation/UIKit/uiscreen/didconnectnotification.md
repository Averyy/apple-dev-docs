# didConnectNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification the system posts when a new screen connects to the device.

**Availability**:
- iOS 3.2+ - Deprecated in 16.0
- iPadOS 3.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- tvOS - Deprecated in 16.0

> **Deprecated**: Use the [`scene(_:willConnectTo:options:)`](../uiscenedelegate/scene%28_,willconnectto,options%29.md) method on a scene delegate or [`willConnectNotification`](../uiscene/willconnectnotification.md) to recieve notification of connecting scenes from other screens.

## Declaration

```swift
nonisolated
class let didConnectNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIScreenDidConnectNotification;
```

## Mentions

- [Processing queued notifications](../processing-queued-notifications.md)

## Discussion

Connection notifications aren’t sent for screens that are already present when the app launches. The app can instead use the [`screens`](./screens.md) method to get the current set of screens at launch time.

The object of the notification is the [`UIScreen`](../uiscreen.md) object representing the new screen. There’s no `userInfo` dictionary.

## See Also

### Deprecated notifications
- [class let didDisconnectNotification: NSNotification.Name](./diddisconnectnotification.md)
  A notification the system posts when a screen disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/didconnectnotification)*