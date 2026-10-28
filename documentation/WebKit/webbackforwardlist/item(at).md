# item(at:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the item at the specified index in the back-forward list.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func item(at index: Int32) -> WebHistoryItem!
```

```objc
- (WebHistoryItem *) itemAtIndex:(int) index;
```

## Return Value

The item at the specified index, or `nil` if `index` exceeds the bounds of the back-forward list (that is, if `index` is greater than the value returned by [`forwardListCount`](./forwardlistcount.md), or less than the negative form of the value returned by [`backListCount`](./backlistcount.md)).

## Parameters

- `index`: The index of the item to return. The position of the current item is index `0`, and the position of any other item is expressed as an offset from index `0`. For example, the item preceding the current item is at index `-1`, and the item following the current item is at index `1`.

## See Also

### Querying the Back-Forward List
- [var backItem: WebHistoryItem!](./backitem.md)
  The item that precedes the current item in the back-forward list.
- [var backListCount: Int32](./backlistcount.md)
  The number of items that precede the current item in the back-forward list.
- [func back(withLimit: Int32) -> [Any]!](./back%28withlimit%29.md)
  Returns the items that precede the current item in the back-forward list, up to the specified number of items.
- [func contains(WebHistoryItem!) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the back-forward list contains the specified item.
- [var currentItem: WebHistoryItem!](./currentitem.md)
  The current item in the back-forward list.
- [var forwardItem: WebHistoryItem!](./forwarditem.md)
  The item that follows the current item in the back-forward list.
- [var forwardListCount: Int32](./forwardlistcount.md)
  The number of items that follow the current item in the back-forward list.
- [func forwardList(withLimit: Int32) -> [Any]!](./forwardlist%28withlimit%29.md)
  Returns the items that follow the current item in the back-forward list, up to the specified number of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/item(at:))*