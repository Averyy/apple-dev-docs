# windowCameraCaptureAccessory

**Framework**: UIKit  
**Kind**: property

A session role for scenes that present content during camera capture.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
static let windowCameraCaptureAccessory: UISceneSession.Role
```

#### Discussion

The system assigns this role automatically to scenes created from a camera capture scene accessory registration. Clients do not set it directly; it is provided so a scene’s purpose can be identified at runtime.

## See Also

- [static let windowApplication: UISceneSession.Role](uiscenesession/role-swift.struct/windowapplication.md)
  A scene that displays interactive windows on the device’s built-in display or an externally connected display.
- [static let windowAssistiveAccessApplication: UISceneSession.Role](uiscenesession/role-swift.struct/windowassistiveaccessapplication.md)
- [static let windowExternalDisplay: UISceneSession.Role](uiscenesession/role-swift.struct/windowexternaldisplay.md)
  A scene that displays noninteractive windows on an externally connected display.
- [static let windowExternalDisplayNonInteractive: UISceneSession.Role](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md)
  A scene that displays noninteractive windows on an externally connected display.
- [static let carTemplateApplication: UISceneSession.Role](uiscenesession/role-swift.struct/cartemplateapplication.md)
  A scene that displays interactive content on a CarPlay-enabled vehicle screen.
- [static let CPTemplateApplicationDashboardSceneSessionRoleApplication: UISceneSession.Role](uiscenesession/role-swift.struct/cptemplateapplicationdashboardscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Dashboard.
- [static let CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication: UISceneSession.Role](uiscenesession/role-swift.struct/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  A scene that displays navigation content on the CarPlay Instruments Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowcameracaptureaccessory)*