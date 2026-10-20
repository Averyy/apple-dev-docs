# indexPathForPreferredFocusedView(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the table view’s index path for the preferred focused view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func indexPathForPreferredFocusedView(in tableView: UITableView) -> IndexPath?
```

```objc
- (NSIndexPath *) indexPathForPreferredFocusedViewInTableView:(UITableView *) tableView;
```

#### Return Value

An index path for the preferred focus row, or the default preferred focus view.

#### Discussion

This functionality of this delegate method is equivalent to overriding [`UITableView`](../uitableview.md) class’s [`preferredFocusedView`](../uifocusguide/preferredfocusedview.md) method in the [`UIFocusEnvironment`](../uifocusenvironment.md) protocol. If the [`UITableView`](../uitableview.md) class’s [`remembersLastFocusedIndexPath`](../uitableview/rememberslastfocusedindexpath.md) method is set to [`true`](../../Swift/true.md), this method defines the index path that gets focused when the table view is focused for the first time.

The effects of this method may be ignored during or immediately after a view controller transition, such as a presentation dismissal or navigation stack pop. In such cases, the view controller attempts to restore focus to the item that was focused prior to the transition (for example, prior to the view controller being presented or pushed), which can take precedence over the effects of this method. To learn how to control or disable this behavior in the view controller, see [`restoresFocusAfterTransition`](../uiviewcontroller/restoresfocusaftertransition.md).

## Parameters

- `tableView`: A table view requesting the index path for preferred focus view.

## See Also

### Managing table view focus
- [func tableView(UITableView, canFocusRowAt: IndexPath) -> Bool](./tableview%28_,canfocusrowat%29.md)
  Asks the delegate whether the cell at the specified index path is itself focusable.
- [func tableView(UITableView, shouldUpdateFocusIn: UITableViewFocusUpdateContext) -> Bool](./tableview%28_,shouldupdatefocusin%29.md)
  Asks the delegate whether the focus update specified by the context is allowed to occur.
- [func tableView(UITableView, didUpdateFocusIn: UITableViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](./tableview%28_,didupdatefocusin,with%29.md)
  Tells the delegate that a focus update specified by the context has just occurred.
- [func tableView(UITableView, selectionFollowsFocusForRowAt: IndexPath) -> Bool](./tableview%28_,selectionfollowsfocusforrowat%29.md)
  Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/indexpathforpreferredfocusedview(in:))*