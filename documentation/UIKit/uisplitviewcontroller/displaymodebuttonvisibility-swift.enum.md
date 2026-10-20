# UISplitViewController.DisplayModeButtonVisibility

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine the visibility of the display mode button.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
enum DisplayModeButtonVisibility
```

```c
enum UISplitViewControllerDisplayModeButtonVisibility : NSInteger;
```

## Topics

### Constants
- [UISplitViewController.DisplayModeButtonVisibility.automatic](./displaymodebuttonvisibility-swift.enum/automatic.md)
  A constant that automatically determines the visibility of the display mode button.
- [UISplitViewController.DisplayModeButtonVisibility.never](./displaymodebuttonvisibility-swift.enum/never.md)
  A constant that prevents the display mode button from appearing.
- [UISplitViewController.DisplayModeButtonVisibility.always](./displaymodebuttonvisibility-swift.enum/always.md)
  A constant that allows the display mode button to always appear.
### Initializers
- [init?(rawValue: Int)](./displaymodebuttonvisibility-swift.enum/init%28rawvalue%29.md)

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
- [UISplitViewController.DisplayMode](./displaymode-swift.enum.md)
  Constants that describe the possible arrangements for a split view interface.
- [var displayModeButtonVisibility: UISplitViewController.DisplayModeButtonVisibility](./displaymodebuttonvisibility-swift.property.md)
  A setting that determines whether the display mode button is visible in the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymodebuttonvisibility-swift.enum)*