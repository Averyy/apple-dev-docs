# tableView(_:willDisplayFooterView:forSection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the table is about to display the footer view for the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, willDisplayFooterView view: UIView, forSection section: Int)
```

```objc
- (void) tableView:(UITableView *) tableView willDisplayFooterView:(UIView *) view forSection:(NSInteger) section;
```

## Parameters

- `tableView`: The table view informing the delegate of this event.
- `view`: The footer view that is about to be displayed.
- `section`: The index number of the section containing the footer view.

## See Also

### Providing custom header and footer views
- [func tableView(UITableView, viewForHeaderInSection: Int) -> UIView?](./tableview%28_,viewforheaderinsection%29.md)
  Asks the delegate for a view to display in the header of the specified section of the table view.
- [func tableView(UITableView, viewForFooterInSection: Int) -> UIView?](./tableview%28_,viewforfooterinsection%29.md)
  Asks the delegate for a view to display in the footer of the specified section of the table view.
- [func tableView(UITableView, willDisplayHeaderView: UIView, forSection: Int)](./tableview%28_,willdisplayheaderview,forsection%29.md)
  Tells the delegate that the table is about to display the header view for the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willdisplayfooterview:forsection:))*