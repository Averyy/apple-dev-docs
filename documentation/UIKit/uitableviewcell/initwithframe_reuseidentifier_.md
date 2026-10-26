# initWithFrame:reuseIdentifier:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Initializes and returns a table cell object.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`init(style:reuseIdentifier:)`](./init%28style,reuseidentifier%29.md) instead.

## Declaration

```objc
- (id) initWithFrame:(CGRect) frame reuseIdentifier:(NSString *) reuseIdentifier;
```

#### Return Value

An initialized [`UITableViewCell`](../uitableviewcell.md) object or `nil` if the object could not be created.

#### Discussion

This method is the designated initializer for the class. The reuse identifier is associated with those cells (rows) of a table view that have the same general configuration, minus cell content. In its implementation of [`tableView(_:cellForRowAt:)`](../uitableviewdatasource/tableview%28_,cellforrowat%29.md), the table view’s delegate calls the `UITableView` method [`dequeueReusableCell(withIdentifier:)`](../uitableview/dequeuereusablecell%28withidentifier%29.md), passing in a reuse identifier, to obtain the cell object to use as the basis for the current row.

## Parameters

- `frame`: The frame rectangle of the cell. Because the table view automatically positions the cell and makes it the optimal size, you can pass in `CGRectZero` in most cases. However, if you have a custom cell with multiple subviews, each with its own autoresizing mask, you must specify a non-zero frame rectangle; this allows the table view to position the subviews automatically as the cell changes size.
- `reuseIdentifier`: A string used to identify the cell object if it is to be reused for drawing multiple rows of a table view. Pass `nil` if the cell object is not to be reused.

## See Also

### Related Documentation
- [var reuseIdentifier: String?](./reuseidentifier.md)
  A string for identifying a reusable cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/initwithframe:reuseidentifier:)*