# canGoForward

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether the next location can be loaded.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var canGoForward: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if able to move forward; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func setMaintainsBackForwardList(Bool)](webview/setmaintainsbackforwardlist(_:).md)
  Sets whether to use a back-forward list.
- [var backForwardList: WebBackForwardList!](webview/backforwardlist.md)
  The receiver’s back-forward list.
- [var canGoBack: Bool](webview/cangoback.md)
  A Boolean that indicates whether the previous location can be loaded.
- [func goBack() -> Bool](webview/goback.md)
  Loads the previous location in the back-forward list.
- [func goBack(Any?)](webview/goback(_:).md)
  An action method that loads the previous location in the back-forward list.
- [func goForward() -> Bool](webview/goforward.md)
  Loads the next location in the back-forward list.
- [func goForward(Any?)](webview/goforward(_:).md)
  An action method that loads the next location in the back-forward list.
- [func go(toBackForwardItem: WebHistoryItem!) -> Bool](webview/go(tobackforwarditem:).md)
  Loads a specific location from the back-forward list and sets it as the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/cangoforward)*