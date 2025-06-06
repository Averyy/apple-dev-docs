# UIScene.SystemProtectionManager

**Framework**: UIKit  
**Kind**: class

A class that represents the status of system protection for the scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
class SystemProtectionManager
```

#### Overview

Use this class to determine if the system protects a scene, such as by locking the app and requiring authentication with Face ID or Touch ID. You may want to disable your own app’s privacy shielding if the system already requires authentication.

The following example shows how a scene can use the manager’s [`isUserAuthenticationEnabled`](uiscene/systemprotectionmanager-swift.class/isuserauthenticationenabled.md) property to decide whether to provide its own UI shielding. When the scene becomes active, the app shows an authentication challenge if the system doesn’t already provide protection. When the scene resigns the active role, the app provides its own shielding only if the system isn’t already doing so.

## Topics

### Inspecting protection state
- [var isUserAuthenticationEnabled: Bool](uiscene/systemprotectionmanager-swift.class/isuserauthenticationenabled.md)
  The current status of system user authentication.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var systemProtectionManager: UIScene.SystemProtectionManager?](uiscene/systemprotectionmanager-swift.property.md)
  The system protection manager associated with this scene.
- [class let systemProtectionDidChangeNotification: NSNotification.Name](uiscene/systemprotectiondidchangenotification.md)
  A notification posted when the system-protection attributes of a scene change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/systemprotectionmanager-swift.class)*