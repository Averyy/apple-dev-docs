# splitViewController

**Framework**: UIKit  
**Kind**: property

The nearest ancestor in the view controller hierarchy that is a split view controller.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var splitViewController: UISplitViewController? { get }
```

#### Discussion

If the view controller or one of its ancestors is a child of a split view controller, this property contains the owning split view controller. This property is `nil` if the view controller is not embedded inside a split view controller.

## See Also

- [var presentingViewController: UIViewController?](uiviewcontroller/presentingviewcontroller.md)
  The view controller that presented this view controller.
- [var presentedViewController: UIViewController?](uiviewcontroller/presentedviewcontroller.md)
  The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [var parent: UIViewController?](uiviewcontroller/parent.md)
  The parent view controller of the recipient.
- [var navigationController: UINavigationController?](uiviewcontroller/navigationcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [var tabBarController: UITabBarController?](uiviewcontroller/tabbarcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/splitviewcontroller)*