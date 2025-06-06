# tableView(_:titleForHeaderInSection:)

**Framework**: UIKit  
**Kind**: method

Asks the data source for the title of the header of the specified section of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String?
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Return Value

A string to use as the title of the section header. If you return `nil` , the section will have no title.

#### Discussion

The table view uses a fixed font style for section header titles. If you want a different font style, return a custom view (for example, a [`UILabel`](uilabel.md) object) in the delegate method [`tableView(_:viewForHeaderInSection:)`](uitableviewdelegate/tableview(_:viewforheaderinsection:).md) instead.

If you don’t implement this method or the [`tableView(_:viewForHeaderInSection:)`](uitableviewdelegate/tableview(_:viewforheaderinsection:).md) method, the table doesn’t display headers for sections. If you implement both methods, the [`tableView(_:viewForHeaderInSection:)`](uitableviewdelegate/tableview(_:viewforheaderinsection:).md) method takes priority.

## Parameters

- `tableView`: The table-view object asking for the title.
- `section`: An index number identifying a section of  .

## See Also

- [func tableView(UITableView, cellForRowAt: IndexPath) -> UITableViewCell](uitableviewdatasource/tableview(_:cellforrowat:).md)
  Asks the data source for a cell to insert in a particular location of the table view.
- [func tableView(UITableView, titleForFooterInSection: Int) -> String?](uitableviewdatasource/tableview(_:titleforfooterinsection:).md)
  Asks the data source for the title of the footer of the specified section of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:titleforheaderinsection:))*