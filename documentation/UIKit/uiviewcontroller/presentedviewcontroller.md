# presentedViewController

**Framework**: UIKit  
**Kind**: property

The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var presentedViewController: UIViewController? { get }
```

#### Discussion

When you present a view controller modally (either explicitly or implicitly) using the [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method, the view controller that called the method has this property set to the view controller that it presented. If the current view controller did not present another view controller modally, the value in this property is `nil`.

## See Also

- [var presentingViewController: UIViewController?](uiviewcontroller/presentingviewcontroller.md)
  The view controller that presented this view controller.
- [var parent: UIViewController?](uiviewcontroller/parent.md)
  The parent view controller of the recipient.
- [var splitViewController: UISplitViewController?](uiviewcontroller/splitviewcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a split view controller.
- [var navigationController: UINavigationController?](uiviewcontroller/navigationcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [var tabBarController: UITabBarController?](uiviewcontroller/tabbarcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/presentedviewcontroller)*