# insetsContentViewsToSafeArea

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var insetsContentViewsToSafeArea: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) (the default), the table view adjusts the insets of the content view within each of its cells, headers, and footers on the leading and trailing sides to make the content fit within the safe area. The safe area ensures that the content within the table view isn’t obscured by other views, or by the edges of the device.

When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the table view doesn’t adjust the insets of the content view within each of its cells, headers, and footers to account for the safe area. In this case, the content views extend to the bounds of their respective superviews, which may cause the content to be obscured.

## See Also

- [var safeAreaInsets: UIEdgeInsets](uiview/safeareainsets.md)
  The insets that you use to determine the safe area for this view.
- [var rowHeight: CGFloat](uitableview/rowheight.md)
  The default height in points of each row in the table view.
- [var estimatedRowHeight: CGFloat](uitableview/estimatedrowheight.md)
  The estimated height of rows in the table view.
- [var fillerRowHeight: CGFloat](uitableview/fillerrowheight.md)
  The height for empty rows that fill the table view.
- [var cellLayoutMarginsFollowReadableWidth: Bool](uitableview/celllayoutmarginsfollowreadablewidth.md)
  A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/insetscontentviewstosafearea)*