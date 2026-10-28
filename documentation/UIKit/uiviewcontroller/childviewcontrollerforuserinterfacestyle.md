# childViewControllerForUserInterfaceStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The child view controller that supports the preferred user interface style.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
var childViewControllerForUserInterfaceStyle: UIViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIViewController * childViewControllerForUserInterfaceStyle;
```

## Discussion

The default value of this property is `nil`. A container view controller can override this property and return the child view controller that supports the currently preferred user interface style, as determined by the [`preferredUserInterfaceStyle`](./preferreduserinterfacestyle.md) property.

## See Also

### Adjusting the interface style
- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](./overrideuserinterfacestyle.md)
  The user interface style adopted by the view controller and all of its children.
- [var preferredUserInterfaceStyle: UIUserInterfaceStyle](./preferreduserinterfacestyle.md)
  The preferred interface style for this view controller.
- [func setNeedsUserInterfaceAppearanceUpdate()](./setneedsuserinterfaceappearanceupdate%28%29.md)
  Notifies the view controller that a change occurred that might affect the preferred interface style.
- [enum UIUserInterfaceStyle](../uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerforuserinterfacestyle)*