# webView(_:didFailProvisionalNavigation:withError:)

**Framework**: Webkit  
**Kind**: method

Tells the delegate that an error occurred during the early navigation process.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: any Error)
```

## Mentions

- [Replacing UIWebView in your app](replacing-uiwebview-in-your-app.md)

## Parameters

- `webView`: The web view that called the delegate method.
- `navigation`: The navigation object for the operation. This object corresponds to a   object that WebKit returned when the load operation began. You use it to track the progress of that operation.
- `error`: The error that occurred.

## See Also

- [func webView(WKWebView, didFail: WKNavigation!, withError: any Error)](wknavigationdelegate/webview(_:didfail:witherror:).md)
  Tells the delegate that an error occurred during navigation.
- [func webViewWebContentProcessDidTerminate(WKWebView)](wknavigationdelegate/webviewwebcontentprocessdidterminate(_:).md)
  Tells the delegate that the web view’s content process was terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didfailprovisionalnavigation:witherror:))*