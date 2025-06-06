# showDetailViewController(_:sender:)

**Framework**: UIKit  
**Kind**: method

Presents the specified view controller as the secondary view controller of the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func showDetailViewController(_ vc: UIViewController, sender: Any?)
```

#### Discussion

Whenever possible, use this method (instead of modifying the contents of the [`viewControllers`](uisplitviewcontroller/viewcontrollers.md) property directly) to replace the secondary view controller of your split view interface. This method displays the specified view controller in a way that’s optimal for the current size class in effect. It also takes advantage of existing navigation controller behaviors whenever possible to minimize changes to the split view interface.

This method calls the delegate’s [`splitViewController(_:showDetail:sender:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:showdetail:sender:).md) method to give the delegate an opportunity to show the view controller. If the delegate doesn’t show the view controller, the split view controller forwards the message to the view controller being replaced. For example, a navigation controller responds by pushing `vc` onto its navigation stack. If no other object shows the view controller, the split view controller shows it using the following heuristics:

- In a horizontally regular environment, the split view controller installs `vc` as the secondary view controller.
- In a horizontally compact environment, the split view controller presents `vc` modally.

All view controllers implement this method. If they do not show the view controller themselves, they forward the message to the parent split view controller (if any) and let it show the view controller. As a result, a child view controller can call this method on itself to achieve the same results as calling this method on the split view controller object.

## Parameters

- `vc`: The view controller to display in the secondary location of the split view interface. If you specify   for this parameter or if this view controller is the same as the one it would replace, this method does nothing.
- `sender`: The view or view controller that made the request.

## See Also

- [func show(UISplitViewController.Column)](uisplitviewcontroller/show(_:).md)
  Presents the view controller in the specified column of the split view interface.
- [func hide(UISplitViewController.Column)](uisplitviewcontroller/hide(_:).md)
  Dismisses the view controller in the specified column of the split view interface.
- [func show(UIViewController, sender: Any?)](uisplitviewcontroller/show(_:sender:).md)
  Presents the specified view controller as the primary view controller in the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/showdetailviewcontroller(_:sender:))*