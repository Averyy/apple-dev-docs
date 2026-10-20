# UISearchTab

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A tab subclass that represents the system’s search tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class UISearchTab
```

```objc
@interface UISearchTab : UITab
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](./elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

#### Overview

For more information, see [Elevating your iPad app with a tab bar and sidebar](./elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## Topics

### Creating a search tab
- [init(viewControllerProvider: ((UITab) -> UIViewController)?)](./uisearchtab/init%28viewcontrollerprovider%29.md)
  Creates a search tab with a system localized title and image.
### Instance Properties
- [var automaticallyActivatesSearch: Bool](./uisearchtab/automaticallyactivatessearch.md)
  Determines if the search tab should automatically activate the embedded search field when the tab becomes visible.
### Type Properties
- [class var identifier: String](./uisearchtab/identifier.md)
  The system-assigned identifier for search tabs.

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
- [class UITabGroup](./uitabgroup.md)
  An object that manages a collection of tab objects.
- [class UIPageViewController](./uipageviewcontroller.md)
  A container view controller that manages navigation between pages of content, where a subview controller manages each page.
- [class UIArrangementViewController](./uiarrangementviewcontroller.md)
  A view controller that dynamically lays out primary and secondary view controllers based on size class, orientation, and reserved regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtab)*