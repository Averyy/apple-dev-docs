# modeDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when a screen’s mode changes.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
nonisolated
class let modeDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIScreenModeDidChangeNotification;
```

## Mentions

- [Processing queued notifications](../processing-queued-notifications.md)

## Discussion

Clients can use this notification to detect changes in the screen resolution.

The object of the notification is the [`UIScreen`](../uiscreen.md) object whose [`currentMode`](./currentmode.md) property changed. There is no `userInfo` dictionary.

The system posts this notification on the main actor.

## See Also

### Notifications
- [class let brightnessDidChangeNotification: NSNotification.Name](./brightnessdidchangenotification.md)
  A notification that posts when a screen’s brightness changes.
- [class let capturedDidChangeNotification: NSNotification.Name](./captureddidchangenotification.md)
  A notification that posts when the capture status of a screen changes.
- [class let referenceDisplayModeStatusDidChangeNotification: NSNotification.Name](./referencedisplaymodestatusdidchangenotification.md)
  A notification that posts when there’s a change to a screen’s reference display mode status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/modedidchangenotification)*