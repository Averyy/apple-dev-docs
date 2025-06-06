# toolbarItems

**Framework**: UIKit  
**Kind**: property

The toolbar items associated with the view controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var toolbarItems: [UIBarButtonItem]? { get set }
```

#### Discussion

This property contains an array of [`UIBarButtonItem`](uibarbuttonitem.md) objects and works in conjunction with a [`UINavigationController`](uinavigationcontroller.md) object. If this view controller is embedded inside a navigation controller interface, and the navigation controller displays a toolbar, this property identifies the items to display in that toolbar.

You can set the value of this property explicitly or use the [`setToolbarItems(_:animated:)`](uiviewcontroller/settoolbaritems(_:animated:).md) method to animate changes to the visible set of toolbar items.

## See Also

- [var navigationItem: UINavigationItem](uiviewcontroller/navigationitem.md)
  The navigation item used to represent the view controller in a parent’s navigation bar.
- [var hidesBottomBarWhenPushed: Bool](uiviewcontroller/hidesbottombarwhenpushed.md)
  A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.
- [func setToolbarItems([UIBarButtonItem]?, animated: Bool)](uiviewcontroller/settoolbaritems(_:animated:).md)
  Sets the toolbar items to be displayed along with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/toolbaritems)*