# tableView(_:dropPreviewParametersForRowAt:)

**Framework**: UIKit  
**Kind**: method

Returns custom information about how to display the row at the specified location during the drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dropPreviewParametersForRowAt indexPath: IndexPath) -> UIDragPreviewParameters?
```

#### Return Value

A [`UIDragPreviewParameters`](uidragpreviewparameters.md) object containing information about how to customize the row’s appearance. Return `nil` to use the default appearance.

#### Discussion

Use this method to customize the appearance of the row before a drop occurs. For example, you might use this method to specify that only part of the cell’s visible content should be used for the drop preview. If you don’t implement this method, or if you return `nil`, the drop preview displays the row’s visible content.

In your implementation, create a [`UIDragPreviewParameters`](uidragpreviewparameters.md) object and specify the custom preview information for the specified row. Use the parameters to specify the portion of the row that you want to display or to change the background color drawn beneath the row’s contents.

## Parameters

- `tableView`: The table view that’s attempting to handle the drop.
- `indexPath`: The index path of the row currently being targeted by the drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:droppreviewparametersforrowat:))*