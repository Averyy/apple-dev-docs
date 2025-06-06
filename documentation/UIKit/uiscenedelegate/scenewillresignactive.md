# sceneWillResignActive(_:)

**Framework**: Uikit  
**Kind**: method

Tells the delegate that the scene is about to resign the active state and stop responding to user events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func sceneWillResignActive(_ scene: UIScene)
```

#### Discussion

To use this method, you must implement the [`UISceneDelegate`](uiscenedelegate.md) protocol and configure scenes for your app (see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md)).

UIKit calls this method for temporary interruptions, such as when displaying system alerts. It also calls the method before transitioning your app to the background state.

Use this method to quiet your interface and prepare it to stop interacting with the user. Specifically, pause ongoing tasks, disable timers, and decrease frame rates or stop updating your interface altogether. Games should use this method to pause the game. By the time this method returns, your app should be doing minimal work while it waits to transition to the background or to the foreground again.

If your scene has unsaved user data, save that data in this method to ensure that it isn’t lost. However, never save data solely from this method. Instead, save it at appropriate points from your view controllers, usually in response to user actions. For example, save data when the user dismisses a data-entry screen. Don’t rely on specific app transitions to save all of your app’s critical data.

In addition to calling this method, UIKit posts a [`willDeactivateNotification`](uiscene/willdeactivatenotification.md) and a [`willResignActiveNotification`](uiapplication/willresignactivenotification.md).

For more information about what to do when your app resigns the active state, see [`Preparing your UI to run in the background`](preparing-your-ui-to-run-in-the-background.md).

> **Note**:  When you implement this method and enable scenes, UIKit calls this method but does not call the [`applicationWillResignActive(_:)`](uiapplicationdelegate/applicationwillresignactive(_:).md) method on [`UIApplicationDelegate`](uiapplicationdelegate.md).

## Parameters

- `scene`: The scene that is about to stop responding to user events.

## See Also

- [func sceneDidEnterBackground(UIScene)](uiscenedelegate/scenedidenterbackground(_:).md)
  Tells the delegate that the scene is running in the background and is no longer onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenewillresignactive(_:))*