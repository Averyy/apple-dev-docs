# tabBarController(_:sidebar:itemFor:)

**Framework**: UIKit  
**Kind**: method

Return a `UITabSidebarItem` for the specified item request. When created, the item will be preconfigured to the appropriate defaults for its given content. If this method is not implemented, a default sidebar item will be provided for the request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, itemFor request: UITabSidebarItem.Request) -> UITabSidebarItem
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemfor:))*