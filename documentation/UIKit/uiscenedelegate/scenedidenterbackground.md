# sceneDidEnterBackground(_:)

**Framework**: Uikit  
**Kind**: method

Tells the delegate that the scene is running in the background and is no longer onscreen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func sceneDidEnterBackground(_ scene: UIScene)
```

#### Discussion

To use this method, you must implement the [`UISceneDelegate`](uiscenedelegate.md) protocol and configure scenes for your app (see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md)).

Use this method to reduce your scene’s memory usage, free up any shared resources, and clean up your scene’s user interface. Shortly after this method returns, UIKit takes a snapshot of your scene’s interface for display in the app switcher. Make sure your interface doesn’t contain sensitive user information.

In addition to calling this method, UIKit posts a [`didEnterBackgroundNotification`](uiscene/didenterbackgroundnotification.md) notification from [`UIApplication`](uiapplication.md) and [`UIScene`](uiscene.md).

For more information about what to do when your app enters the background, see [`Preparing your UI to run in the background`](preparing-your-ui-to-run-in-the-background.md).

> **Note**:  When you implement this method and enable scenes, UIKit calls this method but does not call the [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method on [`UIApplicationDelegate`](uiapplicationdelegate.md).

## Parameters

- `scene`: The scene that entered the background.

## See Also

- [func sceneWillResignActive(UIScene)](uiscenedelegate/scenewillresignactive(_:).md)
  Tells the delegate that the scene is about to resign the active state and stop responding to user events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenedidenterbackground(_:))*