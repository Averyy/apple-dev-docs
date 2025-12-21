# windowScene(_:didUpdateEffectiveGeometry:)

**Framework**: UIKit  
**Kind**: method

Called when the window scene’s effective geometry has changed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
optional func windowScene(_ windowScene: UIWindowScene, didUpdateEffectiveGeometry previousEffectiveGeometry: UIWindowScene.Geometry)
```

#### Discussion

Always called when a `UIWindowScene` moves between screens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdateeffectivegeometry:))*