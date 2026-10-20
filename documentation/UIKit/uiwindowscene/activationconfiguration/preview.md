# preview

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An optional targeted preview that the system uses to animate the transition to the new scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var preview: UITargetedPreview? { get set }
```

```objc
@property (nonatomic, strong, nullable) UITargetedPreview * preview;
```

## See Also

### Getting information about the activation configuration
- [var userActivity: NSUserActivity](./useractivity.md)
  The user activity used to request a scene.
- [var options: UIWindowScene.ActivationRequestOptions?](./options.md)
  Options for customizing the scene request.
- [UIWindowScene.ActivationRequestOptions](../activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration/preview)*