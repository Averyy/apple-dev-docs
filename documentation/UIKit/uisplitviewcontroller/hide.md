# hide(_:)

**Framework**: UIKit  
**Kind**: method

Dismisses the view controller in the specified column of the split view interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func hide(_ column: UISplitViewController.Column)
```

#### Discussion

When you call this method, the split view interface transitions to the closest display mode available for the current split behavior where the specified column is hidden.

This method does not support hiding the [`UISplitViewController.Column.secondary`](uisplitviewcontroller/column/secondary.md) column.

After you call this method, you can use the split view controller’s [`transitionCoordinator`](uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `column`: The corresponding column of the split view interface to hide. See   for values.

## See Also

- [func show(UISplitViewController.Column)](uisplitviewcontroller/show(_:).md)
  Presents the view controller in the specified column of the split view interface.
- [func isShowing(UISplitViewController.Column) -> Bool](uisplitviewcontroller/isshowing(_:).md)
  A Boolean value that indicates whether the split view interface is showing the specified column.
- [func show(UIViewController, sender: Any?)](uisplitviewcontroller/show(_:sender:).md)
  Presents the specified view controller as the primary view controller in the split view interface.
- [func showDetailViewController(UIViewController, sender: Any?)](uisplitviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents the specified view controller as the secondary view controller of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/hide(_:))*