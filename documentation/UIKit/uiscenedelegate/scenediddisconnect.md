# sceneDidDisconnect(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that UIKit removed a scene from your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func sceneDidDisconnect(_ scene: UIScene)
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Discussion

Use this method to perform any final cleanup before your scene is purged from memory. For example, use it to release references to files or shared resources and to save user data.

The removal of a scene is a precursor to the destruction of that scene. UIKit disconnects a scene when the user explicitly closes it in the app switcher. UIKit may also disconnect a scene in order to reclaim memory for other processes. UIKit does not automatically disconnect a scene when the user switches to another app.

UIKit also posts a [`didDisconnectNotification`](uiscene/diddisconnectnotification.md) notification in addition to calling this method.

## Parameters

- `scene`: The scene that UIKit disconnected from your app.

## See Also

- [func scene(UIScene, willConnectTo: UISceneSession, options: UIScene.ConnectionOptions)](uiscenedelegate/scene(_:willconnectto:options:).md)
  Tells the delegate about the addition of a scene to the app.
- [UIScene.ConnectionOptions](uiscene/connectionoptions.md)
  A data object containing information about the reasons why UIKit created the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenediddisconnect(_:))*