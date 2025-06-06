# UISpringLoadedInteractionBehavior

**Framework**: UIKit  
**Kind**: protocol

The interface for specifying the behavior of a spring-loaded interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UISpringLoadedInteractionBehavior : NSObjectProtocol
```

## Topics

### Managing spring-loaded interactions
- [func shouldAllow(UISpringLoadedInteraction, with: any UISpringLoadedInteractionContext) -> Bool](uispringloadedinteractionbehavior/shouldallow(_:with:).md)
  Returns a Boolean value that determines whether spring-loaded interaction should begin or should continue for the specified context.
### Handling spring-loaded interaction notifications
- [func interactionDidFinish(UISpringLoadedInteraction)](uispringloadedinteractionbehavior/interactiondidfinish(_:).md)
  Tells the behavior object when the spring-loading interaction is finished, either because it was canceled or because spring loading was activated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
  The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [class UISpringLoadedInteraction](uispringloadedinteraction.md)
  An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [protocol UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md)
  The interface an object implements to provide information about a spring-loaded interaction.
- [protocol UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md)
  The interface for providing visual styling to a spring-loaded interaction based on the interaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractionbehavior)*