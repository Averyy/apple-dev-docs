# backItem

**Framework**: WebKit  
**Kind**: property

The item that precedes the current item in the back-forward list.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var backItem: WebHistoryItem! { get }
```

#### Discussion

`nil` if none precedes it.

## See Also

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
- [func forwardList(withLimit: Int32) -> [Any]!](webbackforwardlist/forwardlist(withlimit:).md)
  Returns the items that follow the current item in the back-forward list, up to the specified number of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/backitem)*