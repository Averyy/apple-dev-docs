# modalViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The controller for the active presented view’that is, the view that is temporarily displayed on top of the view managed by the receiver.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`presentedViewController`](./presentedviewcontroller.md) instead.

## Declaration

```objc
@property (nonatomic, readonly, nullable) UIViewController * modalViewController;
```

## See Also

### Deprecated properties
- [var shouldAutorotate: Bool](./shouldautorotate.md)
  A Boolean value that indicates whether the view controller’s contents should autorotate.
- [var previewActionItems: [any UIPreviewActionItem]](./previewactionitems.md)
  The quick actions displayed when a user swipes upward on a 3D Touch preview.
- [var automaticallyAdjustsScrollViewInsets: Bool](./automaticallyadjustsscrollviewinsets.md)
  A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets.
- [var bottomLayoutGuide: any UILayoutSupport](./bottomlayoutguide.md)
  Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [contentSizeForViewInPopover](./contentsizeforviewinpopover.md)
  The size of the view controller’s view while displayed in a popover.
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.
- [var isModalInPopover: Bool](./ismodalinpopover.md)
  A Boolean value indicating whether the view controller should be presented modally by a popover.
- [var searchDisplayController: UISearchDisplayController?](./searchdisplaycontroller.md)
  The search display controller associated with the view controller.
- [var topLayoutGuide: any UILayoutSupport](./toplayoutguide.md)
  Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [wantsFullScreenLayout](./wantsfullscreenlayout.md)
  A Boolean value indicating whether the view should underlap the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/modalviewcontroller)*