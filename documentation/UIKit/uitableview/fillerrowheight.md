# fillerRowHeight

**Framework**: UIKit  
**Kind**: property

The height for empty rows that fill the table view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var fillerRowHeight: CGFloat { get set }
```

#### Discussion

Table views with a [`style`](uitableview/style-swift.property.md) of [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md) can display filler rows, empty rows that appear below the last row when there isn’t enough content to fill the table view. Set this property to adjust the height of each filler row:

- Set `0.0` to not display filler rows. This behavior is the default in iOS 15 and later.
- Set [`automaticDimension`](uitableview/automaticdimension.md) to display filler rows that use an automatic height, matching the height of the last row in the table view. This behavior is the default in versions of iOS earlier than iOS 15.
- Set any other positive value to display filler rows of that specified height.

A table view with a [`style`](uitableview/style-swift.property.md) other than [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md) doesn’t show filler rows, so it ignores any value other than `0.0` for this property.

## See Also

- [var rowHeight: CGFloat](uitableview/rowheight.md)
  The default height in points of each row in the table view.
- [var estimatedRowHeight: CGFloat](uitableview/estimatedrowheight.md)
  The estimated height of rows in the table view.
- [var cellLayoutMarginsFollowReadableWidth: Bool](uitableview/celllayoutmarginsfollowreadablewidth.md)
  A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
- [var insetsContentViewsToSafeArea: Bool](uitableview/insetscontentviewstosafearea.md)
  A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/fillerrowheight)*