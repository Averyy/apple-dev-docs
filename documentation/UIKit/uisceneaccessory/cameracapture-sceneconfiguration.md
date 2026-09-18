# cameraCapture(sceneConfiguration:)

**Framework**: UIKit  
**Kind**: method

Creates a scene accessory for presenting content during camera capture.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
class func cameraCapture(sceneConfiguration: UISceneConfiguration) -> Self
```

#### Discussion

The content may be presented while the app is in the foreground and has an active camera capture session. The system determines whether and where to present it. The content can be interactive.

## Parameters

- `sceneConfiguration`: A scene configuration value with a delegate type defined for it.

## See Also

- [class func cameraCapture(sceneConfiguration: UISceneConfiguration, userInfo: Any) -> Self](uisceneaccessory/cameracapture(sceneconfiguration:userinfo:).md)
  Creates a scene accessory for presenting content during camera capture, passing additional context to the scene delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessory/cameracapture(sceneconfiguration:))*