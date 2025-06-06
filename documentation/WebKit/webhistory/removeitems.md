# removeItems(_:)

**Framework**: Webkit  
**Kind**: method

Removes the specified items from the web history.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func removeItems(_ items: [Any]!)
```

#### Discussion

When successful, this method posts a notification ([`WebHistoryItemsRemovedNotification`](webhistoryitemsremovednotification.md)).

## Parameters

- `items`: An array of web history items to remove.

## See Also

- [func addItems([Any]!)](webhistory/additems(_:).md)
  Inserts or updates the specified items in the web history.
- [func removeAllItems()](webhistory/removeallitems.md)
  Removes all items from the web history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/removeitems(_:))*