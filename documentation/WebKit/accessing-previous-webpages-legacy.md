# Accessing Previous Webpages (Legacy)

**Framework**: Webkit

## Topics

### Accessing Previous Webpages (Legacy)
- [class WebBackForwardList](webbackforwardlist.md)
  A `WebBackForwardList` object maintains a list of visited pages used to go back and forward to the most recent page. A `WebBackForwardList` object maintains only the list data—it does not perform actual page loads (in other words, it does not make any client requests). If you need to perform a page load, see the [`load(_:)`](webframe/load(_:)-47p2s.md) method in [`WebFrame`](webframe.md) to find out how to do this.
- [class WebHistory](webhistory.md)
  `WebHistory` objects are used to maintain the pages visited by users. Visited pages are represented by [`WebHistoryItem`](webhistoryitem.md) objects. You add and remove history items using the [`addItems(_:)`](webhistory/additems(_:).md) and [`removeItems(_:)`](webhistory/removeitems(_:).md) methods. These methods post appropriate notifications when items are added or removed so you can update the display. `WebHistory` organizes the `WebHistoryItem` objects by the day they were visited, ordered from most recent to oldest. You can request all the days that contain history items using the [`orderedLastVisitedDays`](webhistory/orderedlastvisiteddays.md) method or request the items visited on a particular day using the [`orderedItemsLastVisited(onDay:)`](webhistory/ordereditemslastvisited(onday:).md) method. `WebHistory` objects can be loaded and saved by specifying a file URL (see [`load(from:)`](webhistory/load(from:).md)).
- [class WebHistoryItem](webhistoryitem.md)
  WebHistoryItem objects encapsulate information about visiting a page so that users can return to that page. WebHistory and WebBackForwardList objects manage lists of WebHistoryItem objects. WebHistoryItem objects are created and added to these lists automatically when loading pages, so you do not need to create WebHistoryItem objects directly.

## See Also

- [Document Object Models API (Legacy)](document-object-models-api-legacy.md)
- [Setting Up a Web View (Legacy)](setting-up-a-web-view-legacy.md)
- [Archiving Webpages (Legacy)](archiving-webpages-legacy.md)
- [Loading Resources (Legacy)](loading-resources-legacy.md)
- [Working with Frames (legacy)](working-with-frames-legacy.md)
- [Downloading Information (Legacy)](downloading-information-legacy.md)
- [Opening a File (Legacy)](opening-a-file-legacy.md)
- [Setting Policies (Legacy)](setting-policies-legacy.md)
- [Implementing Plugins (Legacy)](implementing-plugins-legacy.md)
- [Incorporating Scripts (Legacy)](incorporating-scripts-legacy.md)
- [Working With Document Web Views (Legacy)](working-with-document-web-views-legacy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/accessing-previous-webpages-legacy)*