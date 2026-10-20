# isShowing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

A Boolean value that indicates whether the split view interface is showing the specified column.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func isShowing(_ column: UISplitViewController.Column) -> Bool
```

```objc
- (BOOL) isShowingColumn:(UISplitViewControllerColumn) column;
```

## See Also

### Displaying the child view controllers
- [func show(UISplitViewController.Column)](./show%28_%29.md)
  Presents the view controller in the specified column of the split view interface.
- [func hide(UISplitViewController.Column)](./hide%28_%29.md)
  Dismisses the view controller in the specified column of the split view interface.
- [func show(UIViewController, sender: Any?)](./show%28_,sender%29.md)
  Presents the specified view controller as the primary view controller in the split view interface.
- [func showDetailViewController(UIViewController, sender: Any?)](./showdetailviewcontroller%28_,sender%29.md)
  Presents the specified view controller as the secondary view controller of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/isshowing(_:))*