# preferredSupplementaryColumnWidth

**Framework**: UIKit  
**Kind**: property

The preferred width, in points, of the supplementary view controller’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredSupplementaryColumnWidth: CGFloat { get set }
```

#### Discussion

Use this property to specify your preferred width for the supplementary view controller’s view. The default value of this property is [`automaticDimension`](uisplitviewcontroller/automaticdimension.md). If you set this property to a value different from [`automaticDimension`](uisplitviewcontroller/automaticdimension.md), that value takes precedence over [`preferredSupplementaryColumnWidthFraction`](uisplitviewcontroller/preferredsupplementarycolumnwidthfraction.md).

The values in the [`minimumSupplementaryColumnWidth`](uisplitviewcontroller/minimumsupplementarycolumnwidth.md) and [`maximumSupplementaryColumnWidth`](uisplitviewcontroller/maximumsupplementarycolumnwidth.md) properties constrain the actual width of the supplementary view controller. The split view controller attempts to use the width you specify, but may change this value to accommodate the available space. You can get the actual width for the supplementary view controller’s view from the [`supplementaryColumnWidth`](uisplitviewcontroller/supplementarycolumnwidth.md) property.

## See Also

- [var isCollapsed: Bool](uisplitviewcontroller/iscollapsed.md)
  A Boolean value that indicates whether only one of the child view controllers displays.
- [var preferredPrimaryColumnWidthFraction: CGFloat](uisplitviewcontroller/preferredprimarycolumnwidthfraction.md)
  The relative width of the primary view controller’s content.
- [var preferredPrimaryColumnWidth: CGFloat](uisplitviewcontroller/preferredprimarycolumnwidth.md)
  The preferred width, in points, of the primary view controller’s content.
- [var primaryColumnWidth: CGFloat](uisplitviewcontroller/primarycolumnwidth.md)
  The width, in points, of the primary view controller’s content.
- [var minimumPrimaryColumnWidth: CGFloat](uisplitviewcontroller/minimumprimarycolumnwidth.md)
  The minimum width, in points, for the primary view controller’s content.
- [var maximumPrimaryColumnWidth: CGFloat](uisplitviewcontroller/maximumprimarycolumnwidth.md)
  The maximum width, in points, for the primary view controller’s content.
- [var preferredSupplementaryColumnWidthFraction: CGFloat](uisplitviewcontroller/preferredsupplementarycolumnwidthfraction.md)
  The relative width of the supplementary view controller’s content.
- [var supplementaryColumnWidth: CGFloat](uisplitviewcontroller/supplementarycolumnwidth.md)
  The width, in points, of the supplementary view controller’s content.
- [var minimumSupplementaryColumnWidth: CGFloat](uisplitviewcontroller/minimumsupplementarycolumnwidth.md)
  The minimum width, in points, for the supplementary view controller’s content.
- [var maximumSupplementaryColumnWidth: CGFloat](uisplitviewcontroller/maximumsupplementarycolumnwidth.md)
  The maximum width, in points, for the supplementary view controller’s content.
- [class let automaticDimension: CGFloat](uisplitviewcontroller/automaticdimension.md)
  The default value to apply to a dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferredsupplementarycolumnwidth)*