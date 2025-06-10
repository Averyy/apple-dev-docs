# UIWindowScene.ActivationInteraction.ConfigurationProvider

**Framework**: UIKit  
**Kind**: typealias

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

#### Return Value

An activation configuration you can use to request a window scene.

## Parameters

- `interaction`: The   requesting a configuration.
- `location`: The location in the view of the interaction requesting a configuration.

## See Also

- [init(UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: (any Error) -> Void)](uiwindowscene/activationinteraction/init(_:errorhandler:).md)
  Creates an activation interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction/configurationprovider)*