# UISpringLoadedInteraction

**Framework**: UIKit  
**Kind**: class

An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISpringLoadedInteraction
```

## Topics

### Initializing a spring-loaded interaction
- [init(interactionBehavior: (any UISpringLoadedInteractionBehavior)?, interactionEffect: (any UISpringLoadedInteractionEffect)?, activationHandler: (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)](uispringloadedinteraction/init(interactionbehavior:interactioneffect:activationhandler:).md)
  Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.
- [convenience init(activationHandler: (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)](uispringloadedinteraction/init(activationhandler:).md)
  Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.
### Getting information about the spring-loaded interaction
- [var interactionBehavior: any UISpringLoadedInteractionBehavior](uispringloadedinteraction/interactionbehavior.md)
  The behavior for the spring-loaded interaction.
- [var interactionEffect: any UISpringLoadedInteractionEffect](uispringloadedinteraction/interactioneffect.md)
  The visual effect for the spring-loaded interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [protocol UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md)
  The interface for specifying the behavior of a spring-loaded interaction.
- [protocol UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
  The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [protocol UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md)
  The interface an object implements to provide information about a spring-loaded interaction.
- [protocol UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md)
  The interface for providing visual styling to a spring-loaded interaction based on the interaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteraction)*