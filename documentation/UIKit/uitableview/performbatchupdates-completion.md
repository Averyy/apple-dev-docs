# performBatchUpdates(_:completion:)

**Framework**: UIKit  
**Kind**: method

Animates multiple insert, delete, reload, and move operations as a group.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performBatchUpdates(_ updates: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

#### Discussion

Use this method in cases where you want to make multiple changes to the table view in one single animated operation, as opposed to several separate animations. Use the block passed in the `updates` parameter to specify all of the operations you want to perform.

Deletes are processed before inserts in batch operations. This means the indexes for the deletions are processed relative to the indexes of the table view’s state before the batch operation, and the indexes for the insertions are processed relative to the indexes of the state after all the deletions in the batch operation.

## Parameters

- `updates`: The block that performs the relevant insert, delete, reload, or move operations. In addition to modifying the table’s rows, update your table’s data source to reflect your changes. This block has no return value and takes no parameters.
- `completion`: A completion handler block to execute when all of the operations are finished. This block has no return value and takes the following parameter:

## See Also

- [func beginUpdates()](uitableview/beginupdates.md)
  Begins a series of method calls that insert, delete, or select rows and sections of the table view.
- [func endUpdates()](uitableview/endupdates.md)
  Concludes a series of method calls that insert, delete, select, or reload rows and sections of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/performbatchupdates(_:completion:))*