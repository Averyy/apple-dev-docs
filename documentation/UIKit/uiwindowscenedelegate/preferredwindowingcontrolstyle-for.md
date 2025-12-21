# preferredWindowingControlStyle(for:)

**Framework**: UIKit  
**Kind**: method

Called by the system to determine the windowing control style for the provided scene. `automaticStyle` will be used if this method is not implemented.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
optional func preferredWindowingControlStyle(for windowScene: UIWindowScene) -> UIWindowScene.WindowingControlStyle
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/preferredwindowingcontrolstyle(for:))*