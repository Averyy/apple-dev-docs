# displayModeButtonItem

**Framework**: UIKit  
**Kind**: property

A button that changes the display mode of the split view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var displayModeButtonItem: UIBarButtonItem { get }
```

#### Return Value

A preconfigured bar button item that changes the display mode.

#### Discussion

You use this property in classic split view interfaces only. This button doesn’t affect column-style split view interfaces.

When a user taps this button, the display mode changes to the value last returned by the delegate’s [`targetDisplayModeForAction(in:)`](uisplitviewcontrollerdelegate/targetdisplaymodeforaction(in:).md) method. Use that method to determine what mode to apply next based on the current configuration of the split view controller.

Don’t change the configuration of the returned button. The split view controller updates the button’s configuration and appearance automatically based on the current display mode and the information the delegate object provides.

You must incorporate this button into your user interface yourself.

## See Also

- [var preferredDisplayMode: UISplitViewController.DisplayMode](uisplitviewcontroller/preferreddisplaymode.md)
  The preferred arrangement of the split view interface.
- [var displayMode: UISplitViewController.DisplayMode](uisplitviewcontroller/displaymode-swift.property.md)
  The current arrangement of the split view interface.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymodebuttonitem)*