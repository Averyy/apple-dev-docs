# tableView(_:shouldSpringLoadRowAt:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called to let you fine tune the spring-loading behavior of the rows in a table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, shouldSpringLoadRowAt indexPath: IndexPath, with context: any UISpringLoadedInteractionContext) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView shouldSpringLoadRowAtIndexPath:(NSIndexPath *) indexPath withContext:(id<UISpringLoadedInteractionContext>) context;
```

## Return Value

[`true`](../../Swift/true.md) if the row allows spring-loaded interactions or [`false`](../../Swift/false.md) if it does not.

## Discussion

Override this method when you want to selectively disable spring-loaded interactions with the rows of your table. For example, you might return [`false`](../../Swift/false.md) for rows that represent leaf content and not a folder of content. If you do not implement this method, the table view performs spring-loading animations on the row when it is not currently being dragged.By default, spring-loading animations are performed on the entire row. To modify these animations, modify the provided context object. For example, you might use the context object to apply the spring-loading animations to a single subview of the row instead of to the entire row.

## Parameters

- `tableView`: The table view where the interaction is occurring.
- `indexPath`: The index path of the row whose spring-loading behavior is being considered.
- `context`: A context object that you can use to modify the spring-loading behavior. Use this object to specify the location for spring-loading animations associated in the row.

## See Also

### Configuring rows for the table view
- [func tableView(UITableView, willDisplay: UITableViewCell, forRowAt: IndexPath)](./tableview%28_,willdisplay,forrowat%29.md)
  Tells the delegate the table view is about to draw a cell for a particular row.
- [func tableView(UITableView, indentationLevelForRowAt: IndexPath) -> Int](./tableview%28_,indentationlevelforrowat%29.md)
  Asks the delegate to return the level of indentation for a row in a given section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldspringloadrowat:with:))*