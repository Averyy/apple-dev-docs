# UISplitViewController.Style.unspecified

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The split view interface uses the classic split view style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+ - Deprecated in 1.0 (renamed: UISplitViewController.Style.doubleColumn)

## Declaration

```swift
case unspecified
```

```c
UISplitViewControllerStyleUnspecified
```

#### Discussion

A split view controller with this style represents a classic split view controller created using any other approach than [`init(style:)`](../init%28style%29.md). You cannot create a split view controller with a style of [`UISplitViewController.Style.unspecified`](./unspecified.md) using this initializer.

Split view controllers with this style don’t support any column-style APIs, such as [`setViewController(_:for:)`](../setviewcontroller%28_,for%29.md).

## See Also

### Constants
- [UISplitViewController.Style.doubleColumn](./doublecolumn.md)
  The split view interface displays two columns.
- [UISplitViewController.Style.tripleColumn](./triplecolumn.md)
  The split view interface displays three columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/style-swift.enum/unspecified)*