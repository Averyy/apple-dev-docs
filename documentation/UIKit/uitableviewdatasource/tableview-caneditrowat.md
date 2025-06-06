# tableView(_:canEditRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the data source to verify that the given row is editable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the row indicated by `indexPath` is editable; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The method permits the data source to exclude individual rows from being treated as editable. Editable rows display the insertion or deletion control in their cells. If this method isn’t implemented, all rows are assumed to be editable. Rows that aren’t editable ignore the [`editingStyle`](uitableviewcell/editingstyle-swift.property.md) property of a `UITableViewCell` object and do no indentation for the deletion or insertion control. Rows that are editable, but that don’t want to have an insertion or remove control shown, can return [`UITableViewCell.EditingStyle.none`](uitableviewcell/editingstyle-swift.enum/none.md) from the [`tableView(_:editingStyleForRowAt:)`](uitableviewdelegate/tableview(_:editingstyleforrowat:).md) delegate method.

## Parameters

- `tableView`: The table-view object requesting this information.
- `indexPath`: An index path locating a row in  .

## See Also

- [func tableView(UITableView, commit: UITableViewCell.EditingStyle, forRowAt: IndexPath)](uitableviewdatasource/tableview(_:commit:forrowat:).md)
  Asks the data source to commit the insertion or deletion of a specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:caneditrowat:))*