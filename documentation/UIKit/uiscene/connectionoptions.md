# UIScene.ConnectionOptions

**Framework**: UIKit  
**Kind**: class

A data object containing information about the reasons why UIKit created the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class ConnectionOptions
```

#### Overview

UIKit creates scenes for many reasons. It might do so in response to a Handoff request or a request to open a URL. When there’s a specific reason for creating a scene, UIKit fills a [`UIScene.ConnectionOptions`](uiscene/connectionoptions.md) object with the associated data and passes it to your delegate at connection time. Use the information in this object to respond accordingly. For example, open the URLs that UIKit provides, and display their contents in the scene.

Don’t create [`UIScene.ConnectionOptions`](uiscene/connectionoptions.md) objects directly. UIKit creates [`UIScene.ConnectionOptions`](uiscene/connectionoptions.md) objects for you and passes them to the [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md) method of your scene delegate.

## Topics

### Configuring the scene’s interface
- [var userActivities: Set<NSUserActivity>](uiscene/connectionoptions/useractivities.md)
  Information about user activities that you can use to configure your scene’s interface.
### Handling quick actions
- [var shortcutItem: UIApplicationShortcutItem?](uiscene/connectionoptions/shortcutitem.md)
  The user-selected action to perform.
### Opening URLs
- [var urlContexts: Set<UIOpenURLContext>](uiscene/connectionoptions/urlcontexts.md)
  The URLs to open, along with metadata specifying how to open them.
### Responding to a Handoff request
- [var handoffUserActivityType: String?](uiscene/connectionoptions/handoffuseractivitytype.md)
  The type of the pending Handoff activity.
### Accepting a CloudKit share
- [var cloudKitShareMetadata: CKShareMetadata?](uiscene/connectionoptions/cloudkitsharemetadata.md)
  Information about the CloudKit data that’s now available to the app.
### Responding to notifications
- [var notificationResponse: UNNotificationResponse?](uiscene/connectionoptions/notificationresponse.md)
  A person’s response to one of your app’s notifications.
### Preparing for Near-Field Communication (NFC)
- [var nfcEvent: NFCWindowSceneEvent?](uiscene/connectionoptions/nfcevent.md)
  An event, such as a gesture or exposure to a card reader’s RF field, that creates a Near-Field Communication (NFC) scene.
### Getting the source app
- [var sourceApplication: String?](uiscene/connectionoptions/sourceapplication.md)
  The bundle ID of the app that originated the request.
### Instance Properties
- [var appIntent: (any UISceneAppIntent)?](uiscene/connectionoptions/appintent.md)
  The `AppIntent` that triggered scene creation `AppIntentSceneDelegate.scene(_:willPerform:)` will always be called after scene connection
- [var credentialSessionEvent: CredentialSessionWindowSceneEvent?](uiscene/connectionoptions/credentialsessionevent.md)
  A CredentialSession event has triggered a UIKit scene creation.
- [var gameControllerActivationContext: GCGameControllerActivationContext?](uiscene/connectionoptions/gamecontrolleractivationcontext.md)
- [var marketplaceDisplayOption: MarketplaceDisplayOption?](uiscene/connectionoptions/marketplacedisplayoption.md)
- [var shouldHandleActiveWorkoutRecovery: Bool](uiscene/connectionoptions/shouldhandleactiveworkoutrecovery.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func scene(UIScene, willConnectTo: UISceneSession, options: UIScene.ConnectionOptions)](uiscenedelegate/scene(_:willconnectto:options:).md)
  Tells the delegate about the addition of a scene to the app.
- [func sceneDidDisconnect(UIScene)](uiscenedelegate/scenediddisconnect(_:).md)
  Tells the delegate that UIKit removed a scene from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions)*