# tabBarController(_:sidebar:itemsForAddingTo:tab:)

**Framework**: UIKit  
**Kind**: method

Called when a new drag session is requesting items to add to the existing drag session in the sidebar from the specified `tab`. Return items if the specified tab can add to the drag session, or an empty array if nothing should be added.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, itemsForAddingTo dragSession: any UIDragSession, tab: UITab) -> [UIDragItem]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemsforaddingto:tab:))*