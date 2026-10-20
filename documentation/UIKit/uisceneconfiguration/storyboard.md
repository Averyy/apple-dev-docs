# storyboard

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The storyboard object that contains your scene’s initial view controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var storyboard: UIStoryboard? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIStoryboard * storyboard;
```

#### Discussion

UIKit loads the initial view controller from the specified scene and displays it appropriately.

UIKit sets this property’s initial value using the [`UISceneStoryboardFile`](../../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) key from the appropriate scene in your app’s `Info.plist` file.

## See Also

### Specifying the scene creation details
- [var sceneClass: AnyClass?](./sceneclass.md)
  The class of the scene object that you want UIKit to create.
- [var delegateClass: AnyClass?](./delegateclass.md)
  The class of the custom delegate object that you want UIKit to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneconfiguration/storyboard)*