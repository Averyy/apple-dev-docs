# init(_:errorHandler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an activation interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
init(_ configurationProvider: @escaping UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: @escaping (any Error) -> Void)
```

```objc
- (instancetype) initWithConfigurationProvider:(UIWindowSceneActivationInteractionConfigurationProvider) configurationProvider errorHandler:(void (^)(NSError *)) errorHandler;
```

## Return Value

A newly initialized activation interaction object.

## Parameters

- `configurationProvider`: The closure the system calls when the user triggers the interaction. The closure should return a [`UIWindowScene.ActivationConfiguration`](../activationconfiguration.md) object.
- `errorHandler`: The closure the system calls when the activation request fails.

## See Also

### Creating an activation interaction
- [UIWindowScene.ActivationInteraction.ConfigurationProvider](./configurationprovider.md)
  A type alias defining a closure that provides an activation configuration for the activation interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction/init(_:errorhandler:))*