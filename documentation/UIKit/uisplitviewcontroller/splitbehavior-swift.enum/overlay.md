# UISplitViewController.SplitBehavior.overlay

**Framework**: UIKit  
**Kind**: case

The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+

## Declaration

```swift
case overlay
```

#### Discussion

This split behavior shows one or both sidebars layered on top of the secondary view controller, partially obscuring it. The secondary view controller is dimmed out, preventing interaction with its view.

The possible display modes for this split behavior are:

- [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md)
- [`UISplitViewController.DisplayMode.oneOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/oneoversecondary.md)
- [`UISplitViewController.DisplayMode.twoOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md)

If the current display mode is not [`UISplitViewController.DisplayMode.twoOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md) and [`presentsWithGesture`](uisplitviewcontroller/presentswithgesture.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the split view controller presents a special bar button item styled as a back-chevron icon. When a user taps this button, it changes the current display mode from [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) to [`UISplitViewController.DisplayMode.oneOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/oneoversecondary.md), and from [`UISplitViewController.DisplayMode.oneOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/oneoversecondary.md) to [`UISplitViewController.DisplayMode.twoOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md).

## See Also

- [UISplitViewController.SplitBehavior.automatic](uisplitviewcontroller/splitbehavior-swift.enum/automatic.md)
  The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewController.SplitBehavior.tile](uisplitviewcontroller/splitbehavior-swift.enum/tile.md)
  The sidebars and secondary view controller appear tiled side-by-side.
- [UISplitViewController.SplitBehavior.displace](uisplitviewcontroller/splitbehavior-swift.enum/displace.md)
  The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/overlay)*