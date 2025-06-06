# WebBackForwardList

**Framework**: Webkit  
**Kind**: class

A `WebBackForwardList` object maintains a list of visited pages used to go back and forward to the most recent page. A `WebBackForwardList` object maintains only the list data—it does not perform actual page loads (in other words, it does not make any client requests). If you need to perform a page load, see the [`load(_:)`](webframe/load(_:)-47p2s.md) method in [`WebFrame`](webframe.md) to find out how to do this.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class WebBackForwardList
```

#### Overview

Items are typically inserted in a back-forward list in the order they are visited. A `WebBackForwardList` object also maintains the notion of the current item (which is always at index `0`), the preceding item (which is at index `-1`), and the following item (which is at index `1`). The [`goBack()`](webbackforwardlist/goback().md) and [`goForward()`](webbackforwardlist/goforward().md) methods move the current item backward or forward by one. The [`go(to:)`](webbackforwardlist/go(to:).md) method sets the current item to the specified item. All other methods that return [`WebHistoryItem`](webhistoryitem.md) objects do not change the value of the current item, they just return the requested item or items. You can also limit the number of history items stored in the back-forward list using [`capacity`](webbackforwardlist/capacity.md).

`WebBackForwardList` objects also control the number of pages cached. You can turn page caching off by setting the page cache size to `0` using the [`pageCacheSize()`](webbackforwardlist/pagecachesize().md) method, or limit the number of pages cached by passing a value greater than 0.

## Topics

### Adding and Removing Items
- [func add(WebHistoryItem!)](webbackforwardlist/add(_:).md)
  Inserts an item into the back-forward list, immediately after the current item.
### Moving Backward and Forward
- [func goBack()](webbackforwardlist/goback.md)
  Moves backward one item in the back-forward list.
- [func goForward()](webbackforwardlist/goforward.md)
  Moves forward one item in the back-forward list.
- [func go(to: WebHistoryItem!)](webbackforwardlist/go(to:).md)
  Makes the specified item in the back-forward list the current item.
### Querying the Back-Forward List
- [var backItem: WebHistoryItem!](webbackforwardlist/backitem.md)
  The item that precedes the current item in the back-forward list.
- [var backListCount: Int32](webbackforwardlist/backlistcount.md)
  The number of items that precede the current item in the back-forward list.
- [func back(withLimit: Int32) -> [Any]!](webbackforwardlist/back(withlimit:).md)
  Returns the items that precede the current item in the back-forward list, up to the specified number of items.
- [func contains(WebHistoryItem!) -> Bool](webbackforwardlist/contains(_:).md)
  Returns a Boolean value indicating whether the back-forward list contains the specified item.
- [var currentItem: WebHistoryItem!](webbackforwardlist/currentitem.md)
  The current item in the back-forward list.
- [func item(at: Int32) -> WebHistoryItem!](webbackforwardlist/item(at:).md)
  Returns the item at the specified index in the back-forward list.
- [var forwardItem: WebHistoryItem!](webbackforwardlist/forwarditem.md)
  The item that follows the current item in the back-forward list.
- [var forwardListCount: Int32](webbackforwardlist/forwardlistcount.md)
  The number of items that follow the current item in the back-forward list.
- [func forwardList(withLimit: Int32) -> [Any]!](webbackforwardlist/forwardlist(withlimit:).md)
  Returns the items that follow the current item in the back-forward list, up to the specified number of items.
### Page Caching
- [func pageCacheSize() -> Int](webbackforwardlist/pagecachesize.md)
  Returns the maximum number of pages that the receiver can cache.
- [func setPageCacheSize(Int)](webbackforwardlist/setpagecachesize(_:).md)
  Sets the maximum number of pages the receiver can cache.
### Setting Attributes
- [var capacity: Int32](webbackforwardlist/capacity.md)
  The maximum number of items that the back-forward list can contain.

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

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [class WebHistory](webhistory.md)
  `WebHistory` objects are used to maintain the pages visited by users. Visited pages are represented by [`WebHistoryItem`](webhistoryitem.md) objects. You add and remove history items using the [`addItems(_:)`](webhistory/additems(_:).md) and [`removeItems(_:)`](webhistory/removeitems(_:).md) methods. These methods post appropriate notifications when items are added or removed so you can update the display. `WebHistory` organizes the `WebHistoryItem` objects by the day they were visited, ordered from most recent to oldest. You can request all the days that contain history items using the [`orderedLastVisitedDays`](webhistory/orderedlastvisiteddays.md) method or request the items visited on a particular day using the [`orderedItemsLastVisited(onDay:)`](webhistory/ordereditemslastvisited(onday:).md) method. `WebHistory` objects can be loaded and saved by specifying a file URL (see [`load(from:)`](webhistory/load(from:).md)).
- [class WebHistoryItem](webhistoryitem.md)
  WebHistoryItem objects encapsulate information about visiting a page so that users can return to that page. WebHistory and WebBackForwardList objects manage lists of WebHistoryItem objects. WebHistoryItem objects are created and added to these lists automatically when loading pages, so you do not need to create WebHistoryItem objects directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist)*