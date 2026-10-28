# UISplitViewController.DisplayMode.secondaryOnly

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Only the secondary view controller is shown onscreen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case secondaryOnly
```

```c
UISplitViewControllerDisplayModeSecondaryOnly
```

## Discussion

The primary and supplementary view controllers are offscreen.

This display mode is available for any split behavior.

## See Also

### Constants
- [UISplitViewController.DisplayMode.automatic](./automatic.md)
  The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewController.DisplayMode.oneBesideSecondary](./onebesidesecondary.md)
  One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.oneOverSecondary](./oneoversecondary.md)
  One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoBesideSecondary](./twobesidesecondary.md)
  Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoOverSecondary](./twooversecondary.md)
  Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](./twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/secondaryonly)*