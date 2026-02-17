# tabBarController(_:sidebar:update:)

**Framework**: UIKit  
**Kind**: method

Called whenever the sidebar item’s `configurationState` changes or the item is reconfigured. The passed in item will accrue all modifications until the delegate requests for a new sidebar item from the delegate method `tabBarController:sidebar:itemForRequest:`

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, update item: UITabSidebarItem)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:update:))*