# UISceneSession.Role

**Framework**: UIKit  
**Kind**: struct

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

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

## Topics

### Determining scene roles
- [static let windowApplication: UISceneSession.Role](uiscenesession/role-swift.struct/windowapplication.md)
  A scene that displays interactive windows on the device’s built-in display or an externally connected display.
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
### Creating scene roles
- [init(rawValue: String)](uiscenesession/role-swift.struct/init(rawvalue:).md)
  Creates a scene role with the specified raw value.
### Type Properties
- [static let immersiveSpaceApplication: UISceneSession.Role](uiscenesession/role-swift.struct/immersivespaceapplication.md)
- [static let windowApplicationVolumetric: UISceneSession.Role](uiscenesession/role-swift.struct/windowapplicationvolumetric.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var name: String?](uisceneconfiguration/name.md)
  The app-specific name assigned to the scene configuration.
- [var role: UISceneSession.Role](uisceneconfiguration/role.md)
  The role assigned to the scene configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct)*