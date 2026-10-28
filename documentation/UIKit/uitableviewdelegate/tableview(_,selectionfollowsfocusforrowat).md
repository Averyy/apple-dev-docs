# tableView(_:selectionFollowsFocusForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, selectionFollowsFocusForRowAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView selectionFollowsFocusForRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

[`true`](../../Swift/true.md) if you want to automatically select the row at the specified index path when focus moves to it; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the table view’s [`selectionFollowsFocus`](../uitableview/selectionfollowsfocus.md) property is [`true`](../../Swift/true.md) and you return [`false`](../../Swift/false.md) from this delegate method, focus still moves to the row when the user selects it. However, when focus moves to the row, the row doesn’t automatically select.

## Parameters

- `tableView`: The table view making the request.
- `indexPath`: The index path of the row to determine selection behavior for.

## See Also

### Managing table view focus
- [func tableView(UITableView, canFocusRowAt: IndexPath) -> Bool](./tableview%28_,canfocusrowat%29.md)
  Asks the delegate whether the cell at the specified index path is itself focusable.
- [func tableView(UITableView, shouldUpdateFocusIn: UITableViewFocusUpdateContext) -> Bool](./tableview%28_,shouldupdatefocusin%29.md)
  Asks the delegate whether the focus update specified by the context is allowed to occur.
- [func tableView(UITableView, didUpdateFocusIn: UITableViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](./tableview%28_,didupdatefocusin,with%29.md)
  Tells the delegate that a focus update specified by the context has just occurred.
- [func indexPathForPreferredFocusedView(in: UITableView) -> IndexPath?](./indexpathforpreferredfocusedview%28in%29.md)
  Asks the delegate for the table view’s index path for the preferred focused view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:selectionfollowsfocusforrowat:))*