# preferredUserInterfaceStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred interface style for this view controller.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
var preferredUserInterfaceStyle: UIUserInterfaceStyle { get }
```

```objc
@property (nonatomic, readonly) UIUserInterfaceStyle preferredUserInterfaceStyle;
```

## Discussion

Use this property to apply a specific appearance in your tvOS app. The default value of this property is [`UIUserInterfaceStyle.unspecified`](../uiuserinterfacestyle/unspecified.md), which causes your view controller to follow the system’s current style. You can override this property to force the view controller to adopt a specific style.

## See Also

### Adjusting the interface style
- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](./overrideuserinterfacestyle.md)
  The user interface style adopted by the view controller and all of its children.
- [var childViewControllerForUserInterfaceStyle: UIViewController?](./childviewcontrollerforuserinterfacestyle.md)
  The child view controller that supports the preferred user interface style.
- [func setNeedsUserInterfaceAppearanceUpdate()](./setneedsuserinterfaceappearanceupdate%28%29.md)
  Notifies the view controller that a change occurred that might affect the preferred interface style.
- [enum UIUserInterfaceStyle](../uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferreduserinterfacestyle)*