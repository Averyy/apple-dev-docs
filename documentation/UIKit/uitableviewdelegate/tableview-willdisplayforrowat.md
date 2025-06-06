# tableView(_:willDisplay:forRowAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate the table view is about to draw a cell for a particular row.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath)
```

#### Discussion

A table view sends this message to its delegate just before it uses `cell` to draw a row, thereby permitting the delegate to customize the cell object before it is displayed. This method gives the delegate a chance to override state-based properties set earlier by the table view, such as selection and background color. After the delegate returns, the table view sets only the alpha and frame properties, and then only when animating rows as they slide in or out.

## Parameters

- `tableView`: The table view informing the delegate of this impending event.
- `cell`: A cell that   is going to use when drawing the row.
- `indexPath`: An index path locating the row in  .

## See Also

- [func tableView(UITableView, cellForRowAt: IndexPath) -> UITableViewCell](uitableviewdatasource/tableview(_:cellforrowat:).md)
  Asks the data source for a cell to insert in a particular location of the table view.
- [func prepareForReuse()](uitableviewcell/prepareforreuse.md)
  Prepares a reusable cell for reuse by the table view’s delegate.
- [func tableView(UITableView, indentationLevelForRowAt: IndexPath) -> Int](uitableviewdelegate/tableview(_:indentationlevelforrowat:).md)
  Asks the delegate to return the level of indentation for a row in a given section.
- [func tableView(UITableView, shouldSpringLoadRowAt: IndexPath, with: any UISpringLoadedInteractionContext) -> Bool](uitableviewdelegate/tableview(_:shouldspringloadrowat:with:).md)
  Called to let you fine tune the spring-loading behavior of the rows in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willdisplay:forrowat:))*