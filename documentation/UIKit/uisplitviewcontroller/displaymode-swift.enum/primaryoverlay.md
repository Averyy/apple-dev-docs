# primaryOverlay

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The primary view controller is layered on top of the secondary view controller, leaving the secondary view controller partially visible.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.oneOverSecondary)
- iPadOS 8.0+ - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.oneOverSecondary)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.oneOverSecondary)
- tvOS - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.oneOverSecondary)

> **Deprecated**: Use [`UISplitViewController.DisplayMode.oneOverSecondary`](./oneoversecondary.md) instead.

## Declaration

```swift
static var primaryOverlay: UISplitViewController.DisplayMode { get }
```

```c
UISplitViewControllerDisplayModePrimaryOverlay
```

## See Also

### Deprecated
- [static var primaryHidden: UISplitViewController.DisplayMode](./primaryhidden.md)
  The primary view controller is hidden.
- [static var allVisible: UISplitViewController.DisplayMode](./allvisible.md)
  The primary and secondary view controllers are displayed side-by-side onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/primaryoverlay)*