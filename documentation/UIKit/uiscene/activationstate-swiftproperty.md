# activationState

**Framework**: UIKit  
**Kind**: property

The current execution state of the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var activationState: UIScene.ActivationState { get }
```

#### Discussion

When it is running, a scene is usually in the [`UIScene.ActivationState.foregroundActive`](uiscene/activationstate-swift.enum/foregroundactive.md) or [`UIScene.ActivationState.background`](uiscene/activationstate-swift.enum/background.md) state. A state may also enter other states for a short time as part of a transition.

## See Also

- [UIScene.ActivationState](uiscene/activationstate-swift.enum.md)
  Constants that indicate the foreground or background execution state of your app.
- [var title: String!](uiscene/title.md)
  A user-visible string you supply to help users differentiate among your app’s scenes.
- [var subtitle: String](uiscene/subtitle.md)
  A string that the app displays in the title bar of a window when running in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.property)*