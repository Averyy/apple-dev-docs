# delegateClass

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The class of the custom delegate object that you want UIKit to create.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var delegateClass: AnyClass? { get set }
```

```objc
@property (nonatomic, nullable) Class delegateClass;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)

## Discussion

If you specified [`UIWindowScene`](../uiwindowscene.md) in the [`sceneClass`](./sceneclass.md) property, your delegate class must conform to the [`UIWindowSceneDelegate`](../uiwindowscenedelegate.md) protocol. Otherwise, you must specify a class that conforms to the [`UISceneDelegate`](../uiscenedelegate.md) protocol.

UIKit sets this property’s initial value using the [`UISceneDelegateClassName`](../../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname.md) key from the appropriate scene in your app’s `Info.plist` file.

## See Also

### Specifying the scene creation details
- [var sceneClass: AnyClass?](./sceneclass.md)
  The class of the scene object that you want UIKit to create.
- [var storyboard: UIStoryboard?](./storyboard.md)
  The storyboard object that contains your scene’s initial view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/delegateclass)*