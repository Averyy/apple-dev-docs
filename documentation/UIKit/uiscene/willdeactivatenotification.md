# willDeactivateNotification

**Framework**: UIKit  
**Kind**: property

A notification that indicates that the scene is about to resign the active state and stop responding to user events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let willDeactivateNotification: NSNotification.Name
```

#### Discussion

UIKit posts this notification for temporary interruptions, such as when displaying system alerts. It also posts this notification before transitioning your app to the background state. UIKit places the scene object in the [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) property of the notification.

Use this notification to quiet your interface and prepare it to stop interacting with the user. Specifically, pause ongoing tasks, disable timers, and decrease frame rates or stop updating your interface altogether. Games should use this notification to pause the game. By the time your handler method returns, your app should be doing minimal work while it waits to transition to the background or to the foreground again.

If your scene has unsaved user data, save that data here to ensure that it isn’t lost. However, never save data solely from your notification handler. Instead, save it at appropriate points from your view controllers, usually in response to user actions. For example, save data when the user dismisses a data-entry screen. Do not rely on specific app transitions to save all of your app’s critical data.

UIKit also calls the [`sceneWillResignActive(_:)`](uiscenedelegate/scenewillresignactive(_:).md) method of your scene delegate object.

For more information about what to do when your app resigns the active state, see [`Preparing your UI to run in the background`](preparing-your-ui-to-run-in-the-background.md).

## See Also

- [class let willConnectNotification: NSNotification.Name](uiscene/willconnectnotification.md)
  A notification that indicates that UIKit added a scene to your app.
- [class let didDisconnectNotification: NSNotification.Name](uiscene/diddisconnectnotification.md)
  A notification that indicates that UIKit removed a scene from your app.
- [class let willEnterForegroundNotification: NSNotification.Name](uiscene/willenterforegroundnotification.md)
  A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [class let didActivateNotification: NSNotification.Name](uiscene/didactivatenotification.md)
  A notification that indicates that the scene is now onscreen and responding to user events.
- [class let didEnterBackgroundNotification: NSNotification.Name](uiscene/didenterbackgroundnotification.md)
  A notification that indicates that the scene is running in the background and is no longer onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/willdeactivatenotification)*