# activationState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current execution state of the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var activationState: UIScene.ActivationState { get }
```

```objc
@property (nonatomic, readonly) UISceneActivationState activationState;
```

#### Discussion

When it is running, a scene is usually in the [`UIScene.ActivationState.foregroundActive`](./activationstate-swift.enum/foregroundactive.md) or [`UIScene.ActivationState.background`](./activationstate-swift.enum/background.md) state. A state may also enter other states for a short time as part of a transition.

## See Also

### Getting the scene attributes
- [UIScene.ActivationState](./activationstate-swift.enum.md)
  Constants that indicate the foreground or background execution state of your app.
- [var title: String!](./title.md)
  A user-visible string you supply to help users differentiate among your app’s scenes.
- [var subtitle: String](./subtitle.md)
  A string that the app displays in the title bar of a window when running in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.property)*