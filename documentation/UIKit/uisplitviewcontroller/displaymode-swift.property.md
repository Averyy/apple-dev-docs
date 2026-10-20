# displayMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current arrangement of the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var displayMode: UISplitViewController.DisplayMode { get }
```

```objc
@property (nonatomic, readonly) UISplitViewControllerDisplayMode displayMode;
```

#### Discussion

This property reflects the arrangement of the child view controllers in a split view interface. The value in this property is never set to [`UISplitViewController.DisplayMode.automatic`](./displaymode-swift.enum/automatic.md). To change the current display mode, change the value of the [`preferredDisplayMode`](./preferreddisplaymode.md) property. If you just want to change which columns are shown, consider using [`show(_:)`](./show%28_%29.md) or [`hide(_:)`](./hide%28_%29.md) and the split view controller will determine how to update the display mode to display the desired columns.

When [`isCollapsed`](./iscollapsed.md) is [`true`](../../Swift/true.md), the value of this property is ignored. A collapsed split view interface contains only one view controller, so the display mode is superfluous.

## See Also

### Managing the display mode
- [var preferredDisplayMode: UISplitViewController.DisplayMode](./preferreddisplaymode.md)
  The preferred arrangement of the split view interface.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.property)*