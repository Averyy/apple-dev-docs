# windowCameraCaptureAccessory

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A session role for scenes that present content during camera capture.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static let windowCameraCaptureAccessory: UISceneSession.Role
```

```c
extern UISceneSessionRole const UIWindowSceneSessionRoleCameraCaptureAccessory;
```

#### Discussion

The system assigns this role automatically to scenes created from a camera capture scene accessory registration. Clients do not set it directly; it is provided so a scene’s purpose can be identified at runtime.

## See Also

### Determining scene roles
- [static let windowApplication: UISceneSession.Role](./windowapplication.md)
  A scene that displays interactive windows on the device’s built-in display or an externally connected display.
- [static let windowAssistiveAccessApplication: UISceneSession.Role](./windowassistiveaccessapplication.md)
- [static let windowExternalDisplayNonInteractive: UISceneSession.Role](./windowexternaldisplaynoninteractive.md)
  A scene that displays noninteractive windows on an externally connected display.
- [static let carTemplateApplication: UISceneSession.Role](./cartemplateapplication.md)
  A scene that displays interactive content on a CarPlay-enabled vehicle screen.
- [static let CPTemplateApplicationDashboardSceneSessionRoleApplication: UISceneSession.Role](./cptemplateapplicationdashboardscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Dashboard.
- [static let CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication: UISceneSession.Role](./cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Instruments Cluster.
- [static let windowExternalDisplay: UISceneSession.Role](./windowexternaldisplay.md)
  A scene that displays noninteractive windows on an externally connected display.
- [CPTemplateApplicationSceneSessionRoleApplication](../../../CarPlay/cptemplateapplicationscenesessionroleapplication.md)
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](../../../CarPlay/cptemplateapplicationdashboardscenesessionroleapplication.md)
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](../../../CarPlay/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowcameracaptureaccessory)*