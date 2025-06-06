# viewControllers

**Framework**: UIKit  
**Kind**: property

The array of view controllers the split view controller manages.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var viewControllers: [UIViewController] { get set }
```

#### Discussion

When the split view interface is expanded, this property contains two or three view controllers depending on the interface’s [`style`](uisplitviewcontroller/style-swift.property.md). The first view controller in the array is the primary view controller. It’s followed by the supplementary (if present) and then the secondary view controller.

When the split view interface is collapsed, this property contains only one view controller. If a view controller is set for the [`UISplitViewController.Column.compact`](uisplitviewcontroller/column/compact.md) column, this property contains that view controller. Otherwise, this property contains the primary view controller.

In a column-style split view controller, it’s recommended that you set the child view controllers using the [`setViewController(_:for:)`](uisplitviewcontroller/setviewcontroller(_:for:).md) method and get them using the [`viewController(for:)`](uisplitviewcontroller/viewcontroller(for:).md) method.

In a classic split view controller, you can use this property to assign the primary and secondary view controllers that you want to display initially. After the split view controller is onscreen, you can use this property to get the view controllers in the split view interface. After you assign the initial view controllers, it’s better to set the child view controllers using the [`show(_:sender:)`](uisplitviewcontroller/show(_:sender:).md) and [`showDetailViewController(_:sender:)`](uisplitviewcontroller/showdetailviewcontroller(_:sender:).md) methods. Although you can still change the view controllers in this property directly, you should do so only if you manually manage your app’s view controller transitions.

## See Also

- [func showDetailViewController(UIViewController, sender: Any?)](uisplitviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents the specified view controller as the secondary view controller of the split view interface.
- [func show(UIViewController, sender: Any?)](uisplitviewcontroller/show(_:sender:).md)
  Presents the specified view controller as the primary view controller in the split view interface.
- [UISplitViewController.Column](uisplitviewcontroller/column.md)
  Constants that describe the columns within the split view interface.
- [func setViewController(UIViewController?, for: UISplitViewController.Column)](uisplitviewcontroller/setviewcontroller(_:for:).md)
  Presents the provided view controller in the specified column of the split view interface.
- [func viewController(for: UISplitViewController.Column) -> UIViewController?](uisplitviewcontroller/viewcontroller(for:).md)
  Returns the view controller associated with the specified column of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/viewcontrollers)*