# tabBarController(_:sidebar:contextMenuConfigurationFor:)

**Framework**: UIKit  
**Kind**: method

Called when the sidebar is about to display a context menu for the specified `tab`. Return either a concrete `UIContextMenuConfiguration` or nil if the tab does not show context menus.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, contextMenuConfigurationFor tab: UITab) -> UIContextMenuConfiguration?
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:contextmenuconfigurationfor:))*