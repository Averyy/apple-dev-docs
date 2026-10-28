# tableView(_:canFocusRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the cell at the specified index path is itself focusable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, canFocusRowAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView canFocusRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

[`true`](../../Swift/true.md) if the row indicated by `indexPath`; otherwise, [`false`](../../Swift/false.md).

## Discussion

The functionality of this delegate method is equivalent to overriding the cell’s [`canBecomeFocused`](../uiview/canbecomefocused.md) method. If [`true`](../../Swift/true.md) is returned, then the cell at the specified index path is focusable, meaning none of its contents can be focused. Returning[`false`](../../Swift/false.md) means the cell itself is not focusable, however this does not prevent any of its contents from being focused. If this method is not implemented, then the return value is assumed to be [`true`](../../Swift/true.md).

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path locating a row in `tableView`.

## See Also

### Managing table view focus
- [func tableView(UITableView, shouldUpdateFocusIn: UITableViewFocusUpdateContext) -> Bool](./tableview%28_,shouldupdatefocusin%29.md)
  Asks the delegate whether the focus update specified by the context is allowed to occur.
- [func tableView(UITableView, didUpdateFocusIn: UITableViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](./tableview%28_,didupdatefocusin,with%29.md)
  Tells the delegate that a focus update specified by the context has just occurred.
- [func indexPathForPreferredFocusedView(in: UITableView) -> IndexPath?](./indexpathforpreferredfocusedview%28in%29.md)
  Asks the delegate for the table view’s index path for the preferred focused view.
- [func tableView(UITableView, selectionFollowsFocusForRowAt: IndexPath) -> Bool](./tableview%28_,selectionfollowsfocusforrowat%29.md)
  Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canfocusrowat:))*