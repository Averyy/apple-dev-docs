# removeItems(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified items from the web history.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func removeItems(_ items: [Any]!)
```

```objc
- (void) removeItems:(NSArray *) items;
```

#### Discussion

When successful, this method posts a notification ([`WebHistoryItemsRemovedNotification`](../webhistoryitemsremovednotification.md)).

## Parameters

- `items`: An array of web history items to remove.

## See Also

### Adding and Removing History Items
- [func addItems([Any]!)](./additems%28_%29.md)
  Inserts or updates the specified items in the web history.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the web history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/removeitems(_:))*