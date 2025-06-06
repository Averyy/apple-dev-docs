# sceneWillEnterForeground(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the scene is about to begin running in the foreground and become visible to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func sceneWillEnterForeground(_ scene: UIScene)
```

#### Discussion

To use this method, you must implement the [`UISceneDelegate`](uiscenedelegate.md) protocol and configure scenes for your app (see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md)).

UIKit calls this method before moving a scene to the foreground. This transition occurs both for newly created and connected scenes, as well as for scenes that were running in the background and were brought to the foreground by the system or a user action. A scene enters the foreground as a precursor to becoming visible onscreen, so this method is invariably followed by a call to the [`sceneDidBecomeActive(_:)`](uiscenedelegate/scenedidbecomeactive(_:).md) method.

In addition to calling this method, UIKit posts a [`didActivateNotification`](uiscene/didactivatenotification.md) and a [`willEnterForegroundNotification`](uiscene/willenterforegroundnotification.md).

For more information on what to do when your app is about to enter the foreground, see [`Preparing your UI to run in the foreground`](preparing-your-ui-to-run-in-the-foreground.md).

> **Note**:  When you implement this method and enable scenes, UIKit calls this method but does not call the [`applicationWillEnterForeground(_:)`](uiapplicationdelegate/applicationwillenterforeground(_:).md) method on [`UIApplicationDelegate`](uiapplicationdelegate.md).

 When you implement this method and enable scenes, UIKit calls this method but does not call the [`applicationWillEnterForeground(_:)`](uiapplicationdelegate/applicationwillenterforeground(_:).md) method on [`UIApplicationDelegate`](uiapplicationdelegate.md).

## Parameters

- `scene`: The scene that is about to enter the foreground.

## See Also

- [func sceneDidBecomeActive(UIScene)](uiscenedelegate/scenedidbecomeactive(_:).md)
  Tells the delegate that the scene became active and is now responding to user events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenewillenterforeground(_:))*