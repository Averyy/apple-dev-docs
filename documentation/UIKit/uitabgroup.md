# UITabGroup

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that manages a collection of tab objects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class UITabGroup
```

```objc
@interface UITabGroup : UITab
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](./elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

## Overview

Use tab groups to create a rich hierarchy of tab items. On iPad, the system displays the tab group as a section in the sidebar. For more information, see [Elevating your iPad app with a tab bar and sidebar](./elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## Topics

### Creating tab groups
- [init(title: String, image: UIImage?, identifier: String, children: [UITab], viewControllerProvider: ((UITab) -> UIViewController)?)](./uitabgroup/init%28title,image,identifier,children,viewcontrollerprovider%29.md)
  Creates a tab group.
### Accessing tabs
- [var children: [UITab]](./uitabgroup/children.md)
  The tabs within a tab group.
- [func tab(forIdentifier: String) -> UITab?](./uitabgroup/tab%28foridentifier%29.md)
  Returns a tab with a matching identifier, if any.
- [var defaultChildIdentifier: String?](./uitabgroup/defaultchildidentifier.md)
  The identifier for the default subitem.
- [var selectedChild: UITab?](./uitabgroup/selectedchild.md)
  The currently selected tab.
### Configuring a tab group
- [var sidebarAppearance: UITabGroup.SidebarAppearance](./uitabgroup/sidebarappearance-swift.property.md)
  The appearance of a tab group’s section in a sidebar.
- [UITabGroup.SidebarAppearance](./uitabgroup/sidebarappearance-swift.enum.md)
  The appearance of a section in a sidebar.
- [var managingNavigationController: UINavigationController?](./uitabgroup/managingnavigationcontroller.md)
  The controller that manages navigation for items in a sidebar.
### Managing customization
- [var allowsReordering: Bool](./uitabgroup/allowsreordering.md)
  A Boolean value that indicates people can reorder subitems in the sidebar.
- [var displayOrderIdentifiers: [String]](./uitabgroup/displayorderidentifiers.md)
  An array that contains the identifiers of subitems in their display order.
- [var displayOrder: [UITab]](./uitabgroup/displayorder.md)
  An array that contains instances of subitems in their display order.
### Assigning actions
- [var sidebarActions: [UIAction]](./uitabgroup/sidebaractions.md)
  An array of actions that appear in a section in a sidebar.
### Instance Properties
- [var isCollapsedByDefault: Bool](./uitabgroup/iscollapsedbydefault.md)
  Whether the group is initially displayed in a collapsed state in the sidebar.
- [var isSidebarDestination: Bool](./uitabgroup/issidebardestination.md)
  Determines if the tab group itself can be selected as a destination in the sidebar.

## Relationships

### Inherits From
- [UITab](./uitab.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](./uiaccessibilityidentification.md)
- [UIPopoverPresentationControllerSourceItem](./uipopoverpresentationcontrollersourceitem.md)
- [UISpringLoadedInteractionSupporting](./uispringloadedinteractionsupporting.md)

## See Also

### Container view controllers
- [Creating a custom container view controller](./creating-a-custom-container-view-controller.md)
  Create a composite interface by combining content from one or more view controllers with other custom views.
- [class UISplitViewController](./uisplitviewcontroller.md)
  A container view controller that implements a hierarchical interface.
- [class UINavigationController](./uinavigationcontroller.md)
  A container view controller that defines a stack-based scheme for navigating hierarchical content.
- [class UINavigationBar](./uinavigationbar.md)
  A region that displays the title and controls provided by navigation items.
- [class UINavigationItem](./uinavigationitem.md)
  The items that a navigation bar displays when the associated view controller is visible.
- [class UITabBarController](./uitabbarcontroller.md)
  A container view controller that manages a multiselection interface, where the selection determines which child view controller to display.
- [class UITabBar](./uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](./uitabbaritem.md)
  An object that describes an item in a tab bar.
- [class UITab](./uitab.md)
  An object that manages a tab in a tab bar.
- [class UITabAccessory](./uitabaccessory.md)
- [class UISearchTab](./uisearchtab.md)
  A tab subclass that represents the system’s search tab.
- [class UIPageViewController](./uipageviewcontroller.md)
  A container view controller that manages navigation between pages of content, where a subview controller manages each page.
- [class UIArrangementViewController](./uiarrangementviewcontroller.md)
  A view controller that dynamically lays out primary and secondary view controllers based on size class, orientation, and reserved regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup)*