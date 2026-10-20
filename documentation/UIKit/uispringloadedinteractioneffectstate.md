# UISpringLoadedInteractionEffectState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The spring-loaded interaction states that determine the style of the interaction view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum UISpringLoadedInteractionEffectState
```

```c
enum UISpringLoadedInteractionEffectState : NSInteger;
```

## Topics

### States
- [UISpringLoadedInteractionEffectState.activated](./uispringloadedinteractioneffectstate/activated.md)
  An interaction state that indicates that the view was spring loaded.
- [UISpringLoadedInteractionEffectState.activating](./uispringloadedinteractioneffectstate/activating.md)
  An interaction state that indicates that spring loading is about to start.
- [UISpringLoadedInteractionEffectState.inactive](./uispringloadedinteractioneffectstate/inactive.md)
  An interaction state that indicates that spring loading is not engaged.
- [UISpringLoadedInteractionEffectState.possible](./uispringloadedinteractioneffectstate/possible.md)
  An interaction state that indicates that spring loading is available.
### Initializers
- [init?(rawValue: Int)](./uispringloadedinteractioneffectstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing state
- [var state: UISpringLoadedInteractionEffectState](./uispringloadedinteractioncontext/state.md)
  The current view style for the spring-loaded interaction.
- [var targetItem: Any?](./uispringloadedinteractioncontext/targetitem.md)
  The specific subview, or associated model object, of the target view to use for the spring-loaded interaction.
- [var targetView: UIView?](./uispringloadedinteractioncontext/targetview.md)
  The view to which the current spring-loaded interaction view style is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioneffectstate)*