# WebHistory

**Framework**: Webkit  
**Kind**: class

`WebHistory` objects are used to maintain the pages visited by users. Visited pages are represented by [`WebHistoryItem`](webhistoryitem.md) objects. You add and remove history items using the [`addItems(_:)`](webhistory/additems(_:).md) and [`removeItems(_:)`](webhistory/removeitems(_:).md) methods. These methods post appropriate notifications when items are added or removed so you can update the display. `WebHistory` organizes the `WebHistoryItem` objects by the day they were visited, ordered from most recent to oldest. You can request all the days that contain history items using the [`orderedLastVisitedDays`](webhistory/orderedlastvisiteddays.md) method or request the items visited on a particular day using the [`orderedItemsLastVisited(onDay:)`](webhistory/ordereditemslastvisited(onday:).md) method. `WebHistory` objects can be loaded and saved by specifying a file URL (see [`load(from:)`](webhistory/load(from:).md)).

**Availability**:
- macOS 10.3+

## Declaration

```swift
class WebHistory
```

## Topics

### Accessing Shared History Objects
- [class func optionalShared() -> WebHistory!](webhistory/optionalshared.md)
  Returns a shared web history object, if one exists.
- [class func setOptionalShared(WebHistory!)](webhistory/setoptionalshared(_:).md)
  Sets the web history object to share.
### Adding and Removing History Items
- [func addItems([Any]!)](webhistory/additems(_:).md)
  Inserts or updates the specified items in the web history.
- [func removeItems([Any]!)](webhistory/removeitems(_:).md)
  Removes the specified items from the web history.
- [func removeAllItems()](webhistory/removeallitems.md)
  Removes all items from the web history.
### Getting Web History Items
- [func orderedItemsLastVisited(onDay: NSCalendarDate!) -> [Any]!](webhistory/ordereditemslastvisited(onday:).md)
  Returns web history items that were last visited on the specified date.
- [var orderedLastVisitedDays: [Any]!](webhistory/orderedlastvisiteddays.md)
  An array of all calendar days represented in the web history.
- [func item(for: URL!) -> WebHistoryItem!](webhistory/item(for:).md)
  Returns the web history item that corresponds to the specified web location.
### Loading and Saving History Information
- [func load(from: URL!) throws](webhistory/load(from:).md)
  Loads the contents of the specified web history file.
- [func save(to: URL!) throws](webhistory/save(to:).md)
  Saves the web history to the specified file.
### Getting and Setting Attributes
- [var historyAgeInDaysLimit: Int32](webhistory/historyageindayslimit.md)
  The maximum age of web history items that can be retrieved.
- [var historyItemLimit: Int32](webhistory/historyitemlimit.md)
  The maximum number of web history items that can be stored.
### Constants
- [Web History Dictionary Keys](web-history-dictionary-keys.md)
  The key for accessing the web history items stored in a notification’s user information dictionary.
### Notifications
- [static let WebHistoryAllItemsRemoved: NSNotification.Name](../foundation/nsnotification/name/1521391-webhistoryallitemsremoved.md)
  Posted when all history items have been removed from the web history.
- [static let WebHistoryItemChanged: NSNotification.Name](../foundation/nsnotification/name/1525160-webhistoryitemchanged.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [static let WebHistoryItemsAdded: NSNotification.Name](../foundation/nsnotification/name/1521408-webhistoryitemsadded.md)
  Posted when history items have been added to a web history.
- [static let WebHistoryItemsRemoved: NSNotification.Name](../foundation/nsnotification/name/1521392-webhistoryitemsremoved.md)
  Posted when items have been removed from the web history.
- [static let WebHistoryLoaded: NSNotification.Name](../foundation/nsnotification/name/1521395-webhistoryloaded.md)
  Posted when web history items have been loaded from a URL.
- [static let WebHistorySaved: NSNotification.Name](../foundation/nsnotification/name/1521397-webhistorysaved.md)
  Posted when web history items have been saved to a URL.

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

## See Also

- [class WebBackForwardList](webbackforwardlist.md)
  A `WebBackForwardList` object maintains a list of visited pages used to go back and forward to the most recent page. A `WebBackForwardList` object maintains only the list data—it does not perform actual page loads (in other words, it does not make any client requests). If you need to perform a page load, see the [`load(_:)`](webframe/load(_:)-47p2s.md) method in [`WebFrame`](webframe.md) to find out how to do this.
- [class WebHistoryItem](webhistoryitem.md)
  WebHistoryItem objects encapsulate information about visiting a page so that users can return to that page. WebHistory and WebBackForwardList objects manage lists of WebHistoryItem objects. WebHistoryItem objects are created and added to these lists automatically when loading pages, so you do not need to create WebHistoryItem objects directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory)*