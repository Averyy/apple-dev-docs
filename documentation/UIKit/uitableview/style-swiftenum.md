# UITableView.Style

**Framework**: UIKit  
**Kind**: enum

Constants for the table view styles.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Style
```

#### Overview

You set the table style when you initialize the table view (see [`init(frame:style:)`](uitableview/init(frame:style:).md)). You can’t modify the style thereafter.

## Topics

### Styles
- [UITableView.Style.plain](uitableview/style-swift.enum/plain.md)
  A plain table view.
- [UITableView.Style.grouped](uitableview/style-swift.enum/grouped.md)
  A table view where sections have distinct groups of rows.
- [UITableView.Style.insetGrouped](uitableview/style-swift.enum/insetgrouped.md)
  A table view where the grouped sections are inset with rounded corners.
### Initializers
- [init?(rawValue: Int)](uitableview/style-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var style: UITableView.Style](uitableview/style-swift.property.md)
  The style of the table view.
- [var tableHeaderView: UIView?](uitableview/tableheaderview.md)
  The view that displays above the table’s content.
- [var tableFooterView: UIView?](uitableview/tablefooterview.md)
  The view that displays below the table’s content.
- [var backgroundView: UIView?](uitableview/backgroundview.md)
  The background view of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/style-swift.enum)*