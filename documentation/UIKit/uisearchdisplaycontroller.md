# UISearchDisplayController

**Framework**: UIKit  
**Kind**: class

An object that manages the display of a search bar, along with a table view that displays search results.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UISearchDisplayController
```

#### Overview

You initialize a search display controller with a search bar and a view controller responsible for managing the data to be searched. When the user starts a search, the search display controller superimposes the search interface over the original view controller’s view and shows the search results in its table view.

In addition to managing the searchable data, the original view controller typically plays four more roles you need to fill when using a search display controller. Those roles are the following:

1. Data source for the search results table view ([`searchResultsDataSource`](uisearchdisplaycontroller/searchresultsdatasource.md)), which provides the data for the results table.
2. Delegate for the search results table view ([`searchResultsDelegate`](uisearchdisplaycontroller/searchresultsdelegate.md)), which responds to the user’s selection of an item in the results table.
3. Delegate for the search display controller ([`delegate`](uisearchdisplaycontroller/delegate.md)), which responds to events such the starting or ending of a search, and the showing or hiding of the search interface. As a convenience, this delegate may also be told about changes to the search string or search scope, so that the results table view can be reloaded.
4. Delegate for the search bar ([`delegate`](uisearchbar/delegate.md) described in [`UISearchBar`](uisearchbar.md)), which responds to changes in search criteria.

Typically, you initialize a search display controller from a view controller (usually an instance of [`UITableViewController`](uitableviewcontroller.md)) that’s displaying a list. See the Simple UISearchBar with State Restoration sample code project for an example of how to configure a search display controller in Interface Builder. To perform configuration programmatically, set `self` for the search display controller’s view controller and search results data source and delegate, as shown here:

```objc
searchController = [[UISearchDisplayController alloc]
                         initWithSearchBar:searchBar contentsController:self];
searchController.delegate = self;
searchController.searchResultsDataSource = self;
searchController.searchResultsDelegate = self;
```

If you follow this pattern, then in the table view data source and delegate methods you can check the methods’ table view argument to determine which table view is sending the message:

```objc
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
 
    if (tableView == self.tableView) {
        return ...;
    }
    // If necessary (if self is the data source for other table views),
    // check whether tableView is searchController.searchResultsTableView.
    return ...;
}
```

> ❗ **Important**:  A view controller or search bar can be associated with only a single search display controller at a time. If a search display controller is destroyed (for example, in response to a memory warning), then you can create a new one and associate it with the original view controller or search bar.

 A view controller or search bar can be associated with only a single search display controller at a time. If a search display controller is destroyed (for example, in response to a memory warning), then you can create a new one and associate it with the original view controller or search bar.

Starting in iOS 7.0, you can use a search display controller with a navigation bar (an instance of the [`UINavigationBar`](uinavigationbar.md) class) by configuring the search display controller’s [`displaysSearchBarInNavigationBar`](uisearchdisplaycontroller/displayssearchbarinnavigationbar.md) and [`navigationItem`](uisearchdisplaycontroller/navigationitem.md) properties.

## Topics

### Initializing a search bar
- [init(searchBar: UISearchBar, contentsController: UIViewController)](uisearchdisplaycontroller/init(searchbar:contentscontroller:).md)
  Returns a display controller initialized with the given search bar and contents controller.
### Displaying the search Interface
- [var isActive: Bool](uisearchdisplaycontroller/isactive.md)
  The visibility state of the search interface.
- [func setActive(Bool, animated: Bool)](uisearchdisplaycontroller/setactive(_:animated:).md)
  Displays or hides the search interface, optionally with animation.
### Configuring a search bar
- [var delegate: (any UISearchDisplayDelegate)?](uisearchdisplaycontroller/delegate.md)
  The controller’s delegate.
- [var searchBar: UISearchBar](uisearchdisplaycontroller/searchbar.md)
  The search bar.
- [var searchContentsController: UIViewController](uisearchdisplaycontroller/searchcontentscontroller.md)
  The view controller that manages the contents being searched.
- [var searchResultsTableView: UITableView](uisearchdisplaycontroller/searchresultstableview.md)
  The table view in which the search results are displayed.
- [var searchResultsDataSource: (any UITableViewDataSource)?](uisearchdisplaycontroller/searchresultsdatasource.md)
  The data source for the table view in which the search results are displayed.
- [var searchResultsDelegate: (any UITableViewDelegate)?](uisearchdisplaycontroller/searchresultsdelegate.md)
  The delegate for the table view in which the search results are displayed.
- [var searchResultsTitle: String?](uisearchdisplaycontroller/searchresultstitle.md)
  The title for the search results view.
- [var displaysSearchBarInNavigationBar: Bool](uisearchdisplaycontroller/displayssearchbarinnavigationbar.md)
  Specifies that the navigation bar contains a search bar.
- [var navigationItem: UINavigationItem?](uisearchdisplaycontroller/navigationitem.md)
  Represents the search display controller in a navigation controller’s navigation bar.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIAlertView](uialertview.md)
  A view that displays an alert message.
- [class UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
  A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.
- [class UILocalNotification](uilocalnotification.md)
  A notification that an app can schedule for presentation at a specific date and time.
- [class UIMenuController](uimenucontroller.md)
  The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.
- [class UIMenuItem](uimenuitem.md)
  A custom item in the editing menu managed by the menu controller.
- [class UIMutableUserNotificationAction](uimutableusernotificationaction.md)
  A modifiable version of the user notification action class.
- [class UIMutableUserNotificationCategory](uimutableusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIPopoverController](uipopovercontroller.md)
  An object that manages the presentation of content in a popover.
- [class UIPreviewAction](uipreviewaction.md)
  A preview action, or , that displays below a peek when a user swipes the peek upward.
- [class UIPreviewActionGroup](uipreviewactiongroup.md)
  A group of one or more child quick actions, each an instance of the preview action class.
- [class UIStoryboardPopoverSegue](uistoryboardpopoversegue.md)
  A specific type of segue for presenting content in a popover.
- [class UIUserNotificationAction](uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationCategory](uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIUserNotificationSettings](uiusernotificationsettings.md)
  The types of notifications that can be displayed to the user by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller)*