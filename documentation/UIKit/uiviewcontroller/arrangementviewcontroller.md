# arrangementViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The nearest ancestor arrangement view controller.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
var arrangementViewController: UIArrangementViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIArrangementViewController * arrangementViewController;
```

## See Also

### Getting other related view controllers
- [var presentingViewController: UIViewController?](./presentingviewcontroller.md)
  The view controller that presented this view controller.
- [var presentedViewController: UIViewController?](./presentedviewcontroller.md)
  The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [var parent: UIViewController?](./parent.md)
  The parent view controller of the recipient.
- [var splitViewController: UISplitViewController?](./splitviewcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a split view controller.
- [var navigationController: UINavigationController?](./navigationcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [var tabBarController: UITabBarController?](./tabbarcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/arrangementviewcontroller)*