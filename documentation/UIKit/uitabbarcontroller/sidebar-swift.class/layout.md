# UITabBarController.Sidebar.Layout

**Framework**: UIKit  
**Kind**: enum

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Layout
```

## Topics

### Enumeration Cases
- [UITabBarController.Sidebar.Layout.automatic](uitabbarcontroller/sidebar-swift.class/layout/automatic.md)
- [UITabBarController.Sidebar.Layout.overlap](uitabbarcontroller/sidebar-swift.class/layout/overlap.md)
  When the sidebar is displayed, it will overlap the selected view controller, allowing the selected view controller to render underneath the sidebar. Anchor the view’s content to the `layoutMarginsGuide` or `safeAreaLayoutGuide` to avoid being occluded by the sidebar.
- [UITabBarController.Sidebar.Layout.tile](uitabbarcontroller/sidebar-swift.class/layout/tile.md)
  When the sidebar is displayed, the selected view controller is resized and shifted to display alongside the sidebar. The selected view controller is not occluded by the sidebar, cannot render underneath the sidebar.
### Initializers
- [init?(rawValue: Int)](uitabbarcontroller/sidebar-swift.class/layout/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var isHidden: Bool](uitabbarcontroller/sidebar-swift.class/ishidden.md)
  Determines if the sidebar is currently hidden.
- [var preferredLayout: UITabBarController.Sidebar.Layout](uitabbarcontroller/sidebar-swift.class/preferredlayout.md)
  The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [func reconfigureItem(for: UITab)](uitabbarcontroller/sidebar-swift.class/reconfigureitem(for:).md)
  Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout)*