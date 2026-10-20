# tableView(_:dropSessionDidExit:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when dragged content exits the table view’s bounds rectangle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, dropSessionDidExit session: any UIDropSession)
```

```objc
- (void) tableView:(UITableView *) tableView dropSessionDidExit:(id<UIDropSession>) session;
```

#### Discussion

The table view calls this method when dragged content exits its bounds rectangle. This method isn’t called again until the dragged content enters the table view’s bounds (triggering a call to the [`tableView(_:dropSessionDidEnter:)`](./tableview%28_,dropsessiondidenter%29.md) method) and exits again.

Use this method to clean up any state information that you configured in your [`tableView(_:dropSessionDidEnter:)`](./tableview%28_,dropsessiondidenter%29.md) method.

## Parameters

- `tableView`: The collection view that was tracking the dragged content.
- `session`: The drop session object containing information about the data being dragged.

## See Also

### Tracking the drag movements
- [func tableView(UITableView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UITableViewDropProposal](./tableview%28_,dropsessiondidupdate,withdestinationindexpath%29.md)
  Proposes how to handle a drop at the specified location in the table view.
- [func tableView(UITableView, dropSessionDidEnter: any UIDropSession)](./tableview%28_,dropsessiondidenter%29.md)
  Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidEnd: any UIDropSession)](./tableview%28_,dropsessiondidend%29.md)
  Notifies the delegate when the drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidexit:))*