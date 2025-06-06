# navigationController

**Framework**: UIKit  
**Kind**: property

The nearest ancestor in the view controller hierarchy that is a navigation controller.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var navigationController: UINavigationController? { get }
```

#### Discussion

If the view controller or one of its ancestors is a child of a navigation controller, this property contains the owning navigation controller. This property is `nil` if the view controller is not embedded inside a navigation controller.

## See Also

- [var presentingViewController: UIViewController?](uiviewcontroller/presentingviewcontroller.md)
  The view controller that presented this view controller.
- [var presentedViewController: UIViewController?](uiviewcontroller/presentedviewcontroller.md)
  The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [var parent: UIViewController?](uiviewcontroller/parent.md)
  The parent view controller of the recipient.
- [var splitViewController: UISplitViewController?](uiviewcontroller/splitviewcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a split view controller.
- [var tabBarController: UITabBarController?](uiviewcontroller/tabbarcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/navigationcontroller)*