# forwardList(withLimit:)

**Framework**: Webkit  
**Kind**: method

Returns the items that follow the current item in the back-forward list, up to the specified number of items.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func forwardList(withLimit limit: Int32) -> [Any]!
```

#### Return Value

An array containing (at most) the specified number of items, or `nil` if no items follow the current item.

## Parameters

- `limit`: The greatest number of items to return.

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
- [func item(at: Int32) -> WebHistoryItem!](webbackforwardlist/item(at:).md)
  Returns the item at the specified index in the back-forward list.
- [var forwardItem: WebHistoryItem!](webbackforwardlist/forwarditem.md)
  The item that follows the current item in the back-forward list.
- [var forwardListCount: Int32](webbackforwardlist/forwardlistcount.md)
  The number of items that follow the current item in the back-forward list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/forwardlist(withlimit:))*