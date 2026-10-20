# tabBarController(_:sidebar:sidebarAction:group:acceptItemsFrom:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Receive the drop from into the `sidebarAction` using the specified session. This is only called if the drop operation returned from `tabBarController:sidebar:sidebarAction:operationForAcceptingItemsFromDropSession` is valid for a drop.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, sidebarAction: UIAction, group: UITabGroup, acceptItemsFrom session: any UIDropSession)
```

```objc
- (void) tabBarController:(UITabBarController *) tabBarController sidebar:(UITabBarControllerSidebar *) sidebar sidebarAction:(UIAction *) sidebarAction group:(UITabGroup *) group acceptItemsFromDropSession:(id<UIDropSession>) session;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:sidebaraction:group:acceptitemsfrom:))*