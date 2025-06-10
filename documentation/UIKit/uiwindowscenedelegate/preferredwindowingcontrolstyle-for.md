# preferredWindowingControlStyle(for:)

**Framework**: UIKit  
**Kind**: method

Called by the system to determine the windowing control style for the provided scene. `automaticStyle` will be used if this method is not implemented.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
optional func preferredWindowingControlStyle(for windowScene: UIWindowScene) -> UIWindowScene.WindowingControlStyle
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/preferredwindowingcontrolstyle(for:))*