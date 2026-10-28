# UIScene.ConnectionOptions

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UISceneConnectionOptions : NSObject
```

## Overview

UIKit creates scenes for many reasons. It might do so in response to a Handoff request or a request to open a URL. When there’s a specific reason for creating a scene, UIKit fills a [`UIScene.ConnectionOptions`](./connectionoptions.md) object with the associated data and passes it to your delegate at connection time. Use the information in this object to respond accordingly. For example, open the URLs that UIKit provides, and display their contents in the scene.

Don’t create [`UIScene.ConnectionOptions`](./connectionoptions.md) objects directly. UIKit creates [`UIScene.ConnectionOptions`](./connectionoptions.md) objects for you and passes them to the [`scene(_:willConnectTo:options:)`](../uiscenedelegate/scene%28_,willconnectto,options%29.md) method of your scene delegate.

## Topics

### Configuring the scene’s interface
- [var userActivities: Set<NSUserActivity>](./connectionoptions/useractivities.md)
  Information about user activities that you can use to configure your scene’s interface.
### Handling quick actions
- [var shortcutItem: UIApplicationShortcutItem?](./connectionoptions/shortcutitem.md)
  The user-selected action to perform.
### Opening URLs
- [var urlContexts: Set<UIOpenURLContext>](./connectionoptions/urlcontexts.md)
  The URLs to open, along with metadata specifying how to open them.
### Responding to a Handoff request
- [var handoffUserActivityType: String?](./connectionoptions/handoffuseractivitytype.md)
  The type of the pending Handoff activity.
### Accepting a CloudKit share
- [var cloudKitShareMetadata: CKShareMetadata?](./connectionoptions/cloudkitsharemetadata.md)
  Information about the CloudKit data that’s now available to the app.
### Responding to notifications
- [var notificationResponse: UNNotificationResponse?](./connectionoptions/notificationresponse.md)
  A person’s response to one of your app’s notifications.
### Preparing for Near-Field Communication (NFC)
- [var nfcEvent: NFCWindowSceneEvent?](./connectionoptions/nfcevent.md)
  An event, such as a gesture or exposure to a card reader’s RF field, that creates a Near-Field Communication (NFC) scene.
### Getting the source app
- [var sourceApplication: String?](./connectionoptions/sourceapplication.md)
  The bundle ID of the app that originated the request.
### Getting scene accessory context
- [var sceneAccessoryUserInfo: Any?](./connectionoptions/sceneaccessoryuserinfo.md)
  An optional user info object, provided when creating the `UISceneAccessory` for this scene accessory.
### Instance Properties
- [var appIntent: (any UISceneAppIntent)?](./connectionoptions/appintent.md)
  The `AppIntent` that triggered scene creation `AppIntentSceneDelegate.scene(_:willPerform:)` will always be called after scene connection
- [var credentialSessionEvent: CredentialSessionWindowSceneEvent?](./connectionoptions/credentialsessionevent.md)
  A CredentialSession event has triggered a UIKit scene creation.
- [var gameControllerActivationContext: GCGameControllerActivationContext?](./connectionoptions/gamecontrolleractivationcontext.md)
- [var marketplaceDisplayOption: MarketplaceDisplayOption?](./connectionoptions/marketplacedisplayoption.md)
- [var shouldHandleActiveWorkoutRecovery: Bool](./connectionoptions/shouldhandleactiveworkoutrecovery.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Connecting and disconnecting the scene
- [func scene(UIScene, willConnectTo: UISceneSession, options: UIScene.ConnectionOptions)](../uiscenedelegate/scene%28_,willconnectto,options%29.md)
  Tells the delegate about the addition of a scene to the app.
- [func sceneDidDisconnect(UIScene)](../uiscenedelegate/scenediddisconnect%28_%29.md)
  Tells the delegate that UIKit removed a scene from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions)*