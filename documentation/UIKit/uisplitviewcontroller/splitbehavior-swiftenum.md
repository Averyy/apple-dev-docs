# UISplitViewController.SplitBehavior

**Framework**: UIKit  
**Kind**: enum

Constants that describe the possible ways that the child view controllers appear in relation to each other.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum SplitBehavior
```

#### Overview

A split view controller’s split behavior controls how its secondary view controller appears in relation to the others. You can configure this behavior so that the secondary view controller always appears side-by-side with the others, so that it’s partially obscured by the others, or so that it’s displaced offscreen opposite the others to make space for them.

A split view controller’s split behavior affects its possible display mode ([`displayMode`](uisplitviewcontroller/displaymode-swift.property.md)). For more information, see [`UISplitViewController.DisplayMode`](uisplitviewcontroller/displaymode-swift.enum.md).

| Split Behavior | Possible Display Modes |
| --- | --- |
| Tile | [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.twoBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary.md) |
| Overlay | [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.oneOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/oneoversecondary.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.twoOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md) |
| Displace | [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md) |

![Diagram showing a triple-column split view interface using the tile, overlay, and displace split behaviors.](https://docs-assets.developer.apple.com/published/784c280453b77630f7e439e3aee17f5f/media-3616616%402x.png)

## Topics

### Constants
- [UISplitViewController.SplitBehavior.automatic](uisplitviewcontroller/splitbehavior-swift.enum/automatic.md)
  The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewController.SplitBehavior.tile](uisplitviewcontroller/splitbehavior-swift.enum/tile.md)
  The sidebars and secondary view controller appear tiled side-by-side.
- [UISplitViewController.SplitBehavior.overlay](uisplitviewcontroller/splitbehavior-swift.enum/overlay.md)
  The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.SplitBehavior.displace](uisplitviewcontroller/splitbehavior-swift.enum/displace.md)
  The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
### Initializers
- [init?(rawValue: Int)](uisplitviewcontroller/splitbehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var preferredSplitBehavior: UISplitViewController.SplitBehavior](uisplitviewcontroller/preferredsplitbehavior.md)
  The preferred behavior that determines how the child view controllers appear in relation to each other.
- [var splitBehavior: UISplitViewController.SplitBehavior](uisplitviewcontroller/splitbehavior-swift.property.md)
  The current behavior that determines how the child view controllers appear in relation to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum)*