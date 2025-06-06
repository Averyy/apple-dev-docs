# setViewController(_:for:)

**Framework**: UIKit  
**Kind**: method

Presents the provided view controller in the specified column of the split view interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setViewController(_ vc: UIViewController?, for column: UISplitViewController.Column)
```

#### Discussion

This method doesn’t apply to classic split view controllers with a [`style`](uisplitviewcontroller/style-swift.property.md) of [`UISplitViewController.Style.unspecified`](uisplitviewcontroller/style-swift.enum/unspecified.md). For a classic split view controller, instead use the [`viewControllers`](uisplitviewcontroller/viewcontrollers.md) property to assign the primary and secondary view controllers that you want to display initially. After the split view controller is onscreen, set the child view controllers using the [`show(_:sender:)`](uisplitviewcontroller/show(_:sender:).md) and [`showDetailViewController(_:sender:)`](uisplitviewcontroller/showdetailviewcontroller(_:sender:).md) methods.

For a column-style split view controller, you use this method to assign child view controllers to a specific column of the split view interface. In general, unless your view controller is a navigation controller, the split view creates its own navigation controller to wrap the view controller you assign to the primary, supplementary, and secondary columns. There are some exceptions to this behavior:

- For the primary column, if you assign a [`UIViewController`](uiviewcontroller.md) (or custom subclass) whose first child view controller is a [`UINavigationController`](uinavigationcontroller.md), the split view controller uses that navigation controller as the primary view controller for collapsing the interface and for placing the button to change the display mode.
- For the secondary column, if you assign a [`UIViewController`](uiviewcontroller.md) (or custom subclass) whose first child view controller is a [`UINavigationController`](uinavigationcontroller.md), the split view controller uses that navigation controller as the secondary view controller for placing the button to change the display mode.

| Column | Assigned As-Is |
| --- | --- |
| Primary | [`UINavigationController`](uinavigationcontroller.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UIViewController`](uiviewcontroller.md) with [`UINavigationController`](uinavigationcontroller.md) as its first child |
| Supplementary | [`UINavigationController`](uinavigationcontroller.md) |
| Secondary | [`UITabBarController`](uitabbarcontroller.md) with [`UINavigationController`](uinavigationcontroller.md)s in its tabs ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UINavigationController`](uinavigationcontroller.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UIViewController`](uiviewcontroller.md) with [`UINavigationController`](uinavigationcontroller.md) as its first child |
| Compact | Any [`UIViewController`](uiviewcontroller.md) |

You can’t assign a [`UITabBarController`](uitabbarcontroller.md) to the primary or supplementary columns.

## Parameters

- `vc`: The child view controller to associate with the provided column of the split view interface.
- `column`: The corresponding column of the split view interface. See   for values.

## See Also

- [UISplitViewController.Column](uisplitviewcontroller/column.md)
  Constants that describe the columns within the split view interface.
- [func viewController(for: UISplitViewController.Column) -> UIViewController?](uisplitviewcontroller/viewcontroller(for:).md)
  Returns the view controller associated with the specified column of the split view interface.
- [var viewControllers: [UIViewController]](uisplitviewcontroller/viewcontrollers.md)
  The array of view controllers the split view controller manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/setviewcontroller(_:for:))*