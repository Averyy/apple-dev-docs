# tableView(_:shouldUpdateFocusIn:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the focus update specified by the context is allowed to occur.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, shouldUpdateFocusIn context: UITableViewFocusUpdateContext) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the focus should update; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The functionality of this delegate method is equivalent to overriding [`UITableView`](uitableview.md) class’s  [`shouldUpdateFocus(in:)`](uifocusenvironment/shouldupdatefocus(in:).md) method. This delegate method provides additional [`UITableView`](uitableview.md)-related information in its context parameter, such as the index paths for the previously and next focused views. Note that, these index paths are only available if their views are contained within the table view. To learn more about the information provided by the context, see [`UITableViewFocusUpdateContext`](uitableviewfocusupdatecontext.md).

## Parameters

- `tableView`: A table view in which the focus update is occurring.
- `context`: An instance of   class, contains metadata for the focus related update.

## See Also

- [func tableView(UITableView, canFocusRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:canfocusrowat:).md)
  Asks the delegate whether the cell at the specified index path is itself focusable.
- [func tableView(UITableView, didUpdateFocusIn: UITableViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](uitableviewdelegate/tableview(_:didupdatefocusin:with:).md)
  Tells the delegate that a focus update specified by the context has just occurred.
- [func indexPathForPreferredFocusedView(in: UITableView) -> IndexPath?](uitableviewdelegate/indexpathforpreferredfocusedview(in:).md)
  Asks the delegate for the table view’s index path for the preferred focused view.
- [func tableView(UITableView, selectionFollowsFocusForRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:selectionfollowsfocusforrowat:).md)
  Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldupdatefocusin:))*