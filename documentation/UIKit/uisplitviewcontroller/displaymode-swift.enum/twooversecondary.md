# UISplitViewController.DisplayMode.twoOverSecondary

**Framework**: UIKit  
**Kind**: case

Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+

## Declaration

```swift
case twoOverSecondary
```

#### Discussion

This display mode is only available for [`UISplitViewController.Style.tripleColumn`](uisplitviewcontroller/style-swift.enum/triplecolumn.md) interfaces.

This display mode shows both sidebars layered on top of the secondary view controller, partially obscuring it. The secondary view controller is dimmed out, preventing interaction with its view. Touching the dimmed view dismisses the overlay and returns the interface to the [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) display mode.

The interactive gesture can move the interface freely through [`UISplitViewController.DisplayMode.oneOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/oneoversecondary.md) to [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) and back, stopping at any of the display modes depending on the user interaction.

This display mode is available for the [`UISplitViewController.SplitBehavior.overlay`](uisplitviewcontroller/splitbehavior-swift.enum/overlay.md) split behavior.

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
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twooversecondary)*