# UISpringLoadedInteractionEffectState.activated

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

An interaction state that indicates that the view was spring loaded.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case activated
```

```c
UISpringLoadedInteractionEffectStateActivated
```

## Discussion

The interaction view is styled with the default effect, and the activation handler for the [`UISpringLoadedInteraction`](../uispringloadedinteraction.md) object is called.

## See Also

### States
- [UISpringLoadedInteractionEffectState.activating](./activating.md)
  An interaction state that indicates that spring loading is about to start.
- [UISpringLoadedInteractionEffectState.inactive](./inactive.md)
  An interaction state that indicates that spring loading is not engaged.
- [UISpringLoadedInteractionEffectState.possible](./possible.md)
  An interaction state that indicates that spring loading is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioneffectstate/activated)*