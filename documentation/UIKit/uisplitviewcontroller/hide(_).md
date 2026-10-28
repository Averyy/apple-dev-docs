# hide(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the view controller in the specified column of the split view interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func hide(_ column: UISplitViewController.Column)
```

```objc
- (void) hideColumn:(UISplitViewControllerColumn) column;
```

## Discussion

When you call this method, the split view interface transitions to the closest display mode available for the current split behavior where the specified column is hidden.

This method does not support hiding the [`UISplitViewController.Column.secondary`](./column/secondary.md) column.

After you call this method, you can use the split view controller’s [`transitionCoordinator`](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `column`: The corresponding column of the split view interface to hide. See [`UISplitViewController.Column`](./column.md) for values.

## See Also

### Displaying the child view controllers
- [func show(UISplitViewController.Column)](./show%28_%29.md)
  Presents the view controller in the specified column of the split view interface.
- [func isShowing(UISplitViewController.Column) -> Bool](./isshowing%28_%29.md)
  A Boolean value that indicates whether the split view interface is showing the specified column.
- [func show(UIViewController, sender: Any?)](./show%28_,sender%29.md)
  Presents the specified view controller as the primary view controller in the split view interface.
- [func showDetailViewController(UIViewController, sender: Any?)](./showdetailviewcontroller%28_,sender%29.md)
  Presents the specified view controller as the secondary view controller of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/hide(_:))*