# UITab

**Framework**: UIKit  
**Kind**: class

An object that manages a tab in a tab bar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class UITab
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

#### Overview

To create a tab, call [`init(title:image:identifier:viewControllerProvider:)`](uitab/init(title:image:identifier:viewcontrollerprovider:).md). In the closure, return the view controller your app presents when someone selects the tab. Then pass an array of tabs to your [`UITabBarController`](uitabbarcontroller.md) object’s tabs property.

For more information, see [`Elevating your iPad app with a tab bar and sidebar`](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## Topics

### Creating tabs
- [init(title: String, image: UIImage?, identifier: String, viewControllerProvider: ((UITab) -> UIViewController)?)](uitab/init(title:image:identifier:viewcontrollerprovider:).md)
  Creates a tab object.
### Accessing a tab’s appearance
- [var title: String](uitab/title.md)
  A tab’s title.
- [var subtitle: String?](uitab/subtitle.md)
  A tab’s subtitle.
- [var identifier: String](uitab/identifier.md)
  A string identifier for a tab.
- [var image: UIImage?](uitab/image.md)
  A tab’s image.
- [var badgeValue: String?](uitab/badgevalue.md)
  A tab’s badge value.
- [var viewController: UIViewController?](uitab/viewcontroller.md)
  The view controller that the system presents when someone selects a tab.
### Managing customization
- [var isHidden: Bool](uitab/ishidden.md)
  A Boolean value that indicates whether an item is hidden in a sidebar.
- [var isHiddenByDefault: Bool](uitab/ishiddenbydefault.md)
  A Boolean value that indicates whether an item is hidden by default.
- [var allowsHiding: Bool](uitab/allowshiding.md)
  A Boolean value that indicates whether people can hide a tab in a sidebar.
- [var preferredPlacement: UITab.Placement](uitab/preferredplacement.md)
  The preferred placement for a tab when displayed in contexts that allow different placement.
- [UITab.Placement](uitab/placement.md)
  A tab’s placement when displayed in contexts that allow different placement.
### Accessing context
- [var parent: UITabGroup?](uitab/parent.md)
  The containing tab group.
- [var tabBarController: UITabBarController?](uitab/tabbarcontroller.md)
  The containing tab bar controller.
- [var userInfo: Any?](uitab/userinfo.md)
  A custom object associated with the tab.
### Instance Properties
- [var hasVisiblePlacement: Bool](uitab/hasvisibleplacement.md)
  Determines if the tab has a visible placement. Returns YES if the tab is visible in a tab bar that supports different tab placements. Otherwise returns NO.
- [var isEnabled: Bool](uitab/isenabled.md)
  Determines if the tab is enabled. When NO, tabs will have a disabled appearance and cannot be selected by the user. Default is YES.
- [var managingTabGroup: UITabGroup?](uitab/managingtabgroup.md)
  The managing tab group for the tab. This returns the rootmost `UITabGroup` in the tab’s parent hierarchy with an active `managingNavigationController`. This can be different to `parent` if the tab is nested in multiple levels of tab groups. If the tab does not belong to a hierarchy with a managing navigation controller, then this will return nil. Default is nil.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UISearchTab](uisearchtab.md)
- [UITabGroup](uitabgroup.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)

## See Also

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
  Create a composite interface by combining content from one or more view controllers with other custom views.
- [class UISplitViewController](uisplitviewcontroller.md)
  A container view controller that implements a hierarchical interface.
- [class UINavigationController](uinavigationcontroller.md)
  A container view controller that defines a stack-based scheme for navigating hierarchical content.
- [class UINavigationBar](uinavigationbar.md)
  Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [class UINavigationItem](uinavigationitem.md)
  The items that a navigation bar displays when the associated view controller is visible.
- [class UITabBarController](uitabbarcontroller.md)
  A container view controller that manages a multiselection interface, where the selection determines which child view controller to display.
- [class UITabBar](uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](uitabbaritem.md)
  An object that describes an item in a tab bar.
- [class UISearchTab](uisearchtab.md)
  A tab subclass that represents the system’s search tab.
- [class UITabGroup](uitabgroup.md)
  An object that manages a collection of tab objects.
- [class UIPageViewController](uipageviewcontroller.md)
  A container view controller that manages navigation between pages of content, where a subview controller manages each page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitab)*