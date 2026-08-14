# UISceneSession

**Framework**: UIKit  
**Kind**: class

An object that contains information about one of your app’s scenes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISceneSession
```

#### Overview

A [`UISceneSession`](uiscenesession.md) object manages a unique runtime instance of your scene. When the user adds a new scene to your app, or when you request one programmatically, the system creates a session object to track that scene. The session contains a unique identifier and the configuration details of the scene. UIKit maintains the session information for the lifetime of the scene itself, destroying the session in response to the user closing the scene in the app switcher.

You don’t create session objects directly. UIKit creates sessions in response to user interactions with your app. You can also ask UIKit to create a new scene and session programmatically by calling the [`requestSceneSessionActivation(_:userActivity:options:errorHandler:)`](uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:).md) method of [`UIApplication`](uiapplication.md). UIKit initializes the session with default configuration data based on the contents of your app’s `Info.plist` file.

## Topics

### Getting the scene information
- [var scene: UIScene?](uiscenesession/scene.md)
  The scene associated with the current session.
- [var role: UISceneSession.Role](uiscenesession/role-swift.property.md)
  The role played by the scene’s content.
- [UISceneSession.Role](uiscenesession/role-swift.struct.md)
  Constants that indicate the possible roles for a scene.
### Getting the scene configuration details
- [var configuration: UISceneConfiguration](uiscenesession/configuration.md)
  The configuration data for creating the scene.
- [class UISceneConfiguration](uisceneconfiguration.md)
  Information about the objects and storyboard for UKit to use when creating a particular scene.
### Identifying the scene
- [var persistentIdentifier: String](uiscenesession/persistentidentifier.md)
  A unique identifier that persists for the lifetime of the session.
### Getting additional session information
- [var stateRestorationActivity: NSUserActivity?](uiscenesession/staterestorationactivity.md)
  An activity object you can use to restore the previous contents of your scene’s interface.
- [var userInfo: [String : Any]?](uiscenesession/userinfo.md)
  Custom attributes that you can associate with the scene.
### Initializers
- [init?(coder: NSCoder)](uiscenesession/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)

## See Also

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md)
  Tell the system about your app’s scenes, including the objects you use to manage each scene and its initial user interface.
- [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md)
  The information about the app’s scene-based life-cycle support.
- [class UISceneConfiguration](uisceneconfiguration.md)
  Information about the objects and storyboard for UKit to use when creating a particular scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession)*