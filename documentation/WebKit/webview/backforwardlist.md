# backForwardList

**Framework**: Webkit  
**Kind**: property

The receiver’s back-forward list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var backForwardList: WebBackForwardList! { get }
```

## See Also

- [func setMaintainsBackForwardList(Bool)](webview/setmaintainsbackforwardlist(_:).md)
  Sets whether to use a back-forward list.
- [var canGoBack: Bool](webview/cangoback.md)
  A Boolean that indicates whether the previous location can be loaded.
- [func goBack() -> Bool](webview/goback.md)
  Loads the previous location in the back-forward list.
- [func goBack(Any?)](webview/goback(_:).md)
  An action method that loads the previous location in the back-forward list.
- [var canGoForward: Bool](webview/cangoforward.md)
  A Boolean that indicates whether the next location can be loaded.
- [func goForward() -> Bool](webview/goforward.md)
  Loads the next location in the back-forward list.
- [func goForward(Any?)](webview/goforward(_:).md)
  An action method that loads the next location in the back-forward list.
- [func go(toBackForwardItem: WebHistoryItem!) -> Bool](webview/go(tobackforwarditem:).md)
  Loads a specific location from the back-forward list and sets it as the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/backforwardlist)*