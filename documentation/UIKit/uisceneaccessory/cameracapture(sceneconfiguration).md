# cameraCapture(sceneConfiguration:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a scene accessory for presenting content during camera capture.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
class func cameraCapture(sceneConfiguration: UISceneConfiguration) -> Self
```

```objc
+ (instancetype) cameraCaptureSceneAccessoryWithConfiguration:(UISceneConfiguration *) sceneConfiguration;
```

## Discussion

The content may be presented while the app is in the foreground and has an active camera capture session. The system determines whether and where to present it. The content can be interactive.

## Parameters

- `sceneConfiguration`: A scene configuration value with a delegate type defined for it.

## See Also

### Creating a camera capture accessory
- [class func cameraCapture(sceneConfiguration: UISceneConfiguration, userInfo: Any) -> Self](./cameracapture%28sceneconfiguration,userinfo%29.md)
  Creates a scene accessory for presenting content during camera capture, passing additional context to the scene delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessory/cameracapture(sceneconfiguration:))*