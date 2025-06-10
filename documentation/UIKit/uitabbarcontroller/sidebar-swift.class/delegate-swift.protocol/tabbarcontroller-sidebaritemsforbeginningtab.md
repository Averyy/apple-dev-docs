# tabBarController(_:sidebar:itemsForBeginning:tab:)

**Framework**: UIKit  
**Kind**: method

Called when a new drag session has begun in the sidebar from the specified `tab`. Return drag items if the specified tab can be dragged, or an empty array if no drags should begin. Note that if drag items are returned on tabs in groups that allow reordering, then tab reordering is disabled when the sidebar is not in editing.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, itemsForBeginning dragSession: any UIDragSession, tab: UITab) -> [UIDragItem]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemsforbeginning:tab:))*