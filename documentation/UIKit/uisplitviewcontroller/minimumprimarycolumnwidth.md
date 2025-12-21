# minimumPrimaryColumnWidth

**Framework**: UIKit  
**Kind**: property

The minimum width, in points, for the primary view controller’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumPrimaryColumnWidth: CGFloat { get set }
```

#### Discussion

Use this property in conjunction with the [`maximumPrimaryColumnWidth`](uisplitviewcontroller/maximumprimarycolumnwidth.md) property to ensure the width of the primary view controller’s content is set to an acceptable value. The preliminary width is specified by the [`preferredPrimaryColumnWidthFraction`](uisplitviewcontroller/preferredprimarycolumnwidthfraction.md) property, which is applied to the split view controller’s width and checked against these bounds. If the resulting width is less than the minimum value specified by this property, the width is set to the value in this property.

The default value of this property is [`automaticDimension`](uisplitviewcontroller/automaticdimension.md), which corresponds to a minimum width of 0 points.

## See Also

- [var isCollapsed: Bool](uisplitviewcontroller/iscollapsed.md)
  A Boolean value that indicates whether only one of the child view controllers displays.
- [var preferredPrimaryColumnWidthFraction: CGFloat](uisplitviewcontroller/preferredprimarycolumnwidthfraction.md)
  The relative width of the primary view controller’s content.
- [var preferredPrimaryColumnWidth: CGFloat](uisplitviewcontroller/preferredprimarycolumnwidth.md)
  The preferred width, in points, of the primary view controller’s content.
- [var primaryColumnWidth: CGFloat](uisplitviewcontroller/primarycolumnwidth.md)
  The width, in points, of the primary view controller’s content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/minimumprimarycolumnwidth)*