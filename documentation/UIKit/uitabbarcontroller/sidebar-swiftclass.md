# UITabBarController.Sidebar

**Framework**: UIKit  
**Kind**: class

An object for managing and configuring the sidebar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class Sidebar
```

## Topics

### Setting the sidebar delegate
- [var delegate: (any UITabBarController.Sidebar.Delegate)?](uitabbarcontroller/sidebar-swift.class/delegate-swift.property.md)
- [UITabBarController.Sidebar.Delegate](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol.md)
### Scrolling
- [func scroll(to: UITabBarController.Sidebar.ScrollTarget, animated: Bool)](uitabbarcontroller/sidebar-swift.class/scroll(to:animated:).md)
- [UITabBarController.Sidebar.ScrollTarget](uitabbarcontroller/sidebar-swift.class/scrolltarget.md)
### Managing customization
- [var isHidden: Bool](uitabbarcontroller/sidebar-swift.class/ishidden.md)
- [var preferredLayout: UITabBarController.Sidebar.Layout](uitabbarcontroller/sidebar-swift.class/preferredlayout.md)
- [UITabBarController.Sidebar.Layout](uitabbarcontroller/sidebar-swift.class/layout.md)
- [func reconfigureItem(for: UITab)](uitabbarcontroller/sidebar-swift.class/reconfigureitem(for:).md)
### Headers and footers
- [var bottomBarView: UIView?](uitabbarcontroller/sidebar-swift.class/bottombarview.md)
- [var footerContentConfiguration: (any UIContentConfiguration)?](uitabbarcontroller/sidebar-swift.class/footercontentconfiguration.md)
- [var headerContentConfiguration: (any UIContentConfiguration)?](uitabbarcontroller/sidebar-swift.class/headercontentconfiguration.md)
### Instance Properties
- [var navigationOverflowItems: UIDeferredMenuElement?](uitabbarcontroller/sidebar-swift.class/navigationoverflowitems.md)
  Additional items to add to the overflow menu in the sidebar’s navigation bar. Setting this property to a non-nil value will force the overflow button to appear, regardless of if you provide any content in the element’s callback. Items returned are displayed directly in the presented menu. When set, the “Edit Sidebar” action will also be moved into the overflow menu after the app-provided items.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var mode: UITabBarController.Mode](uitabbarcontroller/mode-swift.property.md)
  The display mode for a tab bar.
- [UITabBarController.Mode](uitabbarcontroller/mode-swift.enum.md)
  A tab bar’s display mode.
- [var sidebar: UITabBarController.Sidebar](uitabbarcontroller/sidebar-swift.property.md)
  A tab bar’s corresponding sidebar.
- [class UITabSidebarItem](uitabsidebaritem.md)
- [UITabSidebarItem.Request](uitabsidebaritem/request.md)
- [UITabBarController.Sidebar.Animating](uitabbarcontroller/sidebar-swift.class/animating.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class)*