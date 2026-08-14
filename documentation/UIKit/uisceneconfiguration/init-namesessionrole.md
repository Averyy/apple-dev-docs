# init(name:sessionRole:)

**Framework**: UIKit  
**Kind**: init

Creates a scene-configuration object with the specified role and app-specific name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(name: String?, sessionRole: UISceneSession.Role)
```

#### Return Value

A new scene-configuration object.

#### Discussion

After creating a scene-configuration object, supply values for the [`sceneClass`](uisceneconfiguration/sceneclass.md), [`delegateClass`](uisceneconfiguration/delegateclass.md), and [`storyboard`](uisceneconfiguration/storyboard.md) properties.

## Parameters

- `name`: The app-specific name you want to assign to the scene. For scenes you specify in your Info.plist file, this value corresponds to the string assigned to the [`UISceneConfigurationName`](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname) key.
- `sessionRole`: The role of the scene. For a list of possible roles, see [`UISceneSession.Role`](uiscenesession/role-swift.struct.md).

## See Also

- [convenience init(name: String?)](uisceneconfiguration/init(name:).md)
  Creates a scene-configuration object with the specified name.
- [convenience init()](uisceneconfiguration/init.md)
  Creates a scene-configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/init(name:sessionrole:))*