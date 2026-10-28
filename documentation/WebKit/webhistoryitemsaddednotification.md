# WebHistoryItemsAddedNotification

**Framework**: WebKit  
**Kind**: var  
**Role**: Global Variable

Posted when history items have been added to a web history.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```c
extern NSString * WebHistoryItemsAddedNotification;
```

## Discussion

The notification object is the web history to which the items were added. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| @“WebHistoryItemsKey” | An [`NSArray`](../Foundation/nsarray.md) object containing the added items. |

## See Also

### Related Documentation
- [func addItems([Any]!)](./webhistory/additems%28_%29.md)
  Inserts or updates the specified items in the web history.
### Notifications
- [WebHistoryAllItemsRemovedNotification](./webhistoryallitemsremovednotification.md)
  Posted when all history items have been removed from the web history.
- [WebHistoryItemChangedNotification](./webhistoryitemchangednotification.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [WebHistoryItemsRemovedNotification](./webhistoryitemsremovednotification.md)
  Posted when items have been removed from the web history.
- [WebHistoryLoadedNotification](./webhistoryloadednotification.md)
  Posted when web history items have been loaded from a URL.
- [WebHistorySavedNotification](./webhistorysavednotification.md)
  Posted when web history items have been saved to a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitemsaddednotification)*