# sceneDidBecomeActive(_:)

**Framework**: Uikit  
**Kind**: method

Tells the delegate that the scene became active and is now responding to user events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func sceneDidBecomeActive(_ scene: UIScene)
```

#### Discussion

To use this method, you must implement the [`UISceneDelegate`](uiscenedelegate.md) protocol and configure scenes for your app (see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md)).

Use this method to prepare your scene to be onscreen. UIKit calls this method after loading the interface for your scene, but before that interface appears onscreen. Use it to refresh the contents of views, start timers, or increase frame rates for your UI.

In addition to calling this method, UIKit posts a [`didActivateNotification`](uiscene/didactivatenotification.md) and a [`didBecomeActiveNotification`](uiapplication/didbecomeactivenotification.md).

For more information on what to do when your app becomes active, see [`Preparing your UI to run in the foreground`](preparing-your-ui-to-run-in-the-foreground.md).

> **Note**:  When you implement this method and enable scenes, UIKit calls this method but does not call the [`applicationDidBecomeActive(_:)`](uiapplicationdelegate/applicationdidbecomeactive(_:).md) method on [`UIApplicationDelegate`](uiapplicationdelegate.md).

## Parameters

- `scene`: The scene that became active and is now responding to user events.

## See Also

- [func sceneWillEnterForeground(UIScene)](uiscenedelegate/scenewillenterforeground(_:).md)
  Tells the delegate that the scene is about to begin running in the foreground and become visible to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenedidbecomeactive(_:))*