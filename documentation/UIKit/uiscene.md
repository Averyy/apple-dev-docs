# UIScene

**Framework**: UIKit  
**Kind**: class

An object that represents one instance of your app’s user interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIScene
```

#### Overview

UIKit creates a scene object for each instance of your app’s UI that the user or your app requests. Typically, UIKit creates a [`UIWindowScene`](uiwindowscene.md) object instead of a [`UIScene`](uiscene.md) object, but you use the methods and properties of this class to access information about a scene.

Every scene object has an associated delegate object, an object that adopts the [`UISceneDelegate`](uiscenedelegate.md) protocol. When the state of the scene changes, the scene object notifies its delegate object and posts appropriate notifications to registered observer objects. Use the delegate object and notifications to respond to changes in the state of the scene. For example, use it to determine when your scene moves to the background.

You don’t create scene objects directly. You can programmatically ask UIKit to create a scene object for your app by calling the [`requestSceneSessionActivation(_:userActivity:options:errorHandler:)`](uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:).md) method of [`UIApplication`](uiapplication.md). UIKit also creates scenes in response to user interactions. When configuring your app’s scene support, specify [`UIWindowScene`](uiwindowscene.md) objects instead of [`UIScene`](uiscene.md) objects.

## Topics

### Creating a scene object
- [init(session: UISceneSession, connectionOptions: UIScene.ConnectionOptions)](uiscene/init(session:connectionoptions:).md)
  Creates a scene object using the specified session and connection information.
### Managing the life cycle of a scene
- [var delegate: (any UISceneDelegate)?](uiscene/delegate.md)
  The object you use to receive life-cycle events associated with the scene.
- [protocol UISceneDelegate](uiscenedelegate.md)
  The core methods you use to respond to life-cycle events occurring within a scene.
### Getting the scene attributes
- [var activationState: UIScene.ActivationState](uiscene/activationstate-swift.property.md)
  The current execution state of the scene.
- [UIScene.ActivationState](uiscene/activationstate-swift.enum.md)
  Constants that indicate the foreground or background execution state of your app.
- [var title: String!](uiscene/title.md)
  A user-visible string you supply to help users differentiate among your app’s scenes.
- [var subtitle: String](uiscene/subtitle.md)
  A string that the app displays in the title bar of a window when running in macOS.
### Specifying the scene’s activation conditions
- [var activationConditions: UISceneActivationConditions](uiscene/activationconditions.md)
  The conditions that define when UIKit activates the scene object.
- [class UISceneActivationConditions](uisceneactivationconditions.md)
  The set of conditions that define when UIKit activates the current scene.
### Responding to life cycle notifications
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
- [class let didEnterBackgroundNotification: NSNotification.Name](uiscene/didenterbackgroundnotification.md)
  A notification that indicates that the scene is running in the background and is no longer onscreen.
### Working with system protection manager
- [var systemProtectionManager: UIScene.SystemProtectionManager?](uiscene/systemprotectionmanager-swift.property.md)
  The system protection manager associated with this scene.
- [UIScene.SystemProtectionManager](uiscene/systemprotectionmanager-swift.class.md)
  A class that represents the status of system protection for the scene.
- [class let systemProtectionDidChangeNotification: NSNotification.Name](uiscene/systemprotectiondidchangenotification.md)
  A notification posted when the system-protection attributes of a scene change.
### Getting the scene’s session
- [var session: UISceneSession](uiscene/session.md)
  The session associated with the scene.
- [class UISceneSession](uiscenesession.md)
  An object that contains information about one of your app’s scenes.
### Opening URLs
- [func open(URL, options: UIScene.OpenExternalURLOptions?, completionHandler: ((Bool) -> Void)?)](uiscene/open(_:options:completionhandler:).md)
  Attempts to open the resource at the specified URL asynchronously.
- [UIScene.OpenExternalURLOptions](uiscene/openexternalurloptions.md)
  Options you specify when asking a scene to open a URL.
### Supporting state restoration
- [func completeStateRestoration()](uiscene/completestaterestoration.md)
- [func extendStateRestoration()](uiscene/extendstaterestoration.md)
### Getting the pointer lock state
- [var pointerLockState: UIPointerLockState?](uiscene/pointerlockstate.md)
  The pointer lock state for the scene.
- [class UIPointerLockState](uipointerlockstate.md)
  An object that contains information about a scene’s pointer lock state.
### Constants
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.
- [UIScene.OpenURLOptions](uiscene/openurloptions.md)
  Options that UIKit provides when asking your app to open a URL.
### Instance Methods
- [func getDefaultAudioSession(completionHandler: (AVAudioSession?) -> Void)](uiscene/getdefaultaudiosession(completionhandler:).md)
  Retrieves the audio session that contains all sounds that implicitly belong to this scene.

## Relationships

### Inherits From
- [UIResponder](uiresponder.md)
### Inherited By
- [UIWindowScene](uiwindowscene.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md)
  Support side-by-side instances of your app’s interface and create new windows.
- [protocol UIWindowSceneDelegate](uiwindowscenedelegate.md)
  Additional methods that you use to manage app-specific tasks occurring in a scene.
- [class UIWindowScene](uiwindowscene.md)
  A scene that manages one or more windows for your app.
- [protocol UISceneDelegate](uiscenedelegate.md)
  The core methods you use to respond to life-cycle events occurring within a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene)*