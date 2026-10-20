# tabBarController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The nearest ancestor in the view controller hierarchy that is a tab bar controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var tabBarController: UITabBarController? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UITabBarController * tabBarController;
```

#### Discussion

If the view controller or one of its ancestors is a child of a tab bar controller, this property contains the owning tab bar controller. This property is `nil` if the view controller is not embedded inside a tab bar controller.

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
- [var arrangementViewController: UIArrangementViewController?](./arrangementviewcontroller.md)
  The nearest ancestor arrangement view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/tabbarcontroller)*