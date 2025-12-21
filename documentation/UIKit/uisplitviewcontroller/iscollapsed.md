# isCollapsed

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether only one of the child view controllers displays.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isCollapsed: Bool { get }
```

#### Discussion

This property is set to [`true`](https://developer.apple.com/documentation/Swift/true) when the split view controller content is semantically collapsed into a single container. Collapsing happens when the split view controller transitions from a horizontally regular to a horizontally compact environment. After it has been collapsed, the split view controller reports having only one child view controller in its [`viewControllers`](uisplitviewcontroller/viewcontrollers.md) property. When collapsed, the [`displayMode`](uisplitviewcontroller/displaymode-swift.property.md) property has no impact on the appearance of the split view interface.

In a column-style split view interface, if this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the split view controller has a view controller set for its [`UISplitViewController.Column.compact`](uisplitviewcontroller/column/compact.md) column, the interface displays that view controller.

The value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) when the split view controller is capable of displaying more than one of its child view controllers at the same time, even if it’s not showing more than one at the moment. In this expanded mode, the split view controller’s configuration of its child view controllers is determined by the [`displayMode`](uisplitviewcontroller/displaymode-swift.property.md) property.

During a transition from an expanded to a collapsed interface, the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) until after the collapse transition finishes and all of the relevant delegate methods have been called. Similarly, when transitioning back to an expanded interface, the value is [`true`](https://developer.apple.com/documentation/Swift/true) until the transition finishes.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/iscollapsed)*