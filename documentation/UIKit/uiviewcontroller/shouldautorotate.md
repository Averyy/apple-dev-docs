# shouldAutorotate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view controller’s contents should autorotate.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Instead, update [`supportedInterfaceOrientations`](./supportedinterfaceorientations.md) and then call [`setNeedsUpdateOfSupportedInterfaceOrientations()`](./setneedsupdateofsupportedinterfaceorientations%28%29.md) to indicate a change to the supported interface orientations.

## Declaration

```swift
var shouldAutorotate: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL shouldAutorotate;
```

## Return Value

[`true`](../../Swift/true.md) if the content should rotate, otherwise [`false`](../../Swift/false.md). This method returns [`true`](../../Swift/true.md) by default.

## See Also

### Deprecated properties
- [var previewActionItems: [any UIPreviewActionItem]](./previewactionitems.md)
  The quick actions displayed when a user swipes upward on a 3D Touch preview.
- [var automaticallyAdjustsScrollViewInsets: Bool](./automaticallyadjustsscrollviewinsets.md)
  A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets.
- [var bottomLayoutGuide: any UILayoutSupport](./bottomlayoutguide.md)
  Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.
- [var isModalInPopover: Bool](./ismodalinpopover.md)
  A Boolean value indicating whether the view controller should be presented modally by a popover.
- [var searchDisplayController: UISearchDisplayController?](./searchdisplaycontroller.md)
  The search display controller associated with the view controller.
- [var topLayoutGuide: any UILayoutSupport](./toplayoutguide.md)
  Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [contentSizeForViewInPopover](./contentsizeforviewinpopover.md)
  The size of the view controller’s view while displayed in a popover.
- [modalViewController](./modalviewcontroller.md)
  The controller for the active presented view’that is, the view that is temporarily displayed on top of the view managed by the receiver.
- [wantsFullScreenLayout](./wantsfullscreenlayout.md)
  A Boolean value indicating whether the view should underlap the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautorotate)*