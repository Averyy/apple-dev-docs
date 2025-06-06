# systemProtectionDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification posted when the system-protection attributes of a scene change.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
nonisolated
class let systemProtectionDidChangeNotification: NSNotification.Name
```

#### Discussion

The object of the notification is the scene for which protection attributes changed.

## See Also

- [var systemProtectionManager: UIScene.SystemProtectionManager?](uiscene/systemprotectionmanager-swift.property.md)
  The system protection manager associated with this scene.
- [UIScene.SystemProtectionManager](uiscene/systemprotectionmanager-swift.class.md)
  A class that represents the status of system protection for the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/systemprotectiondidchangenotification)*