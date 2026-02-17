# tabBarController(_:sidebar:trailingSwipeActionsConfigurationFor:)

**Framework**: UIKit  
**Kind**: method

Called when the sidebar is about to show trailing swipe actions for a particular tab. Return either a UISwipeActionsConfiguration object or nil if this tab does not show swipe actions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, trailingSwipeActionsConfigurationFor tab: UITab) -> UISwipeActionsConfiguration?
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:trailingswipeactionsconfigurationfor:))*