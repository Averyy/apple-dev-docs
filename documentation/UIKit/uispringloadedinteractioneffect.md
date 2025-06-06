# UISpringLoadedInteractionEffect

**Framework**: UIKit  
**Kind**: protocol

The interface for providing visual styling to a spring-loaded interaction based on the interaction state.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UISpringLoadedInteractionEffect : NSObjectProtocol
```

## Topics

### Handling changes
- [func interaction(UISpringLoadedInteraction, didChangeWith: any UISpringLoadedInteractionContext)](uispringloadedinteractioneffect/interaction(_:didchangewith:).md)
  Called when the spring-loaded interaction state has changed.

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
- [protocol UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md)
  The interface an object implements to provide information about a spring-loaded interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioneffect)*