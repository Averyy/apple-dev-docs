# UISplitViewController.SplitBehavior.tile

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The sidebars and secondary view controller appear tiled side-by-side.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case tile
```

```c
UISplitViewControllerSplitBehaviorTile
```

## Discussion

This split behavior shows one or both sidebars tiled next to the secondary view controller. The secondary view controller’s view is fully interactive.

The possible display modes for this split behavior are:

- [`UISplitViewController.DisplayMode.secondaryOnly`](../displaymode-swift.enum/secondaryonly.md)
- [`UISplitViewController.DisplayMode.oneBesideSecondary`](../displaymode-swift.enum/onebesidesecondary.md)
- [`UISplitViewController.DisplayMode.twoBesideSecondary`](../displaymode-swift.enum/twobesidesecondary.md)

If [`presentsWithGesture`](../presentswithgesture.md) is [`true`](../../../Swift/true.md), the split view controller presents a special bar button item styled as a sidebar toggle icon.

For a double-column split view interface, when a user taps this button, it toggles the current display mode between [`UISplitViewController.DisplayMode.secondaryOnly`](../displaymode-swift.enum/secondaryonly.md) and [`UISplitViewController.DisplayMode.oneBesideSecondary`](../displaymode-swift.enum/onebesidesecondary.md).

For a triple-column split view interface, when a user taps this button, it toggles the current display mode between [`UISplitViewController.DisplayMode.oneBesideSecondary`](../displaymode-swift.enum/onebesidesecondary.md) and [`UISplitViewController.DisplayMode.twoBesideSecondary`](../displaymode-swift.enum/twobesidesecondary.md). The button doesn’t appear in [`UISplitViewController.DisplayMode.secondaryOnly`](../displaymode-swift.enum/secondaryonly.md).

## See Also

### Constants
- [UISplitViewController.SplitBehavior.automatic](./automatic.md)
  The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewController.SplitBehavior.overlay](./overlay.md)
  The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.SplitBehavior.displace](./displace.md)
  The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/tile)*