# UIScene.SystemProtectionManager

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UISceneSystemProtectionManager : NSObject
```

## Overview

Use this class to determine if the system protects a scene, such as by locking the app and requiring authentication with Face ID or Touch ID. You may want to disable your own app’s privacy shielding if the system already requires authentication.

The following example shows how a scene can use the manager’s [`isUserAuthenticationEnabled`](./systemprotectionmanager-swift.class/isuserauthenticationenabled.md) property to decide whether to provide its own UI shielding. When the scene becomes active, the app shows an authentication challenge if the system doesn’t already provide protection. When the scene resigns the active role, the app provides its own shielding only if the system isn’t already doing so.

**Swift**:

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    guard scene.systemProtectionManager?.isUserAuthenticationEnabled ?? false else {
        // Show custom authentication.
    }
}

func sceneWillResignActive(_ scene: UIScene) {
    guard scene.systemProtectionManager?.isUserAuthenticationEnabled ?? false else {
        // Show custom shield to hide sensitive information.
    }
}

```

**Objective-C**:

```objc
- (void)sceneDidBecomeActive:(UIScene *)scene {
    if ( scene.systemProtectionManager.userAuthenticationEnabled ) {
        // Don't show custom authentication.
    } else {
        // Show custom shield to hide sensitive information.
    }
}

- (void)sceneWillResignActive:(UIScene *)scene {
    if ( scene.systemProtectionManager.userAuthenticationEnabled ) {
        // Don't show custom shield; system already does so.
    } else {
        // Show custom shield to hide sensitive information.
    }
}
```

## Topics

### Inspecting protection state
- [var isUserAuthenticationEnabled: Bool](./systemprotectionmanager-swift.class/isuserauthenticationenabled.md)
  The current status of system user authentication.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Working with system protection manager
- [var systemProtectionManager: UIScene.SystemProtectionManager?](./systemprotectionmanager-swift.property.md)
  The system protection manager associated with this scene.
- [class let systemProtectionDidChangeNotification: NSNotification.Name](./systemprotectiondidchangenotification.md)
  A notification posted when the system-protection attributes of a scene change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/systemprotectionmanager-swift.class)*