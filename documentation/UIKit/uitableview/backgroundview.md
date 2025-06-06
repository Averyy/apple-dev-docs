# backgroundView

**Framework**: UIKit  
**Kind**: property

The background view of the table view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backgroundView: UIView? { get set }
```

#### Discussion

Assign a background view to change the color behind your table’s sections and rows. The default value of this property is `nil`.

When you assign a view to this property, the table view automatically resizes that view to match its own bounds. Your background view appears behind all cells, header views, and footer views and doesn’t scroll with the rest of the table’s content.

## See Also

- [var style: UITableView.Style](uitableview/style-swift.property.md)
  The style of the table view.
- [UITableView.Style](uitableview/style-swift.enum.md)
  Constants for the table view styles.
- [var tableHeaderView: UIView?](uitableview/tableheaderview.md)
  The view that displays above the table’s content.
- [var tableFooterView: UIView?](uitableview/tablefooterview.md)
  The view that displays below the table’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/backgroundview)*