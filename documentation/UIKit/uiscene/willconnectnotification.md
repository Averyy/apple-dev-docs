# willConnectNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that indicates that UIKit added a scene to your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let willConnectNotification: NSNotification.Name
```

```c
extern NSNotificationName const UISceneWillConnectNotification;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)

#### Discussion

When the user or your app requests a new instance of your user interface, UIKit creates an appropriate [`UIScene`](../uiscene.md) object and places it in the [`object`](../../Foundation/nsnotification/object.md) property of the notification. Use this notification to respond to the addition of the new scene and to begin loading any data that the scene needs to display.

UIKit also calls the [`scene(_:willConnectTo:options:)`](../uiscenedelegate/scene%28_,willconnectto,options%29.md) method of your scene delegate object.

## See Also

### Responding to life cycle notifications
- [class let didDisconnectNotification: NSNotification.Name](./diddisconnectnotification.md)
  A notification that indicates that UIKit removed a scene from your app.
- [class let willEnterForegroundNotification: NSNotification.Name](./willenterforegroundnotification.md)
  A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [class let didActivateNotification: NSNotification.Name](./didactivatenotification.md)
  A notification that indicates that the scene is now onscreen and responding to user events.
- [class let willDeactivateNotification: NSNotification.Name](./willdeactivatenotification.md)
  A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [class let didEnterBackgroundNotification: NSNotification.Name](./didenterbackgroundnotification.md)
  A notification that indicates that the scene is running in the background and is no longer onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/willconnectnotification)*