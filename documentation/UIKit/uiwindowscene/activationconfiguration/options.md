# options

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Options for customizing the scene request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var options: UIWindowScene.ActivationRequestOptions? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIWindowSceneActivationRequestOptions * options;
```

## Discussion

This property is optional. If you don’t specify options, the system requests a scene using the default options.

## See Also

### Getting information about the activation configuration
- [var userActivity: NSUserActivity](./useractivity.md)
  The user activity used to request a scene.
- [UIWindowScene.ActivationRequestOptions](../activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [var preview: UITargetedPreview?](./preview.md)
  An optional targeted preview that the system uses to animate the transition to the new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration/options)*