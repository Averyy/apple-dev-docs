# actionWithIdentifier:alternateAction:configurationProvider:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates an activation action with the specified parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) actionWithIdentifier:(UIActionIdentifier) identifier alternateAction:(UIAction *) alternateAction configurationProvider:(UIWindowSceneActivationActionConfigurationProvider) configurationProvider;
```

## Return Value

A newly initialized activation action object.

## Parameters

- `identifier`: The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.
- `alternateAction`: An alternate action to perform if the platform doesn’t support multiple scenes or if requesting a scene fails.
- `configurationProvider`: The closure the system calls when the user selects the action. The closure should return a [`UIWindowScene.ActivationConfiguration`](../uiwindowscene/activationconfiguration.md) object.

## See Also

### Creating an activation action
- [UIWindowScene.ActivationAction.ConfigurationProvider](../uiwindowscene/activationaction/configurationprovider.md)
  A type alias defining a closure that provides an activation configuration for the activation action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowsceneactivationaction/actionwithidentifier:alternateaction:configurationprovider:)*