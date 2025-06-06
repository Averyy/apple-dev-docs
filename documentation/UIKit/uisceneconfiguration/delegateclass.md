# delegateClass

**Framework**: UIKit  
**Kind**: property

The class of the custom delegate object that you want UIKit to create.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var delegateClass: AnyClass? { get set }
```

#### Discussion

If you specified [`UIWindowScene`](uiwindowscene.md) in the [`sceneClass`](uisceneconfiguration/sceneclass.md) property, your delegate class must conform to the [`UIWindowSceneDelegate`](uiwindowscenedelegate.md) protocol. Otherwise, you must specify a class that conforms to the [`UISceneDelegate`](uiscenedelegate.md) protocol.

UIKit sets this property’s initial value using the [`UISceneDelegateClassName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UIWindowSceneSessionRoleApplication/UISceneDelegateClassName) key from the appropriate scene in your app’s `Info.plist` file.

## See Also

- [var sceneClass: AnyClass?](uisceneconfiguration/sceneclass.md)
  The class of the scene object that you want UIKit to create.
- [var storyboard: UIStoryboard?](uisceneconfiguration/storyboard.md)
  The storyboard object that contains your scene’s initial view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/delegateclass)*