# UITableView.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants for the table view styles.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Style
```

```c
enum UITableViewStyle : NSInteger;
```

#### Overview

You set the table style when you initialize the table view (see [`init(frame:style:)`](./init%28frame,style%29.md)). You can’t modify the style thereafter.

## Topics

### Styles
- [UITableView.Style.plain](./style-swift.enum/plain.md)
  A plain table view.
- [UITableView.Style.grouped](./style-swift.enum/grouped.md)
  A table view where sections have distinct groups of rows.
- [UITableView.Style.insetGrouped](./style-swift.enum/insetgrouped.md)
  A table view where the grouped sections are inset with rounded corners.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the table’s appearance
- [var style: UITableView.Style](./style-swift.property.md)
  The style of the table view.
- [var tableHeaderView: UIView?](./tableheaderview.md)
  The view that displays above the table’s content.
- [var tableFooterView: UIView?](./tablefooterview.md)
  The view that displays below the table’s content.
- [var backgroundView: UIView?](./backgroundview.md)
  The background view of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/style-swift.enum)*