# init(name:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a scene-configuration object with the specified name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init(name: String?)
```

```objc
- (instancetype) initWithName:(NSString *) name;
```

## Discussion

Scene sessions created from this configuration will have their role automatically set by the system.

## See Also

### Creating a configuration object
- [init(name: String?, sessionRole: UISceneSession.Role)](./init%28name,sessionrole%29.md)
  Creates a scene-configuration object with the specified role and app-specific name.
- [convenience init()](./init%28%29.md)
  Creates a scene-configuration object.
- [+ configurationWithName:sessionRole:](./configurationwithname_sessionrole_.md)
  Returns a scene-configuration object with the specified role and app-specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/init(name:))*