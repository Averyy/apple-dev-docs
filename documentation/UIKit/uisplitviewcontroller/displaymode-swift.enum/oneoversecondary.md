# UISplitViewController.DisplayMode.oneOverSecondary

**Framework**: UIKit  
**Kind**: case

One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
case oneOverSecondary
```

#### Discussion

This display mode shows one sidebar layered on top of the secondary view controller, partially obscuring it. The sidebar shown is the primary column for [`UISplitViewController.Style.doubleColumn`](uisplitviewcontroller/style-swift.enum/doublecolumn.md) interfaces and the supplementary column for [`UISplitViewController.Style.tripleColumn`](uisplitviewcontroller/style-swift.enum/triplecolumn.md) interfaces. The secondary view controller is dimmed out, preventing interaction with its view. Touching the dimmed view dismisses the overlay and returns the interface to the [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) display mode.

This display mode is available for the [`UISplitViewController.SplitBehavior.overlay`](uisplitviewcontroller/splitbehavior-swift.enum/overlay.md) split behavior.

## See Also

- [UISplitViewController.DisplayMode.automatic](uisplitviewcontroller/displaymode-swift.enum/automatic.md)
  The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewController.DisplayMode.secondaryOnly](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md)
  Only the secondary view controller is shown onscreen.
- [UISplitViewController.DisplayMode.oneBesideSecondary](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md)
  One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoBesideSecondary](uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary.md)
  Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoOverSecondary](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md)
  Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/oneoversecondary)*