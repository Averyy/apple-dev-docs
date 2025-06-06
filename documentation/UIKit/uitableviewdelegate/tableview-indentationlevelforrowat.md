# tableView(_:indentationLevelForRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to return the level of indentation for a row in a given section.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, indentationLevelForRowAt indexPath: IndexPath) -> Int
```

#### Return Value

Returns the depth of the specified row to show its hierarchical position in the section.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path locating the row in  .

## See Also

- [func tableView(UITableView, willDisplay: UITableViewCell, forRowAt: IndexPath)](uitableviewdelegate/tableview(_:willdisplay:forrowat:).md)
  Tells the delegate the table view is about to draw a cell for a particular row.
- [func tableView(UITableView, shouldSpringLoadRowAt: IndexPath, with: any UISpringLoadedInteractionContext) -> Bool](uitableviewdelegate/tableview(_:shouldspringloadrowat:with:).md)
  Called to let you fine tune the spring-loading behavior of the rows in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:indentationlevelforrowat:))*