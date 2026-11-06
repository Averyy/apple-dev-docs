# UITabBarController.Sidebar.Layout

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Layout
```

```c
enum UITabBarControllerSidebarLayout : NSInteger;
```

## Topics

### Enumeration Cases
- [UITabBarController.Sidebar.Layout.automatic](./layout/automatic.md)
- [UITabBarController.Sidebar.Layout.overlap](./layout/overlap.md)
  When the sidebar is displayed, it will overlap the selected view controller, allowing the selected view controller to render underneath the sidebar. Anchor the view’s content to the `layoutMarginsGuide` or `safeAreaLayoutGuide` to avoid being occluded by the sidebar.
- [UITabBarController.Sidebar.Layout.tile](./layout/tile.md)
  When the sidebar is displayed, the selected view controller is resized and shifted to display alongside the sidebar. The selected view controller is not occluded by the sidebar, cannot render underneath the sidebar.
### Initializers
- [init?(rawValue: Int)](./layout/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Managing customization
- [var isAvailable: Bool](./isavailable.md)
  Indicates when the tab sidebar is available to be displayed in the current context. When available, the sidebar is either visible, or can become visible depending on `isHidden`. Use this property to gate behaviors or UI that is dependent on the availability of the sidebar (like child tabs, or landing pages for groups).
- [var isHidden: Bool](./ishidden.md)
  Determines if the sidebar is currently hidden.
- [var navigationOverflowItems: UIDeferredMenuElement?](./navigationoverflowitems.md)
  Additional items to add to the overflow menu in the sidebar’s navigation bar. Setting this property to a non-nil value will force the overflow button to appear, regardless of if you provide any content in the element’s callback. Items returned are displayed directly in the presented menu. When set, the “Edit Sidebar” action will also be moved into the overflow menu after the app-provided items.
- [var preferredLayout: UITabBarController.Sidebar.Layout](./preferredlayout.md)
  The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [var preferredPlacement: UITabBarController.Sidebar.Placement](./preferredplacement.md)
  The preferred placement for the tab bar controller when the sidebar and tab bar are mutually exclusive, and only one placement can be displayed.
- [UITabBarController.Sidebar.Placement](./placement.md)
- [func reconfigureItem(for: UITab)](./reconfigureitem%28for%29.md)
  Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout)*