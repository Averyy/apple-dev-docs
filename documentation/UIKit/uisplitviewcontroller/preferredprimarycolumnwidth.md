# preferredPrimaryColumnWidth

**Framework**: UIKit  
**Kind**: property

The preferred width, in points, of the primary view controller’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredPrimaryColumnWidth: CGFloat { get set }
```

#### Discussion

Use this property to specify your preferred width for the primary view controller’s view. The default value of this property is [`automaticDimension`](uisplitviewcontroller/automaticdimension.md). If you set this property to a value different from [`automaticDimension`](uisplitviewcontroller/automaticdimension.md), that value takes precedence over [`preferredPrimaryColumnWidthFraction`](uisplitviewcontroller/preferredprimarycolumnwidthfraction.md).

The values in the [`minimumPrimaryColumnWidth`](uisplitviewcontroller/minimumprimarycolumnwidth.md) and [`maximumPrimaryColumnWidth`](uisplitviewcontroller/maximumprimarycolumnwidth.md) properties constrain the actual width of the primary view controller. The split view controller attempts to use the width you specify, but may change this value to accommodate the available space. You can get the actual width for the primary view controller’s view from the [`primaryColumnWidth`](uisplitviewcontroller/primarycolumnwidth.md) property.

## See Also

- [var isCollapsed: Bool](uisplitviewcontroller/iscollapsed.md)
  A Boolean value that indicates whether only one of the child view controllers displays.
- [var preferredPrimaryColumnWidthFraction: CGFloat](uisplitviewcontroller/preferredprimarycolumnwidthfraction.md)
  The relative width of the primary view controller’s content.
- [var primaryColumnWidth: CGFloat](uisplitviewcontroller/primarycolumnwidth.md)
  The width, in points, of the primary view controller’s content.
- [var minimumPrimaryColumnWidth: CGFloat](uisplitviewcontroller/minimumprimarycolumnwidth.md)
  The minimum width, in points, for the primary view controller’s content.
- [var maximumPrimaryColumnWidth: CGFloat](uisplitviewcontroller/maximumprimarycolumnwidth.md)
  The maximum width, in points, for the primary view controller’s content.
- [var preferredSupplementaryColumnWidthFraction: CGFloat](uisplitviewcontroller/preferredsupplementarycolumnwidthfraction.md)
  The relative width of the supplementary view controller’s content.
- [var preferredSupplementaryColumnWidth: CGFloat](uisplitviewcontroller/preferredsupplementarycolumnwidth.md)
  The preferred width, in points, of the supplementary view controller’s content.
- [var supplementaryColumnWidth: CGFloat](uisplitviewcontroller/supplementarycolumnwidth.md)
  The width, in points, of the supplementary view controller’s content.
- [var minimumSupplementaryColumnWidth: CGFloat](uisplitviewcontroller/minimumsupplementarycolumnwidth.md)
  The minimum width, in points, for the supplementary view controller’s content.
- [var maximumSupplementaryColumnWidth: CGFloat](uisplitviewcontroller/maximumsupplementarycolumnwidth.md)
  The maximum width, in points, for the supplementary view controller’s content.
- [var preferredSecondaryColumnWidth: CGFloat](uisplitviewcontroller/preferredsecondarycolumnwidth.md)
  The preferred width, in points, for the secondary view controller’s content.
- [var preferredSecondaryColumnWidthFraction: CGFloat](uisplitviewcontroller/preferredsecondarycolumnwidthfraction.md)
  The relative width of the secondary view controller’s content.
- [var minimumSecondaryColumnWidth: CGFloat](uisplitviewcontroller/minimumsecondarycolumnwidth.md)
  The minimum width, in points, for the secondary view controller’s content.
- [var preferredInspectorColumnWidth: CGFloat](uisplitviewcontroller/preferredinspectorcolumnwidth.md)
  The preferred width, in points, for the inspector view controller’s content.
- [var preferredInspectorColumnWidthFraction: CGFloat](uisplitviewcontroller/preferredinspectorcolumnwidthfraction.md)
  The relative width of the inspector view controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferredprimarycolumnwidth)*