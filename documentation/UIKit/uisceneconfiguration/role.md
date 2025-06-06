# role

**Framework**: UIKit  
**Kind**: property

The role assigned to the scene configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var role: UISceneSession.Role { get }
```

#### Discussion

UIKit populates this property with an appropriate role value based on the contents of your app’s `Info.plist` file. You also specify this value when you create a new scene-configuration object.

## See Also

- [var name: String?](uisceneconfiguration/name.md)
  The app-specific name assigned to the scene configuration.
- [UISceneSession.Role](uiscenesession/role-swift.struct.md)
  Constants that indicate the possible roles for a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/role)*