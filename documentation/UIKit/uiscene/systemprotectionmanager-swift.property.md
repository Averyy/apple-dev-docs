# systemProtectionManager

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The system protection manager associated with this scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var systemProtectionManager: UIScene.SystemProtectionManager? { get }
```

```objc
@property (nonatomic, readonly, nullable) UISceneSystemProtectionManager * systemProtectionManager;
```

#### Discussion

To check whether the scene requires user authentication, inspect the manager’s [`isUserAuthenticationEnabled`](./systemprotectionmanager-swift.class/isuserauthenticationenabled.md) property.

## See Also

### Working with system protection manager
- [UIScene.SystemProtectionManager](./systemprotectionmanager-swift.class.md)
  A class that represents the status of system protection for the scene.
- [class let systemProtectionDidChangeNotification: NSNotification.Name](./systemprotectiondidchangenotification.md)
  A notification posted when the system-protection attributes of a scene change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/systemprotectionmanager-swift.property)*