# setEditing(_:animated:)

**Framework**: UIKit  
**Kind**: method

Toggles the table view into and out of editing mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setEditing(_ editing: Bool, animated: Bool)
```

#### Discussion

When you call this method with the value of `editing` set to [`true`](https://developer.apple.com/documentation/swift/true), the table view goes into editing mode by calling [`setEditing(_:animated:)`](uitableviewcell/setediting(_:animated:).md) on each visible `UITableViewCell` object. Calling this method with `editing` set to [`false`](https://developer.apple.com/documentation/swift/false) turns off editing mode. In editing mode, the cells of the table might show an insertion or deletion control on the left side of each cell and a reordering control on the right side, depending on how the cell is configured. (See [`UITableViewCell`](uitableviewcell.md) for details.) The data source of the table view can selectively exclude cells from editing mode by implementing [`tableView(_:canEditRowAt:)`](uitableviewdatasource/tableview(_:caneditrowat:).md).

## Parameters

- `editing`:   to enter editing mode;   to leave it. The default value is  .
- `animated`:   to animate the transition to editing mode;   to make the transition immediate.

## See Also

- [var isEditing: Bool](uitableview/isediting.md)
  A Boolean value that determines whether the table view is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/setediting(_:animated:))*