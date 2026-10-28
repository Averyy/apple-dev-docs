# didDisconnectNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that indicates that UIKit removed a scene from your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let didDisconnectNotification: NSNotification.Name
```

```c
extern NSNotificationName const UISceneDidDisconnectNotification;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)

## Discussion

Use this notification to perform any final cleanup before your scene is purged from memory. For example, use it to release references to files or shared resources and to save user data. UIKit places the affected scene in the [`object`](../../Foundation/nsnotification/object.md) property of the notification.

The removal of a scene is a precursor to the destruction of that scene. UIKit disconnects a scene when the user explicitly closes it in the app switcher. UIKit may also disconnect a scene in order to reclaim memory for other processes. UIKit does not automatically disconnect a scene when the user switches to another app.

UIKit also calls the [`sceneDidDisconnect(_:)`](../uiscenedelegate/scenediddisconnect%28_%29.md) method of your scene delegate object.

## See Also

### Responding to life cycle notifications
- [class let willConnectNotification: NSNotification.Name](./willconnectnotification.md)
  A notification that indicates that UIKit added a scene to your app.
- [class let willEnterForegroundNotification: NSNotification.Name](./willenterforegroundnotification.md)
  A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [class let didActivateNotification: NSNotification.Name](./didactivatenotification.md)
  A notification that indicates that the scene is now onscreen and responding to user events.
- [class let willDeactivateNotification: NSNotification.Name](./willdeactivatenotification.md)
  A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [class let didEnterBackgroundNotification: NSNotification.Name](./didenterbackgroundnotification.md)
  A notification that indicates that the scene is running in the background and is no longer onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/diddisconnectnotification)*