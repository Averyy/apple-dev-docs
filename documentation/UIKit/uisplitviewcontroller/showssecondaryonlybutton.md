# showsSecondaryOnlyButton

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+

## Declaration

```swift
var showsSecondaryOnlyButton: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsSecondaryOnlyButton;
```

#### Discussion

This value only takes effect when the split view controller’s [`style`](./style-swift.property.md) property is [`UISplitViewController.Style.tripleColumn`](./style-swift.enum/triplecolumn.md).

The default value of this property is [`false`](../../Swift/false.md). If you set the value to [`true`](../../Swift/true.md), the secondary view controller shows a button that lets a user toggle the display mode to and from [`UISplitViewController.DisplayMode.secondaryOnly`](./displaymode-swift.enum/secondaryonly.md).

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
- [UISplitViewController.DisplayMode](./displaymode-swift.enum.md)
  Constants that describe the possible arrangements for a split view interface.
- [var displayModeButtonVisibility: UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.property.md)
  A setting that determines whether the display mode button is visible in the interface.
- [UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.enum.md)
  Constants that determine the visibility of the display mode button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/showssecondaryonlybutton)*