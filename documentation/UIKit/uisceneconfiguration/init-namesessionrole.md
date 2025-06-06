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
@MainActor
init(name: String?, sessionRole: UISceneSession.Role)
```

#### Return Value

A new scene-configuration object.

#### Discussion

After creating a scene-configuration object, supply values for the [`sceneClass`](uisceneconfiguration/sceneclass.md), [`delegateClass`](uisceneconfiguration/delegateclass.md), and [`storyboard`](uisceneconfiguration/storyboard.md) properties.

## Parameters

- `name`: The app-specific name you want to assign to the scene. For scenes you specify in your Info.plist file, this value corresponds to the string assigned to the   key.
- `sessionRole`: The role of the scene. For a list of possible roles, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/init(name:sessionrole:))*