# backForwardList

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s back-forward list.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var backForwardList: WebBackForwardList! { get }
```

```objc
@property (nonatomic, strong, readonly) WebBackForwardList * backForwardList;
```

## See Also

### Moving Back and Forward
- [func setMaintainsBackForwardList(Bool)](./setmaintainsbackforwardlist%28_%29.md)
  Sets whether to use a back-forward list.
- [var canGoBack: Bool](./cangoback.md)
  A Boolean that indicates whether the previous location can be loaded.
- [func goBack() -> Bool](./goback%28%29.md)
  Loads the previous location in the back-forward list.
- [func goBack(Any?)](./goback%28_%29.md)
  An action method that loads the previous location in the back-forward list.
- [var canGoForward: Bool](./cangoforward.md)
  A Boolean that indicates whether the next location can be loaded.
- [func goForward() -> Bool](./goforward%28%29.md)
  Loads the next location in the back-forward list.
- [func goForward(Any?)](./goforward%28_%29.md)
  An action method that loads the next location in the back-forward list.
- [func go(toBackForwardItem: WebHistoryItem!) -> Bool](./go%28tobackforwarditem%29.md)
  Loads a specific location from the back-forward list and sets it as the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/backforwardlist)*