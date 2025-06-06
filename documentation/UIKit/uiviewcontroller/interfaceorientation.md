# interfaceOrientation

**Framework**: UIKit  
**Kind**: property

Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var interfaceOrientation: UIInterfaceOrientation { get }
```

#### Discussion

Do not use this property for informing layout decisions.

The possible values for the [`interfaceOrientation`](uiviewcontroller/interfaceorientation.md) property are described in the [`UIInterfaceOrientation`](uiinterfaceorientation.md) enum.

## See Also

- [var shouldAutorotate: Bool](uiviewcontroller/shouldautorotate.md)
  A Boolean value that indicates whether the view controller’s contents should autorotate.
- [var previewActionItems: [any UIPreviewActionItem]](uiviewcontroller/previewactionitems.md)
  The quick actions displayed when a user swipes upward on a 3D Touch preview.
- [var automaticallyAdjustsScrollViewInsets: Bool](uiviewcontroller/automaticallyadjustsscrollviewinsets.md)
  A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets.
- [var bottomLayoutGuide: any UILayoutSupport](uiviewcontroller/bottomlayoutguide.md)
  Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [var isModalInPopover: Bool](uiviewcontroller/ismodalinpopover.md)
  A Boolean value indicating whether the view controller should be presented modally by a popover.
- [var searchDisplayController: UISearchDisplayController?](uiviewcontroller/searchdisplaycontroller.md)
  The search display controller associated with the view controller.
- [var topLayoutGuide: any UILayoutSupport](uiviewcontroller/toplayoutguide.md)
  Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/interfaceorientation)*