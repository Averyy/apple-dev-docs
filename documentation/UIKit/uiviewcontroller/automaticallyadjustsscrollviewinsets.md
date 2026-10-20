# automaticallyAdjustsScrollViewInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets.

**Availability**:
- iOS 7.0+ - Deprecated in 11.0
- iPadOS 7.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use [`contentInsetAdjustmentBehavior`](../uiscrollview/contentinsetadjustmentbehavior-swift.property.md) instead.

## Declaration

```swift
var automaticallyAdjustsScrollViewInsets: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL automaticallyAdjustsScrollViewInsets;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md), which lets container view controllers know that they should adjust the scroll view insets of this view controller’s view to account for screen areas consumed by a status bar, search bar, navigation bar, toolbar, or tab bar. Set this property to [`false`](../../Swift/false.md) if your view controller implementation manages its own scroll view inset adjustments.

## See Also

### Deprecated properties
- [var shouldAutorotate: Bool](./shouldautorotate.md)
  A Boolean value that indicates whether the view controller’s contents should autorotate.
- [var previewActionItems: [any UIPreviewActionItem]](./previewactionitems.md)
  The quick actions displayed when a user swipes upward on a 3D Touch preview.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/automaticallyadjustsscrollviewinsets)*