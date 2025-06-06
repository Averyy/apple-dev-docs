# numberOfSections(in:)

**Framework**: UIKit  
**Kind**: method

Asks the data source to return the number of sections in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func numberOfSections(in tableView: UITableView) -> Int
```

#### Return Value

The number of sections in `tableView`.

#### Discussion

If you don’t implement this method, the table configures the table with one section.

## Parameters

- `tableView`: An object representing the table view requesting this information.

## See Also

- [func tableView(UITableView, numberOfRowsInSection: Int) -> Int](uitableviewdatasource/tableview(_:numberofrowsinsection:).md)
  Tells the data source to return the number of rows in a given section of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/numberofsections(in:))*