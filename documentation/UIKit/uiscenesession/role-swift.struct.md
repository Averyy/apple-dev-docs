# UISceneSession.Role

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate the possible roles for a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Role
```

```c
typedef NSString * UISceneSessionRole;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)

## Topics

### Determining scene roles
- [static let windowApplication: UISceneSession.Role](./role-swift.struct/windowapplication.md)
  A scene that displays interactive windows on the device’s built-in display or an externally connected display.
- [static let windowAssistiveAccessApplication: UISceneSession.Role](./role-swift.struct/windowassistiveaccessapplication.md)
- [static let windowCameraCaptureAccessory: UISceneSession.Role](./role-swift.struct/windowcameracaptureaccessory.md)
  A session role for scenes that present content during camera capture.
- [static let windowExternalDisplayNonInteractive: UISceneSession.Role](./role-swift.struct/windowexternaldisplaynoninteractive.md)
  A scene that displays noninteractive windows on an externally connected display.
- [static let carTemplateApplication: UISceneSession.Role](./role-swift.struct/cartemplateapplication.md)
  A scene that displays interactive content on a CarPlay-enabled vehicle screen.
- [static let CPTemplateApplicationDashboardSceneSessionRoleApplication: UISceneSession.Role](./role-swift.struct/cptemplateapplicationdashboardscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Dashboard.
- [static let CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication: UISceneSession.Role](./role-swift.struct/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Instruments Cluster.
- [static let windowExternalDisplay: UISceneSession.Role](./role-swift.struct/windowexternaldisplay.md)
  A scene that displays noninteractive windows on an externally connected display.
- [CPTemplateApplicationSceneSessionRoleApplication](../../CarPlay/cptemplateapplicationscenesessionroleapplication.md)
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](../../CarPlay/cptemplateapplicationdashboardscenesessionroleapplication.md)
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](../../CarPlay/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
### Creating scene roles
- [init(rawValue: String)](./role-swift.struct/init%28rawvalue%29.md)
  Creates a scene role with the specified raw value.
### Type Properties
- [static let immersiveSpaceApplication: UISceneSession.Role](./role-swift.struct/immersivespaceapplication.md)
- [static let windowApplicationVolumetric: UISceneSession.Role](./role-swift.struct/windowapplicationvolumetric.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the configuration attributes
- [var name: String?](../uisceneconfiguration/name.md)
  The app-specific name assigned to the scene configuration.
- [var role: UISceneSession.Role](../uisceneconfiguration/role.md)
  The role assigned to the scene configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct)*