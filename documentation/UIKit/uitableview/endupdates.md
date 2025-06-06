# endUpdates()

**Framework**: UIKit  
**Kind**: method

Concludes a series of method calls that insert, delete, select, or reload rows and sections of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func endUpdates()
```

#### Discussion

Use the [`performBatchUpdates(_:completion:)`](uitableview/performbatchupdates(_:completion:).md) method instead of this one whenever possible.

You call this method to bracket a series of method calls that begins with [`beginUpdates()`](uitableview/beginupdates().md) and that consists of operations to insert, delete, select, and reload rows and sections of the table view. When you call `endUpdates`, `UITableView` animates the operations simultaneously. Invocations of [`beginUpdates()`](uitableview/beginupdates().md) and `endUpdates` can be nested. If you don’t make the insertion, deletion, and selection calls inside this block, table attributes such as row count can become invalid.

## See Also

- [func performBatchUpdates((() -> Void)?, completion: ((Bool) -> Void)?)](uitableview/performbatchupdates(_:completion:).md)
  Animates multiple insert, delete, reload, and move operations as a group.
- [func beginUpdates()](uitableview/beginupdates.md)
  Begins a series of method calls that insert, delete, or select rows and sections of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/endupdates())*