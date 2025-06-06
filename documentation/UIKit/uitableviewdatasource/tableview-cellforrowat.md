# tableView(_:cellForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the data source for a cell to insert in a particular location of the table view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell
```

## Mentions

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)
- [Filling a table with data](filling-a-table-with-data.md)

#### Return Value

An object inheriting from [`UITableViewCell`](uitableviewcell.md) that the table view can use for the specified row. UIKit raises an assertion if you return `nil`.

#### Discussion

In your implementation, create and configure an appropriate cell for the given index path. Create your cell using the table view’s [`dequeueReusableCell(withIdentifier:for:)`](uitableview/dequeuereusablecell(withidentifier:for:).md) method, which recycles or creates the cell for you. After creating the cell, update the properties of the cell with appropriate data values.

Never call this method yourself. If you want to retrieve cells from your table, call the table view’s [`cellForRow(at:)`](uitableview/cellforrow(at:).md) method instead.

## Parameters

- `tableView`: A table-view object requesting the cell.
- `indexPath`: An index path locating a row in  .

## See Also

- [func tableView(UITableView, titleForHeaderInSection: Int) -> String?](uitableviewdatasource/tableview(_:titleforheaderinsection:).md)
  Asks the data source for the title of the header of the specified section of the table view.
- [func tableView(UITableView, titleForFooterInSection: Int) -> String?](uitableviewdatasource/tableview(_:titleforfooterinsection:).md)
  Asks the data source for the title of the footer of the specified section of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:cellforrowat:))*