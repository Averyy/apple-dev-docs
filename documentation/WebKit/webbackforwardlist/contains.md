# contains(_:)

**Framework**: Webkit  
**Kind**: method

Returns a Boolean value indicating whether the back-forward list contains the specified item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func contains(_ item: WebHistoryItem!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified item is in the back-forward list; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `item`: The item to find in the back-forward list.

## See Also

- [var backItem: WebHistoryItem!](webbackforwardlist/backitem.md)
  The item that precedes the current item in the back-forward list.
- [var backListCount: Int32](webbackforwardlist/backlistcount.md)
  The number of items that precede the current item in the back-forward list.
- [func back(withLimit: Int32) -> [Any]!](webbackforwardlist/back(withlimit:).md)
  Returns the items that precede the current item in the back-forward list, up to the specified number of items.
- [var currentItem: WebHistoryItem!](webbackforwardlist/currentitem.md)
  The current item in the back-forward list.
- [func item(at: Int32) -> WebHistoryItem!](webbackforwardlist/item(at:).md)
  Returns the item at the specified index in the back-forward list.
- [var forwardItem: WebHistoryItem!](webbackforwardlist/forwarditem.md)
  The item that follows the current item in the back-forward list.
- [var forwardListCount: Int32](webbackforwardlist/forwardlistcount.md)
  The number of items that follow the current item in the back-forward list.
- [func forwardList(withLimit: Int32) -> [Any]!](webbackforwardlist/forwardlist(withlimit:).md)
  Returns the items that follow the current item in the back-forward list, up to the specified number of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/contains(_:))*