# webView(_:shouldGoTo:willUseInstantBack:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, shouldGoTo backForwardListItem: WKBackForwardListItem, willUseInstantBack: Bool, completionHandler: @escaping (Bool) -> Void)
```

```swift
optional func webView(_ webView: WKWebView, shouldGoTo backForwardListItem: WKBackForwardListItem, willUseInstantBack: Bool) async -> Bool
```

```objc
- (void) webView:(WKWebView *) webView shouldGoToBackForwardListItem:(WKBackForwardListItem *) backForwardListItem willUseInstantBack:(BOOL) willUseInstantBack completionHandler:(void (^)(BOOL shouldGoToItem)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:shouldgoto:willuseinstantback:completionhandler:))*