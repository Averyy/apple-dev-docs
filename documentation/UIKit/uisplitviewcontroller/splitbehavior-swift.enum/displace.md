# UISplitViewController.SplitBehavior.displace

**Framework**: UIKit  
**Kind**: case

The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+

## Declaration

```swift
case displace
```

#### Discussion

This split behavior shows one or both sidebars tiled next to the secondary view controller. If both sidebars are visible, they partially displace the secondary view controller offscreen to make space for the primary column. The secondary view controller is dimmed out, preventing interaction with its view.

The possible display modes for this split behavior are:

- [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md)
- [`UISplitViewController.DisplayMode.oneBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md)
- [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md)

If the current display mode is [`UISplitViewController.DisplayMode.oneBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md) and [`presentsWithGesture`](uisplitviewcontroller/presentswithgesture.md) is [`true`](https://developer.apple.com/documentation/swift/true), the split view controller presents a special bar button item styled as a back-chevron icon. When a user taps this button, it changes the current display mode to [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md).

## See Also

- [UISplitViewController.SplitBehavior.automatic](uisplitviewcontroller/splitbehavior-swift.enum/automatic.md)
  The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewController.SplitBehavior.tile](uisplitviewcontroller/splitbehavior-swift.enum/tile.md)
  The sidebars and secondary view controller appear tiled side-by-side.
- [UISplitViewController.SplitBehavior.overlay](uisplitviewcontroller/splitbehavior-swift.enum/overlay.md)
  The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum/displace)*