# UISplitViewController.DisplayMode.twoDisplaceSecondary

**Framework**: UIKit  
**Kind**: case

Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+

## Declaration

```swift
case twoDisplaceSecondary
```

#### Discussion

This display mode is only available for [`UISplitViewController.Style.tripleColumn`](uisplitviewcontroller/style-swift.enum/triplecolumn.md) interfaces.

This display mode shows both sidebars, which partially displace the secondary view controller offscreen to make space for the primary column. The secondary view controller is dimmed out, preventing interaction with its view. Touching the dimmed view or using a gesture returns the interface to the [`UISplitViewController.DisplayMode.oneBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md) display mode.

This display mode is available for the [`UISplitViewController.SplitBehavior.displace`](uisplitviewcontroller/splitbehavior-swift.enum/displace.md) split behavior.

## See Also

- [UISplitViewController.DisplayMode.automatic](uisplitviewcontroller/displaymode-swift.enum/automatic.md)
  The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewController.DisplayMode.secondaryOnly](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md)
  Only the secondary view controller is shown onscreen.
- [UISplitViewController.DisplayMode.oneBesideSecondary](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md)
  One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.oneOverSecondary](uisplitviewcontroller/displaymode-swift.enum/oneoversecondary.md)
  One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoBesideSecondary](uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary.md)
  Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoOverSecondary](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md)
  Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary)*