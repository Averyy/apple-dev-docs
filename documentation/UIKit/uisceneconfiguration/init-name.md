# init(name:)

**Framework**: UIKit  
**Kind**: init

Creates a scene-configuration object with the specified name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(name: String?)
```

#### Discussion

Scene sessions created from this configuration will have their role automatically set by the system.

## See Also

- [init(name: String?, sessionRole: UISceneSession.Role)](uisceneconfiguration/init(name:sessionrole:).md)
  Creates a scene-configuration object with the specified role and app-specific name.
- [convenience init()](uisceneconfiguration/init.md)
  Creates a scene-configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/init(name:))*