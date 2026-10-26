# WebHistoryAllItemsRemovedNotification

**Framework**: WebKit  
**Kind**: var  
**Role**: Global Variable

Posted when all history items have been removed from the web history.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```c
extern NSString * WebHistoryAllItemsRemovedNotification;
```

#### Discussion

The notification object is the web history from which the history items were removed. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| @“WebHistoryItemsKey” | An [`NSArray`](../Foundation/nsarray.md) object containing the removed items. |

## See Also

### Related Documentation
- [func removeAllItems()](./webhistory/removeallitems%28%29.md)
  Removes all items from the web history.
### Notifications
- [WebHistoryItemChangedNotification](./webhistoryitemchangednotification.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [WebHistoryItemsAddedNotification](./webhistoryitemsaddednotification.md)
  Posted when history items have been added to a web history.
- [WebHistoryItemsRemovedNotification](./webhistoryitemsremovednotification.md)
  Posted when items have been removed from the web history.
- [WebHistoryLoadedNotification](./webhistoryloadednotification.md)
  Posted when web history items have been loaded from a URL.
- [WebHistorySavedNotification](./webhistorysavednotification.md)
  Posted when web history items have been saved to a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryallitemsremovednotification)*