# UISplitViewController.DisplayMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the possible arrangements for a split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum DisplayMode
```

```c
enum UISplitViewControllerDisplayMode : NSInteger;
```

#### Overview

A split view controller’s display mode controls the visual arrangement of its child view controllers. You set a preferred display mode by using the [`preferredDisplayMode`](./preferreddisplaymode.md) property, and the split view controller updates itself and reflects the actual display mode in the [`displayMode`](./displaymode-swift.property.md) property.

Display modes apply to a split view controller in an expanded arrangement. When the split view interface is collapsed — when [`isCollapsed`](./iscollapsed.md) is [`true`](../../Swift/true.md) — the display mode has no impact on the appearance of the split view controller interface.

A split view controller’s split behavior ([`splitBehavior`](./splitbehavior-swift.property.md)) affects its possible display modes. For more information, see [`UISplitViewController.SplitBehavior`](./splitbehavior-swift.enum.md).

| Split Behavior | Possible Display Modes |
| --- | --- |
| Tile | [`UISplitViewController.DisplayMode.secondaryOnly`](./displaymode-swift.enum/secondaryonly.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](./displaymode-swift.enum/onebesidesecondary.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.twoBesideSecondary`](./displaymode-swift.enum/twobesidesecondary.md) |
| Overlay | [`UISplitViewController.DisplayMode.secondaryOnly`](./displaymode-swift.enum/secondaryonly.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.oneOverSecondary`](./displaymode-swift.enum/oneoversecondary.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.twoOverSecondary`](./displaymode-swift.enum/twooversecondary.md) |
| Displace | [`UISplitViewController.DisplayMode.secondaryOnly`](./displaymode-swift.enum/secondaryonly.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](./displaymode-swift.enum/onebesidesecondary.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](./displaymode-swift.enum/twodisplacesecondary.md) |

There are several ways for user interaction to change the current display mode. Based on the type of user interaction (gesture or button tap), the display mode can transition between a set of predetermined states.

![Flow diagram showing the possible state transitions between display modes, based on split behavior and column style.](https://developer.apple.com/tutorials/images/com.apple.uikit/UISplitViewController-3@2x.png)

## Topics

### Constants
- [UISplitViewController.DisplayMode.automatic](./displaymode-swift.enum/automatic.md)
  The split view controller automatically decides the most appropriate display mode based on the device and the current app size.
- [UISplitViewController.DisplayMode.secondaryOnly](./displaymode-swift.enum/secondaryonly.md)
  Only the secondary view controller is shown onscreen.
- [UISplitViewController.DisplayMode.oneBesideSecondary](./displaymode-swift.enum/onebesidesecondary.md)
  One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.oneOverSecondary](./displaymode-swift.enum/oneoversecondary.md)
  One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoBesideSecondary](./displaymode-swift.enum/twobesidesecondary.md)
  Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoOverSecondary](./displaymode-swift.enum/twooversecondary.md)
  Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](./displaymode-swift.enum/twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
### Deprecated
- [static var primaryHidden: UISplitViewController.DisplayMode](./displaymode-swift.enum/primaryhidden.md)
  The primary view controller is hidden.
- [static var allVisible: UISplitViewController.DisplayMode](./displaymode-swift.enum/allvisible.md)
  The primary and secondary view controllers are displayed side-by-side onscreen.
- [static var primaryOverlay: UISplitViewController.DisplayMode](./displaymode-swift.enum/primaryoverlay.md)
  The primary view controller is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
### Initializers
- [init?(rawValue: Int)](./displaymode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the display mode
- [var preferredDisplayMode: UISplitViewController.DisplayMode](./preferreddisplaymode.md)
  The preferred arrangement of the split view interface.
- [var displayMode: UISplitViewController.DisplayMode](./displaymode-swift.property.md)
  The current arrangement of the split view interface.
- [var displayModeButtonItem: UIBarButtonItem](./displaymodebuttonitem.md)
  A button that changes the display mode of the split view controller.
- [var presentsWithGesture: Bool](./presentswithgesture.md)
  Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [var showsSecondaryOnlyButton: Bool](./showssecondaryonlybutton.md)
  Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [var displayModeButtonVisibility: UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.property.md)
  A setting that determines whether the display mode button is visible in the interface.
- [UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.enum.md)
  Constants that determine the visibility of the display mode button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum)*