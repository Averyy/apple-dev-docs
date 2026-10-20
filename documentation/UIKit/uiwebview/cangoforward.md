# canGoForward

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver can move forward.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
var canGoForward: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=canGoForward) BOOL canGoForward;
```

#### Discussion

If [`true`](../../Swift/true.md), able to move forward; otherwise, [`false`](../../Swift/false.md) .

## See Also

### Moving back and forward
- [var canGoBack: Bool](./cangoback.md)
  A Boolean value indicating whether the receiver can move backward.
- [func goBack()](./goback%28%29.md)
  Loads the previous location in the back-forward list.
- [func goForward()](./goforward%28%29.md)
  Loads the next location in the back-forward list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/cangoforward)*