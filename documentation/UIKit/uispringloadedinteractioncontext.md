# UISpringLoadedInteractionContext

**Framework**: UIKit  
**Kind**: protocol

The interface an object implements to provide information about a spring-loaded interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UISpringLoadedInteractionContext : NSObjectProtocol
```

## Topics

### Managing state
- [var state: UISpringLoadedInteractionEffectState](uispringloadedinteractioncontext/state.md)
  The current view style for the spring-loaded interaction.
- [var targetItem: Any?](uispringloadedinteractioncontext/targetitem.md)
  The specific subview, or associated model object, of the target view to use for the spring-loaded interaction.
- [var targetView: UIView?](uispringloadedinteractioncontext/targetview.md)
  The view to which the current spring-loaded interaction view style is applied.
- [enum UISpringLoadedInteractionEffectState](uispringloadedinteractioneffectstate.md)
  The spring-loaded interaction states that determine the style of the interaction view.
### Getting the drag activity’s location
- [func location(in: UIView?) -> CGPoint](uispringloadedinteractioncontext/location(in:).md)
  Returns the location of the drag activity within the specified view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md)
  The interface for specifying the behavior of a spring-loaded interaction.
- [protocol UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
  The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [class UISpringLoadedInteraction](uispringloadedinteraction.md)
  An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [protocol UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md)
  The interface for providing visual styling to a spring-loaded interaction based on the interaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioncontext)*