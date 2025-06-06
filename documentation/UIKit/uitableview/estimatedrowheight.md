# estimatedRowHeight

**Framework**: UIKit  
**Kind**: property

The estimated height of rows in the table view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var estimatedRowHeight: CGFloat { get set }
```

## Mentions

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)

#### Discussion

Providing a nonnegative estimate of the height of rows can improve the performance of loading the table view. If the table contains variable height rows, it might be expensive to calculate all their heights when the table loads. Estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

The default value is [`automaticDimension`](uitableview/automaticdimension.md), which means that the table view selects an estimated height to use on your behalf. Setting the value to `0` disables estimated heights, which causes the table view to request the actual height for each cell. If your table uses self-sizing cells, the value of this property must not be `0`.

When using height estimates, the table view actively manages the [`contentOffset`](uiscrollview/contentoffset.md) and [`contentSize`](uiscrollview/contentsize.md) properties inherited from its scroll view. Don’t attempt to read or modify those properties directly.

## See Also

- [var estimatedSectionHeaderHeight: CGFloat](uitableview/estimatedsectionheaderheight.md)
  The estimated height of section headers in the table view.
- [var estimatedSectionFooterHeight: CGFloat](uitableview/estimatedsectionfooterheight.md)
  The estimated height of section footers in the table view.
- [var rowHeight: CGFloat](uitableview/rowheight.md)
  The default height in points of each row in the table view.
- [var fillerRowHeight: CGFloat](uitableview/fillerrowheight.md)
  The height for empty rows that fill the table view.
- [var cellLayoutMarginsFollowReadableWidth: Bool](uitableview/celllayoutmarginsfollowreadablewidth.md)
  A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
- [var insetsContentViewsToSafeArea: Bool](uitableview/insetscontentviewstosafearea.md)
  A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/estimatedrowheight)*