# setToolbarItems(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the toolbar items to be displayed along with the view controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated: Bool)
```

#### Discussion

View controllers that are managed by a navigation controller can use this method to specify toolbar items for the navigation controller’s built-in toolbar. You can set the toolbar items for your view controller before your view controller is displayed or after it is already visible.

## Parameters

- `toolbarItems`: The toolbar items to display in a built-in toolbar.
- `animated`: If  , animate the change of items in the toolbar.

## See Also

- [var navigationItem: UINavigationItem](uiviewcontroller/navigationitem.md)
  The navigation item used to represent the view controller in a parent’s navigation bar.
- [var hidesBottomBarWhenPushed: Bool](uiviewcontroller/hidesbottombarwhenpushed.md)
  A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.
- [var toolbarItems: [UIBarButtonItem]?](uiviewcontroller/toolbaritems.md)
  The toolbar items associated with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/settoolbaritems(_:animated:))*