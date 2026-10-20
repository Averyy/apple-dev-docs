# preferredWindowingControlStyle(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called by the system to determine the windowing control style for the provided scene. `automaticStyle` will be used if this method is not implemented.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional func preferredWindowingControlStyle(for windowScene: UIWindowScene) -> UIWindowScene.WindowingControlStyle
```

```objc
- (UISceneWindowingControlStyle *) preferredWindowingControlStyleForScene:(UIWindowScene *) windowScene;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/preferredwindowingcontrolstyle(for:))*