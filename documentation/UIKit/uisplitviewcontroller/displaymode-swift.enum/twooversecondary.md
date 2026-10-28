# UISplitViewController.DisplayMode.twoOverSecondary

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

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

```c
UISplitViewControllerDisplayModeTwoOverSecondary
```

## Discussion

This display mode is only available for [`UISplitViewController.Style.tripleColumn`](../style-swift.enum/triplecolumn.md) interfaces.

This display mode shows both sidebars layered on top of the secondary view controller, partially obscuring it. The secondary view controller is dimmed out, preventing interaction with its view. Touching the dimmed view dismisses the overlay and returns the interface to the [`UISplitViewController.DisplayMode.secondaryOnly`](./secondaryonly.md) display mode.

The interactive gesture can move the interface freely through [`UISplitViewController.DisplayMode.oneOverSecondary`](./oneoversecondary.md) to [`UISplitViewController.DisplayMode.secondaryOnly`](./secondaryonly.md) and back, stopping at any of the display modes depending on the user interaction.

This display mode is available for the [`UISplitViewController.SplitBehavior.overlay`](../splitbehavior-swift.enum/overlay.md) split behavior.

## See Also

### Constants
- [UISplitViewController.DisplayMode.automatic](./automatic.md)
  The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewController.DisplayMode.secondaryOnly](./secondaryonly.md)
  Only the secondary view controller is shown onscreen.
- [UISplitViewController.DisplayMode.oneBesideSecondary](./onebesidesecondary.md)
  One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.oneOverSecondary](./oneoversecondary.md)
  One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoBesideSecondary](./twobesidesecondary.md)
  Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](./twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/twooversecondary)*