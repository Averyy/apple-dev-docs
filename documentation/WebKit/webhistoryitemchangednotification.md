# WebHistoryItemChangedNotification

**Framework**: WebKit  
**Kind**: var  
**Role**: Global Variable

Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```c
extern NSString * WebHistoryItemChangedNotification;
```

#### Discussion

This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation
- [var alternateTitle: String!](./webhistoryitem/alternatetitle.md)
  An alternate title that may be used in place of the receiver’s page title.
### Notifications
- [WebHistoryAllItemsRemovedNotification](./webhistoryallitemsremovednotification.md)
  Posted when all history items have been removed from the web history.
- [WebHistoryItemsAddedNotification](./webhistoryitemsaddednotification.md)
  Posted when history items have been added to a web history.
- [WebHistoryItemsRemovedNotification](./webhistoryitemsremovednotification.md)
  Posted when items have been removed from the web history.
- [WebHistoryLoadedNotification](./webhistoryloadednotification.md)
  Posted when web history items have been loaded from a URL.
- [WebHistorySavedNotification](./webhistorysavednotification.md)
  Posted when web history items have been saved to a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitemchangednotification)*