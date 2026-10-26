# wantsFullScreenLayout

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view should underlap the status bar.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`edgesForExtendedLayout`](./edgesforextendedlayout.md) and [`extendedLayoutIncludesOpaqueBars`](./extendedlayoutincludesopaquebars.md) instead.

## Declaration

```objc
@property (nonatomic, assign) BOOL wantsFullScreenLayout;
```

#### Discussion

When a view controller presents its view, it normally shrinks that view so that its frame does not overlap the device’s status bar. Setting this property to [`true`](../../Swift/true.md) causes the view controller to size its view so that it fills the entire screen, including the area under the status bar. (Of course, for this to happen, the window hosting the view controller must itself be sized to fill the entire screen, including the area underneath the status bar.) You would typically set this property to [`true`](../../Swift/true.md) in cases where you have a translucent status bar and want your view’s content to be visible behind that view.

If this property is [`true`](../../Swift/true.md), the view is not resized in a way that would cause it to underlap a tab bar but is resized to underlap translucent toolbars. Regardless of the value of this property, navigation controllers always allow views to underlap translucent navigation bars.

The default value of this property is [`false`](../../Swift/false.md), which causes the view to be laid out so it does not underlap the status bar.

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
- [modalViewController](./modalviewcontroller.md)
  The controller for the active presented view’that is, the view that is temporarily displayed on top of the view managed by the receiver.
- [var searchDisplayController: UISearchDisplayController?](./searchdisplaycontroller.md)
  The search display controller associated with the view controller.
- [var topLayoutGuide: any UILayoutSupport](./toplayoutguide.md)
  Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/wantsfullscreenlayout)*