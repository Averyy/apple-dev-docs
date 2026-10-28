# contentSizeForViewInPopover

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The size of the view controller’s view while displayed in a popover.

**Availability**:
- iOS 3.2+ - Deprecated in 7.0
- iPadOS 3.2+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`preferredContentSize`](./preferredcontentsize.md) instead.

## Declaration

```objc
@property (nonatomic, readwrite) CGSize contentSizeForViewInPopover;
```

## Discussion

This property contains the desired size for the view controller when it is displayed in a popover. By default, the width is set to 320 points and the height is set to 1100 points. You can change these values as needed.

The recommended width for popovers is 320 points. If needed, you can return a width value as large as 600 points, but doing so is not recommended.

If the popover controller displaying the view controller sets its [`contentSize`](../uipopovercontroller/contentsize.md) property, the popover controller overrides the values set in the view controller’s [`contentSizeForViewInPopover`](./contentsizeforviewinpopover.md) property.

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
- [var interfaceOrientation: UIInterfaceOrientation](./interfaceorientation.md)
  Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.
- [var isModalInPopover: Bool](./ismodalinpopover.md)
  A Boolean value indicating whether the view controller should be presented modally by a popover.
- [modalViewController](./modalviewcontroller.md)
  The controller for the active presented view’that is, the view that is temporarily displayed on top of the view managed by the receiver.
- [var searchDisplayController: UISearchDisplayController?](./searchdisplaycontroller.md)
  The search display controller associated with the view controller.
- [var topLayoutGuide: any UILayoutSupport](./toplayoutguide.md)
  Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [wantsFullScreenLayout](./wantsfullscreenlayout.md)
  A Boolean value indicating whether the view should underlap the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/contentsizeforviewinpopover)*