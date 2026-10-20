# primaryHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The primary view controller is hidden.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.secondaryOnly)
- iPadOS 8.0+ - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.secondaryOnly)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.secondaryOnly)
- tvOS - Deprecated in 14.0 (renamed: UISplitViewController.DisplayMode.secondaryOnly)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: UISplitViewController.DisplayMode.secondaryOnly)

> **Deprecated**: Use [`UISplitViewController.DisplayMode.secondaryOnly`](./secondaryonly.md) instead.

## Declaration

```swift
static var primaryHidden: UISplitViewController.DisplayMode { get }
```

```c
UISplitViewControllerDisplayModePrimaryHidden
```

## See Also

### Deprecated
- [static var allVisible: UISplitViewController.DisplayMode](./allvisible.md)
  The primary and secondary view controllers are displayed side-by-side onscreen.
- [static var primaryOverlay: UISplitViewController.DisplayMode](./primaryoverlay.md)
  The primary view controller is layered on top of the secondary view controller, leaving the secondary view controller partially visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/primaryhidden)*