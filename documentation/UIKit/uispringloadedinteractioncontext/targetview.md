# targetView

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The view to which the current spring-loaded interaction view style is applied.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var targetView: UIView? { get set }
```

## See Also

- [var state: UISpringLoadedInteractionEffectState](uispringloadedinteractioncontext/state.md)
  The current view style for the spring-loaded interaction.
- [var targetItem: Any?](uispringloadedinteractioncontext/targetitem.md)
  The specific subview, or associated model object, of the target view to use for the spring-loaded interaction.
- [enum UISpringLoadedInteractionEffectState](uispringloadedinteractioneffectstate.md)
  The spring-loaded interaction states that determine the style of the interaction view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioncontext/targetview)*