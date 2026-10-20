# minimumSupplementaryColumnWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The minimum width, in points, for the supplementary view controller’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var minimumSupplementaryColumnWidth: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat minimumSupplementaryColumnWidth;
```

#### Discussion

Use this property in conjunction with the [`maximumSupplementaryColumnWidth`](./maximumsupplementarycolumnwidth.md) property to ensure the width of the supplementary view controller’s content is set to an acceptable value. The preliminary width is specified by the [`preferredSupplementaryColumnWidthFraction`](./preferredsupplementarycolumnwidthfraction.md) property, which is applied to the split view controller’s width and checked against these bounds. If the resulting width is less than the minimum value specified by this property, the width is set to the value in this property.

The default value of this property is [`automaticDimension`](./automaticdimension.md), which corresponds to a minimum width of 0 points.

## See Also

### Managing column dimensions
- [var isCollapsed: Bool](./iscollapsed.md)
  A Boolean value that indicates whether only one of the child view controllers displays.
- [var preferredPrimaryColumnWidthFraction: CGFloat](./preferredprimarycolumnwidthfraction.md)
  The relative width of the primary view controller’s content.
- [var preferredPrimaryColumnWidth: CGFloat](./preferredprimarycolumnwidth.md)
  The preferred width, in points, of the primary view controller’s content.
- [var primaryColumnWidth: CGFloat](./primarycolumnwidth.md)
  The width, in points, of the primary view controller’s content.
- [var minimumPrimaryColumnWidth: CGFloat](./minimumprimarycolumnwidth.md)
  The minimum width, in points, for the primary view controller’s content.
- [var maximumPrimaryColumnWidth: CGFloat](./maximumprimarycolumnwidth.md)
  The maximum width, in points, for the primary view controller’s content.
- [var preferredSupplementaryColumnWidthFraction: CGFloat](./preferredsupplementarycolumnwidthfraction.md)
  The relative width of the supplementary view controller’s content.
- [var preferredSupplementaryColumnWidth: CGFloat](./preferredsupplementarycolumnwidth.md)
  The preferred width, in points, of the supplementary view controller’s content.
- [var supplementaryColumnWidth: CGFloat](./supplementarycolumnwidth.md)
  The width, in points, of the supplementary view controller’s content.
- [var maximumSupplementaryColumnWidth: CGFloat](./maximumsupplementarycolumnwidth.md)
  The maximum width, in points, for the supplementary view controller’s content.
- [var preferredSecondaryColumnWidth: CGFloat](./preferredsecondarycolumnwidth.md)
  The preferred width, in points, for the secondary view controller’s content.
- [var preferredSecondaryColumnWidthFraction: CGFloat](./preferredsecondarycolumnwidthfraction.md)
  The relative width of the secondary view controller’s content.
- [var minimumSecondaryColumnWidth: CGFloat](./minimumsecondarycolumnwidth.md)
  The minimum width, in points, for the secondary view controller’s content.
- [var preferredInspectorColumnWidth: CGFloat](./preferredinspectorcolumnwidth.md)
  The preferred width, in points, for the inspector view controller’s content.
- [var preferredInspectorColumnWidthFraction: CGFloat](./preferredinspectorcolumnwidthfraction.md)
  The relative width of the inspector view controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/minimumsupplementarycolumnwidth)*