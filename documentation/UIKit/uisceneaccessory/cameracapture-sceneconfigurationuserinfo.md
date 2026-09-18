# cameraCapture(sceneConfiguration:userInfo:)

**Framework**: UIKit  
**Kind**: method

Creates a scene accessory for presenting content during camera capture, passing additional context to the scene delegate.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
class func cameraCapture(sceneConfiguration: UISceneConfiguration, userInfo: Any) -> Self
```

#### Discussion

The content may be presented while the app is in the foreground and has an active camera capture session. The system determines whether and where to present it. The content can be interactive.

This variant accepts a `userInfo` object to pass additional context to the scene delegate upon connection. The `userInfo` object is accessible in the corresponding scene via `UISceneConnectionOptions.sceneAccessoryUserInfo`.

## Parameters

- `sceneConfiguration`: A scene configuration value with a delegate type defined for it.
- `userInfo`: An object that can be used to pass additional context to the scene delegate upon connection.

## See Also

- [class func cameraCapture(sceneConfiguration: UISceneConfiguration) -> Self](uisceneaccessory/cameracapture(sceneconfiguration:).md)
  Creates a scene accessory for presenting content during camera capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessory/cameracapture(sceneconfiguration:userinfo:))*