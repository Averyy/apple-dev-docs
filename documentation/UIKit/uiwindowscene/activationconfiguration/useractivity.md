# userActivity

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The user activity used to request a scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var userActivity: NSUserActivity { get }
```

```objc
@property (nonatomic, strong, readonly) NSUserActivity * userActivity;
```

## See Also

### Getting information about the activation configuration
- [var options: UIWindowScene.ActivationRequestOptions?](./options.md)
  Options for customizing the scene request.
- [UIWindowScene.ActivationRequestOptions](../activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [var preview: UITargetedPreview?](./preview.md)
  An optional targeted preview that the system uses to animate the transition to the new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration/useractivity)*