# canGoBack

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver can move backward.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
var canGoBack: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=canGoBack) BOOL canGoBack;
```

## Discussion

If [`true`](../../Swift/true.md), able to move backward; otherwise, [`false`](../../Swift/false.md).

## See Also

### Moving back and forward
- [var canGoForward: Bool](./cangoforward.md)
  A Boolean value indicating whether the receiver can move forward.
- [func goBack()](./goback%28%29.md)
  Loads the previous location in the back-forward list.
- [func goForward()](./goforward%28%29.md)
  Loads the next location in the back-forward list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/cangoback)*