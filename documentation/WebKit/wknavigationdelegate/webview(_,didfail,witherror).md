# webView(_:didFail:withError:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that an error occurred during navigation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: any Error)
```

```objc
- (void) webView:(WKWebView *) webView didFailNavigation:(WKNavigation *) navigation withError:(NSError *) error;
```

## Mentions

- [Replacing UIWebView in your app](../replacing-uiwebview-in-your-app.md)

## Parameters

- `webView`: The web view that reported the error.
- `navigation`: The navigation object for the operation. This object corresponds to a [`WKNavigation`](../wknavigation.md) object that WebKit returned when the load operation began. You use it to track the progress of that operation.
- `error`: The error that occurred.

## See Also

### Responding to navigation errors
- [func webView(WKWebView, didFailProvisionalNavigation: WKNavigation!, withError: any Error)](./webview%28_,didfailprovisionalnavigation,witherror%29.md)
  Tells the delegate that an error occurred during the early navigation process.
- [func webViewWebContentProcessDidTerminate(WKWebView)](./webviewwebcontentprocessdidterminate%28_%29.md)
  Tells the delegate that the web view’s content process was terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didfail:witherror:))*