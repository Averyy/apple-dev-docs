# init(activationHandler:)

**Framework**: UIKit  
**Kind**: init

Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(activationHandler handler: @escaping (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)
```

#### Return Value

A spring-loaded interaction that has a specific activation handler block and a default behavior and visual effect.

## Parameters

- `handler`: The handler that is invoked when the spring-loaded interaction is activated.

## See Also

- [init(interactionBehavior: (any UISpringLoadedInteractionBehavior)?, interactionEffect: (any UISpringLoadedInteractionEffect)?, activationHandler: (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)](uispringloadedinteraction/init(interactionbehavior:interactioneffect:activationhandler:).md)
  Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteraction/init(activationhandler:))*