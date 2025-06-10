# init(_:errorHandler:)

**Framework**: UIKit  
**Kind**: init

Creates an activation interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(_ configurationProvider: @escaping UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: @escaping (any Error) -> Void)
```

#### Return Value

A newly initialized activation interaction object.

## Parameters

- `configurationProvider`: The closure the system calls when the user triggers the interaction. The closure should return a   object.
- `errorHandler`: The closure the system calls when the activation request fails.

## See Also

- [UIWindowScene.ActivationInteraction.ConfigurationProvider](uiwindowscene/activationinteraction/configurationprovider.md)
  A type alias defining a closure that provides an activation configuration for the activation interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction/init(_:errorhandler:))*