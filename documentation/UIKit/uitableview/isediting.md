# isEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the table view is in editing mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEditing: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the table view is in editing mode: The cells of the table might show an insertion or deletion control on the left side of each cell and a reordering control on the right side, depending on how the cell is configured. (See [`UITableViewCell`](uitableviewcell.md) for details.) Tapping a control causes the table view to invoke the data source method [`tableView(_:commit:forRowAt:)`](uitableviewdatasource/tableview(_:commit:forrowat:).md). The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func setEditing(Bool, animated: Bool)](uitableview/setediting(_:animated:).md)
  Toggles the table view into and out of editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/isediting)*