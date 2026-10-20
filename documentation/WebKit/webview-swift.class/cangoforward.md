# canGoForward

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the next location can be loaded.

**Availability**:
- macOS

## Declaration

```swift
var canGoForward: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canGoForward;
```

#### Discussion

[`true`](../../Swift/true.md) if able to move forward; otherwise, [`false`](../../Swift/false.md).

## See Also

### Moving Back and Forward
- [func setMaintainsBackForwardList(Bool)](./setmaintainsbackforwardlist%28_%29.md)
  Sets whether to use a back-forward list.
- [var backForwardList: WebBackForwardList!](./backforwardlist.md)
  The receiver’s back-forward list.
- [var canGoBack: Bool](./cangoback.md)
  A Boolean that indicates whether the previous location can be loaded.
- [func goBack() -> Bool](./goback%28%29.md)
  Loads the previous location in the back-forward list.
- [func goBack(Any?)](./goback%28_%29.md)
  An action method that loads the previous location in the back-forward list.
- [func goForward() -> Bool](./goforward%28%29.md)
  Loads the next location in the back-forward list.
- [func goForward(Any?)](./goforward%28_%29.md)
  An action method that loads the next location in the back-forward list.
- [func go(toBackForwardItem: WebHistoryItem!) -> Bool](./go%28tobackforwarditem%29.md)
  Loads a specific location from the back-forward list and sets it as the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/cangoforward)*