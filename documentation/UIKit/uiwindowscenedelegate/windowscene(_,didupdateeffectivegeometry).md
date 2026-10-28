# windowScene(_:didUpdateEffectiveGeometry:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when the window scene’s effective geometry has changed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional func windowScene(_ windowScene: UIWindowScene, didUpdateEffectiveGeometry previousEffectiveGeometry: UIWindowScene.Geometry)
```

```objc
- (void) windowScene:(UIWindowScene *) windowScene didUpdateEffectiveGeometry:(UIWindowSceneGeometry *) previousEffectiveGeometry;
```

## Discussion

Always called when a `UIWindowScene` moves between screens.

## See Also

### Responding to scene changes
- [func windowScene(UIWindowScene, didUpdate: any UICoordinateSpace, interfaceOrientation: UIInterfaceOrientation, traitCollection: UITraitCollection)](./windowscene%28_,didupdate,interfaceorientation,traitcollection%29.md)
  Notifies you when the size, orientation, or traits of a scene change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdateeffectivegeometry:))*