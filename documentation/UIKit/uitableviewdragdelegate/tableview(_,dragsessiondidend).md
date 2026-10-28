# tableView(_:dragSessionDidEnd:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Signals the end of a drag operation involving content from the specified table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, dragSessionDidEnd session: any UIDragSession)
```

```objc
- (void) tableView:(UITableView *) tableView dragSessionDidEnd:(id<UIDragSession>) session;
```

## Discussion

This method is called after the drag session ended, usually because the content was dropped but possibly because the drag was terminated. Use this method to close out any tasks related to the management of the drag session in your app.

Each call to this method is always preceded by a call to the [`tableView(_:dragSessionWillBegin:)`](./tableview%28_,dragsessionwillbegin%29.md) method.

## Parameters

- `tableView`: The table view from which the drag operation originated.
- `session`: The drag session object providing context for the drag operation.

## See Also

### Tracking the drag session
- [func tableView(UITableView, dragSessionWillBegin: any UIDragSession)](./tableview%28_,dragsessionwillbegin%29.md)
  Signals the start of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](./tableview%28_,dragsessionisrestrictedtodraggingapplication%29.md)
  Returns a Boolean value indicating whether the dragged content must be dropped in the same app.
- [func tableView(UITableView, dragSessionAllowsMoveOperation: any UIDragSession) -> Bool](./tableview%28_,dragsessionallowsmoveoperation%29.md)
  Returns a Boolean value indicating whether your app supports a move operation for the dragged content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessiondidend:))*