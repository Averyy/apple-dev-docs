# UISplitViewController.Style.unspecified

**Framework**: UIKit  
**Kind**: case

The split view interface uses the classic split view style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case unspecified
```

#### Discussion

A split view controller with this style represents a classic split view controller created using any other approach than [`init(style:)`](uisplitviewcontroller/init(style:).md). You cannot create a split view controller with a style of [`UISplitViewController.Style.unspecified`](uisplitviewcontroller/style-swift.enum/unspecified.md) using this initializer.

Split view controllers with this style don’t support any column-style APIs, such as [`setViewController(_:for:)`](uisplitviewcontroller/setviewcontroller(_:for:).md).

## See Also

- [UISplitViewController.Style.doubleColumn](uisplitviewcontroller/style-swift.enum/doublecolumn.md)
  The split view interface displays two columns.
- [UISplitViewController.Style.tripleColumn](uisplitviewcontroller/style-swift.enum/triplecolumn.md)
  The split view interface displays three columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/style-swift.enum/unspecified)*