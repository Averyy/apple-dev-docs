# UIWindowScene.ActivationAction.ConfigurationProvider

**Framework**: UIKit  
**Kind**: typealias

A type alias defining a closure that provides an activation configuration for the activation action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
typealias ConfigurationProvider = (UIWindowScene.ActivationAction) -> UIWindowScene.ActivationConfiguration?
```

#### Return Value

An activation configuration you can use to request a window scene.

## Parameters

- `action`: The   requesting a configuration.

## See Also

- [convenience init(title: String?, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, alternate: UIAction?, UIWindowScene.ActivationAction.ConfigurationProvider)](uiwindowscene/activationaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:alternate:_:).md)
  Creates an activation action using the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction/configurationprovider)*