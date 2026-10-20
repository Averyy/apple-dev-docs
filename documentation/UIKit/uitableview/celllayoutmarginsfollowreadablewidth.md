# cellLayoutMarginsFollowReadableWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var cellLayoutMarginsFollowReadableWidth: Bool { get set }
```

```objc
@property (nonatomic) BOOL cellLayoutMarginsFollowReadableWidth;
```

## See Also

### Related Documentation
- [var readableContentGuide: UILayoutGuide](../uiview/readablecontentguide.md)
  A layout guide representing an area with a readable width within the view.
### Configuring cell height and layout
- [var rowHeight: CGFloat](./rowheight.md)
  The default height in points of each row in the table view.
- [var estimatedRowHeight: CGFloat](./estimatedrowheight.md)
  The estimated height of rows in the table view.
- [var fillerRowHeight: CGFloat](./fillerrowheight.md)
  The height for empty rows that fill the table view.
- [var insetsContentViewsToSafeArea: Bool](./insetscontentviewstosafearea.md)
  A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/celllayoutmarginsfollowreadablewidth)*