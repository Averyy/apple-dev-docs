# windowScene(_:didUpdateEffectiveGeometry:)

**Framework**: UIKit  
**Kind**: method

Called when the window scene’s effective geometry has changed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
optional func windowScene(_ windowScene: UIWindowScene, didUpdateEffectiveGeometry previousEffectiveGeometry: UIWindowScene.Geometry)
```

#### Discussion

Always called when a `UIWindowScene` moves between screens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdateeffectivegeometry:))*