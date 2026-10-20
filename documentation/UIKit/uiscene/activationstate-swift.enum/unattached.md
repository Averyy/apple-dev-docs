# UIScene.ActivationState.unattached

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A state that indicates that the scene is not currently connected to your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case unattached
```

```c
UISceneActivationStateUnattached
```

#### Discussion

A scene starts in the unattached state and remains in that state until the system sends a connection notification to it. A scene reenters the attached state when the user dismisses the interface from the app switcher or to reclaim its resources.

## See Also

### Scene States
- [UIScene.ActivationState.foregroundInactive](./foregroundinactive.md)
  A state that indicates that the scene is running in the foreground but is not receiving events.
- [UIScene.ActivationState.foregroundActive](./foregroundactive.md)
  A state that indicates that the scene is running in the foreground and is currently receiving events.
- [UIScene.ActivationState.background](./background.md)
  A state that indicates that the scene is running in the background and is not onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum/unattached)*