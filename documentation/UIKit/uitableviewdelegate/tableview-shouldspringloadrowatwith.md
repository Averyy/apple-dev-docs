# tableView(_:shouldSpringLoadRowAt:with:)

**Framework**: UIKit  
**Kind**: method

Called to let you fine tune the spring-loading behavior of the rows in a table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, shouldSpringLoadRowAt indexPath: IndexPath, with context: any UISpringLoadedInteractionContext) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the row allows spring-loaded interactions or [`false`](https://developer.apple.com/documentation/swift/false) if it does not.

#### Discussion

Override this method when you want to selectively disable spring-loaded interactions with the rows of your table. For example, you might return [`false`](https://developer.apple.com/documentation/swift/false) for rows that represent leaf content and not a folder of content. If you do not implement this method, the table view performs spring-loading animations on the row when it is not currently being dragged.By default, spring-loading animations are performed on the entire row. To modify these animations, modify the provided context object. For example, you might use the context object to apply the spring-loading animations to a single subview of the row instead of to the entire row.

## Parameters

- `tableView`: The table view where the interaction is occurring.
- `indexPath`: The index path of the row whose spring-loading behavior is being considered.
- `context`: A context object that you can use to modify the spring-loading behavior. Use this object to specify the location for spring-loading animations associated in the row.

## See Also

- [func tableView(UITableView, willDisplay: UITableViewCell, forRowAt: IndexPath)](uitableviewdelegate/tableview(_:willdisplay:forrowat:).md)
  Tells the delegate the table view is about to draw a cell for a particular row.
- [func tableView(UITableView, indentationLevelForRowAt: IndexPath) -> Int](uitableviewdelegate/tableview(_:indentationlevelforrowat:).md)
  Asks the delegate to return the level of indentation for a row in a given section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldspringloadrowat:with:))*