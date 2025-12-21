# UISplitViewController.Style

**Framework**: UIKit  
**Kind**: enum

Constants that describe the number of columns the split view interface displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Style
```

#### Overview

In iOS 14 and later, [`UISplitViewController`](uisplitviewcontroller.md) supports column-style layouts. A column-style split view controller lets you create an interface with two or three columns by using [`init(style:)`](uisplitviewcontroller/init(style:).md) with the appropriate [`style`](uisplitviewcontroller/style-swift.property.md):

- Use the [`UISplitViewController.Style.doubleColumn`](uisplitviewcontroller/style-swift.enum/doublecolumn.md) style to create a split view interface with a two-column layout. This style of split view controller manages two child view controllers, placed in the primary and secondary columns.
- Use the [`UISplitViewController.Style.tripleColumn`](uisplitviewcontroller/style-swift.enum/triplecolumn.md) style to create a split view interface with a three-column layout. This style of split view controller manages three child view controllers, placed in the primary, supplementary, and secondary columns.

![Diagram showing a double-column and a triple-column split view interface, each with an inspector.](https://docs-assets.developer.apple.com/published/23c5e4fd7c1663d788630da117b02829/UISplitViewController-2%402x.png)

Before iOS 14, [`UISplitViewController`](uisplitviewcontroller.md) supported just one split view interface style with a primary view controller and a secondary view controller. This classic interface style applies to split view controllers created using any other approach than [`init(style:)`](uisplitviewcontroller/init(style:).md). Split view controllers with the classic interface have a [`style`](uisplitviewcontroller/style-swift.property.md) of [`UISplitViewController.Style.unspecified`](uisplitviewcontroller/style-swift.enum/unspecified.md) and they don’t respond to any of the column-style APIs introduced in iOS 14 and later.

## Topics

### Constants
- [UISplitViewController.Style.unspecified](uisplitviewcontroller/style-swift.enum/unspecified.md)
  The split view interface uses the classic split view style.
- [UISplitViewController.Style.doubleColumn](uisplitviewcontroller/style-swift.enum/doublecolumn.md)
  The split view interface displays two columns.
- [UISplitViewController.Style.tripleColumn](uisplitviewcontroller/style-swift.enum/triplecolumn.md)
  The split view interface displays three columns.
### Initializers
- [init?(rawValue: Int)](uisplitviewcontroller/style-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var style: UISplitViewController.Style](uisplitviewcontroller/style-swift.property.md)
  The style that determines the number of columns that the split view interface displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/style-swift.enum)*