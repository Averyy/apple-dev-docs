# overrideUserInterfaceStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The user interface style adopted by the view controller and all of its children.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var overrideUserInterfaceStyle: UIUserInterfaceStyle { get set }
```

```objc
@property (nonatomic) UIUserInterfaceStyle overrideUserInterfaceStyle;
```

## Discussion

Use this property to force the view controller to always adopt a light or dark interface style. The default value of this property is [`UIUserInterfaceStyle.unspecified`](../uiuserinterfacestyle/unspecified.md), which causes the view controller to inherit the interface style from the system or a parent view controller. If you assign a different value, the new style applies to the view controller, its entire view hierarchy, and any embedded child view controllers.

## See Also

### Adjusting the interface style
- [var preferredUserInterfaceStyle: UIUserInterfaceStyle](./preferreduserinterfacestyle.md)
  The preferred interface style for this view controller.
- [var childViewControllerForUserInterfaceStyle: UIViewController?](./childviewcontrollerforuserinterfacestyle.md)
  The child view controller that supports the preferred user interface style.
- [func setNeedsUserInterfaceAppearanceUpdate()](./setneedsuserinterfaceappearanceupdate%28%29.md)
  Notifies the view controller that a change occurred that might affect the preferred interface style.
- [enum UIUserInterfaceStyle](../uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/overrideuserinterfacestyle)*