# beginUpdates()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Begins a series of method calls that insert, delete, or select rows and sections of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func beginUpdates()
```

```objc
- (void) beginUpdates;
```

#### Discussion

Use the [`performBatchUpdates(_:completion:)`](./performbatchupdates%28_,completion%29.md) method instead of this one whenever possible.

Call this method if you want subsequent insertions, deletion, and selection operations (for example, [`cellForRow(at:)`](./cellforrow%28at%29.md) and [`indexPathsForVisibleRows`](./indexpathsforvisiblerows.md)) to be animated simultaneously. You can also use this method followed by the [`endUpdates()`](./endupdates%28%29.md) method to animate the change in the row heights without reloading the cell. This group of methods must conclude with an invocation of [`endUpdates()`](./endupdates%28%29.md). These method pairs can be nested. If you don’t make the insertion, deletion, and selection calls inside this block, table attributes such as row count might become invalid. You shouldn’t call [`reloadData()`](./reloaddata%28%29.md) within the group; if you call this method within the group, you must perform any animations yourself.

## See Also

### Performing batch updates to rows and sections
- [func performBatchUpdates((() -> Void)?, completion: ((Bool) -> Void)?)](./performbatchupdates%28_,completion%29.md)
  Animates multiple insert, delete, reload, and move operations as a group.
- [func endUpdates()](./endupdates%28%29.md)
  Concludes a series of method calls that insert, delete, select, or reload rows and sections of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/beginupdates())*