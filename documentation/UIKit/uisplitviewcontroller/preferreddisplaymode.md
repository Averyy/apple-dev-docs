# preferredDisplayMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred arrangement of the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var preferredDisplayMode: UISplitViewController.DisplayMode { get set }
```

```objc
@property (nonatomic) UISplitViewControllerDisplayMode preferredDisplayMode;
```

## Discussion

Use this property to specify the display mode that you prefer to use. The split view controller makes every effort to adopt the interface you specify, but may use a different type of interface if there isn’t enough space to support your preferred choice. If changing the value of this property leads to an actual change in the current display mode, the split view controller updates [`displayMode`](./displaymode-swift.property.md). The resulting change is animated if you made the change in an animation block.

Setting the value of this property to [`UISplitViewController.DisplayMode.automatic`](./displaymode-swift.enum/automatic.md) causes the split view controller to choose the most appropriate display mode for the currently available space. The default value of this property is [`UISplitViewController.DisplayMode.automatic`](./displaymode-swift.enum/automatic.md).

A split view controller’s split behavior affects its possible display mode. The preferred display mode is interpreted to match the current [`splitBehavior`](./splitbehavior-swift.property.md). For example, if you set the preferred display mode to [`UISplitViewController.DisplayMode.twoBesideSecondary`](./displaymode-swift.enum/twobesidesecondary.md), the actual [`displayMode`](./displaymode-swift.property.md) is interpreted as [`UISplitViewController.DisplayMode.twoOverSecondary`](./displaymode-swift.enum/twooversecondary.md) for [`UISplitViewController.SplitBehavior.overlay`](./splitbehavior-swift.enum/overlay.md), and as [`UISplitViewController.DisplayMode.twoDisplaceSecondary`](./displaymode-swift.enum/twodisplacesecondary.md) for [`UISplitViewController.SplitBehavior.displace`](./splitbehavior-swift.enum/displace.md).

If [`presentsWithGesture`](./presentswithgesture.md) is [`false`](../../Swift/false.md), the value of this property is strictly respected.

## See Also

### Managing the display mode
- [var displayMode: UISplitViewController.DisplayMode](./displaymode-swift.property.md)
  The current arrangement of the split view interface.
- [var displayModeButtonItem: UIBarButtonItem](./displaymodebuttonitem.md)
  A button that changes the display mode of the split view controller.
- [var presentsWithGesture: Bool](./presentswithgesture.md)
  Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [var showsSecondaryOnlyButton: Bool](./showssecondaryonlybutton.md)
  Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [UISplitViewController.DisplayMode](./displaymode-swift.enum.md)
  Constants that describe the possible arrangements for a split view interface.
- [var displayModeButtonVisibility: UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.property.md)
  A setting that determines whether the display mode button is visible in the interface.
- [UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.enum.md)
  Constants that determine the visibility of the display mode button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferreddisplaymode)*