# webView(_:willPresentEditMenuWithAnimator:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the web view is about to present an edit menu.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, willPresentEditMenuWithAnimator animator: any UIEditMenuInteractionAnimating)
```

```objc
- (void) webView:(WKWebView *) webView willPresentEditMenuWithAnimator:(id<UIEditMenuInteractionAnimating>) animator;
```

## See Also

### Displaying an edit menu
- [func webView(WKWebView, willDismissEditMenuWithAnimator: any UIEditMenuInteractionAnimating)](./webview%28_,willdismisseditmenuwithanimator%29.md)
  Tells the delegate that the web view is about to dismiss an edit menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:willpresenteditmenuwithanimator:))*