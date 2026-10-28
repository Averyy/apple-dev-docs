# tableView(_:estimatedHeightForRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the estimated height of a row in a specified location.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, estimatedHeightForRowAt indexPath: IndexPath) -> CGFloat
```

```objc
- (CGFloat) tableView:(UITableView *) tableView estimatedHeightForRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Mentions

- [Estimating the height of a table’s scrolling area](../estimating-the-height-of-a-table-s-scrolling-area.md)

## Return Value

A nonnegative floating-point value that estimates the height (in points) that `row` should be. Return [`automaticDimension`](../uitableview/automaticdimension.md) if you have no estimate.

## Discussion

Providing an estimate the height of rows can improve the user experience when loading the table view. If the table contains variable height rows, it might be expensive to calculate all their heights and so lead to a longer load time. Using estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path that locates a row in `tableView`.

## See Also

### Related Documentation
- [func tableView(UITableView, heightForRowAt: IndexPath) -> CGFloat](./tableview%28_,heightforrowat%29.md)
  Asks the delegate for the height to use for a row in a specified location.
### Estimating heights for the table’s content
- [func tableView(UITableView, estimatedHeightForHeaderInSection: Int) -> CGFloat](./tableview%28_,estimatedheightforheaderinsection%29.md)
  Asks the delegate for the estimated height of the header of a particular section.
- [func tableView(UITableView, estimatedHeightForFooterInSection: Int) -> CGFloat](./tableview%28_,estimatedheightforfooterinsection%29.md)
  Asks the delegate for the estimated height of the footer of a particular section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforrowat:))*