# UISplitViewController.SplitBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UISplitViewControllerSplitBehavior : NSInteger;
```

## Overview

A split view controller’s split behavior controls how its secondary view controller appears in relation to the others. You can configure this behavior so that the secondary view controller always appears side-by-side with the others, so that it’s partially obscured by the others, or so that it’s displaced offscreen opposite the others to make space for them.

A split view controller’s split behavior affects its possible display mode ([`displayMode`](./displaymode-swift.property.md)). For more information, see [`UISplitViewController.DisplayMode`](./displaymode-swift.enum.md).

| Split Behavior | Possible Display Modes |
| --- | --- |
| Tile | [`UISplitViewController.DisplayMode.secondaryOnly`](./displaymode-swift.enum/secondaryonly.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](./displaymode-swift.enum/onebesidesecondary.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.twoBesideSecondary`](./displaymode-swift.enum/twobesidesecondary.md) |
| Overlay | [`UISplitViewController.DisplayMode.secondaryOnly`](./displaymode-swift.enum/secondaryonly.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.oneOverSecondary`](./displaymode-swift.enum/oneoversecondary.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.twoOverSecondary`](./displaymode-swift.enum/twooversecondary.md) |
| Displace | [`UISplitViewController.DisplayMode.secondaryOnly`](./displaymode-swift.enum/secondaryonly.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](./displaymode-swift.enum/onebesidesecondary.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](./displaymode-swift.enum/twodisplacesecondary.md) |

![Diagram showing a triple-column split view interface using the tile, overlay, and displace split behaviors.](https://developer.apple.com/tutorials/images/com.apple.uikit/UISplitViewController-4@2x.png)

## Topics

### Constants
- [UISplitViewController.SplitBehavior.automatic](./splitbehavior-swift.enum/automatic.md)
  The split view controller automatically decides the most appropriate split behavior based on the device and the current app size.
- [UISplitViewController.SplitBehavior.tile](./splitbehavior-swift.enum/tile.md)
  The sidebars and secondary view controller appear tiled side-by-side.
- [UISplitViewController.SplitBehavior.overlay](./splitbehavior-swift.enum/overlay.md)
  The sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.SplitBehavior.displace](./splitbehavior-swift.enum/displace.md)
  The sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
### Initializers
- [init?(rawValue: Int)](./splitbehavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the split behavior
- [var preferredSplitBehavior: UISplitViewController.SplitBehavior](./preferredsplitbehavior.md)
  The preferred behavior that determines how the child view controllers appear in relation to each other.
- [var splitBehavior: UISplitViewController.SplitBehavior](./splitbehavior-swift.property.md)
  The current behavior that determines how the child view controllers appear in relation to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.enum)*