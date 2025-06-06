# preferredUserInterfaceStyle

**Framework**: UIKit  
**Kind**: property

The preferred interface style for this view controller.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
var preferredUserInterfaceStyle: UIUserInterfaceStyle { get }
```

#### Discussion

Use this property to apply a specific appearance in your tvOS app. The default value of this property is [`UIUserInterfaceStyle.unspecified`](uiuserinterfacestyle/unspecified.md), which causes your view controller to follow the system’s current style. You can override this property to force the view controller to adopt a specific style.

## See Also

- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](uiviewcontroller/overrideuserinterfacestyle.md)
  The user interface style adopted by the view controller and all of its children.
- [var childViewControllerForUserInterfaceStyle: UIViewController?](uiviewcontroller/childviewcontrollerforuserinterfacestyle.md)
  The child view controller that supports the preferred user interface style.
- [func setNeedsUserInterfaceAppearanceUpdate()](uiviewcontroller/setneedsuserinterfaceappearanceupdate.md)
  Notifies the view controller that a change occurred that might affect the preferred interface style.
- [enum UIUserInterfaceStyle](uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferreduserinterfacestyle)*