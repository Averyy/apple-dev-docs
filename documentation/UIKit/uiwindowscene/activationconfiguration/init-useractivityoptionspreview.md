# init(userActivity:options:preview:)

**Framework**: UIKit  
**Kind**: init

Creates an activation configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
convenience init(userActivity: NSUserActivity, options: UIWindowScene.ActivationRequestOptions? = nil, preview: UITargetedPreview? = nil)
```

## Parameters

- `userActivity`: The user activity used to request a scene.
- `options`: Options for customizing the scene request. If you don’t provide options, the system uses the default options.
- `preview`: An optional targeted preview that the system uses to animate the transition to the new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration/init(useractivity:options:preview:))*