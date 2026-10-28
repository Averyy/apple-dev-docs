# windowExternalDisplayNonInteractive

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A scene that displays noninteractive windows on an externally connected display.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static let windowExternalDisplayNonInteractive: UISceneSession.Role
```

```c
extern UISceneSessionRole const UIWindowSceneSessionRoleExternalDisplayNonInteractive;
```

## Mentions

- [Presenting content on a connected display](../../presenting-content-on-a-connected-display.md)
- [Building a desktop-class iPad app](../../building-a-desktop-class-ipad-app.md)
- [Transitioning to the UIKit scene-based life cycle](../../transitioning-to-the-uikit-scene-based-life-cycle.md)

## Discussion

> **Note**: Beginning in iOS 27, your app receives a scene with the [`windowExternalDisplayNonInteractive`](./windowexternaldisplaynoninteractive.md) role only after it registers a scene accessory. In earlier releases, the system connected this scene automatically, and your app opted out by declining to provide content for it. For more information, see [Presenting content on a connected display](../../presenting-content-on-a-connected-display.md).

## See Also

### Determining scene roles
- [static let windowApplication: UISceneSession.Role](./windowapplication.md)
  A scene that displays interactive windows on the device’s built-in display or an externally connected display.
- [static let windowAssistiveAccessApplication: UISceneSession.Role](./windowassistiveaccessapplication.md)
- [static let windowCameraCaptureAccessory: UISceneSession.Role](./windowcameracaptureaccessory.md)
  A session role for scenes that present content during camera capture.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive)*