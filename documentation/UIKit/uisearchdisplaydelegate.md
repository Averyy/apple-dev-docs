# UISearchDisplayDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for the delegate of a search display controller.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
protocol UISearchDisplayDelegate : NSObjectProtocol
```

#### Overview

This protocol defines delegate methods for [`UISearchDisplayController`](uisearchdisplaycontroller.md) objects.

## Topics

### Responding to search state change
- [func searchDisplayControllerWillBeginSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerwillbeginsearch(_:).md)
  Tells the delegate that the controller is about to begin searching.
- [func searchDisplayControllerDidBeginSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerdidbeginsearch(_:).md)
  Tells the delegate that the controller has started searching.
- [func searchDisplayControllerWillEndSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerwillendsearch(_:).md)
  Tells the delegate that the controller is about to end searching.
- [func searchDisplayControllerDidEndSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerdidendsearch(_:).md)
  Tells the delegate that the controller has finished searching.
### Loading and unloading the table view
- [func searchDisplayController(UISearchDisplayController, didLoadSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didloadsearchresultstableview:).md)
  Tells the delegate that the controller has loaded its table view.
- [func searchDisplayController(UISearchDisplayController, willUnloadSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willunloadsearchresultstableview:).md)
  Tells the delegate that the controller is about to unload its table view.
### Showing and hiding the table view
- [func searchDisplayController(UISearchDisplayController, willShowSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willshowsearchresultstableview:).md)
  Tells the delegate that the controller is about to display its table view.
- [func searchDisplayController(UISearchDisplayController, didShowSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didshowsearchresultstableview:).md)
  Tells the delegate that the controller just displayed its table view.
- [func searchDisplayController(UISearchDisplayController, willHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willhidesearchresultstableview:).md)
  Tells the delegate that the controller is about to hide its table view.
- [func searchDisplayController(UISearchDisplayController, didHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didhidesearchresultstableview:).md)
  Tells the delegate that the controller just hid its table view.
### Responding to changes in search criteria
- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearch: String?) -> Bool](uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearch:).md)
  Asks the delegate if the table view should be reloaded for a given search string.
- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearchScope: Int) -> Bool](uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:).md)
  Asks the delegate if the table view should be reloaded for a given scope.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UIAccelerometerDelegate](uiaccelerometerdelegate.md)
  The interface for receiving acceleration-related data from the system.
- [protocol UIActionSheetDelegate](uiactionsheetdelegate.md)
  The interface for the delegate of an action sheet object.
- [protocol UIAlertViewDelegate](uialertviewdelegate.md)
  The interface for the delegate of an alert view object.
- [protocol UIPopoverControllerDelegate](uipopovercontrollerdelegate.md)
  The interface for the delegate of a popover controller object.
- [protocol UIViewControllerPreviewing](uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.
- [protocol UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md)
  A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate)*