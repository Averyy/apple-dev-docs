# parent

**Framework**: UIKit  
**Kind**: property

The parent view controller of the recipient.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var parent: UIViewController? { get }
```

#### Discussion

If the recipient is a child of a container view controller, this property holds the view controller it is contained in. If the recipient has no parent, the value in this property is `nil`.

Prior to iOS 5.0, if a view did not have a parent view controller and was being presented, the presenting view controller would be returned. On iOS 5, this behavior no longer occurs. Instead, use the [`presentingViewController`](uiviewcontroller/presentingviewcontroller.md) property to access the presenting view controller.

## See Also

- [var presentingViewController: UIViewController?](uiviewcontroller/presentingviewcontroller.md)
  The view controller that presented this view controller.
- [var presentedViewController: UIViewController?](uiviewcontroller/presentedviewcontroller.md)
  The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [var splitViewController: UISplitViewController?](uiviewcontroller/splitviewcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a split view controller.
- [var navigationController: UINavigationController?](uiviewcontroller/navigationcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [var tabBarController: UITabBarController?](uiviewcontroller/tabbarcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/parent)*