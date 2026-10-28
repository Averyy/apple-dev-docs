# rowHeight

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default height in points of each row in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var rowHeight: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat rowHeight;
```

## Mentions

- [Configuring the cells for your table](../configuring-the-cells-for-your-table.md)

## Discussion

Use this property to specify a custom height for the cells in your table view. The default value of this property is [`automaticDimension`](./automaticdimension.md), which causes the table view to choose an appropriate height based on your cell’s content.

If you create a self-sizing cell in Interface Builder, the table view changes the default row height to the value you set in Interface Builder. To get the expected self-sizing behavior for a cell that you create in Interface Builder, you must explicitly set [`rowHeight`](./rowheight.md) to [`automaticDimension`](./automaticdimension.md) in your code.

The table view ignores the value of this property if its delegate implements the [`tableView(_:heightForRowAt:)`](../uitableviewdelegate/tableview%28_,heightforrowat%29.md) method. Prefer the use of this property over the delegate method when specifying row heights. When you implement the delegate method, the table view must call that method for every row of the table, including those that are offscreen. For tables with large numbers of rows (1000 or more), calling that method many times can negatively impact performance.

## See Also

### Configuring cell height and layout
- [var estimatedRowHeight: CGFloat](./estimatedrowheight.md)
  The estimated height of rows in the table view.
- [var fillerRowHeight: CGFloat](./fillerrowheight.md)
  The height for empty rows that fill the table view.
- [var cellLayoutMarginsFollowReadableWidth: Bool](./celllayoutmarginsfollowreadablewidth.md)
  A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
- [var insetsContentViewsToSafeArea: Bool](./insetscontentviewstosafearea.md)
  A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/rowheight)*