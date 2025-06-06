# role

**Framework**: UIKit  
**Kind**: property

The role played by the scene’s content.

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

Use this property to determine how the user interacts with the content of the associated scene. UIKit sets the initial value of this property based on the information in your app’s `Info.plist` file. If you don’t provide scene configuration data for your app, UIKit sets the role to an appropriate value.

## See Also

- [var scene: UIScene?](uiscenesession/scene.md)
  The scene associated with the current session.
- [UISceneSession.Role](uiscenesession/role-swift.struct.md)
  Constants that indicate the possible roles for a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.property)*