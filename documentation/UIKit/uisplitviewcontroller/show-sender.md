# show(_:sender:)

**Framework**: UIKit  
**Kind**: method

Presents the specified view controller as the primary view controller in the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func show(_ vc: UIViewController, sender: Any?)
```

#### Discussion

Whenever possible, use this method (instead of modifying the contents of the [`viewControllers`](uisplitviewcontroller/viewcontrollers.md) property directly) to replace the primary view controller of your split view interface. This method displays the specified view controller in a way that’s optimal for the current size class in effect.

Typically, you call this method from an action method when you want to replace the primary view controller with the one specified in `vc`. This method calls the split view controller delegate’s [`splitViewController(_:show:sender:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:).md) method to give the delegate an opportunity to show the view controller. If the delegate does not show the view controller, the split view controller shows it using the following heuristics:

- In a horizontally regular environment, the split view controller installs `vc` as the primary view controller unless `vc` is already a child of the primary view controller. In that case, it installs `vc` as the secondary view controller.
- In a horizontally compact environment, the split view controller presents `vc` modally.

## Parameters

- `vc`: The view controller to display in the primary location of the split view interface.
- `sender`: The object that made the request to show the view controller.

## See Also

- [func show(UISplitViewController.Column)](uisplitviewcontroller/show(_:).md)
  Presents the view controller in the specified column of the split view interface.
- [func hide(UISplitViewController.Column)](uisplitviewcontroller/hide(_:).md)
  Dismisses the view controller in the specified column of the split view interface.
- [func showDetailViewController(UIViewController, sender: Any?)](uisplitviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents the specified view controller as the secondary view controller of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/show(_:sender:))*