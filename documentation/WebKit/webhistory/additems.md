# addItems(_:)

**Framework**: WebKit  
**Kind**: method

Inserts or updates the specified items in the web history.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func addItems(_ newItems: [Any]!)
```

#### Discussion

When successful, this method posts a notification ([`WebHistoryItemsAddedNotification`](webhistoryitemsaddednotification.md)).

## Parameters

- `newItems`: An array of web history items to add. If an item in the array already exists in the web history this method replaces the existing item, so that the last-visited date for the item is updated.

## See Also

- [func removeItems([Any]!)](webhistory/removeitems(_:).md)
  Removes the specified items from the web history.
- [func removeAllItems()](webhistory/removeallitems.md)
  Removes all items from the web history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/additems(_:))*