# moreNavigationController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller that manages the More navigation interface.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var moreNavigationController: UINavigationController { get }
```

```objc
@property (nonatomic, readonly) UINavigationController * moreNavigationController;
```

#### Discussion

This property always contains a valid More navigation controller, even if a More button is not displayed on the screen. You can use the value of this property to select the More navigation controller in the tab bar interface or to compare it against the currently selected view controller.

Do not add the object stored in this property to your tab bar interface manually. The More controller is displayed automatically by the tab bar controller as it is needed. You must also not look for the More navigation controller in the array of view controllers stored in the [`viewControllers`](./viewcontrollers.md) property. The tab bar controller does not include the More navigation controller in that array of objects.

> **Note**:  The More interface is not available in tvOS.

## See Also

### Managing the view controllers
- [var viewControllers: [UIViewController]?](./viewcontrollers.md)
  An array of the root view controllers displayed by the tab bar interface.
- [func setViewControllers([UIViewController]?, animated: Bool)](./setviewcontrollers%28_,animated%29.md)
  Sets the root view controllers of the tab bar controller.
- [var customizableViewControllers: [UIViewController]?](./customizableviewcontrollers.md)
  The subset of view controllers managed by this tab bar controller that can be customized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/morenavigationcontroller)*