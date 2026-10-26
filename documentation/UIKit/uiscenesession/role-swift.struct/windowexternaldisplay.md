# windowExternalDisplay

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A scene that displays noninteractive windows on an externally connected display.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0 (renamed: UISceneSession.Role.windowExternalDisplayNonInteractive)
- iPadOS 13.0+ - Deprecated in 16.0 (renamed: UISceneSession.Role.windowExternalDisplayNonInteractive)
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: UISceneSession.Role.windowExternalDisplayNonInteractive)
- tvOS 13.0+ - Deprecated in 16.0 (renamed: UISceneSession.Role.windowExternalDisplayNonInteractive)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: UISceneSession.Role.windowExternalDisplayNonInteractive)

> **Deprecated**: Use [`windowExternalDisplayNonInteractive`](./windowexternaldisplaynoninteractive.md) for a scene that displays noninteractive windows on an externally connected screen. A scene that displays interactive windows uses [`windowApplication`](./windowapplication.md), even if the windows display on an externally connected screen.

## Declaration

```swift
static let windowExternalDisplay: UISceneSession.Role
```

```c
extern UISceneSessionRole const UIWindowSceneSessionRoleExternalDisplay;
```

## See Also

### Determining scene roles
- [static let windowApplication: UISceneSession.Role](./windowapplication.md)
  A scene that displays interactive windows on the device’s built-in display or an externally connected display.
- [static let windowAssistiveAccessApplication: UISceneSession.Role](./windowassistiveaccessapplication.md)
- [static let windowCameraCaptureAccessory: UISceneSession.Role](./windowcameracaptureaccessory.md)
  A session role for scenes that present content during camera capture.
- [static let windowExternalDisplayNonInteractive: UISceneSession.Role](./windowexternaldisplaynoninteractive.md)
  A scene that displays noninteractive windows on an externally connected display.
- [static let carTemplateApplication: UISceneSession.Role](./cartemplateapplication.md)
  A scene that displays interactive content on a CarPlay-enabled vehicle screen.
- [static let CPTemplateApplicationDashboardSceneSessionRoleApplication: UISceneSession.Role](./cptemplateapplicationdashboardscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Dashboard.
- [static let CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication: UISceneSession.Role](./cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Instruments Cluster.
- [CPTemplateApplicationSceneSessionRoleApplication](../../../CarPlay/cptemplateapplicationscenesessionroleapplication.md)
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](../../../CarPlay/cptemplateapplicationdashboardscenesessionroleapplication.md)
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](../../../CarPlay/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowexternaldisplay)*