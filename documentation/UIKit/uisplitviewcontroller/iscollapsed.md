# isCollapsed

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether only one of the child view controllers displays.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isCollapsed: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCollapsed) BOOL collapsed;
```

## Discussion

This property is set to [`true`](../../Swift/true.md) when the split view controller content is semantically collapsed into a single container. Collapsing happens when the split view controller transitions from a horizontally regular to a horizontally compact environment. After it has been collapsed, the split view controller reports having only one child view controller in its [`viewControllers`](./viewcontrollers.md) property. When collapsed, the [`displayMode`](./displaymode-swift.property.md) property has no impact on the appearance of the split view interface.

In a column-style split view interface, if this property is [`true`](../../Swift/true.md) and the split view controller has a view controller set for its [`UISplitViewController.Column.compact`](./column/compact.md) column, the interface displays that view controller.

The value of this property is [`false`](../../Swift/false.md) when the split view controller is capable of displaying more than one of its child view controllers at the same time, even if it’s not showing more than one at the moment. In this expanded mode, the split view controller’s configuration of its child view controllers is determined by the [`displayMode`](./displaymode-swift.property.md) property.

During a transition from an expanded to a collapsed interface, the value of this property is [`false`](../../Swift/false.md) until after the collapse transition finishes and all of the relevant delegate methods have been called. Similarly, when transitioning back to an expanded interface, the value is [`true`](../../Swift/true.md) until the transition finishes.

## See Also

### Managing column dimensions
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/iscollapsed)*