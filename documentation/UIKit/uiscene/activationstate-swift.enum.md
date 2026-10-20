# UIScene.ActivationState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UISceneActivationState : NSInteger;
```

## Topics

### Scene States
- [UIScene.ActivationState.unattached](./activationstate-swift.enum/unattached.md)
  A state that indicates that the scene is not currently connected to your app.
- [UIScene.ActivationState.foregroundInactive](./activationstate-swift.enum/foregroundinactive.md)
  A state that indicates that the scene is running in the foreground but is not receiving events.
- [UIScene.ActivationState.foregroundActive](./activationstate-swift.enum/foregroundactive.md)
  A state that indicates that the scene is running in the foreground and is currently receiving events.
- [UIScene.ActivationState.background](./activationstate-swift.enum/background.md)
  A state that indicates that the scene is running in the background and is not onscreen.
### Initializers
- [init?(rawValue: Int)](./activationstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the scene attributes
- [var activationState: UIScene.ActivationState](./activationstate-swift.property.md)
  The current execution state of the scene.
- [var title: String!](./title.md)
  A user-visible string you supply to help users differentiate among your app’s scenes.
- [var subtitle: String](./subtitle.md)
  A string that the app displays in the title bar of a window when running in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum)*