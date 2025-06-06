# estimatedSectionHeaderHeight

**Framework**: UIKit  
**Kind**: property

The estimated height of section headers in the table view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var estimatedSectionHeaderHeight: CGFloat { get set }
```

## Mentions

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)

#### Discussion

Providing a nonnegative estimate of the height of section headers can improve the performance of loading the table view. If the table contains variable height section headers, it might be expensive to calculate all their heights when the table loads. Estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

The default value is [`automaticDimension`](uitableview/automaticdimension.md), which means that the table view selects an estimated height to use on your behalf. Setting the value to `0` disables estimated heights, which causes the table view to request the actual height for each header. If your table uses self-sizing headers, the value of this property must not be `0`.

When using height estimates, the table view actively manages the [`contentOffset`](uiscrollview/contentoffset.md) and [`contentSize`](uiscrollview/contentsize.md) properties inherited from its scroll view. Don’t attempt to read or modify those properties directly.

## See Also

- [var estimatedRowHeight: CGFloat](uitableview/estimatedrowheight.md)
  The estimated height of rows in the table view.
- [var sectionHeaderHeight: CGFloat](uitableview/sectionheaderheight.md)
  The height of section headers in the table view.
- [var sectionFooterHeight: CGFloat](uitableview/sectionfooterheight.md)
  The height of section footers in the table view.
- [var estimatedSectionFooterHeight: CGFloat](uitableview/estimatedsectionfooterheight.md)
  The estimated height of section footers in the table view.
- [var sectionHeaderTopPadding: CGFloat](uitableview/sectionheadertoppadding.md)
  The amount of padding above each section header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/estimatedsectionheaderheight)*