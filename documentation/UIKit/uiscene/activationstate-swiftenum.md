# UIScene.ActivationState

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the foreground or background execution state of your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum ActivationState
```

## Topics

### Scene States
- [UIScene.ActivationState.unattached](uiscene/activationstate-swift.enum/unattached.md)
  A state that indicates that the scene is not currently connected to your app.
- [UIScene.ActivationState.foregroundInactive](uiscene/activationstate-swift.enum/foregroundinactive.md)
  A state that indicates that the scene is running in the foreground but is not receiving events.
- [UIScene.ActivationState.foregroundActive](uiscene/activationstate-swift.enum/foregroundactive.md)
  A state that indicates that the scene is running in the foreground and is currently receiving events.
- [UIScene.ActivationState.background](uiscene/activationstate-swift.enum/background.md)
  A state that indicates that the scene is running in the background and is not onscreen.
### Initializers
- [init?(rawValue: Int)](uiscene/activationstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var activationState: UIScene.ActivationState](uiscene/activationstate-swift.property.md)
  The current execution state of the scene.
- [var title: String!](uiscene/title.md)
  A user-visible string you supply to help users differentiate among your app’s scenes.
- [var subtitle: String](uiscene/subtitle.md)
  A string that the app displays in the title bar of a window when running in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum)*