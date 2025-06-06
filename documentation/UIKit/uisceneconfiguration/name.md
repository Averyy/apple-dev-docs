# name

**Framework**: UIKit  
**Kind**: property

The app-specific name assigned to the scene configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var name: String? { get }
```

#### Discussion

UIKit sets this property’s initial value using the [`UISceneConfigurationName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UIWindowSceneSessionRoleApplication/UISceneConfigurationName) key from the appropriate scene in your app’s `Info.plist` file. You also specify this value when you create a new scene-configuration object.

## See Also

- [var role: UISceneSession.Role](uisceneconfiguration/role.md)
  The role assigned to the scene configuration.
- [UISceneSession.Role](uiscenesession/role-swift.struct.md)
  Constants that indicate the possible roles for a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/name)*