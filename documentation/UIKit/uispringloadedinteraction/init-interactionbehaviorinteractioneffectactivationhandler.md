# init(interactionBehavior:interactionEffect:activationHandler:)

**Framework**: UIKit  
**Kind**: init

Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(interactionBehavior: (any UISpringLoadedInteractionBehavior)?, interactionEffect: (any UISpringLoadedInteractionEffect)?, activationHandler handler: @escaping (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)
```

#### Return Value

A spring-loaded interaction that has a specific behavior, visual effect, and activation handler block.

## Parameters

- `interactionBehavior`: The interaction behavior object controlling the spring-loaded interaction activation. If the value is  , the default behavior is used.
- `interactionEffect`: The interaction effect object styling the interaction’s view. If the value is  , the default effect is used.
- `handler`: The handler that is invoked when the spring-loaded interaction is activated.

## See Also

- [convenience init(activationHandler: (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)](uispringloadedinteraction/init(activationhandler:).md)
  Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteraction/init(interactionbehavior:interactioneffect:activationhandler:))*