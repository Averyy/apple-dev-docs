# webView(_:willPresentEditMenuWithAnimator:)

**Framework**: Webkit  
**Kind**: method

Tells the delegate that the web view is about to present an edit menu.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, willPresentEditMenuWithAnimator animator: any UIEditMenuInteractionAnimating)
```

## See Also

- [func webView(WKWebView, willDismissEditMenuWithAnimator: any UIEditMenuInteractionAnimating)](wkuidelegate/webview(_:willdismisseditmenuwithanimator:).md)
  Tells the delegate that the web view is about to dismiss an edit menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:willpresenteditmenuwithanimator:))*