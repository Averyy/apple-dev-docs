# beginUpdates()

**Framework**: UIKit  
**Kind**: method

Begins a series of method calls that insert, delete, or select rows and sections of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func beginUpdates()
```

#### Discussion

Use the [`performBatchUpdates(_:completion:)`](uitableview/performbatchupdates(_:completion:).md) method instead of this one whenever possible.

Call this method if you want subsequent insertions, deletion, and selection operations (for example, [`cellForRow(at:)`](uitableview/cellforrow(at:).md) and [`indexPathsForVisibleRows`](uitableview/indexpathsforvisiblerows.md)) to be animated simultaneously. You can also use this method followed by the [`endUpdates()`](uitableview/endupdates().md) method to animate the change in the row heights without reloading the cell. This group of methods must conclude with an invocation of [`endUpdates()`](uitableview/endupdates().md). These method pairs can be nested. If you don’t make the insertion, deletion, and selection calls inside this block, table attributes such as row count might become invalid. You shouldn’t call [`reloadData()`](uitableview/reloaddata().md) within the group; if you call this method within the group, you must perform any animations yourself.

## See Also

- [func performBatchUpdates((() -> Void)?, completion: ((Bool) -> Void)?)](uitableview/performbatchupdates(_:completion:).md)
  Animates multiple insert, delete, reload, and move operations as a group.
- [func endUpdates()](uitableview/endupdates.md)
  Concludes a series of method calls that insert, delete, select, or reload rows and sections of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/beginupdates())*