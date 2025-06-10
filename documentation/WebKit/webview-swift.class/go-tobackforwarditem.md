# go(toBackForwardItem:)

**Framework**: WebKit  
**Kind**: method

Loads a specific location from the back-forward list and sets it as the current item.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func go(toBackForwardItem item: WebHistoryItem!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `item` is in the back-forward list; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `item`: The index of the location to load. This method sets the current item in the back-forward list to  .

## See Also

- [func setMaintainsBackForwardList(Bool)](webview-swift.class/setmaintainsbackforwardlist(_:).md)
  Sets whether to use a back-forward list.
- [var backForwardList: WebBackForwardList!](webview-swift.class/backforwardlist.md)
  The receiver’s back-forward list.
- [var canGoBack: Bool](webview-swift.class/cangoback.md)
  A Boolean that indicates whether the previous location can be loaded.
- [func goBack() -> Bool](webview-swift.class/goback.md)
  Loads the previous location in the back-forward list.
- [func goBack(Any?)](webview-swift.class/goback(_:).md)
  An action method that loads the previous location in the back-forward list.
- [var canGoForward: Bool](webview-swift.class/cangoforward.md)
  A Boolean that indicates whether the next location can be loaded.
- [func goForward() -> Bool](webview-swift.class/goforward.md)
  Loads the next location in the back-forward list.
- [func goForward(Any?)](webview-swift.class/goforward(_:).md)
  An action method that loads the next location in the back-forward list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/go(tobackforwarditem:))*