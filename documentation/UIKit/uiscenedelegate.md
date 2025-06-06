# UISceneDelegate

**Framework**: UIKit  
**Kind**: protocol

The core methods you use to respond to life-cycle events occurring within a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UISceneDelegate : NSObjectProtocol
```

#### Overview

Use your [`UISceneDelegate`](uiscenedelegate.md) object to manage life-cycle events in one instance of your app’s user interface. This interface defines methods for responding to state transitions that affect the scene, including when the scene enters the foreground and becomes active, and when it enters the background. Use your delegate to provide appropriate behavior when these transitions occur. For example, finish critical tasks and quiet your app when it enters the background.

Don’t create [`UISceneDelegate`](uiscenedelegate.md) objects directly. Instead, specify the name of your custom delegate class as part of the configuration data for your scenes. You can specify this information in your app’s `Info.plist` file, or in the [`UISceneConfiguration`](uisceneconfiguration.md) object you return from your app delegate’s [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) method. For more information about how to configure scenes, see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md).

## Topics

### Working with window scenes
- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md)
  Support side-by-side instances of your app’s interface and create new windows.
### Connecting and disconnecting the scene
- [func scene(UIScene, willConnectTo: UISceneSession, options: UIScene.ConnectionOptions)](uiscenedelegate/scene(_:willconnectto:options:).md)
  Tells the delegate about the addition of a scene to the app.
- [func sceneDidDisconnect(UIScene)](uiscenedelegate/scenediddisconnect(_:).md)
  Tells the delegate that UIKit removed a scene from your app.
- [UIScene.ConnectionOptions](uiscene/connectionoptions.md)
  A data object containing information about the reasons why UIKit created the scene.
### Transitioning to the foreground
- [func sceneWillEnterForeground(UIScene)](uiscenedelegate/scenewillenterforeground(_:).md)
  Tells the delegate that the scene is about to begin running in the foreground and become visible to the user.
- [func sceneDidBecomeActive(UIScene)](uiscenedelegate/scenedidbecomeactive(_:).md)
  Tells the delegate that the scene became active and is now responding to user events.
### Transitioning to the background
- [func sceneWillResignActive(UIScene)](uiscenedelegate/scenewillresignactive(_:).md)
  Tells the delegate that the scene is about to resign the active state and stop responding to user events.
- [func sceneDidEnterBackground(UIScene)](uiscenedelegate/scenedidenterbackground(_:).md)
  Tells the delegate that the scene is running in the background and is no longer onscreen.
### Opening URLs
- [func scene(UIScene, openURLContexts: Set<UIOpenURLContext>)](uiscenedelegate/scene(_:openurlcontexts:).md)
  Asks the delegate to open one or more URLs.
### Continuing user activities
- [func scene(UIScene, willContinueUserActivityWithType: String)](uiscenedelegate/scene(_:willcontinueuseractivitywithtype:).md)
  Tells the delegate that it’s about to receive Handoff-related data.
- [func scene(UIScene, continue: NSUserActivity)](uiscenedelegate/scene(_:continue:).md)
  Tells the delegate to handle the specified Handoff-related activity.
- [func scene(UIScene, didFailToContinueUserActivityWithType: String, error: any Error)](uiscenedelegate/scene(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the activity couldn’t be continued.
### Saving the state of the scene
- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [func stateRestorationActivity(for: UIScene) -> NSUserActivity?](uiscenedelegate/staterestorationactivity(for:).md)
  Returns a user activity object encapsulating the current state of the specified scene.
- [func scene(UIScene, restoreInteractionStateWith: NSUserActivity)](uiscenedelegate/scene(_:restoreinteractionstatewith:).md)
- [func scene(UIScene, didUpdate: NSUserActivity)](uiscenedelegate/scene(_:didupdate:).md)
  Tells the delegate that the specified activity object was updated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UIWindowSceneDelegate](uiwindowscenedelegate.md)

## See Also

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md)
  Support side-by-side instances of your app’s interface and create new windows.
- [protocol UIWindowSceneDelegate](uiwindowscenedelegate.md)
  Additional methods that you use to manage app-specific tasks occurring in a scene.
- [class UIWindowScene](uiwindowscene.md)
  A scene that manages one or more windows for your app.
- [class UIScene](uiscene.md)
  An object that represents one instance of your app’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate)*