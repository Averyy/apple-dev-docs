# externalNonInteractive(sceneConfiguration:userInfo:)

**Framework**: UIKit  
**Kind**: method

Creates a new scene accessory configuration for presenting non-interactive content on an external display.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
class func externalNonInteractive(sceneConfiguration: UISceneConfiguration, userInfo: Any) -> Self
```

#### Discussion

When the display connects, the scene accessory’s content may be presented on it.

This variant accepts a `userInfo` object to pass additional context to the scene delegate upon connection. The `userInfo` object is accessible in the corresponding scene via `UISceneConnectionOptions.sceneAccessoryUserInfo`.

## Parameters

- `sceneConfiguration`: A scene configuration value with delegate type defined for it.
- `userInfo`: An object that can be used to pass additional context to the scene delegate upon connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessory/externalnoninteractive(sceneconfiguration:userinfo:))*