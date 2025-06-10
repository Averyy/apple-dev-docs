# webView(_:navigationAction:didBecome:)

**Framework**: WebKit  
**Kind**: method

Tells the delegate that a navigation action became a download.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, navigationAction: WKNavigationAction, didBecome download: WKDownload)
```

#### Discussion

Implement this method to begin tracking download progress.

## Parameters

- `webView`: The web view in which the navigation action took place.
- `navigationAction`: Descriptive information about the navigation response that turned into a download.
- `download`: An object that represents the download of a web resource.

## See Also

- [func webView(WKWebView, navigationResponse: WKNavigationResponse, didBecome: WKDownload)](wknavigationdelegate/webview(_:navigationresponse:didbecome:).md)
  Tells the delegate that a navigation response became a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:navigationaction:didbecome:))*