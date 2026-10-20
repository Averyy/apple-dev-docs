# referenceDisplayModeStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when there’s a change to a screen’s reference display mode status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+

## Declaration

```swift
nonisolated
class let referenceDisplayModeStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIScreenReferenceDisplayModeStatusDidChangeNotification;
```

#### Discussion

The notification’s [`object`](../../Foundation/notification/object.md) is the changed screen. Use that object’s [`referenceDisplayModeStatus`](./referencedisplaymodestatus-swift.property.md) property to retrieve the new status.

The system posts this notification on the main actor.

## See Also

### Notifications
- [class let brightnessDidChangeNotification: NSNotification.Name](./brightnessdidchangenotification.md)
  A notification that posts when a screen’s brightness changes.
- [class let modeDidChangeNotification: NSNotification.Name](./modedidchangenotification.md)
  A notification that posts when a screen’s mode changes.
- [class let capturedDidChangeNotification: NSNotification.Name](./captureddidchangenotification.md)
  A notification that posts when the capture status of a screen changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatusdidchangenotification)*