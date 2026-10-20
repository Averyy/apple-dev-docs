# forwardItem

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The item that follows the current item in the back-forward list.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
var forwardItem: WebHistoryItem! { get }
```

```objc
@property (nonatomic, strong, readonly) WebHistoryItem * forwardItem;
```

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
- [func item(at: Int32) -> WebHistoryItem!](./item%28at%29.md)
  Returns the item at the specified index in the back-forward list.
- [var forwardListCount: Int32](./forwardlistcount.md)
  The number of items that follow the current item in the back-forward list.
- [func forwardList(withLimit: Int32) -> [Any]!](./forwardlist%28withlimit%29.md)
  Returns the items that follow the current item in the back-forward list, up to the specified number of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/forwarditem)*