# item(at:)

**Framework**: WebKit  
**Kind**: method

Returns the item at the specified index in the back-forward list.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func item(at index: Int32) -> WebHistoryItem!
```

#### Return Value

The item at the specified index, or `nil` if `index` exceeds the bounds of the back-forward list (that is, if `index` is greater than the value returned by [`forwardListCount`](webbackforwardlist/forwardlistcount.md), or less than the negative form of the value returned by [`backListCount`](webbackforwardlist/backlistcount.md)).

## Parameters

- `index`: The index of the item to return. The position of the current item is index  , and the position of any other item is expressed as an offset from index  . For example, the item preceding the current item is at index  , and the item following the current item is at index  .

## See Also

- [var backItem: WebHistoryItem!](webbackforwardlist/backitem.md)
  The item that precedes the current item in the back-forward list.
- [var backListCount: Int32](webbackforwardlist/backlistcount.md)
  The number of items that precede the current item in the back-forward list.
- [func back(withLimit: Int32) -> [Any]!](webbackforwardlist/back(withlimit:).md)
  Returns the items that precede the current item in the back-forward list, up to the specified number of items.
- [func contains(WebHistoryItem!) -> Bool](webbackforwardlist/contains(_:).md)
  Returns a Boolean value indicating whether the back-forward list contains the specified item.
- [var currentItem: WebHistoryItem!](webbackforwardlist/currentitem.md)
  The current item in the back-forward list.
- [var forwardItem: WebHistoryItem!](webbackforwardlist/forwarditem.md)
  The item that follows the current item in the back-forward list.
- [var forwardListCount: Int32](webbackforwardlist/forwardlistcount.md)
  The number of items that follow the current item in the back-forward list.
- [func forwardList(withLimit: Int32) -> [Any]!](webbackforwardlist/forwardlist(withlimit:).md)
  Returns the items that follow the current item in the back-forward list, up to the specified number of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/item(at:))*