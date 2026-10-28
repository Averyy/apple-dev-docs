# name

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The app-specific name assigned to the scene configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var name: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * name;
```

## Discussion

UIKit sets this property’s initial value using the [`UISceneConfigurationName`](../../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname.md) key from the appropriate scene in your app’s `Info.plist` file. You also specify this value when you create a new scene-configuration object.

## See Also

### Getting the configuration attributes
- [var role: UISceneSession.Role](./role.md)
  The role assigned to the scene configuration.
- [UISceneSession.Role](../uiscenesession/role-swift.struct.md)
  Constants that indicate the possible roles for a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/name)*