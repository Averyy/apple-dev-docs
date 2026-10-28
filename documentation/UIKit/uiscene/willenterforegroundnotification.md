# willEnterForegroundNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let willEnterForegroundNotification: NSNotification.Name
```

```c
extern NSNotificationName const UISceneWillEnterForegroundNotification;
```

## Discussion

UIKit posts this notification before moving a scene to the foreground. This transition occurs both for newly created and connected scenes and for scenes that were running in the background and were brought to the foreground by the system or a user action. A scene enters the foreground as a precursor to becoming visible onscreen, so this method is invariably followed by the posting of a [`didActivateNotification`](./didactivatenotification.md) notification. UIKit places the scene object in the [`object`](../../Foundation/nsnotification/object.md) property of the notification.

UIKit also calls the [`sceneWillEnterForeground(_:)`](../uiscenedelegate/scenewillenterforeground%28_%29.md) method of your scene delegate object.

## See Also

### Responding to life cycle notifications
- [class let willConnectNotification: NSNotification.Name](./willconnectnotification.md)
  A notification that indicates that UIKit added a scene to your app.
- [class let didDisconnectNotification: NSNotification.Name](./diddisconnectnotification.md)
  A notification that indicates that UIKit removed a scene from your app.
- [class let didActivateNotification: NSNotification.Name](./didactivatenotification.md)
  A notification that indicates that the scene is now onscreen and responding to user events.
- [class let willDeactivateNotification: NSNotification.Name](./willdeactivatenotification.md)
  A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [class let didEnterBackgroundNotification: NSNotification.Name](./didenterbackgroundnotification.md)
  A notification that indicates that the scene is running in the background and is no longer onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/willenterforegroundnotification)*