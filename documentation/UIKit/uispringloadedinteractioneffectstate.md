# UISpringLoadedInteractionEffectState

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### States
- [UISpringLoadedInteractionEffectState.activated](uispringloadedinteractioneffectstate/activated.md)
  An interaction state that indicates that the view was spring loaded.
- [UISpringLoadedInteractionEffectState.activating](uispringloadedinteractioneffectstate/activating.md)
  An interaction state that indicates that spring loading is about to start.
- [UISpringLoadedInteractionEffectState.inactive](uispringloadedinteractioneffectstate/inactive.md)
  An interaction state that indicates that spring loading is not engaged.
- [UISpringLoadedInteractionEffectState.possible](uispringloadedinteractioneffectstate/possible.md)
  An interaction state that indicates that spring loading is available.
### Initializers
- [init?(rawValue: Int)](uispringloadedinteractioneffectstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: UISpringLoadedInteractionEffectState](uispringloadedinteractioncontext/state.md)
  The current view style for the spring-loaded interaction.
- [var targetItem: Any?](uispringloadedinteractioncontext/targetitem.md)
  The specific subview, or associated model object, of the target view to use for the spring-loaded interaction.
- [var targetView: UIView?](uispringloadedinteractioncontext/targetview.md)
  The view to which the current spring-loaded interaction view style is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioneffectstate)*