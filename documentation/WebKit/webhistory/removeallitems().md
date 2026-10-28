# removeAllItems()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Removes all items from the web history.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func removeAllItems()
```

```objc
- (void) removeAllItems;
```

## Discussion

When successful, this method posts a notification ([`WebHistoryAllItemsRemovedNotification`](../webhistoryallitemsremovednotification.md)).

## See Also

### Adding and Removing History Items
- [func addItems([Any]!)](./additems%28_%29.md)
  Inserts or updates the specified items in the web history.
- [func removeItems([Any]!)](./removeitems%28_%29.md)
  Removes the specified items from the web history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/removeallitems())*