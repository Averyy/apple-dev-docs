# UISplitViewController.DisplayMode

**Framework**: UIKit  
**Kind**: enum

Constants that describe the possible arrangements for a split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum DisplayMode
```

#### Overview

A split view controller’s display mode controls the visual arrangement of its child view controllers. You set a preferred display mode by using the [`preferredDisplayMode`](uisplitviewcontroller/preferreddisplaymode.md) property, and the split view controller updates itself and reflects the actual display mode in the [`displayMode`](uisplitviewcontroller/displaymode-swift.property.md) property.

Display modes apply to a split view controller in an expanded arrangement. When the split view interface is collapsed — when [`isCollapsed`](uisplitviewcontroller/iscollapsed.md) is [`true`](https://developer.apple.com/documentation/Swift/true) — the display mode has no impact on the appearance of the split view controller interface.

A split view controller’s split behavior ([`splitBehavior`](uisplitviewcontroller/splitbehavior-swift.property.md)) affects its possible display modes. For more information, see [`UISplitViewController.SplitBehavior`](uisplitviewcontroller/splitbehavior-swift.enum.md).

| Split Behavior | Possible Display Modes |
| --- | --- |
| Tile | [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.twoBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary.md) |
| Overlay | [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.oneOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/oneoversecondary.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.twoOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md) |
| Displace | [`UISplitViewController.DisplayMode.secondaryOnly`](uisplitviewcontroller/displaymode-swift.enum/secondaryonly.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.oneBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/onebesidesecondary.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md) |

There are several ways for user interaction to change the current display mode. Based on the type of user interaction (gesture or button tap), the display mode can transition between a set of predetermined states.

![Flow diagram showing the possible state transitions between display modes, based on split behavior and column style.](https://docs-assets.developer.apple.com/published/3ca2e98704a9ec01f1bc5c968908aaf7/UISplitViewController-3%402x.png)

## Topics

### Constants
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
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.
### Deprecated
- [static var primaryHidden: UISplitViewController.DisplayMode](uisplitviewcontroller/displaymode-swift.enum/primaryhidden.md)
  The primary view controller is hidden.
- [static var allVisible: UISplitViewController.DisplayMode](uisplitviewcontroller/displaymode-swift.enum/allvisible.md)
  The primary and secondary view controllers are displayed side-by-side onscreen.
- [static var primaryOverlay: UISplitViewController.DisplayMode](uisplitviewcontroller/displaymode-swift.enum/primaryoverlay.md)
  The primary view controller is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
### Initializers
- [init?(rawValue: Int)](uisplitviewcontroller/displaymode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var preferredDisplayMode: UISplitViewController.DisplayMode](uisplitviewcontroller/preferreddisplaymode.md)
  The preferred arrangement of the split view interface.
- [var displayMode: UISplitViewController.DisplayMode](uisplitviewcontroller/displaymode-swift.property.md)
  The current arrangement of the split view interface.
- [var displayModeButtonItem: UIBarButtonItem](uisplitviewcontroller/displaymodebuttonitem.md)
  A button that changes the display mode of the split view controller.
- [var presentsWithGesture: Bool](uisplitviewcontroller/presentswithgesture.md)
  Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [var showsSecondaryOnlyButton: Bool](uisplitviewcontroller/showssecondaryonlybutton.md)
  Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [var displayModeButtonVisibility: UISplitViewController.DisplayModeButtonVisibility](uisplitviewcontroller/displaymodebuttonvisibility-swift.property.md)
  A setting that determines whether the display mode button is visible in the interface.
- [UISplitViewController.DisplayModeButtonVisibility](uisplitviewcontroller/displaymodebuttonvisibility-swift.enum.md)
  Constants that determine the visibility of the display mode button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum)*