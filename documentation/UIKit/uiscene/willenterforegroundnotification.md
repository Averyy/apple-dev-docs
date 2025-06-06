# willEnterForegroundNotification

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

UIKit posts this notification before moving a scene to the foreground. This transition occurs both for newly created and connected scenes and for scenes that were running in the background and were brought to the foreground by the system or a user action. A scene enters the foreground as a precursor to becoming visible onscreen, so this method is invariably followed by the posting of a [`didActivateNotification`](uiscene/didactivatenotification.md) notification. UIKit places the scene object in the [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) property of the notification.

UIKit also calls the [`sceneWillEnterForeground(_:)`](uiscenedelegate/scenewillenterforeground(_:).md) method of your scene delegate object.

## See Also

- [class let willConnectNotification: NSNotification.Name](uiscene/willconnectnotification.md)
  A notification that indicates that UIKit added a scene to your app.
- [class let didDisconnectNotification: NSNotification.Name](uiscene/diddisconnectnotification.md)
  A notification that indicates that UIKit removed a scene from your app.
- [class let didActivateNotification: NSNotification.Name](uiscene/didactivatenotification.md)
  A notification that indicates that the scene is now onscreen and responding to user events.
- [class let willDeactivateNotification: NSNotification.Name](uiscene/willdeactivatenotification.md)
  A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [class let didEnterBackgroundNotification: NSNotification.Name](uiscene/didenterbackgroundnotification.md)
  A notification that indicates that the scene is running in the background and is no longer onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/willenterforegroundnotification)*