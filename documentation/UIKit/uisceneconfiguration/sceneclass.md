# sceneClass

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The class of the scene object that you want UIKit to create.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var sceneClass: AnyClass? { get set }
```

```objc
@property (nonatomic, nullable) Class sceneClass;
```

## Discussion

The class you specify must be [`UIScene`](../uiscene.md) or one of its subclasses. Typically, you specify the [`UIWindowScene`](../uiwindowscene.md) class for all windows associated with your app.

UIKit sets this property’s initial value using the [`UISceneClassName`](../../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md) key from the appropriate scene in your app’s `Info.plist` file.

## See Also

### Specifying the scene creation details
- [var delegateClass: AnyClass?](./delegateclass.md)
  The class of the custom delegate object that you want UIKit to create.
- [var storyboard: UIStoryboard?](./storyboard.md)
  The storyboard object that contains your scene’s initial view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/sceneclass)*