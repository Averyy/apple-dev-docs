# init(name:sessionRole:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithName:(NSString *) name sessionRole:(UISceneSessionRole) sessionRole;
```

#### Return Value

A new scene-configuration object.

#### Discussion

After creating a scene-configuration object, supply values for the [`sceneClass`](./sceneclass.md), [`delegateClass`](./delegateclass.md), and [`storyboard`](./storyboard.md) properties.

## Parameters

- `name`: The app-specific name you want to assign to the scene. For scenes you specify in your Info.plist file, this value corresponds to the string assigned to the [`UISceneConfigurationName`](../../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname.md) key.
- `sessionRole`: The role of the scene. For a list of possible roles, see [`UISceneSession.Role`](../uiscenesession/role-swift.struct.md).

## See Also

### Creating a configuration object
- [convenience init(name: String?)](./init%28name%29.md)
  Creates a scene-configuration object with the specified name.
- [convenience init()](./init%28%29.md)
  Creates a scene-configuration object.
- [+ configurationWithName:sessionRole:](./configurationwithname_sessionrole_.md)
  Returns a scene-configuration object with the specified role and app-specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/init(name:sessionrole:))*