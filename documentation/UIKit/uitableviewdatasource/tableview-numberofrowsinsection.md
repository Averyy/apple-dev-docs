# tableView(_:numberOfRowsInSection:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the data source to return the number of rows in a given section of a table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int
```

#### Return Value

The number of rows in `section`.

## Parameters

- `tableView`: The table-view object requesting this information.
- `section`: An index number identifying a section in  .

## See Also

- [func numberOfSections(in: UITableView) -> Int](uitableviewdatasource/numberofsections(in:).md)
  Asks the data source to return the number of sections in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:numberofrowsinsection:))*