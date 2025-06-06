# tableView(_:didUpdateFocusIn:with:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that a focus update specified by the context has just occurred.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, didUpdateFocusIn context: UITableViewFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator)
```

#### Discussion

This functionality of this delegate method is equivalent to overriding [`UITableView`](uitableview.md) class’s  implementation of [`tableView(_:didUpdateFocusIn:with:)`](uitableviewdelegate/tableview(_:didupdatefocusin:with:).md). This delegate method provides additional UITableView-related information in its context parameter, such as the index paths for the previously and next focused views. Note that, these index paths are available only if their views are contained within the table view. To learn more about the information provided by the context, see see [`UITableViewFocusUpdateContext`](uitableviewfocusupdatecontext.md).

## Parameters

- `tableView`: A table view informing the delegate about the new focus.
- `context`: An instance of the   class, containing metadata for the focus related update.
- `coordinator`: An instance of the   class, containing metadata for the focus related update.

## See Also

- [func tableView(UITableView, canFocusRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:canfocusrowat:).md)
  Asks the delegate whether the cell at the specified index path is itself focusable.
- [func tableView(UITableView, shouldUpdateFocusIn: UITableViewFocusUpdateContext) -> Bool](uitableviewdelegate/tableview(_:shouldupdatefocusin:).md)
  Asks the delegate whether the focus update specified by the context is allowed to occur.
- [func indexPathForPreferredFocusedView(in: UITableView) -> IndexPath?](uitableviewdelegate/indexpathforpreferredfocusedview(in:).md)
  Asks the delegate for the table view’s index path for the preferred focused view.
- [func tableView(UITableView, selectionFollowsFocusForRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:selectionfollowsfocusforrowat:).md)
  Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didupdatefocusin:with:))*