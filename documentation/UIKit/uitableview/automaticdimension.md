# automaticDimension

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A constant representing the default value for a given dimension.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class let automaticDimension: CGFloat
```

```c
extern const CGFloat UITableViewAutomaticDimension;
```

#### Discussion

Return this value from your table view’s delegate methods when you want the table view to choose a default value for the given dimension. For example, if you return this constant from [`tableView(_:heightForHeaderInSection:)`](../uitableviewdelegate/tableview%28_,heightforheaderinsection%29.md) or [`tableView(_:heightForFooterInSection:)`](../uitableviewdelegate/tableview%28_,heightforfooterinsection%29.md), the table view uses a height that fits the value returned from [`tableView(_:titleForHeaderInSection:)`](../uitableviewdatasource/tableview%28_,titleforheaderinsection%29.md) or [`tableView(_:titleForFooterInSection:)`](../uitableviewdatasource/tableview%28_,titleforfooterinsection%29.md), if the title is not `nil`.

## See Also

### Providing header, footer, and row heights
- [func tableView(UITableView, heightForRowAt: IndexPath) -> CGFloat](../uitableviewdelegate/tableview%28_,heightforrowat%29.md)
  Asks the delegate for the height to use for a row in a specified location.
- [func tableView(UITableView, heightForHeaderInSection: Int) -> CGFloat](../uitableviewdelegate/tableview%28_,heightforheaderinsection%29.md)
  Asks the delegate for the height to use for the header of a particular section.
- [func tableView(UITableView, heightForFooterInSection: Int) -> CGFloat](../uitableviewdelegate/tableview%28_,heightforfooterinsection%29.md)
  Asks the delegate for the height to use for the footer of a particular section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/automaticdimension)*