# previewActionItems

**Framework**: UIKit  
**Kind**: property

The quick actions displayed when a user swipes upward on a 3D Touch preview.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var previewActionItems: [any UIPreviewActionItem] { get }
```

#### Return Value

An array of preview (peek) quick actions.

#### Discussion

This property is for use with a preview (peek) view controller which you present in your implementation of the [`previewingContext(_:viewControllerForLocation:)`](uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:).md) delegate method..

Implement this method to provide quick actions for such a preview. When the user swipes upward on the preview, the system presents these quick action items in a sheet below the preview.

The default implementation of this method returns an empty array.

For guidance on appropriate items to include as preview quick actions, read the material on 3D Touch in the [`iOS Technologies`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/MobileHIG/3DTouch.html#//apple_ref/doc/uid/TP40006556-CH31) chapter of [`iOS Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/).

For more information on preview quick actions, see [`UIPreviewActionItem`](uipreviewactionitem.md) and [`UIPreviewAction`](uipreviewaction.md).

## See Also

- [var shouldAutorotate: Bool](uiviewcontroller/shouldautorotate.md)
  A Boolean value that indicates whether the view controller’s contents should autorotate.
- [var automaticallyAdjustsScrollViewInsets: Bool](uiviewcontroller/automaticallyadjustsscrollviewinsets.md)
  A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets.
- [var bottomLayoutGuide: any UILayoutSupport](uiviewcontroller/bottomlayoutguide.md)
  Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [var interfaceOrientation: UIInterfaceOrientation](uiviewcontroller/interfaceorientation.md)
  Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.
- [var isModalInPopover: Bool](uiviewcontroller/ismodalinpopover.md)
  A Boolean value indicating whether the view controller should be presented modally by a popover.
- [var searchDisplayController: UISearchDisplayController?](uiviewcontroller/searchdisplaycontroller.md)
  The search display controller associated with the view controller.
- [var topLayoutGuide: any UILayoutSupport](uiviewcontroller/toplayoutguide.md)
  Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/previewactionitems)*