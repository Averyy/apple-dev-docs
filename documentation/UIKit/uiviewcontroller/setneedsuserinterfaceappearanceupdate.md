# setNeedsUserInterfaceAppearanceUpdate()

**Framework**: UIKit  
**Kind**: method

Notifies the view controller that a change occurred that might affect the preferred interface style.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
func setNeedsUserInterfaceAppearanceUpdate()
```

#### Discussion

UIKit calls this method to let the view controller know when system-level interface style changes occur. You can also call it to let UIKit know when you change your view controller in a way that affects the preferred user interface style.

## See Also

- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](uiviewcontroller/overrideuserinterfacestyle.md)
  The user interface style adopted by the view controller and all of its children.
- [var preferredUserInterfaceStyle: UIUserInterfaceStyle](uiviewcontroller/preferreduserinterfacestyle.md)
  The preferred interface style for this view controller.
- [var childViewControllerForUserInterfaceStyle: UIViewController?](uiviewcontroller/childviewcontrollerforuserinterfacestyle.md)
  The child view controller that supports the preferred user interface style.
- [enum UIUserInterfaceStyle](uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsuserinterfaceappearanceupdate())*