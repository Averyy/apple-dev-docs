# UISplitViewController.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UISplitViewControllerStyle : NSInteger;
```

#### Overview

In iOS 14 and later, [`UISplitViewController`](../uisplitviewcontroller.md) supports column-style layouts. A column-style split view controller lets you create an interface with two or three columns by using [`init(style:)`](./init%28style%29.md) with the appropriate [`style`](./style-swift.property.md):

- Use the [`UISplitViewController.Style.doubleColumn`](./style-swift.enum/doublecolumn.md) style to create a split view interface with a two-column layout. This style of split view controller manages two child view controllers, placed in the primary and secondary columns.
- Use the [`UISplitViewController.Style.tripleColumn`](./style-swift.enum/triplecolumn.md) style to create a split view interface with a three-column layout. This style of split view controller manages three child view controllers, placed in the primary, supplementary, and secondary columns.

![Diagram showing a double-column and a triple-column split view interface, each with an inspector.](https://developer.apple.com/tutorials/images/com.apple.uikit/UISplitViewController-2@2x.png)

Before iOS 14, [`UISplitViewController`](../uisplitviewcontroller.md) supported just one split view interface style with a primary view controller and a secondary view controller. This classic interface style applies to split view controllers created using any other approach than [`init(style:)`](./init%28style%29.md). Split view controllers with the classic interface have a [`style`](./style-swift.property.md) of [`UISplitViewController.Style.unspecified`](./style-swift.enum/unspecified.md) and they don’t respond to any of the column-style APIs introduced in iOS 14 and later.

## Topics

### Constants
- [UISplitViewController.Style.unspecified](./style-swift.enum/unspecified.md)
  The split view interface uses the classic split view style.
- [UISplitViewController.Style.doubleColumn](./style-swift.enum/doublecolumn.md)
  The split view interface displays two columns.
- [UISplitViewController.Style.tripleColumn](./style-swift.enum/triplecolumn.md)
  The split view interface displays three columns.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the split view style
- [var style: UISplitViewController.Style](./style-swift.property.md)
  The style that determines the number of columns that the split view interface displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/style-swift.enum)*