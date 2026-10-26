# WebHistoryLoadedNotification

**Framework**: WebKit  
**Kind**: var  
**Role**: Global Variable

Posted when web history items have been loaded from a URL.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```c
extern NSString * WebHistoryLoadedNotification;
```

#### Discussion

The notification object is the web history that loaded the history items. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation
- [func load(from: URL!) throws](./webhistory/load%28from%29.md)
  Loads the contents of the specified web history file.
### Notifications
- [WebHistoryAllItemsRemovedNotification](./webhistoryallitemsremovednotification.md)
  Posted when all history items have been removed from the web history.
- [WebHistoryItemChangedNotification](./webhistoryitemchangednotification.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [WebHistoryItemsAddedNotification](./webhistoryitemsaddednotification.md)
  Posted when history items have been added to a web history.
- [WebHistoryItemsRemovedNotification](./webhistoryitemsremovednotification.md)
  Posted when items have been removed from the web history.
- [WebHistorySavedNotification](./webhistorysavednotification.md)
  Posted when web history items have been saved to a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryloadednotification)*