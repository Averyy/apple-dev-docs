# tableView(_:leadingSwipeActionsConfigurationForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the swipe actions to display on the leading edge of the row.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, leadingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration?
```

```objc
- (UISwipeActionsConfiguration *) tableView:(UITableView *) tableView leadingSwipeActionsConfigurationForRowAtIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

The swipe actions to display next to the leading edge of the row. Return `nil` if you want the table to display the default set of actions.

#### Discussion

Use this method to return a set of actions to display when the user swipes the row. The actions you return are displayed on the leading edge of the row. For example, in a left-to-right language environment, they are displayed on the left side of the row when the user swipes from left to right.

## Parameters

- `tableView`: The table view containing the row.
- `indexPath`: The index path of the row.

## See Also

### Responding to row actions
- [func tableView(UITableView, trailingSwipeActionsConfigurationForRowAt: IndexPath) -> UISwipeActionsConfiguration?](./tableview%28_,trailingswipeactionsconfigurationforrowat%29.md)
  Returns the swipe actions to display on the trailing edge of the row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:))*