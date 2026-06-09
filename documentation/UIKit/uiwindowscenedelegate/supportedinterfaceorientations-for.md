# supportedInterfaceOrientations(for:)

**Framework**: UIKit  
**Kind**: method

Returns the interface orientations supported by the window scene. The returned value replaces the app’s UISupportedInterfaceOrientations Info.plist value for this scene. If not implemented, the Info.plist value is used.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
optional func supportedInterfaceOrientations(for windowScene: UIWindowScene) -> UIInterfaceOrientationMask
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/supportedinterfaceorientations(for:))*