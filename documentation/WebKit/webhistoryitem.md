# WebHistoryItem

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

WebHistoryItem objects encapsulate information about visiting a page so that users can return to that page. WebHistory and WebBackForwardList objects manage lists of WebHistoryItem objects. WebHistoryItem objects are created and added to these lists automatically when loading pages, so you do not need to create WebHistoryItem objects directly.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
class WebHistoryItem
```

```objc
@interface WebHistoryItem : NSObject
```

## Topics

### Initializing WebHistoryItem objects
- [init!(urlString: String!, title: String!, lastVisitedTimeInterval: TimeInterval)](./webhistoryitem/init%28urlstring,title,lastvisitedtimeinterval%29-5amr.md)
  Initializes the receiver with a URL,`URLString`, a title specified by `title` and the last time this item was visited specified by `time` title, and time last visited.
### Getting URL information
- [var urlString: String!](./webhistoryitem/urlstring.md)
  The string representation of the URL for the receiver’s page.
- [var originalURLString: String!](./webhistoryitem/originalurlstring.md)
  The string representation of the original URL for the receiver’s page.
### Getting and setting page titles
- [var title: String!](./webhistoryitem/title.md)
  The receiver’s original page title.
- [var alternateTitle: String!](./webhistoryitem/alternatetitle.md)
  An alternate title that may be used in place of the receiver’s page title.
### Getting other attributes
- [var icon: NSImage!](./webhistoryitem/icon.md)
  The icon for the receiver’s page, or `nil` if none exists.
- [var lastVisitedTimeInterval: TimeInterval](./webhistoryitem/lastvisitedtimeinterval.md)
  The last time and date the receiver’s page was visited.
### Initializers
- [init!(URLString: String!, title: String!, lastVisitedTimeInterval: TimeInterval)](./webhistoryitem/init%28urlstring,title,lastvisitedtimeinterval%29-d9r0.md)
### Notifications
- [WebHistoryItemChangedNotification](./webhistoryitemchangednotification.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing Previous Webpages (Legacy)
- [class WebBackForwardList](./webbackforwardlist.md)
  A `WebBackForwardList` object maintains a list of visited pages used to go back and forward to the most recent page. A `WebBackForwardList` object maintains only the list data—it does not perform actual page loads (in other words, it does not make any client requests). If you need to perform a page load, see the [`load(_:)`](./webframe/load%28_%29-47p2s.md) method in [`WebFrame`](./webframe.md) to find out how to do this.
- [class WebHistory](./webhistory.md)
  `WebHistory` objects are used to maintain the pages visited by users. Visited pages are represented by [`WebHistoryItem`](./webhistoryitem.md) objects. You add and remove history items using the [`addItems(_:)`](./webhistory/additems%28_%29.md) and [`removeItems(_:)`](./webhistory/removeitems%28_%29.md) methods. These methods post appropriate notifications when items are added or removed so you can update the display. `WebHistory` organizes the `WebHistoryItem` objects by the day they were visited, ordered from most recent to oldest. You can request all the days that contain history items using the [`orderedLastVisitedDays`](./webhistory/orderedlastvisiteddays.md) method or request the items visited on a particular day using the [`orderedItemsLastVisited(onDay:)`](./webhistory/ordereditemslastvisited%28onday%29.md) method. `WebHistory` objects can be loaded and saved by specifying a file URL (see [`load(from:)`](./webhistory/load%28from%29.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitem)*