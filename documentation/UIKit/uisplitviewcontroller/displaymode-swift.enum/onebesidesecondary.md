# UISplitViewController.DisplayMode.oneBesideSecondary

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

One sidebar appears side-by-side with the secondary view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case oneBesideSecondary
```

```c
UISplitViewControllerDisplayModeOneBesideSecondary
```

## Discussion

This display mode shows one sidebar tiled next to the secondary view controller. The sidebar shown is the primary column for [`UISplitViewController.Style.doubleColumn`](../style-swift.enum/doublecolumn.md) interfaces and the supplementary column for [`UISplitViewController.Style.tripleColumn`](../style-swift.enum/triplecolumn.md) interfaces. The sidebar is displayed on the side specified by [`primaryEdge`](../primaryedge-swift.property.md), followed by the secondary view controller. The secondary view controller’s view is fully interactive.

This display mode is available for the [`UISplitViewController.SplitBehavior.tile`](../splitbehavior-swift.enum/tile.md) and [`UISplitViewController.SplitBehavior.displace`](../splitbehavior-swift.enum/displace.md) split behaviors.

## See Also

### Constants
- [UISplitViewController.DisplayMode.automatic](./automatic.md)
  The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewController.DisplayMode.secondaryOnly](./secondaryonly.md)
  Only the secondary view controller is shown onscreen.
- [UISplitViewController.DisplayMode.oneOverSecondary](./oneoversecondary.md)
  One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoBesideSecondary](./twobesidesecondary.md)
  Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoOverSecondary](./twooversecondary.md)
  Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](./twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary)*