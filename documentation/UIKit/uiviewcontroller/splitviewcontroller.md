# splitViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The nearest ancestor in the view controller hierarchy that is a split view controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var splitViewController: UISplitViewController? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UISplitViewController * splitViewController;
```

## Discussion

If the view controller or one of its ancestors is a child of a split view controller, this property contains the owning split view controller. This property is `nil` if the view controller is not embedded inside a split view controller.

## See Also

### Getting other related view controllers
- [var presentingViewController: UIViewController?](./presentingviewcontroller.md)
  The view controller that presented this view controller.
- [var presentedViewController: UIViewController?](./presentedviewcontroller.md)
  The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [var parent: UIViewController?](./parent.md)
  The parent view controller of the recipient.
- [var navigationController: UINavigationController?](./navigationcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [var tabBarController: UITabBarController?](./tabbarcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a tab bar controller.
- [var arrangementViewController: UIArrangementViewController?](./arrangementviewcontroller.md)
  The nearest ancestor arrangement view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/splitviewcontroller)*