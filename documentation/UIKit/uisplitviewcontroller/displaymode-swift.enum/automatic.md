# UISplitViewController.DisplayMode.automatic

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The split view controller automatically decides the most appropriate display mode based on the device and the current app size.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case automatic
```

```c
UISplitViewControllerDisplayModeAutomatic
```

## Discussion

This constant represents the default value of the [`preferredDisplayMode`](../preferreddisplaymode.md) property. Although you can assign the property this constant as its value, the [`displayMode`](../displaymode-swift.property.md) property never reports it.

## See Also

### Constants
- [UISplitViewController.DisplayMode.secondaryOnly](./secondaryonly.md)
  Only the secondary view controller is shown onscreen.
- [UISplitViewController.DisplayMode.oneBesideSecondary](./onebesidesecondary.md)
  One sidebar appears side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.oneOverSecondary](./oneoversecondary.md)
  One sidebar is layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoBesideSecondary](./twobesidesecondary.md)
  Two sidebars appear side-by-side with the secondary view controller.
- [UISplitViewController.DisplayMode.twoOverSecondary](./twooversecondary.md)
  Two sidebars are layered on top of the secondary view controller, leaving the secondary view controller partially visible.
- [UISplitViewController.DisplayMode.twoDisplaceSecondary](./twodisplacesecondary.md)
  Two sidebars displace the secondary view controller instead of overlapping it, moving it partially offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.enum/automatic)*