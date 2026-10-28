# UIWindowScene.ActivationInteraction.ConfigurationProvider

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A type alias defining a closure that provides an activation configuration for the activation interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
typealias ConfigurationProvider = (UIWindowScene.ActivationInteraction, CGPoint) -> UIWindowScene.ActivationConfiguration?
```

```c
typedef UIWindowSceneActivationConfiguration *(^)(UIWindowSceneActivationInteraction *, struct CGPoint) UIWindowSceneActivationInteractionConfigurationProvider;
```

## Return Value

An activation configuration you can use to request a window scene.

## Parameters

- `interaction`: The [`UIWindowScene.ActivationInteraction`](../activationinteraction.md) requesting a configuration.
- `location`: The location in the view of the interaction requesting a configuration.

## See Also

### Creating an activation interaction
- [init(UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: (any Error) -> Void)](./init%28_,errorhandler%29.md)
  Creates an activation interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction/configurationprovider)*