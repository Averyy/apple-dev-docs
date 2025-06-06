# tableView(_:accessoryButtonTappedForRowWith:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user tapped the detail button for the specified row.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWith indexPath: IndexPath)
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

Use this method to respond to taps in the detail button accessory view of a row. The table view does not call this method for other types of accessory views.

## Parameters

- `tableView`: The table view informing the delegate of this event.
- `indexPath`: The index path of the row whose detail button was tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:accessorybuttontappedforrowwith:))*