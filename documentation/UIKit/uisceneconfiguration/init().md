# init()

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a scene-configuration object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init()
```

```objc
- (instancetype) init;
```

## Discussion

Scene sessions created from this configuration will have their role automatically set by the system.

## See Also

### Creating a configuration object
- [init(name: String?, sessionRole: UISceneSession.Role)](./init%28name,sessionrole%29.md)
  Creates a scene-configuration object with the specified role and app-specific name.
- [convenience init(name: String?)](./init%28name%29.md)
  Creates a scene-configuration object with the specified name.
- [+ configurationWithName:sessionRole:](./configurationwithname_sessionrole_.md)
  Returns a scene-configuration object with the specified role and app-specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/init())*