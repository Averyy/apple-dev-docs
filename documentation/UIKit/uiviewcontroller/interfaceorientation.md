# interfaceOrientation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`viewWillTransition(to:with:)`](../uicontentcontainer/viewwilltransition%28to,with%29.md) to make interface-based adjustments.

## Declaration

```swift
var interfaceOrientation: UIInterfaceOrientation { get }
```

```objc
@property (nonatomic, readonly) UIInterfaceOrientation interfaceOrientation;
```

#### Discussion

Do not use this property for informing layout decisions.

The possible values for the [`interfaceOrientation`](./interfaceorientation.md) property are described in the [`UIInterfaceOrientation`](../uiinterfaceorientation.md) enum.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/interfaceorientation)*