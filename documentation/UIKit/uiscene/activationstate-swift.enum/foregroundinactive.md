# UIScene.ActivationState.foregroundInactive

**Framework**: UIKit  
**Kind**: case

A state that indicates that the scene is running in the foreground but is not receiving events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case foregroundInactive
```

#### Discussion

A scene transits through the foreground-inactive state on its way to or from another state.

## See Also

- [UIScene.ActivationState.unattached](uiscene/activationstate-swift.enum/unattached.md)
  A state that indicates that the scene is not currently connected to your app.
- [UIScene.ActivationState.foregroundActive](uiscene/activationstate-swift.enum/foregroundactive.md)
  A state that indicates that the scene is running in the foreground and is currently receiving events.
- [UIScene.ActivationState.background](uiscene/activationstate-swift.enum/background.md)
  A state that indicates that the scene is running in the background and is not onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum/foregroundinactive)*