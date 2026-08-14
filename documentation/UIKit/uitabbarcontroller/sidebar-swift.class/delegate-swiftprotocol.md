# UITabBarController.Sidebar.Delegate

**Framework**: UIKit  
**Kind**: protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
protocol Delegate : NSObjectProtocol
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

## Topics

### Instance Methods
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, contextMenuConfigurationFor: UITab) -> UIContextMenuConfiguration?](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:contextmenuconfigurationfor:).md)
  Called when the sidebar is about to display a context menu for the specified `tab`. Return either a concrete `UIContextMenuConfiguration` or nil if the tab does not show context menus.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, didEndDisplaying: UITab)](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:didenddisplaying:).md)
  Notifies the delegate when the sidebar has finished displaying the row representing the specified `tab`
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, itemFor: UITabSidebarItem.Request) -> UITabSidebarItem](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemfor:).md)
  Return a `UITabSidebarItem` for the specified item request. When created, the item will be preconfigured to the appropriate defaults for its given content. If this method is not implemented, a default sidebar item will be provided for the request.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, itemsForAddingTo: any UIDragSession, tab: UITab) -> [UIDragItem]](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemsforaddingto:tab:).md)
  Called when a new drag session is requesting items to add to the existing drag session in the sidebar from the specified `tab`. Return items if the specified tab can add to the drag session, or an empty array if nothing should be added.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, itemsForBeginning: any UIDragSession, tab: UITab) -> [UIDragItem]](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:itemsforbeginning:tab:).md)
  Called when a new drag session has begun in the sidebar from the specified `tab`. Return drag items if the specified tab can be dragged, or an empty array if no drags should begin. Note that if drag items are returned on tabs in groups that allow reordering, then tab reordering is disabled when the sidebar is not in editing.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, leadingSwipeActionsConfigurationFor: UITab) -> UISwipeActionsConfiguration?](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:leadingswipeactionsconfigurationfor:).md)
  Called when the sidebar is about to show leading swipe actions for the specified `tab`. Return either a concrete `UISwipeActionsConfiguration` or nil if the tab does not show swipe actions.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, sidebarAction: UIAction, group: UITabGroup, acceptItemsFrom: any UIDropSession)](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:sidebaraction:group:acceptitemsfrom:).md)
  Receive the drop from into the `sidebarAction` using the specified session. This is only called if the drop operation returned from `tabBarController:sidebar:sidebarAction:operationForAcceptingItemsFromDropSession` is valid for a drop.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, sidebarAction: UIAction, group: UITabGroup, operationForAcceptingItemsFrom: any UIDropSession) -> UIDropOperation](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:sidebaraction:group:operationforacceptingitemsfrom:).md)
  Determines if items from the specified drop session can be dropped into the specified `sidebarAction`. If the operation is either a `.move` or `.copy`, then the drop will proceed and `tabBarController:sidebar:sidebarAction:acceptItemsFromDropSession:` is called. By default, the drop will be treated as a cancel operation if this is not implemented.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, trailingSwipeActionsConfigurationFor: UITab) -> UISwipeActionsConfiguration?](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:trailingswipeactionsconfigurationfor:).md)
  Called when the sidebar is about to show trailing swipe actions for a particular tab. Return either a UISwipeActionsConfiguration object or nil if this tab does not show swipe actions.
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, update: UITabSidebarItem)](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:update:).md)
  Called whenever the sidebar item’s `configurationState` changes or the item is reconfigured. The passed in item will accrue all modifications until the delegate requests for a new sidebar item from the delegate method `tabBarController:sidebar:itemForRequest:`
- [func tabBarController(UITabBarController, sidebar: UITabBarController.Sidebar, willBeginDisplaying: UITab)](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:willbegindisplaying:).md)
  Notifies the delegate when the sidebar is about to display the row representing the specified `tab`
- [func tabBarController(UITabBarController, sidebarAvailabilityDidChange: UITabBarController.Sidebar)](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebaravailabilitydidchange:).md)
  Notifies the delegate when `UITabBarController.Sidebar.isAvailable` changes.
- [func tabBarController(UITabBarController, sidebarVisibilityWillChange: UITabBarController.Sidebar, animator: any UITabBarController.Sidebar.Animating)](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebarvisibilitywillchange:animator:).md)
  Notifies the delegate when the visibility of the sidebar is about to change when `sidebar.isHidden` changes. Add animations to the animator to run alongside the visibility update. Alongside animations and completions will run immediately if the sidebar visibility is changed without animation.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var delegate: (any UITabBarController.Sidebar.Delegate)?](uitabbarcontroller/sidebar-swift.class/delegate-swift.property.md)
  The object managing the delegate of the sidebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol)*