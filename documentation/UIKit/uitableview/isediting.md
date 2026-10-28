# isEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the table view is in editing mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isEditing: Bool { get set }
```

```objc
@property (nonatomic, getter=isEditing) BOOL editing;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the table view is in editing mode: The cells of the table might show an insertion or deletion control on the left side of each cell and a reordering control on the right side, depending on how the cell is configured. (See [`UITableViewCell`](../uitableviewcell.md) for details.) Tapping a control causes the table view to invoke the data source method [`tableView(_:commit:forRowAt:)`](../uitableviewdatasource/tableview%28_,commit,forrowat%29.md). The default value is [`false`](../../Swift/false.md).

## See Also

### Putting the table into edit mode
- [func setEditing(Bool, animated: Bool)](./setediting%28_,animated%29.md)
  Toggles the table view into and out of editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/isediting)*