# UISceneAccessory

**Framework**: UIKit  
**Kind**: class

A type which can be used to register for a specific type of scene accessory presentation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
class UISceneAccessory
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Overview

A scene accessory declares supplementary content that the system presents on the app’s behalf when an associated piece of system functionality becomes available, for example when an external display is connected. The app declares what content to provide; the system decides when and where to present it. Scene accessories enhance the app’s experience when available, but the app must remain fully functional without them.

Use an instance of this type along with `UIViewController.registerSceneAccessory(_:)`.

## Topics

### Type Methods
- [class func externalNonInteractive(sceneConfiguration: UISceneConfiguration) -> Self](uisceneaccessory/externalnoninteractive(sceneconfiguration:).md)
  Creates a new scene accessory configuration for presenting non-interactive content on an external display.
- [class func externalNonInteractive(sceneConfiguration: UISceneConfiguration, userInfo: Any) -> Self](uisceneaccessory/externalnoninteractive(sceneconfiguration:userinfo:).md)
  Creates a new scene accessory configuration for presenting non-interactive content on an external display.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class UISceneAccessoryRegistration](uisceneaccessoryregistration.md)
  A type which represents the registration for a given scene accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessory)*