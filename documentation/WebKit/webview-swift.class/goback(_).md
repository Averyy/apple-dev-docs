# goBack(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that loads the previous location in the back-forward list.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func goBack(_ sender: Any?)
```

```objc
- (void) goBack:(id) sender;
```

## Discussion

This method does nothing if it is unable to move backward.

## Parameters

- `sender`: The object that sent this message.

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
- [var canGoForward: Bool](./cangoforward.md)
  A Boolean that indicates whether the next location can be loaded.
- [func goForward() -> Bool](./goforward%28%29.md)
  Loads the next location in the back-forward list.
- [func goForward(Any?)](./goforward%28_%29.md)
  An action method that loads the next location in the back-forward list.
- [func go(toBackForwardItem: WebHistoryItem!) -> Bool](./go%28tobackforwarditem%29.md)
  Loads a specific location from the back-forward list and sets it as the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/goback(_:))*