# tableView(_:heightForFooterInSection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the height to use for the footer of a particular section.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, heightForFooterInSection section: Int) -> CGFloat
```

```objc
- (CGFloat) tableView:(UITableView *) tableView heightForFooterInSection:(NSInteger) section;
```

## Mentions

- [Adding headers and footers to table sections](../adding-headers-and-footers-to-table-sections.md)

## Return Value

A nonnegative floating-point value that specifies the height (in points) of the footer for `section`.

## Discussion

Use this method to specify the height of custom header views returned by your [`tableView(_:viewForFooterInSection:)`](./tableview%28_,viewforfooterinsection%29.md) method.

## Parameters

- `tableView`: The table view requesting this information.
- `section`: An index number identifying a section of `tableView` .

## See Also

### Related Documentation
- [func tableView(UITableView, viewForFooterInSection: Int) -> UIView?](./tableview%28_,viewforfooterinsection%29.md)
  Asks the delegate for a view to display in the footer of the specified section of the table view.
- [func tableView(UITableView, estimatedHeightForFooterInSection: Int) -> CGFloat](./tableview%28_,estimatedheightforfooterinsection%29.md)
  Asks the delegate for the estimated height of the footer of a particular section.
### Providing header, footer, and row heights
- [func tableView(UITableView, heightForRowAt: IndexPath) -> CGFloat](./tableview%28_,heightforrowat%29.md)
  Asks the delegate for the height to use for a row in a specified location.
- [func tableView(UITableView, heightForHeaderInSection: Int) -> CGFloat](./tableview%28_,heightforheaderinsection%29.md)
  Asks the delegate for the height to use for the header of a particular section.
- [class let automaticDimension: CGFloat](../uitableview/automaticdimension.md)
  A constant representing the default value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:heightforfooterinsection:))*