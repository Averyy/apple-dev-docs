# tableView(_:shouldUpdateFocusIn:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the focus update specified by the context is allowed to occur.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, shouldUpdateFocusIn context: UITableViewFocusUpdateContext) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView shouldUpdateFocusInContext:(UITableViewFocusUpdateContext *) context;
```

## Return Value

[`true`](../../Swift/true.md) if the focus should update; otherwise [`false`](../../Swift/false.md).

## Discussion

The functionality of this delegate method is equivalent to overriding [`UITableView`](../uitableview.md) class’s  [`shouldUpdateFocus(in:)`](../uifocusenvironment/shouldupdatefocus%28in%29.md) method. This delegate method provides additional [`UITableView`](../uitableview.md)-related information in its context parameter, such as the index paths for the previously and next focused views. Note that, these index paths are only available if their views are contained within the table view. To learn more about the information provided by the context, see [`UITableViewFocusUpdateContext`](../uitableviewfocusupdatecontext.md).

## Parameters

- `tableView`: A table view in which the focus update is occurring.
- `context`: An instance of [`UIFocusUpdateContext`](../uifocusupdatecontext.md) class, contains metadata for the focus related update.

## See Also

### Managing table view focus
- [func tableView(UITableView, canFocusRowAt: IndexPath) -> Bool](./tableview%28_,canfocusrowat%29.md)
  Asks the delegate whether the cell at the specified index path is itself focusable.
- [func tableView(UITableView, didUpdateFocusIn: UITableViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](./tableview%28_,didupdatefocusin,with%29.md)
  Tells the delegate that a focus update specified by the context has just occurred.
- [func indexPathForPreferredFocusedView(in: UITableView) -> IndexPath?](./indexpathforpreferredfocusedview%28in%29.md)
  Asks the delegate for the table view’s index path for the preferred focused view.
- [func tableView(UITableView, selectionFollowsFocusForRowAt: IndexPath) -> Bool](./tableview%28_,selectionfollowsfocusforrowat%29.md)
  Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldupdatefocusin:))*