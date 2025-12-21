# tableView(_:selectionFollowsFocusForRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, selectionFollowsFocusForRowAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you want to automatically select the row at the specified index path when focus moves to it; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the table view’s [`selectionFollowsFocus`](uitableview/selectionfollowsfocus.md) property is [`true`](https://developer.apple.com/documentation/Swift/true) and you return [`false`](https://developer.apple.com/documentation/Swift/false) from this delegate method, focus still moves to the row when the user selects it. However, when focus moves to the row, the row doesn’t automatically select.

## Parameters

- `tableView`: The table view making the request.
- `indexPath`: The index path of the row to determine selection behavior for.

## See Also

- [func tableView(UITableView, canFocusRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:canfocusrowat:).md)
  Asks the delegate whether the cell at the specified index path is itself focusable.
- [func tableView(UITableView, shouldUpdateFocusIn: UITableViewFocusUpdateContext) -> Bool](uitableviewdelegate/tableview(_:shouldupdatefocusin:).md)
  Asks the delegate whether the focus update specified by the context is allowed to occur.
- [func tableView(UITableView, didUpdateFocusIn: UITableViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](uitableviewdelegate/tableview(_:didupdatefocusin:with:).md)
  Tells the delegate that a focus update specified by the context has just occurred.
- [func indexPathForPreferredFocusedView(in: UITableView) -> IndexPath?](uitableviewdelegate/indexpathforpreferredfocusedview(in:).md)
  Asks the delegate for the table view’s index path for the preferred focused view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:selectionfollowsfocusforrowat:))*