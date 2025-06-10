# tabBarController(_:sidebar:sidebarAction:group:operationForAcceptingItemsFrom:)

**Framework**: UIKit  
**Kind**: method

Determines if items from the specified drop session can be dropped into the specified `sidebarAction`. If the operation is either a `.move` or `.copy`, then the drop will proceed and `tabBarController:sidebar:sidebarAction:acceptItemsFromDropSession:` is called. By default, the drop will be treated as a cancel operation if this is not implemented.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, sidebarAction: UIAction, group: UITabGroup, operationForAcceptingItemsFrom session: any UIDropSession) -> UIDropOperation
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:sidebaraction:group:operationforacceptingitemsfrom:))*