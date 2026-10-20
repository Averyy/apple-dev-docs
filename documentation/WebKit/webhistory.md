# WebHistory

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

`WebHistory` objects are used to maintain the pages visited by users. Visited pages are represented by [`WebHistoryItem`](./webhistoryitem.md) objects. You add and remove history items using the [`addItems(_:)`](./webhistory/additems%28_%29.md) and [`removeItems(_:)`](./webhistory/removeitems%28_%29.md) methods. These methods post appropriate notifications when items are added or removed so you can update the display. `WebHistory` organizes the `WebHistoryItem` objects by the day they were visited, ordered from most recent to oldest. You can request all the days that contain history items using the [`orderedLastVisitedDays`](./webhistory/orderedlastvisiteddays.md) method or request the items visited on a particular day using the [`orderedItemsLastVisited(onDay:)`](./webhistory/ordereditemslastvisited%28onday%29.md) method. `WebHistory` objects can be loaded and saved by specifying a file URL (see [`load(from:)`](./webhistory/load%28from%29.md)).

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
class WebHistory
```

```objc
@interface WebHistory : NSObject
```

## Topics

### Accessing Shared History Objects
- [class func optionalShared() -> WebHistory!](./webhistory/optionalshared%28%29.md)
  Returns a shared web history object, if one exists.
- [class func setOptionalShared(WebHistory!)](./webhistory/setoptionalshared%28_%29.md)
  Sets the web history object to share.
### Adding and Removing History Items
- [func addItems([Any]!)](./webhistory/additems%28_%29.md)
  Inserts or updates the specified items in the web history.
- [func removeItems([Any]!)](./webhistory/removeitems%28_%29.md)
  Removes the specified items from the web history.
- [func removeAllItems()](./webhistory/removeallitems%28%29.md)
  Removes all items from the web history.
### Getting Web History Items
- [func orderedItemsLastVisited(onDay: NSCalendarDate!) -> [Any]!](./webhistory/ordereditemslastvisited%28onday%29.md)
  Returns web history items that were last visited on the specified date.
- [var orderedLastVisitedDays: [Any]!](./webhistory/orderedlastvisiteddays.md)
  An array of all calendar days represented in the web history.
- [func item(for: URL!) -> WebHistoryItem!](./webhistory/item%28for%29.md)
  Returns the web history item that corresponds to the specified web location.
### Loading and Saving History Information
- [func load(from: URL!) throws](./webhistory/load%28from%29.md)
  Loads the contents of the specified web history file.
- [func save(to: URL!) throws](./webhistory/save%28to%29.md)
  Saves the web history to the specified file.
### Getting and Setting Attributes
- [var historyAgeInDaysLimit: Int32](./webhistory/historyageindayslimit.md)
  The maximum age of web history items that can be retrieved.
- [var historyItemLimit: Int32](./webhistory/historyitemlimit.md)
  The maximum number of web history items that can be stored.
### Constants
- [Web History Dictionary Keys](./web-history-dictionary-keys.md)
  The key for accessing the web history items stored in a notification’s user information dictionary.
### Notifications
- [static let WebHistoryAllItemsRemoved: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/webhistoryallitemsremoved.md)
  Posted when all history items have been removed from the web history.
- [static let WebHistoryItemChanged: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/webhistoryitemchanged.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [static let WebHistoryItemsAdded: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/webhistoryitemsadded.md)
  Posted when history items have been added to a web history.
- [static let WebHistoryItemsRemoved: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/webhistoryitemsremoved.md)
  Posted when items have been removed from the web history.
- [static let WebHistoryLoaded: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/webhistoryloaded.md)
  Posted when web history items have been loaded from a URL.
- [static let WebHistorySaved: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/webhistorysaved.md)
  Posted when web history items have been saved to a URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing Previous Webpages (Legacy)
- [class WebBackForwardList](./webbackforwardlist.md)
  A `WebBackForwardList` object maintains a list of visited pages used to go back and forward to the most recent page. A `WebBackForwardList` object maintains only the list data—it does not perform actual page loads (in other words, it does not make any client requests). If you need to perform a page load, see the [`load(_:)`](./webframe/load%28_%29-47p2s.md) method in [`WebFrame`](./webframe.md) to find out how to do this.
- [class WebHistoryItem](./webhistoryitem.md)
  WebHistoryItem objects encapsulate information about visiting a page so that users can return to that page. WebHistory and WebBackForwardList objects manage lists of WebHistoryItem objects. WebHistoryItem objects are created and added to these lists automatically when loading pages, so you do not need to create WebHistoryItem objects directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory)*