# tableView(_:canPerformPrimaryActionForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to perform a primary action for the row at the specified index path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, canPerformPrimaryActionForRowAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView canPerformPrimaryActionForRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

[`true`](../../Swift/true.md) if the primary action can be performed; otherwise, [`false`](../../Swift/false.md). If you don’t implement this method, the default return value is [`true`](../../Swift/true.md) when the table view isn’t in an editing state, and [`false`](../../Swift/false.md) when it is.

## Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single row without extending an existing selection.

UIKit calls this method before [`tableView(_:performPrimaryActionForRowAt:)`](./tableview%28_,performprimaryactionforrowat%29.md).

## Parameters

- `tableView`: The table view object asking whether to perform a primary action.
- `indexPath`: The index path of the row.

## See Also

### Performing primary actions
- [func tableView(UITableView, performPrimaryActionForRowAt: IndexPath)](./tableview%28_,performprimaryactionforrowat%29.md)
  Tells the delegate to perform the primary action for the row at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canperformprimaryactionforrowat:))*