# preferredSupplementaryColumnWidthFraction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The relative width of the supplementary view controller’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var preferredSupplementaryColumnWidthFraction: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat preferredSupplementaryColumnWidthFraction;
```

#### Discussion

Use this property to specify your preferred width for the supplementary view controller’s view. The value of this property is a floating-point number between `0.0` and `1.0` that represents the percentage of the overall width of the split view controller. For example, the value `0.4` represents 40% of the current width. The default value of this property is [`automaticDimension`](./automaticdimension.md), which results in an appropriate width for the supplementary view controller.

The values in the [`minimumSupplementaryColumnWidth`](./minimumsupplementarycolumnwidth.md) and [`maximumSupplementaryColumnWidth`](./maximumsupplementarycolumnwidth.md) properties constrain the actual width of the supplementary view controller. The split view controller attempts to use the width you specify, but may change this value to accommodate the available space. You can get the actual width for the supplementary view controller’s view from the [`supplementaryColumnWidth`](./supplementarycolumnwidth.md) property.

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
- [var preferredSupplementaryColumnWidth: CGFloat](./preferredsupplementarycolumnwidth.md)
  The preferred width, in points, of the supplementary view controller’s content.
- [var supplementaryColumnWidth: CGFloat](./supplementarycolumnwidth.md)
  The width, in points, of the supplementary view controller’s content.
- [var minimumSupplementaryColumnWidth: CGFloat](./minimumsupplementarycolumnwidth.md)
  The minimum width, in points, for the supplementary view controller’s content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferredsupplementarycolumnwidthfraction)*