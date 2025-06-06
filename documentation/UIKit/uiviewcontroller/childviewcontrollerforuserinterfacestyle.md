# childViewControllerForUserInterfaceStyle

**Framework**: UIKit  
**Kind**: property

The child view controller that supports the preferred user interface style.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
var childViewControllerForUserInterfaceStyle: UIViewController? { get }
```

#### Discussion

The default value of this property is `nil`. A container view controller can override this property and return the child view controller that supports the currently preferred user interface style, as determined by the [`preferredUserInterfaceStyle`](uiviewcontroller/preferreduserinterfacestyle.md) property.

## See Also

- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](uiviewcontroller/overrideuserinterfacestyle.md)
  The user interface style adopted by the view controller and all of its children.
- [var preferredUserInterfaceStyle: UIUserInterfaceStyle](uiviewcontroller/preferreduserinterfacestyle.md)
  The preferred interface style for this view controller.
- [func setNeedsUserInterfaceAppearanceUpdate()](uiviewcontroller/setneedsuserinterfaceappearanceupdate.md)
  Notifies the view controller that a change occurred that might affect the preferred interface style.
- [enum UIUserInterfaceStyle](uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerforuserinterfacestyle)*