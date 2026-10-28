# show(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents the view controller in the specified column of the split view interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func show(_ column: UISplitViewController.Column)
```

```objc
- (void) showColumn:(UISplitViewControllerColumn) column;
```

## Discussion

When you call this method, the split view interface transitions to the closest display mode available for the current split behavior where the specified column is fully visible.

The split view controller chooses the appropriate transition to display the view controller in the specified column. For example, calling this method with [`UISplitViewController.Column.secondary`](./column/secondary.md) when the split behavior is [`UISplitViewController.SplitBehavior.displace`](./splitbehavior-swift.enum/displace.md) changes the display mode from [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](./displaymode-swift.enum/twodisplacesecondary.md) to [`UISplitViewController.DisplayMode.oneBesideSecondary`](./displaymode-swift.enum/onebesidesecondary.md), which hides the primary column to show the unobstructed secondary column.

After you call this method, you can use the split view controller’s [`transitionCoordinator`](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## Parameters

- `column`: The corresponding column of the split view interface to show. See [`UISplitViewController.Column`](./column.md) for values.

## See Also

### Displaying the child view controllers
- [func hide(UISplitViewController.Column)](./hide%28_%29.md)
  Dismisses the view controller in the specified column of the split view interface.
- [func isShowing(UISplitViewController.Column) -> Bool](./isshowing%28_%29.md)
  A Boolean value that indicates whether the split view interface is showing the specified column.
- [func show(UIViewController, sender: Any?)](./show%28_,sender%29.md)
  Presents the specified view controller as the primary view controller in the split view interface.
- [func showDetailViewController(UIViewController, sender: Any?)](./showdetailviewcontroller%28_,sender%29.md)
  Presents the specified view controller as the secondary view controller of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/show(_:))*