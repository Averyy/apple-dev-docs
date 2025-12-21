# preferredDisplayMode

**Framework**: UIKit  
**Kind**: property

The preferred arrangement of the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredDisplayMode: UISplitViewController.DisplayMode { get set }
```

#### Discussion

Use this property to specify the display mode that you prefer to use. The split view controller makes every effort to adopt the interface you specify, but may use a different type of interface if there isn’t enough space to support your preferred choice. If changing the value of this property leads to an actual change in the current display mode, the split view controller updates [`displayMode`](uisplitviewcontroller/displaymode-swift.property.md). The resulting change is animated if you made the change in an animation block.

Setting the value of this property to [`UISplitViewController.DisplayMode.automatic`](uisplitviewcontroller/displaymode-swift.enum/automatic.md) causes the split view controller to choose the most appropriate display mode for the currently available space. The default value of this property is [`UISplitViewController.DisplayMode.automatic`](uisplitviewcontroller/displaymode-swift.enum/automatic.md).

A split view controller’s split behavior affects its possible display mode. The preferred display mode is interpreted to match the current [`splitBehavior`](uisplitviewcontroller/splitbehavior-swift.property.md). For example, if you set the preferred display mode to [`UISplitViewController.DisplayMode.twoBesideSecondary`](uisplitviewcontroller/displaymode-swift.enum/twobesidesecondary.md), the actual [`displayMode`](uisplitviewcontroller/displaymode-swift.property.md) is interpreted as [`UISplitViewController.DisplayMode.twoOverSecondary`](uisplitviewcontroller/displaymode-swift.enum/twooversecondary.md) for [`UISplitViewController.SplitBehavior.overlay`](uisplitviewcontroller/splitbehavior-swift.enum/overlay.md), and as [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](uisplitviewcontroller/displaymode-swift.enum/twodisplacesecondary.md) for [`UISplitViewController.SplitBehavior.displace`](uisplitviewcontroller/splitbehavior-swift.enum/displace.md).

If [`presentsWithGesture`](uisplitviewcontroller/presentswithgesture.md) is [`false`](https://developer.apple.com/documentation/Swift/false), the value of this property is strictly respected.

## See Also

- [var displayMode: UISplitViewController.DisplayMode](uisplitviewcontroller/displaymode-swift.property.md)
  The current arrangement of the split view interface.
- [var displayModeButtonItem: UIBarButtonItem](uisplitviewcontroller/displaymodebuttonitem.md)
  A button that changes the display mode of the split view controller.
- [var presentsWithGesture: Bool](uisplitviewcontroller/presentswithgesture.md)
  Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [var showsSecondaryOnlyButton: Bool](uisplitviewcontroller/showssecondaryonlybutton.md)
  Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [UISplitViewController.DisplayMode](uisplitviewcontroller/displaymode-swift.enum.md)
  Constants that describe the possible arrangements for a split view interface.
- [var displayModeButtonVisibility: UISplitViewController.DisplayModeButtonVisibility](uisplitviewcontroller/displaymodebuttonvisibility-swift.property.md)
  A setting that determines whether the display mode button is visible in the interface.
- [UISplitViewController.DisplayModeButtonVisibility](uisplitviewcontroller/displaymodebuttonvisibility-swift.enum.md)
  Constants that determine the visibility of the display mode button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferreddisplaymode)*