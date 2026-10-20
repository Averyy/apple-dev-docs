# UITabBarController.Sidebar

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UITabBarControllerSidebar : NSObject
```

## Topics

### Setting the sidebar delegate
- [var delegate: (any UITabBarController.Sidebar.Delegate)?](./sidebar-swift.class/delegate-swift.property.md)
  The object managing the delegate of the sidebar.
- [UITabBarController.Sidebar.Delegate](./sidebar-swift.class/delegate-swift.protocol.md)
### Scrolling
- [func scroll(to: UITabBarController.Sidebar.ScrollTarget, animated: Bool)](./sidebar-swift.class/scroll%28to,animated%29.md)
- [UITabBarController.Sidebar.ScrollTarget](./sidebar-swift.class/scrolltarget.md)
### Managing customization
- [var isHidden: Bool](./sidebar-swift.class/ishidden.md)
  Determines if the sidebar is currently hidden.
- [var preferredLayout: UITabBarController.Sidebar.Layout](./sidebar-swift.class/preferredlayout.md)
  The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [UITabBarController.Sidebar.Layout](./sidebar-swift.class/layout.md)
- [func reconfigureItem(for: UITab)](./sidebar-swift.class/reconfigureitem%28for%29.md)
  Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.
### Headers and footers
- [var bottomBarView: UIView?](./sidebar-swift.class/bottombarview.md)
  A view to display at the bottom of the sidebar, like a UIToolbar. The width of this view will be managed by the sidebar itself, and its height will be set to the value it returns from `systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:` Default is nil.
- [var footerContentConfiguration: (any UIContentConfiguration)?](./sidebar-swift.class/footercontentconfiguration.md)
- [var headerContentConfiguration: (any UIContentConfiguration)?](./sidebar-swift.class/headercontentconfiguration.md)
### Instance Properties
- [var isAvailable: Bool](./sidebar-swift.class/isavailable.md)
  Indicates when the tab sidebar is available to be displayed in the current context. When available, the sidebar is either visible, or can become visible depending on `isHidden`. Use this property to gate behaviors or UI that is dependent on the availability of the sidebar (like child tabs, or landing pages for groups).
- [var navigationOverflowItems: UIDeferredMenuElement?](./sidebar-swift.class/navigationoverflowitems.md)
  Additional items to add to the overflow menu in the sidebar’s navigation bar. Setting this property to a non-nil value will force the overflow button to appear, regardless of if you provide any content in the element’s callback. Items returned are displayed directly in the presented menu. When set, the “Edit Sidebar” action will also be moved into the overflow menu after the app-provided items.
- [var preferredPlacement: UITabBarController.Sidebar.Placement](./sidebar-swift.class/preferredplacement.md)
  The preferred placement for the tab bar controller when the sidebar and tab bar are mutually exclusive, and only one placement can be displayed.
### Enumerations
- [UITabBarController.Sidebar.Placement](./sidebar-swift.class/placement.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Supporting the sidebar
- [var mode: UITabBarController.Mode](./mode-swift.property.md)
  The display mode for a tab bar.
- [UITabBarController.Mode](./mode-swift.enum.md)
  A tab bar’s display mode.
- [var sidebar: UITabBarController.Sidebar](./sidebar-swift.property.md)
  A tab bar’s corresponding sidebar.
- [class UITabSidebarItem](../uitabsidebaritem.md)
- [UITabSidebarItem.Request](../uitabsidebaritem/request.md)
- [UITabBarController.Sidebar.Animating](./sidebar-swift.class/animating.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class)*