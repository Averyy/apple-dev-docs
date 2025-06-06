# didEnterBackgroundNotification

**Framework**: UIKit  
**Kind**: property

A notification that indicates that the scene is running in the background and is no longer onscreen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let didEnterBackgroundNotification: NSNotification.Name
```

#### Discussion

Use this notification to reduce your scene’s memory usage, free up any shared resources, and clean up your scene’s user interface. Shortly after your notification handler returns, UIKit takes a snapshot of your scene’s interface for display in the app switcher. Make sure your interface doesn’t contain sensitive user information.

UIKit also calls the [`sceneDidEnterBackground(_:)`](uiscenedelegate/scenedidenterbackground(_:).md) method of your scene delegate object.

For more information about what to do when your app enters the background, see [`Preparing your UI to run in the background`](preparing-your-ui-to-run-in-the-background.md).

## See Also

- [class let willConnectNotification: NSNotification.Name](uiscene/willconnectnotification.md)
  A notification that indicates that UIKit added a scene to your app.
- [class let didDisconnectNotification: NSNotification.Name](uiscene/diddisconnectnotification.md)
  A notification that indicates that UIKit removed a scene from your app.
- [class let willEnterForegroundNotification: NSNotification.Name](uiscene/willenterforegroundnotification.md)
  A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [class let didActivateNotification: NSNotification.Name](uiscene/didactivatenotification.md)
  A notification that indicates that the scene is now onscreen and responding to user events.
- [class let willDeactivateNotification: NSNotification.Name](uiscene/willdeactivatenotification.md)
  A notification that indicates that the scene is about to resign the active state and stop responding to user events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/didenterbackgroundnotification)*