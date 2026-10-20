# tableView(_:heightForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the height to use for a row in a specified location.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat
```

```objc
- (CGFloat) tableView:(UITableView *) tableView heightForRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Mentions

- [Configuring the cells for your table](../configuring-the-cells-for-your-table.md)

#### Return Value

A nonnegative floating-point value that specifies the height (in points) that `row` should be.

#### Discussion

Override this method when the rows of your table are not all the same height. If your rows are the same height, do not override this method; assign a value to the [`rowHeight`](../uitableview/rowheight.md) property of [`UITableView`](../uitableview.md) instead. The value returned by this method takes precedence over the value in the [`rowHeight`](../uitableview/rowheight.md) property.

Before it appears onscreen, the table view calls this method for the items in the visible portion of the table. As the user scrolls, the table view calls the method for items only when they move onscreen. It calls the method each time the item appears onscreen, regardless of whether it appeared onscreen previously.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path that locates a row in `tableView`.

## See Also

### Related Documentation
- [func tableView(UITableView, estimatedHeightForRowAt: IndexPath) -> CGFloat](./tableview%28_,estimatedheightforrowat%29.md)
  Asks the delegate for the estimated height of a row in a specified location.
### Providing header, footer, and row heights
- [func tableView(UITableView, heightForHeaderInSection: Int) -> CGFloat](./tableview%28_,heightforheaderinsection%29.md)
  Asks the delegate for the height to use for the header of a particular section.
- [func tableView(UITableView, heightForFooterInSection: Int) -> CGFloat](./tableview%28_,heightforfooterinsection%29.md)
  Asks the delegate for the height to use for the footer of a particular section.
- [class let automaticDimension: CGFloat](../uitableview/automaticdimension.md)
  A constant representing the default value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:heightforrowat:))*