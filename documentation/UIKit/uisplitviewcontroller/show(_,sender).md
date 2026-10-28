# show(_:sender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents the specified view controller as the primary view controller in the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func show(_ vc: UIViewController, sender: Any?)
```

```objc
- (void) showViewController:(UIViewController *) vc sender:(id) sender;
```

## Discussion

Whenever possible, use this method (instead of modifying the contents of the [`viewControllers`](./viewcontrollers.md) property directly) to replace the primary view controller of your split view interface. This method displays the specified view controller in a way that’s optimal for the current size class in effect.

Typically, you call this method from an action method when you want to replace the primary view controller with the one specified in `vc`. This method calls the split view controller delegate’s [`splitViewController(_:show:sender:)`](../uisplitviewcontrollerdelegate/splitviewcontroller%28_,show,sender%29.md) method to give the delegate an opportunity to show the view controller. If the delegate does not show the view controller, the split view controller shows it using the following heuristics:

- In a horizontally regular environment, the split view controller installs `vc` as the primary view controller unless `vc` is already a child of the primary view controller. In that case, it installs `vc` as the secondary view controller.
- In a horizontally compact environment, the split view controller presents `vc` modally.

## Parameters

- `vc`: The view controller to display in the primary location of the split view interface.
- `sender`: The object that made the request to show the view controller.

## See Also

### Displaying the child view controllers
- [func show(UISplitViewController.Column)](./show%28_%29.md)
  Presents the view controller in the specified column of the split view interface.
- [func hide(UISplitViewController.Column)](./hide%28_%29.md)
  Dismisses the view controller in the specified column of the split view interface.
- [func isShowing(UISplitViewController.Column) -> Bool](./isshowing%28_%29.md)
  A Boolean value that indicates whether the split view interface is showing the specified column.
- [func showDetailViewController(UIViewController, sender: Any?)](./showdetailviewcontroller%28_,sender%29.md)
  Presents the specified view controller as the secondary view controller of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/show(_:sender:))*