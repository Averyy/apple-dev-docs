# UISpringLoadedInteraction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UISpringLoadedInteraction : NSObject
```

## Topics

### Initializing a spring-loaded interaction
- [init(interactionBehavior: (any UISpringLoadedInteractionBehavior)?, interactionEffect: (any UISpringLoadedInteractionEffect)?, activationHandler: (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)](./uispringloadedinteraction/init%28interactionbehavior,interactioneffect,activationhandler%29.md)
  Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.
- [convenience init(activationHandler: (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)](./uispringloadedinteraction/init%28activationhandler%29.md)
  Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.
### Getting information about the spring-loaded interaction
- [var interactionBehavior: any UISpringLoadedInteractionBehavior](./uispringloadedinteraction/interactionbehavior.md)
  The behavior for the spring-loaded interaction.
- [var interactionEffect: any UISpringLoadedInteractionEffect](./uispringloadedinteraction/interactioneffect.md)
  The visual effect for the spring-loaded interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIInteraction](./uiinteraction.md)

## See Also

### Spring-loaded interactions
- [protocol UISpringLoadedInteractionBehavior](./uispringloadedinteractionbehavior.md)
  The interface for specifying the behavior of a spring-loaded interaction.
- [protocol UISpringLoadedInteractionSupporting](./uispringloadedinteractionsupporting.md)
  The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [protocol UISpringLoadedInteractionContext](./uispringloadedinteractioncontext.md)
  The interface an object implements to provide information about a spring-loaded interaction.
- [protocol UISpringLoadedInteractionEffect](./uispringloadedinteractioneffect.md)
  The interface for providing visual styling to a spring-loaded interaction based on the interaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteraction)*