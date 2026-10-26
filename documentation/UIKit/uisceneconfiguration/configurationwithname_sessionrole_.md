# configurationWithName:sessionRole:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns a scene-configuration object with the specified role and app-specific name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) configurationWithName:(NSString *) name sessionRole:(UISceneSessionRole) sessionRole;
```

## See Also

### Creating a configuration object
- [init(name: String?, sessionRole: UISceneSession.Role)](./init%28name,sessionrole%29.md)
  Creates a scene-configuration object with the specified role and app-specific name.
- [convenience init(name: String?)](./init%28name%29.md)
  Creates a scene-configuration object with the specified name.
- [convenience init()](./init%28%29.md)
  Creates a scene-configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/configurationwithname:sessionrole:)*