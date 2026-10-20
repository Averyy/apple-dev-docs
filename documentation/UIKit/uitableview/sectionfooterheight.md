# sectionFooterHeight

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The height of section footers in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var sectionFooterHeight: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat sectionFooterHeight;
```

## Mentions

- [Adding headers and footers to table sections](../adding-headers-and-footers-to-table-sections.md)

#### Discussion

The default value is [`automaticDimension`](./automaticdimension.md). If the delegate doesn’t implement [`tableView(_:heightForFooterInSection:)`](../uitableviewdelegate/tableview%28_,heightforfooterinsection%29.md), the table view calculates the height automatically. To override automatic height calculation, set this property to a positive value.

## See Also

### Related Documentation
- [var tableFooterView: UIView?](./tablefooterview.md)
  The view that displays below the table’s content.
### Configuring header and footer appearance
- [var sectionHeaderHeight: CGFloat](./sectionheaderheight.md)
  The height of section headers in the table view.
- [var estimatedSectionHeaderHeight: CGFloat](./estimatedsectionheaderheight.md)
  The estimated height of section headers in the table view.
- [var estimatedSectionFooterHeight: CGFloat](./estimatedsectionfooterheight.md)
  The estimated height of section footers in the table view.
- [var sectionHeaderTopPadding: CGFloat](./sectionheadertoppadding.md)
  The amount of padding above each section header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/sectionfooterheight)*