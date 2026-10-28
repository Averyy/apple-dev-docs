# init(activationHandler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(activationHandler handler: @escaping (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)
```

```objc
- (instancetype) initWithActivationHandler:(void (^)(UISpringLoadedInteraction *interaction, id<UISpringLoadedInteractionContext>context)) handler;
```

## Return Value

A spring-loaded interaction that has a specific activation handler block and a default behavior and visual effect.

## Parameters

- `handler`: The handler that is invoked when the spring-loaded interaction is activated.

## See Also

### Initializing a spring-loaded interaction
- [init(interactionBehavior: (any UISpringLoadedInteractionBehavior)?, interactionEffect: (any UISpringLoadedInteractionEffect)?, activationHandler: (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)](./init%28interactionbehavior,interactioneffect,activationhandler%29.md)
  Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteraction/init(activationhandler:))*