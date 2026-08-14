# UISceneConfiguration

**Framework**: UIKit  
**Kind**: class

Information about the objects and storyboard for UKit to use when creating a particular scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISceneConfiguration
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)
- [Transitioning to the UIKit scene-based life cycle](transitioning-to-the-uikit-scene-based-life-cycle.md)

#### Overview

Use a [`UISceneConfiguration`](uisceneconfiguration.md) object to specify information that UIKit can use to create a new scene for your app. Specifically, you must provide the class of the specific scene you want, the class of the scene delegate object your app uses to manage scenes of that type, and a storyboard containing the scene’s initial view controller.

When the user requests a new instance of your app’s user interface, UIKit looks in your app’s `Info.plist` file for the configuration data it needs to create the corresponding scene object. It then packages that information into a [`UISceneConfiguration`](uisceneconfiguration.md) object and delivers it as part of the session it passes to the [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) method of your app delegate. You can accept that configuration data as is or create a return a new [`UISceneConfiguration`](uisceneconfiguration.md) object with a different set of configuration details.

## Topics

### Creating a configuration object
- [init(name: String?, sessionRole: UISceneSession.Role)](uisceneconfiguration/init(name:sessionrole:).md)
  Creates a scene-configuration object with the specified role and app-specific name.
- [convenience init(name: String?)](uisceneconfiguration/init(name:).md)
  Creates a scene-configuration object with the specified name.
- [convenience init()](uisceneconfiguration/init.md)
  Creates a scene-configuration object.
### Specifying the scene creation details
- [var sceneClass: AnyClass?](uisceneconfiguration/sceneclass.md)
  The class of the scene object that you want UIKit to create.
- [var delegateClass: AnyClass?](uisceneconfiguration/delegateclass.md)
  The class of the custom delegate object that you want UIKit to create.
- [var storyboard: UIStoryboard?](uisceneconfiguration/storyboard.md)
  The storyboard object that contains your scene’s initial view controller.
### Getting the configuration attributes
- [var name: String?](uisceneconfiguration/name.md)
  The app-specific name assigned to the scene configuration.
- [var role: UISceneSession.Role](uisceneconfiguration/role.md)
  The role assigned to the scene configuration.
- [UISceneSession.Role](uiscenesession/role-swift.struct.md)
  Constants that indicate the possible roles for a scene.
### Initializers
- [init?(coder: NSCoder)](uisceneconfiguration/init(coder:).md)

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
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)

## See Also

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md)
  Tell the system about your app’s scenes, including the objects you use to manage each scene and its initial user interface.
- [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md)
  The information about the app’s scene-based life-cycle support.
- [class UISceneSession](uiscenesession.md)
  An object that contains information about one of your app’s scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration)*