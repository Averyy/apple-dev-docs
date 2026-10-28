# presentsWithGesture

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.

**Availability**:
- iOS 5.1+
- iPadOS 5.1+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
var presentsWithGesture: Bool { get set }
```

```objc
@property (nonatomic) BOOL presentsWithGesture;
```

## Discussion

When this property is [`true`](../../Swift/true.md), the split view controller installs a gesture recognizer for changing the current display mode. In a column-style split view interface, the gesture is interactive.

In a classic split view interface, the gesture recognizer applies the display mode returned by the delegate’s [`targetDisplayModeForAction(in:)`](../uisplitviewcontrollerdelegate/targetdisplaymodeforaction%28in%29.md) method. If that method returns the [`UISplitViewController.DisplayMode.automatic`](./displaymode-swift.enum/automatic.md) mode, the split view controller applies the most appropriate display mode given its current configuration and size class.

When this property is [`false`](../../Swift/false.md), the split view controller doesn’t install a gesture recognizer for changing the display mode. The split view controller also doesn’t display a button to change the display mode.

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Managing the display mode
- [var preferredDisplayMode: UISplitViewController.DisplayMode](./preferreddisplaymode.md)
  The preferred arrangement of the split view interface.
- [var displayMode: UISplitViewController.DisplayMode](./displaymode-swift.property.md)
  The current arrangement of the split view interface.
- [var displayModeButtonItem: UIBarButtonItem](./displaymodebuttonitem.md)
  A button that changes the display mode of the split view controller.
- [var showsSecondaryOnlyButton: Bool](./showssecondaryonlybutton.md)
  Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [UISplitViewController.DisplayMode](./displaymode-swift.enum.md)
  Constants that describe the possible arrangements for a split view interface.
- [var displayModeButtonVisibility: UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.property.md)
  A setting that determines whether the display mode button is visible in the interface.
- [UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.enum.md)
  Constants that determine the visibility of the display mode button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/presentswithgesture)*