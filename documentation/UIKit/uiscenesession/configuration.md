# configuration

**Framework**: UIKit  
**Kind**: property

The configuration data for creating the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var configuration: UISceneConfiguration { get }
```

#### Discussion

Before the creation of a scene, UIKit creates a [`UISceneConfiguration`](uisceneconfiguration.md) object and fills it with details from your app’s `Info.plist` file. (Normally, UIKit chooses the first scene of the appropriate type listed in your scene configuration data.) If the [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) method of your app delegate returns a new [`UISceneConfiguration`](uisceneconfiguration.md) object, UIKit copies that object to this property.

## See Also

- [class UISceneConfiguration](uisceneconfiguration.md)
  Information about the objects and storyboard for UKit to use when creating a particular scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesession/configuration)*