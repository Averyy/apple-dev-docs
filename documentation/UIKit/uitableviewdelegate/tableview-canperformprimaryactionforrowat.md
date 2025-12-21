# tableView(_:canPerformPrimaryActionForRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to perform a primary action for the row at the specified index path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, canPerformPrimaryActionForRowAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the primary action can be performed; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). If you don’t implement this method, the default return value is [`true`](https://developer.apple.com/documentation/Swift/true) when the table view isn’t in an editing state, and [`false`](https://developer.apple.com/documentation/Swift/false) when it is.

#### Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single row without extending an existing selection.

UIKit calls this method before [`tableView(_:performPrimaryActionForRowAt:)`](uitableviewdelegate/tableview(_:performprimaryactionforrowat:).md).

## Parameters

- `tableView`: The table view object asking whether to perform a primary action.
- `indexPath`: The index path of the row.

## See Also

- [func tableView(UITableView, performPrimaryActionForRowAt: IndexPath)](uitableviewdelegate/tableview(_:performprimaryactionforrowat:).md)
  Tells the delegate to perform the primary action for the row at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canperformprimaryactionforrowat:))*