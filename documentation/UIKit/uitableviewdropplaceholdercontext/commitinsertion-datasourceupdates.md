# commitInsertion(dataSourceUpdates:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Exchanges the placeholder cell for a cell with the final content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func commitInsertion(dataSourceUpdates: (IndexPath) -> Void) -> Bool
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the placeholder was replaced by your content or [`false`](https://developer.apple.com/documentation/swift/false) if the placeholder was no longer in the table view.

#### Discussion

When you receive the actual data for a cell, call this method on your app’s main thread to remove the corresponding placeholder cell and insert the actual cell. If the placeholder cell is still present in the table view, this method calls the `dataSourceUpdates` handler. Use that block only to update the data source object of your table view. Don’t update the table view itself, and don’t call [`reloadData()`](uitableview/reloaddata().md) on the table view. When your block finishes, the table view updates itself automatically, creating a new cell for your data.

If the placeholder cell is no longer present, this method doesn’t execute your `dataSourceUpdates` block.

## Parameters

- `dataSourceUpdates`: The handler block to execute as part of committing your changes. Use this block to update your table view’s data source with the actual data that you received. This block has no return value and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates:))*