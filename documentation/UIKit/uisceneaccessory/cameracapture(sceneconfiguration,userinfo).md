# cameraCapture(sceneConfiguration:userInfo:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a scene accessory for presenting content during camera capture, passing additional context to the scene delegate.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
class func cameraCapture(sceneConfiguration: UISceneConfiguration, userInfo: Any) -> Self
```

```objc
+ (instancetype) cameraCaptureSceneAccessoryWithConfiguration:(UISceneConfiguration *) sceneConfiguration userInfo:(id) userInfo;
```

#### Discussion

The content may be presented while the app is in the foreground and has an active camera capture session. The system determines whether and where to present it. The content can be interactive.

This variant accepts a `userInfo` object to pass additional context to the scene delegate upon connection. The `userInfo` object is accessible in the corresponding scene via `UISceneConnectionOptions.sceneAccessoryUserInfo`.

## Parameters

- `sceneConfiguration`: A scene configuration value with a delegate type defined for it.
- `userInfo`: An object that can be used to pass additional context to the scene delegate upon connection.

## See Also

### Creating a camera capture accessory
- [class func cameraCapture(sceneConfiguration: UISceneConfiguration) -> Self](./cameracapture%28sceneconfiguration%29.md)
  Creates a scene accessory for presenting content during camera capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessory/cameracapture(sceneconfiguration:userinfo:))*